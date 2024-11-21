---
title: Ввод предиката
kbId: 2479
---

# Ввод предиката

## Инструкции

1. В позиции предиката нажмите клавиши `Ctrl``Пробел`.
2. Отобразится список [объявленных префиксов][n3_editor_prefix_autocomplete].

_![Список доступных префиксов](https://kb.comindware.ru/assets/n3_editor_predicate_prefix_autocomplete.png)_
3. Выберите префикс в списке, чтобы просмотреть его описание.
4. Дважды нажмите префикс, например `task`, чтобы вставить его в выражение.
5. В позиции после префикса введите двоеточие `:`.
6. Отобразится список функций для префикса.

_![Список функций для префикса](https://kb.comindware.ru/assets/n3_editor_predicate_prefix_function_autocomplete.png)_
7. Дважды нажмите имя функции, например `objectId`, чтобы вставить его в выражение.

**Пример: выражение, возвращающее ID исполнителей выполняющихся задач для текущей записи**

```
@prefix cmw: <http://comindware.com/logics#>.
@prefix task: <http://comindware.com/ontology/task#>.
@prefix taskStatus: <http://comindware.com/ontology/taskStatus#>.
{
  # Получаем список ID задач, связанных с текущей записью
  ?task task:objectId ?item.
  # Получаем ID задач со статусом inProgress (Выполняется)
  ?task cmw:taskStatus taskStatus:inProgress.

  # Возвращаем ID назначенных исполнителей задач
  or {?task cmw:assignee ?value.}
  or {?task cmw:possibleAssignee ?value.}.
}
```

--8<-- "related_topics_heading.md"

**[Редактор выражений][expression_editor]**

**[Примеры использования языка N3](https://kb.comindware.ru/category.php?id=408)**

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
