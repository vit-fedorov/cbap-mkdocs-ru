---
title: Ввод заготовки конструкции на языке
kbId: 2480
tags:
  - выражения
  - n3
  - тройки
  - операторы
  - вычисляемые атрибуты
  - проверка значения
  - предиктивный ввод
  - подсказки
  - редактор выражений
  - сценарии
hide:
  - tags
---

# Ввод заготовки конструкции на языке N3 {: #n3_editor_block_autocomplete}

1. Введите фигурные скобки `{  }` в пустое выражение (после [префиксов][n3_editor_prefix_autocomplete]).
2. Внутри фигурных скобок нажмите клавиши ++ctrl+space++.
3. Отобразится список доступных конструкций.
4. Выберите конструкцию в списке, чтобы просмотреть её описание.
*![Список доступных конструкций N3](n3_editor_block_autocomplete.png)*
4. Дважды нажмите конструкцию в списке, чтобы вставить её заготовку в выражение.

```turtle title="Пример: заготовка конструкции if-then-else"
{
if { }
  then { }
  else { }.
}
```

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Ввод префикса][n3_editor_prefix_autocomplete]_
- _[Редактор выражений][expression_editor]_
- _[Примеры использования языка N3. База знаний Comindware]({{ kbCategoryURLPrefix }}408){:target="_blank"}_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
