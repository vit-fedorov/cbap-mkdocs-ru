---
title: Ввод значений из атрибута типа «Список значений»
kbId: 5044
---

# Ввод значений из атрибута типа «Список значений»

## Инструкции

Если предикат определяет [атрибут типа «Список значений»][attribute_enum], предиктивный ввод подсказывает значения из этого списка.

1. Введите предикат, например `cmw:taskStatus`, который определяет системный [атрибут типа «Список значений»][attribute_enum], содержащий статус задачи.
2. В позиции через пробел после предиката нажмите клавиши `Ctrl` `Пробел`.
3. В отобразившемся списке значений нажмите требуемое значение, например `taskStatus:inProgress` (активная задача), чтобы вставить его в выражение.

_![Список значений атрибута taskStatus](https://kb.comindware.ru/assets/n3_editor_enum_autocomplete.png)_

**Пример: выражение, возвращающее список задач со статусом «Выполняется»**

```
@prefix cmw: <http://comindware.com/logics#>.
@prefix taskStatus: <http://comindware.com/ontology/taskStatus#>.
{
  ?value cmw:taskStatus taskStatus:inProgress.
}
```

--8<-- "related_topics_heading.md"

**[Редактор выражений][expression_editor]**

**[Примеры использования языка N3](https://kb.comindware.ru/category.php?id=877)**

**[Атрибут типа «Список значений»][attribute_enum]**

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
