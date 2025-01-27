---
title:
kbId:
---

# Значение связанного атрибута через разделитель

## Введение

## Прикладная задача

## Исходные данные

Имеется шаблон «Заказы» (Orders), с текстовым атрибутом «Номер заказа» (OrderNumber).

Имеется шаблон «Клиенты» (Clients) со следующим атрибутом:

| Название | Системное имя | Тип данных | Свойства |
|---|---|---|---|
| _Ф. И. О._ | _FullName_ | Текст | |
| _Заказы_ | _Orders_ | Запись | <li>Связанный шаблон: Заказы</li><li>Хранить несколько записей: флажок установлен</li> |

## Настройка шаблона

1. В шаблоне _«Клиенты»_ добавьте атрибут _«Номера заказов»_ со следующими свойствами:

    - Тип данных: текст
    - Вычислять автоматически: флажок установлен
    - Выражение для вычислений: N3

        ``` turtle
        # Импортируем функции для работы
        # с записями, строками и базой данных
        @prefix object: <http://comindware.com/ontology/object#>.
        @prefix account: <http://comindware.com/ontology/account#>.
        @prefix string: <http://www.w3.org/2000/10/swap/string#>.
        @prefix cmwstring: <http://comindware.com/logics/string#>.
        {
            # Находим в шаблоне Clients атрибут Orders
            # и помещаем в переменную
            ("Clients" "Orders") object:findProperty ?Kollekciya.
            # Находим в шаблоне Orders атрибут OrderNumber
            # и помещаем в переменную
            ("Orders" "OrderNumber") object:findProperty ?Atribyt.


            from {
                # Находим содержимое атрибута 
                ?item ?Kollekciya ?KollekciyaVal.
                ?KollekciyaVal ?Atribyt ?AtribytVal.

            } select ?AtribytVal -> ?ItogKomment.
          ("; " ?ItogKomment) cmwstring:join ?FinalString.
            
            ?FinalString -> ?value.
        }
        ```

2. Поместите атрибут _«Номера заказов»_ на форму.

## Тестирование

1. Создайте запись в шаблоне «Клиенты».
2. Добавьте несколько записей в таблицу «Заказы».
3. В поле «Номера заказов» отобразятся данные из связанных записей.

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- 

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
