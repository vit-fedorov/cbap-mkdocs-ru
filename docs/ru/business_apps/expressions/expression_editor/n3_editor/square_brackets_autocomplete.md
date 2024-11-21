---
tags:
  - выражения
  - n3
  - тройки
  - функции
  - аргументы
  - ObjectAlias
  - object:alias
  - приложения
  - шаблоны
  - атрибуты
  - системное имя
  - квадратные скобки
  - вычисляемые атрибуты
  - проверка значения
  - предиктивный ввод
  - подсказки
  - редактор выражений
  - сценарии
hide:
  - tags
---

# Ввод запроса списка записей шаблона по его системному имени с помощью функции object:alias

Функция `#!turtle object:alias` возвращает записи шаблона с заданным системным именем. При предиктивном вводе для неё формируется заготовка, отображается список подходящих шаблонов и формируется компактный запрос записей выбранного шаблона с использованием квадратных скобок.

1. Внутри фигурных скобок нажмите клавиши ++ctrl+space++.
2. В отобразившемся списке конструкций дважды нажмите функцию `ObjectAlias`.
*![Список конструкций на языке N3](n3_editor_square_brackets_autocomplete.png)*
3. В выражение будет вставлена заготовка функции:

  ```turtle
  a [object:alias ].
  ```

4. В позиции перед закрывающей квадратной скобкой нажмите клавиши ++ctrl+space++.
5. Отобразится список шаблонов в приложении.
*![Список шаблонов в приложении](n3_editor_square_brackets_templates_autocomplete.png)*
6. Дважды нажмите системное имя шаблона, например `Zayavkanaotpusk`.
7. В выражение будет вставлен запрос записей выбранного шаблона:
  ```turtle
  ?objectZayavkanaotpusk a [object:alias "Zayavkanaotpusk"].
  ```
8. Чтобы присвоить результат выражения значению вычисляемого атрибута, замените имя переменной `objectZayavkanaotpusk` на `value`.

{% include-markdown ".snippets/pdfPageBreakHard.md" %}

```turtle title="Пример: компактное выражение, возвращающее все записи шаблона по его системному имени"
@prefix object: <http://comindware.com/ontology/object#>.
{
  # Получаем список записей шаблона Zayavkanaotpusk
  ?value a [object:alias "Zayavkanaotpusk"].
}
```

```turtle title="Эквивалентное выражение без квадратных скобок"
@prefix object: <http://comindware.com/ontology/object#>.
{
  # Получаем ID шаблона Zayavkanaotpusk
  ?zayavkiTemplate object:alias "Zayavkanaotpusk".
  # Получаем список записей шаблона Zayavkanaotpusk
  ?value a ?zayavkiTemplate.
}
```

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Редактор выражений][expression_editor]_
- _[Примеры использования языка N3. База знаний Comindware][n3_use_examples]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
