---
title: Атрибут типа «Документ». Скачивание архива с файлами
tags:
    - C#
    - C#-скрипт
    - скрипт
    - скачать документы
    - документ
    - атрибут типа «Документ»
    - атрибут типа «Запись»
    - скачать файлы
    - скачать архив
hide: tags
kbId: 4921
---

# Атрибуты типа «Запись» и «Документ». Формирование и скачивание архива с файлами из связанных записей {: #download_document_archive_related_record}

## Введение

**{{ productName }}** позволяет прикрепить любые файлы к атрибуту типа «**Документ**». При этом, для каждой записи файл приходится скачивать отдельно.

Атрибут типа «**Запись**» позволяет настроить связь записи шаблона с документами, которые хранятся в отдельном реестре. С помощью C#-скрипта можно настроить кнопку для скачивания в одном архиве всех файлов, связанных с определённой записью.

Также при помощи сценария и C#-скрипта можно настроить добавление архива файлов в атрибут типа «**Документ**».

Здесь представлен пример настройки добавление архива файлов в атрибут по нажатию кнопки «**Сохранить**» и кнопки, скачивающей файлы из всех записей, которые связаны с текущей записью посредством атрибута.

## Прикладная задача

Имеется шаблон _«Заявки»_. С ним связан шаблон _«Реестр документов»_, в котором хранятся файлы.

Пользователь должен иметь возможность скачать все файлы из записей шаблона _«Реестр документов»_, которые связаны с записью шаблона _«Заявки»_.

## Настройка кнопки для скачивания файлов

Чтобы скачать документы, нужно настроить соответствующую кнопку и скрипт для неё.

1. Создайте **шаблон записи** _«Реестр документов»_.
2. Создайте следующие **атрибуты**:

    | Название       | Системное имя | Тип данных   | Свойства                                               |
    | -------------- | ------------- | ------------ | ------------------------------------------------------ |
    | _Наименование_ | _Name_        | **Текст**    |                                                        |
    | _Вложение_     | _Attachment_  | **Документ** | **Использовать для поиска записей:** флажок установлен |

    !!! warning "Внимание!"

        Для корректного скачивания файлов с помощью C#-скрипта у атрибута типа **«Документ**» рекомендуется установить флажок «**Использовать для поиска записей**». В противном случае скрипт может не сработать.

3. В **шаблоне записи** _«Заявки»_ создайте **атрибут**:

    | Название    | Системное имя | Тип данных | Свойства                                                                                                         |
    | ----------- | ------------- | ---------- | ---------------------------------------------------------------------------------------------------------------- |
    | _Документы_ | _Documents_   | **Запись** | <ul><li>**Связанный шаблон:** _Реестр документов_</li><li>**Хранить несколько значений:** флажок установлен</li> |

4. Создайте [**кнопку**][buttons] _«Скачать все вложения»_ со следующими свойствами:

    - **Контекст операции: запись**;
    - **Операция:** **С#-скрипт**;
    - **Результат выполнения: скачать документ**.

5. На вкладке «**Скрипт**» добавьте следующий C#-скрипт:

    ``` cs title="Скрипт для скачивания архива с файлами"
    using System; 
    using System.Collections.Generic;
    using System.IO; 
    using System.IO.Compression;
    using Comindware.Data.Entity;
    using Comindware.TeamNetwork.Api.Data.UserCommands;
    using Comindware.TeamNetwork.Api.Data;

    class Script
    {
        // Функция UserCommandResult указывает, что скрипт выполняется в контексте кнопки
        public static UserCommandResult Main(UserCommandContext userCommandContext, Comindware.Entities entities)
        { 
            // Получаем ID текущей записи шаблона «Заявки» из контекста операции кнопки.
            var id = userCommandContext.ObjectIds[0];
            // Помещаем в массив data идентификаторы записей шаблона «Реестр документов»
            // из атрибута «Документы» текущей записи.
            // Documents — системное имя атрибута «Документы».
            var data = Api.TeamNetwork.ObjectService.GetPropertyValues(new string[] {id}, new [] {"Documents"});
            // По идентификаторам получаем массив записей шаблона «Реестр документов», связанных с текущей записью.
            var DocumentsRecords = data[id].TryGetValue("Documents", out object OutputRecordArray) && OutputRecordArray != null ? OutputRecordArray as object[] : null;
            // Инициализируем словарь файлов для архива в виде пар «имя:содержимое».
            var files = new Dictionary<string, byte[]>();
            // Добавляем файлы в поток для дальнейшего архивирования
            // из каждой записи шаблона «Реестр документов».
            foreach (var DocumentRecord in DocumentsRecords)
            {
                // Получаем идентификатор записи шаблона «Реестр документов».
                var idDoc = DocumentRecord.ToString();
                // Помещаем в массив documentIds идентификаторы прикреплённых документов.
                // Attachment — системное имя атрибута «Вложение» шаблона «Реестр документов».
                var documentIds = Api.TeamNetwork.ObjectService.GetPropertyValues(new []{idDoc} , new [] {"Attachment"});
                // Из текущей записи берём идентификатор прикреплённого документа.
                var documentId = documentIds[idDoc].TryGetValue("Attachment", out object doc_Obj) && doc_Obj != null ? doc_Obj as string : null;
                if(documentId != null)
                {
                    // Получаем содержимое прикреплённого файла.
                    var documentData = Api.TeamNetwork.DocumentService.GetContent(documentId);
                    // Помещаем содержимое файла в словарь файлов для архива.
                    files[documentData.Name] = documentData.Data;
                }
            }
            // Формируем архив файлов из словаря files.
            var resultingArchive = Api.TeamNetwork.DocumentService.GetZippedStreams(files);
            // Возвращаем архив в качестве результата кнопки.
            return new UserCommandResult
            {
                Success = true,
                Commited = true,
                File = new UserCommandFileResult
                {
                    Content = resultingArchive,
                    // Укажите имя архива
                    Name = "Data.zip"
                }
            };
        }
    }
    ```

