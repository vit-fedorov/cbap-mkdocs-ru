---
tags:
  - выражения
  - n3
  - тройки
  - функции
  - findProperty
  - аргументы
  - шаблоны
  - атрибуты
  - системное имя
  - вычисляемые атрибуты
  - проверка значения
  - предиктивный ввод
  - подсказки
  - редактор выражений
  - сценарии
hide:
  - tags
---

# Ввод запроса ID атрибута с помощью функции object:findProperty

Функция `#!turtle object:findProperty` возвращает ID атрибута шаблона по заданным системным именам шаблона и атрибута. По ID атрибута можно получить его значение.
При предиктивном вводе для неё формируется заготовка и для ввода аргументов отображаются списки подходящих шаблонов и атрибутов.

1. Внутри фигурных скобок нажмите клавиши ++ctrl+space++.
2. В отобразившемся списке конструкций дважды нажмите функцию `FindProperty`.

    *![Список конструкций на языке N3](n3_editor_findproperty_autocomplete.png)*

3. В выражение будет вставлена заготовка функции:

    ```#!turtle
    ( ) object:findProperty ?foundProperty
    ```

4. В позиции первого аргумента (после открывающей скобки) нажмите клавиши ++ctrl+space++.
5. Отобразится список подходящих шаблонов в приложении.

    *![Список шаблонов в приложении](n3_editor_findproperty_argument1_autocomplete.png)*

6. Дважды нажмите системное имя шаблона, например `Zayavkanaotpusk`, чтобы вставить его в выражение.
7. В позиции второго аргумента (через пробел после первого) нажмите клавиши ++ctrl+space++.
8. Отобразится список атрибутов шаблона, выбранного на шаге 4.

    *![Список атрибутов шаблона](n3_editor_findproperty_argument2_autocomplete.png)*

9. Дважды нажмите системное имя атрибута, например `_creationDate`, чтобы вставить его в выражение.

{% include-markdown ".snippets/pdfPageBreakHard.md" %}

```turtle title="Пример: выражение, возвращающее месяц по значению атрибута типа «Дата и время»"
@prefix object: <http://comindware.com/ontology/object#>.
@prefix cmwtime: <http://comindware.com/logics/time#>.
{
    # Находим атрибут _creationDate шаблона Zayavkanaotpusk
    ("Zayavkanaotpusk" "_creationDate") object:findProperty ?dtProperty.

    # Определяем значение атрибута _creationDate
    # в текущей записи шаблона Zayavkanaotpusk
    ?item ?dtProperty ?dmonth.
    # Извлекаем номер месяца из значения атрибута _creationDate
    ?dmonth cmwutc:month ?value.
}
```

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- *[Редактор выражений][expression_editor]*
- *[Примеры использования языка N3. База знаний Comindware][n3_use_examples]*

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
