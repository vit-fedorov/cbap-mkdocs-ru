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

# Вычисление исполнителя активной задачи {: #calculate_active_task_assignee }

## Введение {: #calculate_active_task_assignee_intro }

В **{{ productName }}** можно вычислить ответственного за текущую активную задачу по конкретной записи. Это может быть полезно для отображения информации об исполнителе или для использования в других вычислениях.

## Прикладная задача {: #calculate_active_task_assignee_use_case .pageBreakBefore }

Требуется определить исполнителя текущей активной задачи для конкретной записи.

## Настройка вычисления {: #calculate_active_task_assignee_configure }

Для вычисления исполнителя активной задачи используйте следующее выражение N3:

``` turtle
@prefix cmw: <http://comindware.com/logics#>.
@prefix task: <http://comindware.com/ontology/task#>.
@prefix taskStatus: <http://comindware.com/ontology/taskStatus#>.
{
    ?task task:objectId ?item.
    ?task cmw:taskStatus taskStatus:inProgress.
    or {?task cmw:assignee ?value.}
    or {?task cmw:possibleAssignee ?value.}
}
```

!!! note "Примечание"

    Это выражение можно использовать в атрибуте типа «Аккаунт» для хранения информации об исполнителе текущей активной задачи.

## Тестирование {: #calculate_active_task_assignee_test }

1. Создайте атрибут типа «Аккаунт».
2. В качестве вычисляемого значения укажите приведенное выше выражение N3.
3. Проверьте, что атрибут содержит информацию об исполнителе текущей активной задачи.

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- [Вычисление пользователей с активными задачами][calculate_active_task_accounts]
- [Периодические напоминания об открытых задачах][n3_periodic_task_notifications]
- [Уведомления. Типы, назначение, настройка, использование][notification_types]

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
