---
title: 'N3. Фильтрация списка по многоуровневой иерархии'
kbId: 5108
tags:
  - запись
  - коллекция
  - список
  - фильтрация
  - иерархия
  - N3
  - Notation3
  - Notation 3
  - тройки
  - триплеты
hide: tags
---

# N3. Объединение и фильтрация списков по многоуровневой иерархии {: #example_n3_dataset_join_filter_multilevel }

## Введение {: #example_n3_dataset_join_filter_multilevel_intro }

Атрибут типа «**Запись**» хранит ID записей в связанном шаблоне (ссылки на них). Эти записи можно выводить в виде раскрывающегося списка.

Во многих бизнес-сценариях требуется предоставлять пользователю для выбора списки записей, отфильтрованные по сложным правилам. Например, когда данные для фильтрации находятся не в самой записи, а в связанной иерархии справочников.

Здесь представлен пример, как с помощью N3-выражения сформировать список контрагентов на основе трехуровневой иерархии продуктовых категорий, а затем дополнительно отфильтровать его по правам доступа текущего пользователя.

## Прикладная задача {: #example_n3_dataset_join_filter_multilevel_use_case }

Менеджер по продажам оформляет заявку на квоту для клиента. В заявке он указывает продуктовую категорию, к которой относится квота. Система должна предложить ему для выбора только тех контрагентов, которые работают с продукцией из указанной категории.

Иерархия категорий трехуровневая. Если в верхнем уровне не нашлось контрагентов, поиск должен идти по среднему уровню, а затем по нижнему.

Кроме того, в итоговом списке менеджер должен видеть только тех контрагентов, за которых он является ответственным.

## Исходные данные {: #example_n3_dataset_join_filter_multilevel_initial_data }

Для реализации этого сценария используются следующие шаблоны:

1.  **`Общая категория продуктов`**: Справочник верхнего уровня.
    -   `Название` (Текст)
2.  **`Продуктовая категория`**: Справочник для всех уровней иерархии.
    -   `Название` (Текст)
    -   `Общая категория` (Запись, ссылка на `Общая категория продуктов`)
3.  **`Контрагент`**: Карточка клиента или партнера.
    -   `Название` (Текст)
    -   `Продуктовые категории` (Запись, ссылка на `Общая категория продуктов`, множественное)
    -   `Контакты` (Запись, ссылка на `Контакт`, множественное)
4.  **`Контакт`**: Контактное лицо в организации.
    -   `Ответственный` (Запись, ссылка на `Сотрудник`)
    -   `Активен` (Логический)
5.  **`Сотрудник`**: Карточка сотрудника.
    -   `Учетная запись` (Пользователь)
6.  **`Заявка на квоту`**: Основная запись, где происходит вычисление.
    -   `Категория (ур. 1)` (Запись, ссылка на `Продуктовая категория`)
    -   `Категория (ур. 2)` (Запись, ссылка на `Продуктовая категория`)
    -   `Категория (ур. 3)` (Запись, ссылка на `Продуктовая категория`)
    -   `Доступные контрагенты` (Запись, ссылка на `Контрагент`, множественное, вычисляемый)

## Настройка вычислений {: #example_n3_dataset_join_filter_multilevel_calculation .pageBreakBefore }

Логику можно разделить на две части:
1.  Сбор всех контрагентов по трем уровням категорий.
2.  Фильтрация полученного списка по текущему пользователю для настройки прав доступа.

### 1. Вычисление списка контрагентов

В шаблоне `Заявка на квоту` для атрибута `Доступные контрагенты` настройте вычисление на N3.

