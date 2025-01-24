---
title: Сценарий проверка и изменение данных с помощью действия «Проверить результат скрипта»
kbId:
---

# Сценарий проверка и изменение данных с помощью действия «Проверить результат скрипта»


## Исходные данные

Имеется шаблон _«Заявки»_. В нём есть текстовый атрибут _«Комментарий»_ (_Comment_) и логический атрибут _«Заявка заполнена»_ (_RequireFilled_). Требуется настроить проверку данных и заполнение значения атрибута с помощью действия сценария «Проверить результат скрипта».

## Настройка сценария

1. Создайте новый сценарий _«Заполнение заявок»_.
2. В начальном событии «**Нажата кнопка**» выберите контекстный шаблон _«Заявки»_ и кнопку «**Сохранить**».
3. Добавьте действие «**Проверить результат скрипта**» со следующими свойствами:

    - **Сообщение об ошибке:** _Длительность поездки не может быть нулевой_
    - **Выражение:**

    ``` cs
    using System; 
    using System.Collections.Generic;
    using System.Linq;
    using Comindware.Data.Entity;
    using Comindware.TeamNetwork.Api.Data.UserCommands;
    using Comindware.TeamNetwork.Api.Data;

    class Script
    {
        public static bool Main(Object FullObjectId)
        { 
            var ObjectId = FullObjectId.ToString().Replace("user.", "");
            var data = Api.TeamNetwork.ObjectService.GetPropertyValues(new []{ObjectId}, new []{"Comment"});
            var dataLog = data[ObjectId].TryGetValue("Comment", out object OutputRecordArray) && OutputRecordArray != null ? OutputRecordArray as string : null; 
                                                                    
            if(dataLog != null)
            {        
             	var Dict = new Dictionary<string,object>
                {
                    { "RequireFilled", true }
                }; 
                Api.TeamNetwork.ObjectService.EditWithAlias(ObjectId, Dict);
                return true;
            }
            else
            {
                return false;
            }

        }
    }
    ```

## Тестирование сценария

1. Создайте заявку и не заполняйте поле _«Комментарий»_.
2. Нажмите кнопку «**Сохранить**».
3. На экране отобразится сообщение _«Длительность поездки не может быть нулевой»_.
4. Заполните поле _«Длительность поездки»_ и нажмите кнопку «**Сохранить**».
5. Отобразится сообщение об успешном сохранении записи.

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Событие и действия сценария. Определения, типы, свойства, настройка][scenario_elements]_
- _[Отладка формул, выражений N3, сценариев и C#-скриптов][expression_debug]_

</div>

{%
include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md"
%}
