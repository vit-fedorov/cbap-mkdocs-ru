---
title: Пути и содержимое директорий экземпляра ПО
kbId: 4620
---

# Пути и содержимое директорий экземпляра ПО {: #paths}

## Введение

Здесь представлена информация о расположении файлов и директорий экземпляра ПО **{{ productName }}**.

{% if adminGuideLinux or kbExport %}

## Содержимое директорий {% if userGuide or kbExport %}— Linux{% endif %} {: #paths_linux}

По умолчанию файлы экземпляра ПО находятся {% if gostech %}в файловой системе контейнера{% endif %} в директории `/var/lib/comindware/<instanceName>`

Здесь и далее `<instanceName>` — имя экземпляра ПО.

Просмотреть фактические пути к директориям экземпляра ПО можно в файле конфигурации `/usr/share/comindware/configs/instance/<instanceName>.yml`

Пути по умолчанию:
- `/usr/share/comindware/configs/instance/<instanceName>.yml` — файл конфигурации. В этом файле задаются все остальные пути, перечисленные ниже.
{% if gostech %}
- `/usr/share/comindware/<instanceName>` — исполняемые и конфигурационные файлы экземпляра ПО.
{% else %}
- `/var/www/<instanceName>` — исполняемые и конфигурационные файлы экземпляра ПО.
{% endif %}
- `/var/lib/comindware/<instanceName>/Database/db` — файлы базы данных.
{% if not gostech %}
- `/var/lib/comindware/<instanceName>/Database/log` — файлы журналов {{ apacheIgniteVariants }}.
- `/var/log/comindware/<instanceName>/Logs/` — файлы журналов.
- `/var/log/comindware/<instanceName>/Logs/Archive` — архивы журналов.
{% endif %}
- `/var/lib/comindware/<instanceName>/Database/Scripts` — скомпилированные библиотеки для скриптов на языке С#.
- `/var/lib/comindware/<instanceName>/Database/FullTextSearch` — индексы полнотекстового поиска.
- `/var/lib/comindware/<instanceName>/Database/snapshots` — снимки данных {{ apacheIgniteVariants }}.
- `/var/lib/comindware/<instanceName>/Database/wal` — файлы журнала предварительной записи.
- `/var/lib/comindware/<instanceName>/Streams` — загруженные пользователями и сформированные системой файлы, которые прикреплены к соответствующим атрибутам.
{: .pageBreakAfter }
- Временные данные, обеспечивающие работу экземпляра ПО. В этих папках нет пользовательских данных и файлов базы данных экземпляра ПО:
    - `/var/lib/comindware/<instanceName>/Temp`
    - `/var/lib/comindware/<instanceName>/Database/cache`
    - `/var/lib/comindware/<instanceName>/Database/diagnostic`
    - `/var/lib/comindware/<instanceName>/Database/FullTextSearch`

{% endif %}

{% if adminGuideWindows or kbExport %}

## Содержимое директорий {% if userGuide or kbExport %}— Windows{% endif %} {: #paths_windows}

Просмотреть фактические пути к директориям экземпляра ПО можно в файле конфигурации:
`C:\ProgramData\сomindware\configs\instance\<instanceName>.yml`

Здесь и далее `<instanceName>` — имя экземпляра ПО.

Пути по умолчанию:
- `C:\Program Files\Comindware\CBAP` — исполняемые файлы ПО разных версий.
- `C:\ProgramData\сomindware\configs` — общие файлы конфигурации ПО.
- `C:\ProgramData\сomindware\configs\instance\<instanceName>.yml` — файл конфигурации. В этом файле задаются все остальные пути, перечисленные ниже..
- `C:\ProgramData\сomindware\Instances` — папка с экземплярами ПО.
- `C:\ProgramData\сomindware\Instances\<instanceName>` — экземпляр ПО.
- `C:\ProgramData\сomindware\Instances\<instanceName>\config` — конфигурационные файлы:
    - `logs.config` (конфигурация журналов, см. статью *«[Подсистема журналирования][logging_engine]»*);
    - `Web.config` (конфигурация экземпляра системы);
    - `adapterhost.yml` (конфигурация экземпляра Adapterhost);
    - `apigateway.yml` (конфигурация экземпляра Apigateway);
    - `Ignite.config` (конфигурация экземпляра Ignite).
- `C:\ProgramData\сomindware\Instances\<instanceName>\Database` — файлы базы данных.
- `C:\ProgramData\сomindware\Instances\<instanceName>\Database\Scripts` — DLL-файлы, скомпилированные из скриптов на языке C#.
- `C:\ProgramData\сomindware\Instances\<instanceName>\Database\FullTextSearch` — индексы полнотекстового поиска.
- `C:\ProgramData\сomindware\Instances\<instanceName>\Database\snapshots` — снимки данных Apache Ignite.
- `C:\ProgramData\сomindware\Instances\<instanceName>\Database\wal` — файлы журнала предварительной записи.
- `C:\ProgramData\сomindware\Instances\<instanceName>\Streams` — файлы, загруженные пользователями и сформированные ПО.
- `C:\ProgramData\сomindware\Instances\<instanceName>\Logs` — журналы экземпляра ПО.
- `C:\ProgramData\сomindware\Instances\<instanceName>\Temp` — временные файлы.
- Временные данные, обеспечивающие работу экземпляра ПО. В этих папках нет пользовательских данных и файлов базы данных экземпляра ПО:
    - `C:\ProgramData\сomindware\Instances\<instanceName>\Temp`
    - `C:\ProgramData\сomindware\Instances\<instanceName>\Database\cache`
    - `C:\ProgramData\сomindware\Instances\<instanceName>\Database\diagnostic`

{% endif %}

## Рекомендации по настройке путей
ХХХ



<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

{% if adminGuideLinux or kbExport %}
- _[Конфигурация экземпляра, компонентов ПО и служб. Настройка в Linux][configuration_files_linux]_
{% endif %}
{% if not gostech %}
- _[Антивирусное ПО. Настройка исключений: пути и файлы {{ productName }}][antivirus_exceptions_configure]_
{% endif %}
- _[Подсистема журналирования][logging_engine]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
