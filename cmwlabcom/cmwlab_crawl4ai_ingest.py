import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy
import tiktoken
from datetime import datetime
import os
import json
from bs4 import BeautifulSoup
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy
import collections

OUTPUT_MD = "cmwlab_com_for_llm_ingestion_dirty.md"
PROGRESS_FILE = "cmwlab_com_progress_dirty.json"
START_URL = "https://kb.cmwlab.com/article/29/cmw-platform-v4-7-section-content-2162.html"
BATCH_SIZE = 5
BATCH_TIMEOUT = 120  # seconds
ARTICLE_TIMEOUT = 15  # seconds

# --- Utility functions ---
def count_tokens(text):
    enc = tiktoken.get_encoding("cl100k_base")
    return len(enc.encode(text))

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
            return set(json.load(f))
    return set()

def save_progress(processed_urls):
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(list(processed_urls), f)

def write_batch(articles):
    if not articles:
        return
    with open(OUTPUT_MD, "a", encoding="utf-8") as f:
        for article in articles:
            f.write(article)
        f.flush()
        os.fsync(f.fileno())
    print(f"[WRITE] Wrote {len(articles)} articles.")

async def extract_urls_from_sitemap(crawler, url):
    config = CrawlerRunConfig(scraping_strategy=LXMLWebScrapingStrategy(), verbose=False)
    result = await crawler.arun(url, config=config)
    links = []
    if hasattr(result, '__iter__'):
        for r in result:
            links.extend([l['href'] for l in r.links.get('internal', []) if 'href' in l])
    else:
        links = [l['href'] for l in result.links.get('internal', []) if 'href' in l]
    return sorted(set([l for l in links if l.startswith("https://kb.cmwlab.com")]))

