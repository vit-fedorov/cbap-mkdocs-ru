---
title:
kbId:
---

# Значение связанного атрибута через разделитель

## Введение

## Прикладная задача

## Исходные данные

Имеется шаблон «Заказы», с текстовым атрибутом «Номер заказа».

Имеется шаблон «Клиенты» со следующим атрибутом:

| Название | Системное имя | Тип данных | Свойства |
|---|---|---|---|
| Ф. И. О. | FullName | Текст

## Настройка шаблона

1.

``` turtle
# Импортируем функции для работы
# с записями, строками и базой данных
@prefix object: <http://comindware.com/ontology/object#>.
@prefix account: <http://comindware.com/ontology/account#>.
@prefix string: <http://www.w3.org/2000/10/swap/string#>.
@prefix cmwstring: <http://comindware.com/logics/string#>.
{
    ("Tekyshiishablon" "Kollekciya") object:findProperty ?Kollekciya.
    ("Shablonkollekcii" "Atribyt") object:findProperty ?Atribyt.


    from {
        ?item ?Kollekciya ?KollekciyaVal.
        ?KollekciyaVal ?Atribyt ?AtribytVal.

    } select ?AtribytVal -> ?ItogKomment.
  ("; " ?ItogKomment) cmwstring:join ?FinalString.
    
    ?FinalString -> ?value.
}
```
