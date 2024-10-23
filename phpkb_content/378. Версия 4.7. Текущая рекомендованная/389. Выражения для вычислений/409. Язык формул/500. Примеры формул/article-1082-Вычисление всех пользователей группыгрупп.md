---
title: Вычисление всех пользователей группы/групп
kbId: 1082
---

# Вычисление всех пользователей группы/групп

Для вычисления пользователей, входящих в определённую/ые группу/ы без учета подгрупп и их участников (в случае, если в группе нет вложенности), введите следующее выражение:

| (from ag in db->\_AccountGroup where OR (ag->groupName == "users",ag->groupName == "admins") select ag->groupUsers->id) |
| --- |

**где:**

**"users", "admins"** — названия групп.

Альтернатива статье [Вычисление всех пользователей группы](https://kb.comindware.ru/article.php?id=2488).

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
