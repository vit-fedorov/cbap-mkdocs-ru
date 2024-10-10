---
title: Пути и содержимое папок экземпляра ПО
kbId: 2502
---

# Пути и содержимое папок экземпляра ПО

## Введение

В этой статье представлена информация о расположении файлов и папок экземпляра ПО **{{ productName }}**в операционных системах семейства [Linux](#mcetoc_1hchr2nua1) (Альт Сервер, Astra Linux, РЕД ОС, Rocky Linux и Ubuntu) и [Windows.](#mcetoc_1hpdpt8tk1)

## Содержимое каталогов — Linux

По умолчанию файлы экземпляра ПО находятся в каталоге `/var/lib/comindware/instancename`

Здесь и далее `instancename` — имя экземпляра ПО.

- `/usr/share/comindware/configs/instance/instancename.yml` — файл конфигурации. В этом файле задаются все остальные пути, перечисленные ниже.
- `/var/www/instancename` — исполняемые и конфигурационные файлы экземпляра ПО.
- `/var/lib/comindware``/instancename/Database/db` — файлы базы данных.
- `/var/lib/comindware``/instancename/Database/log` — файлы журналов Apache Ignite.
- `/var/log/comindware/instancename/Logs/` — файлы журналов.
- `/var/log/comindware/instancename/Logs/Archive` — архивы журналов.
- `/var/lib/comindware``/instancename/Database/Scripts` — скомпилированные библиотеки для скриптов на языке С#.
- `/var/lib/comindware``/instancename/Database/``snapshots` — снимки данных Apache Ignite.
- `/var/lib/comindware``/instancename/Database/wal` — файлы журнала предварительной записи.
- `/var/lib/comindware``/instancename/Streams` — загруженные пользователями и сформированные системой файлы, которые прикреплены к соответствующим атрибутам.
- Временные данные, обеспечивающие работу экземпляра ПО. В этих папках нет пользовательских данных и файлов базы данных экземпляра ПО:
    - `/var/lib/comindware``/instancename/Temp`
    - `/var/lib/comindware``/instancename/Database/cache`
    - `/var/lib/comindware``/instancename/Database/diagnostic`
    - `/var/lib/comindware``/instancename/Database/FullTextSearch`

_![Пример файла конфигурации instancename.yml](https://kb.comindware.ru/assets/img_66546f9baeb01.png)_

## Содержимое папок — Windows

База данных по умолчанию находится в папке с экземпляром ПО: `C``:\``ProgramData``\``Comindware``\``Instances``\instancename`. Здесь `instancename` — имя экземпляра ПО.

Просмотреть фактические пути к папкам экземпляра ПО можно в Утилите администрирования. См. статью *«[Настройка конфигурации и просмотр фактических путей к папкам экземпляра продукта](https://kb.comindware.ru/article.php?id=2036)»*).

- `C:\Program Files\Comindware\CBAP` — исполняемые файлы ПО разных версий.
- `C:\ProgramData\сomindware\configs` — общие файлы конфигурации ПО.
- `C:\ProgramData\сomindware\configs\instance\instancename.yml` — файл конфигурации. В этом файле задаются все остальные пути, перечисленные ниже..
- `C``:\` `ProgramData``\сomindware``\``Instances` — папка с экземплярами ПО.
- `C``:\``ProgramData``\сomindware``\``Instances``\instancename` — экземпляр ПО.
- `C``:\``ProgramData``\сomindware``\``Instances``\instancename``\``Config` — конфигурационные файлы:
    - `logs.config` (конфигурация журналов, см. статью *«[Подсистема журналирования](https://kb.comindware.ru/article.php?id=2501)»*);
    - `Web.config` (конфигурация экземпляра системы);
    - `Workers.config` (конфигурация системных служб экземпляра системы).
- `C``:\``ProgramData``\``сomindware``\``Instances``\instancename``\``Data` — файлы базы данных.
- `C``:\``ProgramData``\с``omindware``\``Instances``\instancename\Data\Scripts` — DLL-файлы, скомпилированные из скриптов на языке C#.
- `C``:\``ProgramData``\с``omindware``\``Instances``\instancename\Data\FullTextSearch` — индексы полнотекстового поиска.
- `C``:\``ProgramData``\с``omindware``\``Instances``\instancename\Streams` — файлы, загруженные пользователями и сформированные ПО.
- `C``:\``ProgramData``\с``omindware``\``Instances``\instancename\Logs` — журналы экземпляра ПО.
- `C``:\``ProgramData``\с``omindware``\``Instances``\instancename\Temp` — временные файлы.

--8<-- "related_topics_heading.md"

**[Настройка конфигурации и просмотр фактических путей к папкам экземпляра продукта](https://kb.comindware.ru/article.php?id=2036)**

**[Антивирусное ПО. Настройка исключений: пути и файлы Comindware Business Application Platform](https://kb.comindware.ru/article.php?id=2581)**

**[Подсистема журналирования](https://kb.comindware.ru/article.php?id=2501)**



{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