6. Поместите на форму шаблона _«Заявки»_ **атрибут** _«Документы»_ и настройте его **представление** в виде **таблицы**.
7. Поместите в таблицу _«Документы»_ на форме **атрибуты** _«Наименование»_ и _«Вложение»_ шаблона записи _«Реестр документов»_.
8. В область кнопок таблицы _«Документы»_ поместите кнопки «**Создать**».
9. В область кнопок формы шаблона _«Заявки»_ поместите кнопку _«Скачать все вложения»_.

## Настройка кнопки для добавления архива с вложениями в атрибут

1. В шаблоне _«Заявки»_ создайте атрибут _«Архив с вложениями»_ типа «**Документ**».эээээ
2. Поместите атрибут _«Архив с вложениями»_ на форму.
3. Создайте сценарий _«Добавление архива с вложениями»_.
4. Настройте событие «**Нажата кнопка**»:

    - **Контекстный шаблон:** _Заявки_
    - **Кнопка: сохранить**

5. Добавьте действие «**Изменить значение скриптом**» со следующими свойствами:

    - **Атрибут** _Архив с вложениями_
    - **Операция со значениями: заменить**
    - **Значение:**

        ``` cs
        using System;
        using System.Collections.Generic;
        using System.Linq;
        using Comindware.Data.Entity;
        using Comindware.TeamNetwork.Api.Data.UserCommands;
        using Comindware.TeamNetwork.Api.Data;
        using System.IO;
        using System.IO.Compression;

        class Script
        {
            public static void Main(Comindware.Process.Api.Data.ScriptContext context, Comindware.Entities entities)
            {
                var id = context.BusinessObjectId;
                byte[] compressedBytes;
                try
                {
                    using(var resultStream = new MemoryStream())
                    {
                        using(var zip = new ZipArchive(resultStream, ZipArchiveMode.Update))
                        {
                            // Укажите системное имя атрибута «Документы» шаблона «Заявки»
                            var data = Api.TeamNetwork.ObjectService.GetPropertyValues(new string[] {id}, new string[] {"Documents"});
                            // Укажите системное имя атрибута «Документы» шаблона «Заявки»
                            var documentIdsObj = data[id]["Documents"];

                            var documentIds = documentIdsObj as IEnumerable<object>;
                            if (documentIds == null)
                            {
                                documentIds = new string[] {documentIdsObj as string};
                            }
                            var newDocuments = new List<string>();
                            foreach (var documentIdObj in documentIds)
                            {
                                var documentId = documentIdObj as string;
                                // Укажите системное имя атрибута «Вложение» шаблона «Реестр документов»
                                if (!documentId.StartsWith("Attachment"))
                                    continue;
                                var documentData = Api.TeamNetwork.DocumentService.GetContent(documentId);

                                var startStream = new MemoryStream();
                                startStream.Write(documentData.Data, 0, documentData.Data.Length);
                                startStream.Seek(0, SeekOrigin.Begin);

                                var fileInArchive = zip.CreateEntry(documentData.Name , CompressionLevel.Optimal);
                                using (var entryStream = fileInArchive.Open())
                                {
                                    startStream.CopyTo(entryStream);
                                }
                            }
                        }
                        compressedBytes = resultStream.ToArray();
                    }
                    var docData = new Document 
                    {
                        Title = "Data"+".zip",
                        Extension = ".zip"
                        };
                    var resultStream2 = new MemoryStream();
                    resultStream2.Write(compressedBytes, 0, compressedBytes.Length);
                    resultStream2.Seek(0, SeekOrigin.Begin);

                    string doc = Api.TeamNetwork.DocumentService.CreateDocumentWithStream(docData, resultStream2, "");
                    var data2 = new Dictionary<string,object>
                    {
                        // Укажите ID атрибута «Архив с вложениями»
                        { "op.1", doc }
                    };
                    Api.TeamNetwork.ObjectService.Edit(id, data2);
                }
                catch
                {}
            }
        }
        ```

## Тестирование

1. Создайте новую запись шаблона _«Заявки»_ и добавьте несколько строк с документами в таблицу _«Документы»_.
2. Сохраните запись.
3. В поле атрибута _«Архив с вложениями»_ отобразится архив с файлами, которые связаны с записью шаблона _«Заявки»_.
4. Нажмите кнопку _«Скачать все вложения»_.
5. Браузер скачает архив со всеми файлами, которые связаны с записью шаблона _«Заявки»_.

    !!! note "Примечание"

        Если в браузере отобразится сообщение «**Незащищенное скачивание заблокировано**», нажмите кнопку «**Сохранить**», чтобы продолжить скачивание.

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Атрибут типа «Запись»][attribute_record]_
- _[Атрибут типа «Документ»][attribute_document]_
- _[Кнопки. Определение, настройка, удаление][buttons]_
- _[Написание скриптов на языке C#][manual_csharp]_
- _[Атрибут типа «Документ». Скачивание архива с файлами из таблицы и записи][download_document_archive_csharp]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
