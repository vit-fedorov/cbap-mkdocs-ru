---
title: Вычисление исполнителя текущей активной задачи
kbId: 4950
---

# Вычисление исполнителя текущей активной задачи

Для того, чтобы вычислить ответственного за текущую задачу по конкретной записи, введите следующее выражение:

| @prefix cmw: <http://comindware.com/logics#>. @prefix task: <http://comindware.com/ontology/task#>. @prefix taskStatus: <http://comindware.com/ontology/taskStatus#>.   {   ?task task:objectId ?item.   ?task cmw:taskStatus taskStatus:inProgress.      or {?task cmw:assignee ?value.}   or {?task cmw:possibleAssignee ?value.}. } |
| --- |

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
