---
kbId: 2474
tags:
  - выражения
  - формулы
  - шаблоны
  - атрибуты
  - вычисляемые атрибуты
  - проверка значения
  - предиктивный ввод
  - подсказки
  - редактор выражений
  - сценарии
hide:
  - tags
---
# Ввод системного имени атрибута текущего шаблона

1. Введите символ `$`.
2. Отобразится список атрибутов текущего шаблона.
    *![Список атрибутов текущего шаблона](formula_editor_template_attribute_autocomplete.png)*
3. Дважды нажмите системное имя атрибута, чтобы вставить его в формулу.

```mysql title="Пример: формула, возвращающая целочисленное значение атрибута Passazhiry в текущей записи"
INT($Passazhiry)
```

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Редактор выражений][expression_editor]_
- _[Примеры использования формул. База знаний Comindware][formula_use_examples]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
