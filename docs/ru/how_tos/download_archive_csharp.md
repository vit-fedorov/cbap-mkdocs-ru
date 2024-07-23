## Пример: кнопка для скачивания архива документов
## Введение

**Comindware Business Application Platform** позволяет прикрепить любые файлы к атрибуту типа «**Документ**». При этом, если к атрибуту прикреплено несколько файлов, на форме и в таблице каждый файл приходится скачивать отдельно.

С помощью C#-скрипта можно настроить кнопку для скачивания всех файлов, прикреплённых к атрибуту, в одном архиве. Более того, можно скачать все файлы, прикреплённые к атрибуту, из нескольких записей, выбранных в таблице.

В статье описано, как настроить кнопку, скачивающую файлы из выбранных записей в таблице. На форме эта кнопка будет скачивать файлы, прикреплённые к атрибуту в текущей записи.
## Прикладная задача

Имеется шаблон *«Реестр документов»*, в котором хранятся файлы. Каждый документ может содержать несколько файлов.
В записи шаблона *«Заявка»* можно указать документы из *«Реестра документов»*.

Пользователь должен иметь возможность скачать все файлы из всех выбранных строк в таблице на форме в заявке, из выбранных строк в *«Реестре документов»*, а также на форме одного документа.

## Настройка кнопки для скачивания файлов

Чтобы скачать документы, нужно настроить соответствующую кнопку и скрипт для неё.

1. Создайте **шаблон записи** *«Реестр документов»*.
2. Добавьте следующие **атрибуты**:

| Название       | Тип данных   | Свойства                                                                                                    |
| -------------- | ------------ | ----------------------------------------------------------------------------------------------------------- |
| *Наименование* | **Текст**    |                                                                                                             |
| *Вложение*     | **Документ** | **Хранить несколько значений:** флажок установлен<br>**Использовать для поиска записей:** флажок установлен |
3. Создайте [**кнопку**](https://kb.comindware.ru/article.php?id=2276) *«Скачать вложения»* со следующими свойствами:
    * **Контекст операции:** **запись**;
    * **Операция:** **С# скрипт**;
    * **Результат выполнения:** **скачать документ**.
4. На вкладке «**Скрипт**» добавьте следующий C#-скрипт:
```cs
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
    public static UserCommandResult Main(UserCommandContext userCommandContext, Comindware.Entities entities)
    {
        var selected_Ids = userCommandContext.ObjectIds;
        byte[] compressedBytes;
        var mes = "0";

        try
        {
// Vlozhenie - системное имя атрибута «Вложение» шаблона записи «Реестр документов»
            var data = Api.TeamNetwork.ObjectService.GetPropertyValues(selected_Ids, new[] { "Vlozhenie" });
            using (var resultStream = new MemoryStream())
            {
                using (var zip = new ZipArchive(resultStream, ZipArchiveMode.Update))
                {
                    foreach (var id in selected_Ids)
                    {
// Vlozhenie - системное имя атрибута «Вложение» шаблона записи «Реестр документов»
                        if (data[id].TryGetValue("Vlozhenie", out object doc_Obj) && doc_Obj != null)
                        {
                            var doc_Array = doc_Obj as object[];
                            if(doc_Array.Length > 0)
                            {
                                foreach(var doc in doc_Array)
                                {
                                    var documentData = Api.TeamNetwork.DocumentService.GetContent(doc.ToString());

                                    var startStream = new MemoryStream();
                                    startStream.Write(documentData.Data, 0, documentData.Data.Length);
                                    startStream.Seek(0, SeekOrigin.Begin);
                                    var fileInArchive = zip.CreateEntry(documentData.Name, CompressionLevel.Optimal);
                                    using (var entryStream = fileInArchive.Open())
                                    {
                                        startStream.CopyTo(entryStream);
                                    }
                                }
                            }
                        }
                    }
                }
                compressedBytes = resultStream.ToArray();
            }
            var memStream = new MemoryStream(compressedBytes);
            var sign_content = memStream.ToArray();

            var resulterr = new UserCommandResult
            {
                Success = true,
                Commited = true,
                File = new UserCommandFileResult()
                {
                    Content = sign_content,
// Имя архива для группы файлов
                    Name = "ZipedFiles.zip"
                    },
                Messages = new[]
                {
                    new UserCommandMessage
                    {
                        Severity = SeverityLevel.Normal,
                        Text = "Успешно"
                        }
                }
            };
            return resulterr;
        }
        catch
        {
            var resulterr = new UserCommandResult
            {
                Success = false,
                Commited = true,
                ResultType = UserCommandResultType.Notificate,
                Messages = new[]
                {
                    new UserCommandMessage
                    {
                        Severity = SeverityLevel.Normal,
                        Text = "Ошибка"
                        }
                }
            };
            return resulterr;
        }
    }
}
```
5. Вынесите на форму шаблона *«Реестр документов»* созданные атрибуты и кнопку *«Скачать вложения»*.
6. Настройте **таблицу** для всех записей и вынесите кнопку *«Скачать вложения»* на форму.
7. В **шаблоне записи** *«Заявка»* создайте **атрибут**:

| Название   | Тип данных | Свойства                                                                                       |
| ---------- | ---------- | ---------------------------------------------------------------------------------------------- |
| *Вложения* | **Запись** | **Связанный шаблон:** *Реестр документов*<br>**Хранить несколько значений:** флажок установлен |
8. Добавьте на форму шаблона *«Заявка»* **атрибут** *«Вложения»* и настройте его **представление** в виде **таблицы**.
9. Вынесите на форму в таблицу **атрибуты** *«Наименование»* и *«Вложение»* шаблона записи *«Реестр документов»*.
10. В область кнопок таблицы вынесите кнопку «**Создать**».
11. В область кнопок таблицы вынесите кнопку *«Скачать вложения»*.
## Тестирование

1. Создайте новую запись шаблона *«Заявка»* и добавьте несколько строк с документами в таблицу вложений.
2. Выберите вложения для скачивания и нажмите кнопку *«Скачать вложения»*.
3. Браузер скачает архив с выбранными файлами.

**Примечание**
В браузере может отобразиться сообщение: «Незащищенное скачивание заблокировано». Чтобы продолжить скачивание, нажмите кнопку «Сохранить».

4. Перейдите к таблице всех записей шаблона *«Реестр документов»*.
5. Выберите записи, из которых нужно скачать вложения, и нажмите кнопку *«Скачать вложения»*.
6. Браузер скачает архив с выбранными файлами.
7. Перейдите в любую запись шаблона *«Реестр документов»* и нажмите кнопку *«Скачать вложения»*.
8. Браузер скачает архив с файлами, прикреплёнными к записи. 
![Отображение кнопки «Скачать вложения» в таблице записей шаблона «Реестр документов»](Pasted%20image%2020240710121848.png)
## Связанные статьи

[Атрибут типа «Документ»](https://kb.comindware.ru/article.php?id=2241)

[Кнопки. Определение, настройка, удаление](https://kb.comindware.ru/article.php?id=2276)
## Теги

C#
C#-скрипт
скрипт
скачать документы