async def get_page_title_from_html(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.title.string.strip() if soup.title and soup.title.string else ''
        return title
    except Exception as e:
        return f'ERROR: {e}'

async def crawl_article_with_timeout(url, config, crawler):
    try:
        print(f"[CRAWL] About to crawl: {url}")
        results = await asyncio.wait_for(
            crawler.arun_many([url], config=config),
            timeout=ARTICLE_TIMEOUT
        )
        for result in results:
            print(f"[RESULT] {getattr(result, 'url', None)} - {getattr(result, 'success', False)}")
        return results
    except asyncio.TimeoutError:
        print(f"[TIMEOUT] {url} timed out after {ARTICLE_TIMEOUT} seconds. Skipping.")
        return []
    except Exception as e:
        print(f"[FAIL] {url} - Exception: {e}")
        return []

# --- Main batch crawling logic ---
async def main():
    ingestion_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    source_line = f"Source: {START_URL}"
    processed_urls = load_progress()
    total_tokens = 0
    total_words = 0
    files_analyzed = 0
    total_articles = 0

    # Write header if file doesn't exist
    if not os.path.exists(OUTPUT_MD):
        with open(OUTPUT_MD, "w", encoding="utf-8") as f:
            f.write(
                f"\n----------------------\n\n"
                f"Ingestion date: {ingestion_date}\n"
                f"Title: kb.cmwlab.com knowledge base for AI ingestion\n"
                f"Description: Provide this file to your AI agent. For better results, add the prompt below\n"
                f"{source_line}\n"
                f"----------------------\n\n"
                "## Prompting instructions\n\n"
                "- Answer the following question: <YOUR_QUESTION>\n"
                "- In your answer, provide links to the referenced articles in the format:\n"
                "  `[URL]`\n\n"
                "## Articles\n\n"
            )

    async with AsyncWebCrawler() as crawler:
        # Set custom User-Agent header if possible
        if hasattr(crawler, 'session') and hasattr(crawler.session, 'headers'):
            crawler.session.headers.update({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            })
            print('[DEBUG] Set custom User-Agent header on crawler session')
        print(f"[DEEPCRAWL] Starting deep crawl from {START_URL} (depth=5, domain-only)...")
        config = CrawlerRunConfig(
            scraping_strategy=LXMLWebScrapingStrategy(),
            css_selector='#articleContent',
            verbose=False,
        )
        queue = collections.deque([START_URL])
        articles = []
        while queue:
            url = queue.popleft()
            if url in processed_urls:
                continue
            try:
                results = await crawler.arun_many([url], config=config)
                for result in results:
                    page_url = getattr(result, 'url', None)
                    if not getattr(result, 'success', False):
                        print(f"[FAIL] {page_url} - {getattr(result, 'error_message', 'Unknown error')}")
                        continue
                    # 1. Extract and queue all internal links before marking as processed
                    # Custom extraction for category/non-article pages
                    full_html = getattr(result, 'cleaned_html', None) or getattr(result, 'html', None)
                    if full_html:
                        # DEBUG: Save the last fetched HTML for inspection
                        with open('debug_last_page.html', 'w', encoding='utf-8') as f:
                            f.write(full_html)
                        soup = BeautifulSoup(full_html, 'html.parser')
                        bs_links_added = 0
                        # Main content extraction
                        for div in soup.find_all('div', class_='article-title'):
                            h2 = div.find('h2', class_='d-table-cell')
                            if h2:
                                a = h2.find('a', href=True)
                                if a and a['href'].startswith('https://kb.cmwlab.com/article/') and a['href'] not in processed_urls and a['href'] not in queue:
                                    queue.append(a['href'])
                                    bs_links_added += 1
                                    print(f"[DEBUG][BS] Queued article link (main): {a['href']}")
                        # Sidebar extraction
                        for a in soup.find_all('a', class_='articleNode', href=True):
                            if a['href'].startswith('https://kb.cmwlab.com/article/') and a['href'] not in processed_urls and a['href'] not in queue:
                                queue.append(a['href'])
                                bs_links_added += 1
                                print(f"[DEBUG][BS] Queued article link (sidebar): {a['href']}")
                        print(f"[DEBUG][BS] Total article links queued from BeautifulSoup: {bs_links_added}")
                    # Also keep the original crawl4ai link extraction for completeness
                    if hasattr(result, 'links'):
                        crawl4ai_links_added = 0
                        for l in result.links.get('internal', []):
                            if 'href' in l:
                                link_url = l['href']
                                if link_url.startswith("https://kb.cmwlab.com") and link_url not in processed_urls and link_url not in queue:
                                    queue.append(link_url)
                                    crawl4ai_links_added += 1
                                    print(f"[DEBUG][C4AI] Queued internal link: {link_url}")
                        print(f"[DEBUG][C4AI] Total internal links queued from crawl4ai: {crawl4ai_links_added}")
                    # 2. If it's an article, extract and save content
                    if page_url and page_url.startswith("https://kb.cmwlab.com/article/"):
                        md_content = getattr(result, 'markdown', None)
                        if md_content and hasattr(md_content, 'raw_markdown'):
                            md_content = md_content.raw_markdown
                        elif md_content:
                            md_content = str(md_content)
                        else:
                            md_content = ""
                        tokens = count_tokens(md_content)
                        word_count = len(md_content.split())
                        total_tokens += tokens
                        total_words += word_count
                        files_analyzed += 1
                        total_articles += 1
                        if full_html:
                            title = await get_page_title_from_html(full_html)
                        else:
                            title = getattr(result, 'title', '') or ''
                        article = (
                            f"================================================\n"
                            f"---\n"
                            f"title: {title}\n"
                            f"url: {page_url}\n"
                            f"tokens: {tokens}\n"
                            f"words: {word_count}\n"
                            f"---\n\n"
                            f"### [{title}]({page_url})\n\n"
                            f"{md_content}\n\n---\n"
                        )
                        articles.append(article)
                        print(f"[ARTICLE] Saved: {page_url}")
                        if len(articles) >= BATCH_SIZE:
                            write_batch(articles)
                            articles = []
                            save_progress(processed_urls)
                    else:
                        print(f"[SKIP] Not an article page: {page_url}")
                    # 3. Mark as processed after extracting links and (if applicable) saving content
                    processed_urls.add(page_url)
            except Exception as e:
                print(f"[FAIL] {url} - Exception during processing: {e}")
        # Write any remaining articles
        if articles:
            write_batch(articles)
            save_progress(processed_urls)
        print(f"[DEEPCRAWL] Done: {files_analyzed} files, {total_tokens} tokens.")

    print(f"Done. {files_analyzed} files, {total_tokens} tokens.")
    print(f"Progress saved in {PROGRESS_FILE}")

    # Update header in output file with totals
    with open(OUTPUT_MD, "r", encoding="utf-8") as f:
        content = f.read()
    header_start = content.find('----------------------')
    header_end = content.find('----------------------', header_start + 1)
    if header_start != -1 and header_end != -1:
        new_header = (
            "----------------------\n\n"
            f"Ingestion date: {ingestion_date}\n"
            "Title: kb.cmwlab.com knowledge base for AI ingestion\n"
            "Description: Provide this file to your AI agent. For better results, add the prompt below\n"
            f"Source: {START_URL}\n"
            f"Total tokens: {total_tokens}\n"
            f"Total words: {total_words}\n"
            f"Total articles: {total_articles}\n"
            "----------------------\n\n"
        )
        content = new_header + content[header_end+22:]
        with open(OUTPUT_MD, "w", encoding="utf-8") as f:
            f.write(content)

if __name__ == "__main__":
    asyncio.run(main()) 