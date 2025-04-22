---
title: 'Выгрузка выбранных записей из пользовательской таблицы'
kbId: 5008
---

# Выгрузка выбранных записей из пользовательской таблицы {: #example_csharp_table_download_selected_entries }

## Введение

Здесь представлен пример скрипта для скачивания выбранных столбцов и строк из таблицы в виде файла Excel.

Скрипт запускается по нажатию кнопки.

Приведённый пример скрипта поддерживает экспорт столбцов следующих типов:

- **Логический**
- **Число**
- **Длительность**
- **Текст**
- **Запись**
- **Дата и время**
- **Аккаунт**

## Прикладная задача

Имеется шаблон _«Заявки»_.

Требуется экспортировать из таблицы в шаблоне _«Заявки»_ строки и столбцы, выбранные пользователем.

Данные должны выгружаться в файл формата `XLSX` по нажатию кнопки.

Пользователь выбирает столбцы и строки экспорта следующим образом:

- устанавливает флажки выбора в требуемых строках  выбираются
- скрывает ненужные столбцы с помощью меню «**Мои настройки**» <i class="fa-light fa-edit"></i> — «**Настроить внешний вид**» <i class="fa-light fa-table"></i>.

## Настройка скрипта

1. В шаблоне _«Заявки»_ создайте кнопку со следующими свойствами:

    - **Отображаемое название:** _Экспортировать в Excel_
    - **Контекст операции: запись**
    - **Операция: C#-скрипт**
    - **Результат выполнения: скачать документ**

