---
kbId: 
title: 'Атрибут «Документ». Формирование ссылки на файл'
---

# Атрибут «Документ». Формирование ссылки на файл {: #document_uri}

## Введение

**{{ productName }}** позволяет прикрепить любые файлы к атрибуту типа «**Документ**». При этом он хранит не сами файлы непосредственно, а ссылки на них. Эти файлы доступны для скачивания по прямой ссылке без предоставления доступа к атрибуту типа «**Документ**».

Здесь представлена настройка текстового атрибута, в который помещаются ссылки на файлы, загруженные в атрибут типа «**Документ**», с помощью выражения N3.

!!! question "Структура атрибута типа «Документ»"

    --8<-- "attribute_document_logic.md"
    --8<-- "attribute_document_get_file_n3.md"
    --8<-- "attribute_document_get_file_formula.md"

## Прикладная задача

Имеется шаблон, к которому прикрепляются различные файлы. Требуется создать и настроить атрибут, в котором будут перечислены названия документов с ссылками на их скачивание.

## Исходные данные

В шаблоне _«Заявки»_ (системное имя _Requires_) имеется атрибут _«Вложения»_ со следующими свойствами:

- **Тип: документ**
- **Системное имя:** _Files_
- **Хранить несколько значений: флажок установлен**

## Настройка шаблона

1. Создайте текстовый атрибут со следующими настройками:

    - **Название:** _Ссылки для скачивания_
    - **Формат отображения: HTML-текст**
    - **Вычислять автоматически: флажок установлен**
    - **Вычисляемое значение:**
        - **N3**

            ``` turtle
            # Импортируем функции для работы
            # с документами и строками
            @prefix object: <http://comindware.com/ontology/object#>.
            @prefix document: <http://comindware.com/ontology/document#>.
            @prefix cmwstring: <http://comindware.com/logics/string#>.
            @prefix string: <http://www.w3.org/2000/10/swap/string#>.
            {
                # Находим атрибут «Вложения» (Files) и помещаем в ?filesAttribute
                ("Requires" "Files") object:findProperty ?filesAttribute.
                # Запускаем цикл
                from {
                    # Находим содержимое ?filesAttribute в текущей
                    # записи и помещаем в ?file
                    ?item ?filesAttribute ?file.
                    # Получаем текущую ревизию документа и
                    # помещаем в ?fileRevision
                    ?file document:currentRevision ?fileRevision.
                    # Получаем ссылку на файл без имени хоста
                    # и помещаем в ?fileUri
                    ?fileRevision document:httpUri ?fileUri.
                    # Помещаем имя файла в ?fileName
                    ?fileRevision document:name ?fileName.
                    # Формируем строки с именами файлов и ссылками на них
                    # и помещаем в ?formatUri
                    # 'https://host-name' — имя хоста {{ productName }}
                    ("<a href='https://host-name{0}'>{1}</a>" ?fileUri ?fileName) string:format ?formatUri.
                    }
                # Формируем ?uriList из ?formatUri.
                select ?formatUri -> ?uriList.
                # Формируем из ?uriList HTML из ссылок
                # с разделителем <br/> (перенос строки)
                # и возвращаем её в значение атрибута
                ("<br/>" ?uriList) cmwstring:join ?value.
            }
            ```

        **или**

        - **Формула:**

            ``` cs
            # Из атрибута «Вложения» (Files) собираем URI и имена всех прикреплённых файлов
            # и соединяем в HTML с разделителем <br/>
            # 'https://host-name' — имя хоста {{ productName }}
            JOIN("<br/>", from a in $Files select
                FORMAT("<a href='https://host-name{0}'>{1}</a>", 
                LIST(a->currentRevision->httpUri, a->currentRevision->revisionFilename)
                )
            )
            ```

2. Создайте **форму** _«Скачать вложения»_.
3. Поместите атрибут _«Ссылки для скачивания»_ на форму _«Скачать вложения»_.

## Тестирование

1. Создайте запись в шаблоне _«Заявки»_.
2. Прикрепите несколько файлов к атрибуту _«Вложения»_.
3. С помощью селектора <em class="fa-light fa-angle-down anchor">‌</em> перейдите к форме _«Скачать вложения»_.
4. В поле атрибута _«Ссылки для скачивания»_ отобразится список с ссылками на скачивание прикреплённых файлов.

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Атрибут типа «Документ»][attribute_document]_
- _[Атрибут типа «Документ». Скачивание архива с файлами из выбранных строк таблицы и записи][example_document_download_archive_csharp]_
- _[Атрибут типа «Документ». Скачивание архива с файлами из всех строк таблицы с прикреплением архива к атрибуту][example_document_download_archive_related_records_csharp]_
- _[Атрибут типа «Документ». Скачивание файлов в папку на сервере][example_document_download_to_server_csharp]_
- _[Атрибут типа «Документ». Клонирование записи вместе с прикреплёнными файлами][example_document_clone_scenario_n3]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
