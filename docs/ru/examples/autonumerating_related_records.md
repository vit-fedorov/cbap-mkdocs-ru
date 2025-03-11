---
kbId:
title:
---

# Автонумерация связанных записей

## Введение

## Исходные данные

Имеется шаблон «**Заявки**». В нём имеется атрибут «**Документы**», связанный с шаблоном «**Реестр документов**».

## Настройка автонумерации

1. Добавьте текстовый атрибут _«Порядковый номер»_ в шаблоне «**Реестр документов**».
2. Создайте новый сценарий _«Автонумерация»_.
3. Настройте начальное событие «**Нажата кнопка**»:

    - **Контекстный шаблон:** _Заявки_
    - **Кнопка: Сохранить**

4. Добавьте действие «**Проверить результат выражения**» со следующими свойствами:

    - **Выражение: N3**

        ``` turtle
        @prefix variable: <http://comindware.com/ontology/session/variable#>.
        @prefix operator: <http://comindware.com/ontology/session/operator#>.
        {
            variable:index operator:replace 0.
            true -> ?value.
        }
        ```

5. Добавьте действие «**Сменить контекст**» со следующими свойствами:

    - Целевой шаблон записи: Реестр документов
    - Атрибут или выражения для поиска объектов: формула

        ``` cs
        from a in $Documents select a->id
        ```

6. Добавьте действие «**Изменить значения атрибутов**» внутрь действие «**Сменить контекст**» со следующими свойствами:

    - Атрибут: Порядковый номер
    - Действие: заменить
    - Значение: N3

        ``` turtle
        @prefix variable: <http://comindware.com/ontology/session/variable#>.
        @prefix operator: <http://comindware.com/ontology/session/operator#>.
        @prefix session: <http://comindware.com/ontology/session#>.
        @prefix string: <http://www.w3.org/2000/10/swap/string#>.
        @prefix math: <http://www.w3.org/2000/10/swap/math#>.
        {
            session:context variable:index ?startVal.
            
            (?startVal 1 )math:sum ?result.
            
            ("test {0}" ?result)string:format ?resultFormat.
            
            variable:index operator:replace ?result.
            ?resultFormat -> ?value.
        }
        ```