2. Сохраните кнопку.
3. На вкладке «**Скрипт**» введите следующий код:

    ``` cs
    // Импорт базовых типов и функций .NET Framework для работы с основными типами данных.
    using System;
    // Импорт расширений LINQ для работы с коллекциями и выполнения запросов.
    using System.Linq;
    // Импорт классов для обработки нажатий кнопок и возврата результатов выполнения скрипта.
    using Comindware.TeamNetwork.Api.Data.UserCommands;
    // Импорт основных классов для работы с данными в {{ pdroductName }}.
    using Comindware.TeamNetwork.Api.Data;
    // Импорт классов для работы с формами.
    using Comindware.TeamNetwork.Api.Data.Forms;
    // Импорт классов для работы с потоками данных, файлами и операциями ввода-вывода.
    using System.IO;
    // Импорт библиотеки Aspose.Cells для создания и форматирования документов Excel.
    using Aspose.Cells;
    // Импорт дополнительных классов Aspose.Cells для работы с таблицами и их стилями в Excel.
    using Aspose.Cells.Tables;

    class Script
    {
        // userCommandContext содержит данные контекста при нажатии кнопки.
        public static UserCommandResult Main(UserCommandContext userCommandContext, Comindware.Entities entities)
        {
            // Получаем ID выбранных записей в таблице при нажатии кнопки.
            var items = userCommandContext.ObjectIds as string[];
            if(items.Count() > 0)
            {
                try
                {
                    // Получаем ID таблицы, в которой была нажата кнопка.
                    var listId = userCommandContext.Query.DatasetId;
                    // Получаем параметры разбиения таблицы на страницы.
                    var paging = userCommandContext.Query.Paging;
                    // Получаем параметры сортировки данных в таблице.
                    var sorting = userCommandContext.Query.Sorting;
                    // Получаем параметры фильтрации данных в таблице.
                    var filter = userCommandContext.Query.Filter;
                    // Получаем ID шаблона, к которому относится таблица, по ID первой из записей.
                    var containerId = Api.Base.OntologyService.GetAxioms(items.First())["cmw.container"].First().ToString();
                    // Получаем все таблицы шаблона для дальнейшей обработки.
                    var dataTables = Api.TeamNetwork.DatasetService.GetQueries(containerId); 

                    // Создаём пустую таблицу.
                    Dataset dataset;
                    // Создаём пустой файл Excel для экспорта данных.
                    Workbook workbook = new Workbook();
                    // Получаем первый лист рабочей книги для заполнения данными.
                    Worksheet wh = workbook.Worksheets[0];

                    // Создаём стили для форматирования ячеек Excel.
                    var style = workbook.CreateStyle();
                    // Разрешаем числовые типы для форматирования.
                    var flag = new StyleFlag();
                    flag.NumberFormat = true;

                    // Перебираем все таблицы шаблона для поиска нужной таблицы.
                    foreach(var table in dataTables)
                    {
                        // Применяем параметры пагинации, сортировки и фильтрации к таблице.
                        table.Paging = paging;
                        table.Sorting = sorting;
                        table.Filter = filter;
                        // Проверяем, что текущая таблица - это та, на которой нажали кнопку выгрузки.
                        if(table.DatasetId == listId)
                        {
                            // Получаем персональные настройки таблицы для определения видимых столбцов.
                            var personalDataset = Api.TeamNetwork.DatasetConfigurationService.GetPersonalDataset(table.DatasetId);
                            // Получаем данные таблицы, включая значения и структуру столбцов.
                            dataset = Api.TeamNetwork.DatasetService.QueryData(table);
                            // Создаем массив для хранения информации о видимых столбцах.
                            var tableColumns = new Container[personalDataset.Columns.Count()];
                            // Инициализируем счётчик видимых столбцов.
                            var i=0;
                            // Перебираем все столбцы из персональных настроек таблицы.
                            foreach(var coll in personalDataset.Columns)
                            {
                                // Проверяем, что столбец не скрыт пользователем.
                                if(!coll.IsHidden)
                                {
                                    // Создаем контейнер для хранения информации о столбце и его позиции.
                                    tableColumns[i] = new Container(coll.DataSourceInfo.Id, i);
                                    // Записываем название столбца в заголовок Excel.
                                    wh.Cells[0,i].PutValue(coll.Name);
                                    // Получаем путь к свойству столбца для определения его типа.
                                    var prop = coll.DataSourceInfo.PropertyPath.Last().ToString();

                                    // Проверяем, что свойство не является системным.
                                    if(prop != "id" && prop != "lastWriteDate" && prop != "creationDate" && prop != "В архиве" && prop != "creator" && prop != "processes" && prop != "isDisabled")
                                    {
                                        // Получаем метаданные свойства для определения его типа.
                                        var propData = Api.Base.OntologyService.GetAxioms(prop);
                                        // Извлекаем тип свойства из метаданных.
                                        prop = propData["cmw.propertyType"].Last().ToString();
                                    }

                                    // В зависимости от типа данных настраиваем разные стили для столбцов.
                                    switch(prop)
                                    {
                                        case "xsd.decimal":
                                            {
                                                // Устанавливаем числовой формат (код 1) для десятичных чисел.
                                                style.Number = 1;
                                                // Применяем стиль к столбцу.
                                                wh.Cells.Columns[i].ApplyStyle(style, flag);
                                            }break;
                                            case "lastWriteDate":
                                                {
                                                    // Устанавливаем формат даты (код 22) для столбца даты последнего изменения.
                                                    style.Number = 22;
                                                    // Применяем стиль к столбцу.
                                                    wh.Cells.Columns[i].ApplyStyle(style, flag);
                                                    // Устанавливаем ширину столбца для удобства отображения даты.
                                                    wh.Cells.Columns[i].Width = 15;
                                                }break;
                                                case "creationDate":
                                                    {
                                                        // Устанавливаем формат даты для столбца даты создания.
                                                        style.Number = 22;
                                                        // Применяем стиль к столбцу.
                                                        wh.Cells.Columns[i].ApplyStyle(style, flag);
                                                        // Устанавливаем ширину столбца для удобства отображения даты.
                                                        wh.Cells.Columns[i].Width = 15;
                                                    }break;
                                                    case "xsd.dateTime":
                                                        {
                                                            // Устанавливаем формат даты для столбца даты и времени.
                                                            style.Number = 22;
                                                            // Применяем стиль к столбцу.
                                                            wh.Cells.Columns[i].ApplyStyle(style, flag);
                                                            // Устанавливаем ширину столбца для удобства отображения даты и времени.
                                                            wh.Cells.Columns[i].Width = 15;
                                                        }break;
                                    }
                                    // Увеличиваем счётчик видимых столбцов.
                                    i++;
                                }
                            }
                            // Инициализируем счётчик строк, начиная с 1 (0 - заголовки).
                            var j=1;
                            // Инициализируем счётчик для определения позиции столбца в исходных данных.
                            var y = 0;
                            // Перебираем все столбцы из набора данных для определения их позиций.
                            foreach(var coll in dataset.Columns)
                            {
                                try
                                {
                                    // Получаем идентификатор источника данных столбца.
                                    var ds = coll.DataSourceInfo.Id;
                                    // Находим индекс столбца в массиве видимых столбцов.
                                    var t = Array.Find(tableColumns, x=> x.DS == ds).Id;
                                    // Сохраняем позицию столбца в исходных данных.
                                    tableColumns[t].Place = y;
                                }catch{}
                                // Увеличиваем счётчик позиции.
                                y++;
                            }

                            // Перебираем все строки из набора данных.
                            foreach(var row in dataset.Rows)
                            {
                                // Проверяем, что строка выбрана пользователем для экспорта.
                                if(Array.Find(items, v => v == row.Id) != null)
                                {
                                    // Получаем данные строки.
                                    var rowData = row.Data;
                                    // Перебираем все видимые столбцы.
                                    for(var jj = 0; jj < i; jj++)
                                    {
                                        // Получаем позицию столбца в исходных данных.
                                        var ii = tableColumns[jj].Place;
                                        // Проверяем, что данные в ячейке не пустые.
                                        if(rowData[ii] != null)
                                        {
                                            // Проверяем тип данных в ячейке и обрабатываем их соответственно.
                                            if(rowData[ii].GetType() != typeof(Comindware.TeamNetwork.Api.Data.Forms.AccountReference) && rowData[ii].GetType() != typeof(System.Boolean) && rowData[ii].GetType() != typeof(Comindware.TeamNetwork.Api.Data.Forms.InstanceReference))
                                            {
                                                // Для обычных типов данных просто записываем значение в ячейку.
                                                wh.Cells[j,jj].PutValue(rowData[ii]);
                                            }
                                            else if (rowData[ii].GetType() == typeof(Comindware.TeamNetwork.Api.Data.Forms.AccountReference))
                                            {
                                                // Для ссылок на аккаунты записываем только имя аккаунта.
                                                wh.Cells[j,jj].PutValue(((AccountReference)rowData[ii]).Name);
                                            }
                                            else if(rowData[ii].GetType() == typeof(System.Boolean))
                                            {
                                                // Для логических значений преобразуем их в текстовый формат.
                                                if((bool)rowData[ii])
                                                {
                                                    wh.Cells[j,jj].PutValue("Истина");
                                                }
                                                else
                                                {
                                                    wh.Cells[j,jj].PutValue("Ложь");
                                                }
                                            }
                                            else if(rowData[ii].GetType() == typeof(Comindware.TeamNetwork.Api.Data.Forms.InstanceReference))
                                            {
                                                // Для ссылок на записи записываем только имя записи.
                                                wh.Cells[j,jj].PutValue(((Comindware.TeamNetwork.Api.Data.Forms.InstanceReference)rowData[ii]).Name);
                                            }
                                        }
                                    }
                                    // Увеличиваем счётчик строк после обработки текущей строки.
                                    j++;
                                }
                            }
                            // Создаем таблицу в Excel для улучшения внешнего вида и функциональности.
                            ListObject listObject = wh.ListObjects[wh.ListObjects.Add(0,0, j-1,i-1, true)];
                        }
                    }

                    // Создаем поток в памяти для сохранения файла Excel.
                    MemoryStream stream = new MemoryStream();
                    // Сохраняем рабочую книгу в поток в формате XLSX.
                    workbook.Save(stream, SaveFormat.Xlsx);

                    // Создаем результат команды пользователя с успешным статусом.
                    var result = new UserCommandResult
                    {
                        Success = true,
                        Commited = true,

                        File=new UserCommandFileResult(){
                            Content = stream.ToArray(),
                            // Задаём имя файла для экспорта.
                            Name = "ЭкспортИзТаблицы.xlsx"
                            },

                        Messages = new[]
                        {
                            new UserCommandMessage
                            {
                                Severity = SeverityLevel.Normal,
                                Text = "Экспорт выполнен"
                                }
                        }
                    };
                    return result;

                }
                catch
                {
                    // Создаем результат команды пользователя с ошибкой.
                    var result1 = new UserCommandResult
                    {
                        Success = false,
                        Commited = true,
                        Messages = new[]
                        {
                            new UserCommandMessage
                            {
                                Severity = SeverityLevel.Normal,
                                Text = "Не удалось выполнить экспорт"
                                }
                        }
                    };
                    return result1;
                }
            }
            else
            {
                // Создаем результат команды пользователя с ошибкой, если не выбрано ни одной записи.
                var result1 = new UserCommandResult
                {
                    Success = false,
                    Commited = true,
                    Messages = new[]
                    {
                        new UserCommandMessage
                        {
                            Severity = SeverityLevel.Normal,
                            Text = "Неудачно"
                            }
                    }
                };
                return result1;
            }
        }

        // Вспомогательный класс для хранения информации о столбцах таблицы.
        public class Container
        {
            // Идентификатор столбца в массиве видимых столбцов.
            public int Id {get;set;}
            // Позиция столбца в исходных данных.
            public int Place {get;set;}
            // Идентификатор источника данных столбца.
            public string DS {get;set;}

            // Конструктор класса Container.
            public Container(string ds , int id )
            {
                DS = ds; Id = id;
            }
        }
    }
    ```

4. Сохраните кнопку.
5. Поместите кнопку _«Экспортировать в Excel»_ на **область кнопок** таблицы «**Все записи**» шаблона _«Заявки»_.

## Тестирование скрипта

1. Откройте таблицу «**Все записи**» шаблона _«Заявки»_.
2. Откройте меню «**Мои настройки**» <i class="fa-light fa-edit"></i> — «**Настроить внешний вид**» <i class="fa-light fa-table"></i>.
3. Скройте любой из столбцов таблицы и сохраните настройки внешнего вида.
4. Выберите требуемые строки в таблице с помощью флажков в левом столбце.
5. Нажмите кнопку _«Экспортировать в Excel»_.
6. Браузер должен скачать файл формата `.XLSX` с выбранными данными.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
