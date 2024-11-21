---
tags:
  - выражения
  - n3
  - тройки
  - функции
  - атрибуты
  - предикаты
  - taskStatus
  - список значений
  - статус задачи
  - задача
  - enum
  - атрибут типа «Список значений»
  - вычисляемые атрибуты
  - проверка значения
  - предиктивный ввод
  - подсказки
  - редактор выражений
  - сценарии
hide:
  - tags
---

# Ввод значений из атрибута типа «Список значений»

Если предикат определяет [атрибут типа «Список значений»][attribute_enum], предиктивный ввод подсказывает значения из этого списка.

1. Введите предикат, например `#!turtle cmw:taskStatus`, который определяет системный [атрибут типа «Список значений»][attribute_enum], содержащий статус задачи.
2. В позиции через пробел после предиката нажмите клавиши ++ctrl+space++.
3. В отобразившемся списке значений нажмите требуемое значение, например `#!turtle taskStatus:inProgress` (активная задача), чтобы вставить его в выражение.
*![Список значений атрибута taskStatus](n3_editor_enum_autocomplete.png)*

```turtle title="Пример: выражение, возвращающее список задач со статусом «Выполняется»"
@prefix cmw: <http://comindware.com/logics#>.
@prefix taskStatus: <http://comindware.com/ontology/taskStatus#>.
{
  ?value cmw:taskStatus taskStatus:inProgress.
}
```

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Редактор выражений][expression_editor]_
- _[Примеры использования языка N3. База знаний Comindware][n3_use_examples]_
- _[Атрибут типа «Список значений»][attribute_enum]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
