---
title: 'Вычисление пользователей с активными задачами'
kbTitle: 'Вычисление пользователей, у которых есть активные задачи (с учетом замещений)'
tags:
    - процессы
    - уведомления
    - N3
    - задачи
    - замещения
hide:
    - tags
kbId: 4966
---

# Вычисление пользователей с активными задачами {: #calculate_active_task_accounts }

## Введение {: #calculate_active_task_accounts_intro }

В **{{ productName }}** можно вычислить всех пользователей, у которых на данный момент есть активные задачи, с учетом всех замещений. Это может быть полезно, например, для запуска подпроцесса отправки уведомлений по задачам.

## Прикладная задача {: #calculate_active_task_accounts_use_case .pageBreakBefore }

Требуется настроить процесс для отправки уведомлений пользователям, у которых есть активные задачи, с учетом всех замещений.

## Настройка процесса {: #calculate_active_task_accounts_configure }

Для вычисления пользователей с активными задачами используйте следующее выражение N3:

``` turtle
@prefix cmw: <http://comindware.com/logics#>.
@prefix container: <http://comindware.com/ontology/container#>.
@prefix account: <http://comindware.com/ontology/account#>.
@prefix taskStatus: <http://comindware.com/ontology/taskStatus#>.
{
    ?class cmw:className "Account".
    ?value a ?class.
    ?value account:active true.
    not {?value cmw:isDisabled true.}.
    or {?tasks cmw:assignee ?value.}
    or {?tasks cmw:possibleAssignee ?value.}.
    ?tasks cmw:taskStatus taskStatus:inProgress.
}
```

!!! note "Примечание"

    Это выражение можно использовать в атрибуте типа «Аккаунт» с установленным флажком «Хранить несколько значений» для хранения списка пользователей с активными задачами.

## Тестирование {: #calculate_active_task_accounts_test }

1. Создайте атрибут типа «Аккаунт» с установленным флажком «Хранить несколько значений».
2. В качестве вычисляемого значения укажите приведенное выше выражение N3.
3. Проверьте, что атрибут содержит список пользователей с активными задачами.

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- [Периодические напоминания об открытых задачах][n3_periodic_task_notifications]
- [Настройка процесса для отправки email][process_email_configure]
- [Уведомления. Типы, назначение, настройка, использование][notification_types]

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
