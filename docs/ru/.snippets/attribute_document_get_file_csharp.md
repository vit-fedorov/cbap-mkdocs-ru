- Чтобы считать файл из атрибута типа «**Документ**» с помощью C#-скрипта, необходимо:
    - из текущей записи получить массив идентификаторов файлов, прикреплённых к атрибуту:
        ``` cs
        var fileIds = Api.TeamNetwork.ObjectService.GetPropertyValues(recordId, new [] {"documentAttributeSystemName"})`;
        ```
    - получить массив объектов с прикреплёнными файлами:
        ``` cs
        var attachedFileObjects = fileIds[docId].TryGetValue("Files", out object fileObject) 
                                  && fileObject != null ? fileObject as object[] : null;
        ```
    - получить объект файла (`attachedFile`):
        ``` cs
        var attachedFile = Api.TeamNetwork.DocumentService.GetContent(attachedFileObjects[0].ToString());
        ```
    - получить имя файла с расширением (`attachedFile.Name`);
    - получить содержимое файла (`attachedFile.Data`);
    - при необходимости получить объект с метаданными документа:
        ``` cs
        var attachedFileMeta = Api.TeamNetwork.DocumentService.GetDocument(attachedFileObjects[0].ToString());
        ```
        - `attachedFileMeta.Title` — имя файла с расширением;
        - `attachedFileMeta.Extension` — расширение файла;
        - `attachedFileMeta.PreviewUri` относительная ссылка на файл.