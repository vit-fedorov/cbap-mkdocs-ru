{% if pdfOutput %}
<!--hack for PDF output, prevents PDF build crash after indented paragraphs-->
<p class="pdfEndOfBlockHack">.</p>
{% endif %}