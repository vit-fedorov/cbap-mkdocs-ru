---
title: 'Вычисление исполнителя активной задачи'
kbTitle: 'Вычисление исполнителя текущей активной задачи'
tags:
    - процессы
    - задачи
    - N3
    - исполнитель
hide:
    - tags
kbId: 4950
---

# Вычисление исполнителя активной задачи {: #n3_calculate_active_task_assignee }

## Введение {: #n3_calculate_active_task_assignee_intro }

В **{{ productName }}** можно вычислить ответственного за активную задачу по конкретной записи. Это может быть полезно для отображения информации об исполнителе или для использования в иных вычислениях.

## Прикладная задача {: #n3_calculate_active_task_assignee_use_case .pageBreakBefore }

Требуется определить исполнителя активной задачи для записи, связанной с бизнес-процессом.

## Настройка вычисления {: #n3_calculate_active_task_assignee_configure }

С помощью следующего выражения на N3 можно вычислить список исполнителей активной задачи и записать его в атрибут типа «**Аккаунт**» с установленным значком «**Хранить несколько значений**»:

``` turtle
# Импортируем функции для работы с логикой и задачами
@prefix cmw: <http://comindware.com/logics#>.
# Импортируем функции для работы с задачами
@prefix task: <http://comindware.com/ontology/task#>.
# Импортируем функции для работы со статусами задач
@prefix taskStatus: <http://comindware.com/ontology/taskStatus#>.
{
    # Находим задачу, связанную с текущей записью
    ?task task:objectId ?item.
    # Проверяем, является ли задача активной
    ?task cmw:taskStatus taskStatus:inProgress.
    # Определяем исполнителя задачи
    or {
        # Возвращаем фактического исполнителя
        ?task cmw:assignee ?value.
    }
    or {
        # Возвращаем список возможных исполнителей
        ?task cmw:possibleAssignee ?value.
    }
}
```

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- [Вычисление пользователей с активными задачами][n3_calculate_active_task_accounts]
- [Периодические напоминания об открытых задачах][n3_periodic_task_notifications]
- [Уведомления. Типы, назначение, настройка, использование][notification_types]

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
