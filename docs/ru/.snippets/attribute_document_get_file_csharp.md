- Чтобы считать файл из атрибута типа «**Документ**» с помощью C#-скрипта, необходимо:
    - из текущей записи получить массив идентификаторов файлов, прикреплённых к атрибуту:
        ```
        var fileIds = Api.TeamNetwork.ObjectService.GetPropertyValues(recordId, new [] {"documentAttributeSystemName"})`;
        ```
    - получить массив объектов с прикреплёнными файлами:
        ```
        var attachedFileObjects = fileIds[docId].TryGetValue("Files", out object fileObject) 
                                  && fileObject != null ? fileObject as object[] : null;
        ```
    - получить объект (`attachedFile`) файла:
        ```
        var attachedFile = Api.TeamNetwork.DocumentService.GetContent(attachedFileObject[0].ToString());
        ```
    - получить имя файла `attachedFile.Name`;
    - получить содержимое файла (`attachedFile.Data`).