---
title: Пути и содержимое директорий экземпляра ПО
kbId: 2502
---

# Пути и содержимое директорий экземпляра ПО {: #paths}

## Введение

Здесь представлена информация о расположении файлов и директорий экземпляра ПО **{{ productName }}**.

{% if adminGuideLinux or kbExport %}

## Содержимое директорий {% if userGuide or kbExport %}— Linux{% endif %} {: #paths_linux}

По умолчанию файлы экземпляра ПО находятся в директории `/var/lib/comindware/<instanceName>`

Здесь и далее `<instanceName>` — имя экземпляра ПО.

- `/usr/share/comindware/configs/instance/<instanceName>.yml` — файл конфигурации. В этом файле задаются все остальные пути, перечисленные ниже.
- `/var/www/<instanceName>` — исполняемые и конфигурационные файлы экземпляра ПО.
- `/var/lib/comindware/<instanceName>/Database/db` — файлы базы данных.
- `/var/lib/comindware/<instanceName>/Database/log` — файлы журналов Apache Ignite.
- `/var/log/comindware/<instanceName>/Logs/` — файлы журналов.
- `/var/log/comindware/<instanceName>/Logs/Archive` — архивы журналов.
- `/var/lib/comindware/<instanceName>/Database/Scripts` — скомпилированные библиотеки для скриптов на языке С#.
- `/var/lib/comindware/<instanceName>/Database/snapshots` — снимки данных Apache Ignite.
- `/var/lib/comindware/<instanceName>/Database/wal` — файлы журнала предварительной записи.
- `/var/lib/comindware/<instanceName>/Streams` — загруженные пользователями и сформированные системой файлы, которые прикреплены к соответствующим атрибутам.
{: .pageBreakAfter }
- Временные данные, обеспечивающие работу экземпляра ПО. В этих папках нет пользовательских данных и файлов базы данных экземпляра ПО:
    - `/var/lib/comindware/<instanceName>/Temp`
    - `/var/lib/comindware/<instanceName>/Database/cache`
    - `/var/lib/comindware/<instanceName>/Database/diagnostic`
    - `/var/lib/comindware/<instanceName>/Database/FullTextSearch`

    _![Пример файла конфигурации <instanceName>.yml](https://kb.comindware.ru/assets/img_66546f9baeb01.png)_

{% endif %}

{% if adminGuideWindows or kbExport %}

## Содержимое директорий {% if userGuide or kbExport %}— Windows{% endif %} {: #paths_windows}

База данных по умолчанию находится в директории с экземпляром ПО: `C:\ProgramData\Comindware\Instances\<instanceName>`. Здесь `<instanceName>` — имя экземпляра ПО.

Просмотреть фактические пути к директориям экземпляра ПО можно в Утилите администрирования. См. статью *«[Настройка конфигурации и просмотр фактических путей к папкам экземпляра продукта][instance_configure_windows]»*.

- `C:\Program Files\Comindware\CBAP` — исполняемые файлы ПО разных версий.
- `C:\ProgramData\сomindware\configs` — общие файлы конфигурации ПО.
- `C:\ProgramData\сomindware\configs\instance\<instanceName>.yml` — файл конфигурации. В этом файле задаются все остальные пути, перечисленные ниже..
- `C:\ProgramData\сomindware\Instances` — папка с экземплярами ПО.
- `C:\ProgramData\сomindware\Instances\<instanceName>` — экземпляр ПО.
- `C:\ProgramData\сomindware\Instances\<instanceName>\Config` — конфигурационные файлы:
    - `logs.config` (конфигурация журналов, см. статью *«[Подсистема журналирования][logging_engine]»*);
    - `Web.config` (конфигурация экземпляра системы);
    - `Workers.config` (конфигурация системных служб экземпляра системы).
- `C:\ProgramData\сomindware\Instances\<instanceName>\Data` — файлы базы данных.
- `C:\ProgramData\сomindware\Instances\<instanceName>\Data\Scripts` — DLL-файлы, скомпилированные из скриптов на языке C#.
- `C:\ProgramData\сomindware\Instances\<instanceName>\Data\FullTextSearch` — индексы полнотекстового поиска.
- `C:\ProgramData\сomindware\Instances\<instanceName>\Streams` — файлы, загруженные пользователями и сформированные ПО.
- `C:\ProgramData\сomindware\Instances\<instanceName>\Logs` — журналы экземпляра ПО.
- `C:\ProgramData\сomindware\Instances\<instanceName>\Temp` — временные файлы.

{% endif %}

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

{% if adminGuideWindows or kbExport %}
- _[Настройка конфигурации и просмотр фактических путей к папкам экземпляра продукта][instance_configure_windows]_
{% endif %}
- _[Антивирусное ПО. Настройка исключений: пути и файлы {{ productName }}][antivirus_exceptions_configure]_
- _[Подсистема журналирования][logging_engine]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