```turtle
# Импортируем префиксы для работы со списками и объектами
@prefix object: <http://comindware.com/ontology/object#>.
@prefix list: <http://www.w3.org/2000/10/swap/list#>.

{
    # Находим URI нужных атрибутов
    ("LegalEntities" "ProductCategories") object:findProperty ?ProductCategoriesProperty.
    ("Quotas" "ProductCategorieslevel3") object:findProperty ?ProductCategorieslevel3Property.
    ("Quotas" "ProductCategorieslevel2") object:findProperty ?ProductCategorieslevel2Property.
    ("Quotas" "ProductCategorieslevel1") object:findProperty ?ProductCategorieslevel1Property.
    ("ProductCategories" "CommonCategory") object:findProperty ?CommonCategoryProperty.

    # Ищем контрагентов для категории 3-го уровня
    from {
        ?item ?ProductCategorieslevel3Property ?ProductCategorieslevel3.
        ?ProductCategorieslevel3 ?CommonCategoryProperty ?CommonCategory3.
        # Ищем всех контрагентов (?LegalEntities3), у которых продуктовая категория
        # совпадает с общей категорией, найденной выше.
        ?LegalEntities3 ?ProductCategoriesProperty ?CommonCategory3.
    }
    select ?LegalEntities3 -> ?LegalEntities3List.

    # Аналогично для категории 2-го уровня
    from {
        ?item ?ProductCategorieslevel2Property ?ProductCategorieslevel2.
        ?ProductCategorieslevel2 ?CommonCategoryProperty ?CommonCategory2.
        ?LegalEntities2 ?ProductCategoriesProperty ?CommonCategory2.
    }
    select ?LegalEntities2 -> ?LegalEntities2List.

    # Объединяем списки по 2-му и 3-му уровням
    (?LegalEntities3List ?LegalEntities2List) list:append ?LegalEntities32List.

    # Аналогично для категории 1-го уровня
    from {
        ?item ?ProductCategorieslevel1Property ?ProductCategorieslevel1.
        ?ProductCategorieslevel1 ?CommonCategoryProperty ?CommonCategory1.
        ?LegalEntities1 ?ProductCategoriesProperty ?CommonCategory1.
    }
    select ?LegalEntities1 -> ?LegalEntities1List.

    # Объединяем список по 1-му уровню с остальными
    (?LegalEntities32List ?LegalEntities1List) list:append ?LegalEntitiesList.

    # Возвращаем уникальные значения из итогового списка
    ?LegalEntitiesList list:member ?value.
}
```

!!! note "Важно"
    В N3-выражении используются внутренние имена шаблонов и атрибутов (`LegalEntities`, `ProductCategorieslevel1` и т.д.). Убедитесь, что они соответствуют именам в вашей системе.

### 2. Фильтрация для роли

Чтобы ограничить доступ к списку, можно использовать похожее N3-выражение в настройках роли доступа к шаблону `Контрагент`. Это выражение проверит, является ли текущий пользователь ответственным за данного контрагента.

```turtle
# ... (блок получения ?LegalEntitiesList из предыдущего примера) ...

# Получаем идентификатор текущего пользователя
cmw:securityContext cmw:currentUser ?user.

# Находим URI атрибутов для проверки связи с пользователем
("LegalEntity" "Contacts") object:findProperty ?relationsProperty.
("Contact" "Active") object:findProperty ?activeProperty.
("Contact" "Responsible") object:findProperty ?individualProperty.
("Employee" "Account") object:findProperty ?accountProperty.

# Из полного списка контрагентов отбираем только те,
# где текущий пользователь является активным ответственным
from {
    ?LegalEntitiesList list:member ?legalEntity.
    ?legalEntity ?relationsProperty ?relation.
    ?relation ?activeProperty true.
    ?relation ?individualProperty ?individual.
    ?individual ?accountProperty ?user.
} select ?legalEntity.

} -> ?value.
```

## Тестирование {: #example_n3_dataset_join_filter_multilevel_test .pageBreakBefore }

1.  Заполните справочники `Общая категория продуктов`, `Продуктовая категория`, `Сотрудник` и `Контрагент`.
2.  Для нескольких контрагентов укажите продуктовые категории и назначьте активных ответственных (указав свою учетную запись).
3.  Создайте новую `Заявку на квоту`.
4.  Выберите `Категорию (ур. 1)`, `(ур. 2)` или `(ур. 3)`.
5.  В поле `Доступные контрагенты` должен появиться отфильтрованный список. Например, если вы выбрали категорию, с которой работает 3 контрагента, но вы ответственны только за одного из них, в списке будет только одна запись.

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- [Атрибут типа «Запись»][attribute_record]
- [Язык N3][n3_guide]
- [Настройка прав доступа][cmw_rights_configure]

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %} 