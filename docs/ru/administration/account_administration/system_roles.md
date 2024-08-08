---
tags:
  - администрирование системы
  - роли
  - системные роли
  - разрешения
  - аккаунты
  - группы
hide:
  - tags
---

# Системные роли
В **{{ productName }}** предусмотрена возможность контроля доступа к различным ресурсам посредством ролей, разрешений и прав доступа.

Для контроля доступа к системным ресурсам используются системные роли.

Для контроля доступа к ресурсам приложения используются [роли в приложении][roles].

{%
include-markdown "../../business_apps/roles_in_application.md"
start="<!--role-definition-start-->"
end="<!---role-definition-end-->"
%}

## Просмотр списка системных ролей

1. В разделе «**[Администрирование][администрирование]**» — **[Администрирование аккаунтов][администрирование-аккаунтов]** выберите пункт «**Системные роли**» <i class=" fa-light  fa-user-shield "></i>.
2. Отобразится список системных ролей.

*![Список системных ролей](system_role_list.png)*

{%
include-markdown "../../business_apps/roles_in_application.md"
start="<!--role-list-elements1-start-->"
end="<!--role-list-elements1-end-->"
rewrite-relative-urls=false
%}
{%
include-markdown "../../business_apps/roles_in_application.md"
start="<!--role-list-elements2-start-->"
end="<!--role-list-elements2-end-->"
rewrite-relative-urls=false
%}
* **Перейти к администрированию системы** <i class="fa-light fa-gears"></i> — переход к разделу «**[Администрирование][администрирование]**».
--8<-- "list_search_button.md"

## Стандартные системные роли

В **{{ productName }}** предусмотрены стандартные системные роли с заранее заданными разрешениями на доступ к ресурсам системы.

Ниже перечислены стандартные системные роли и их разрешения.

* **Администраторы безопасности**
    -  _Полный доступ_
          *  Аккаунты
          *  Группы
          *  Системные роли
    -  _Просмотр_
          * Журналы событий
* **Администраторы инфраструктуры**
    -  _Полный доступ_
          *  Адаптеры
          *  Подключения
          *  Резервное копирование
    -  _Просмотр_
          * Журналы событий
* **Системные администраторы**
    -  _Полный доступ_
          *  Все ресурсы системы
* **Системные архитекторы**
    -  _Полный доступ_
          *  Приложения

{%
include-markdown "../../business_apps/roles_in_application.md"
start="<!--role-creation-start-->"
end="<!--role-creation-end-->"
rewrite-relative-urls=false
%}

!!! Note "Примечание"
    * Удалить можно только роли, созданные пользователями системы (у которых в списке указан создатель).

    * Если выбрать роль, созданную системой (у которой в списке не указан создатель), то кнопка «**Удалить**» не будет отображаться.

## Настройка роли

1. Дважды нажмите строку роли в списке.
2. Отобразится страница «**Системная роль**».
{%
include-markdown "../../business_apps/roles_in_application.md"
start="<!--role-properties1-start-->"
end="<!--role-properties1-end-->"
rewrite-relative-urls=false
%}

*![Страница настройки системной роли](system_role_properties.png)*

### Операции на странице «Системная роль»

* **Сохранить** — сохранение настроенной роли.
* **Клонировать** — создание дубликата данной роли.

{%
include-markdown "../../business_apps/roles_in_application.md"
start="<!--role-properties2-start-->"
end="<!--role-properties2-end-->"
rewrite-relative-urls=false
%}
* «**Активная**» — установите или снимите этот флажок, чтобы использовать или отключить данную роль. Данный флажок нельзя снять для ролей, созданных системой (у которых не указан создатель).{%
include-markdown "../../business_apps/roles_in_application.md"
start="<!--role-properties3-start-->"
end="<!--role-properties3-end-->"
rewrite-relative-urls=false
%}

### Разрешения

На вкладке «**Разрешения**» задаются полномочия на действия с ресурсами в рамках системной [роли](#роль).

*![Разрешения системной роли](system_role_permissions.png)*

{%
include-markdown "../../business_apps/roles_in_application.md"
start="<!--role-permissions1-start-->"
end="<!--role-permissions1-end-->"
rewrite-relative-urls=false
%}

*![Список системных ресурсов](system_role_resource_list.png)*

{%
include-markdown "../../business_apps/roles_in_application.md"
start="<!--role-permissions2-start-->"
end="<!--role-permissions2-end-->"
rewrite-relative-urls=false
%}

*![Список разрешений системной роли](system_role_permission_list.png)*

##### Сведения в списке разрешений

* **Флажки выбора** — устанавливайте флажки в этом столбце, чтобы выбрать один или несколько ресурсов.
{: #флажки-выбора-ресурсов}
* **Название** — наименование ресурса.
* **Просмотр** — разрешение на просмотр данных ресурса.
* **Полный доступ** — предоставление доступа ко всем функциям администрирования ресурса.

##### Операции в списке разрешений

* **Удалить** — удаление разрешений для выбранных ресурсов. Эта кнопка отображается только для системных ролей, созданных вручную.

{%
include-markdown "../../business_apps/roles_in_application.md"
start="<!--role-permissions3-start-->"
end="<!--role-permissions3-end-->"
rewrite-relative-urls=false
%}

{%
include-markdown "../../business_apps/roles_in_application.md"
start="<!--role-permissions4-start-->"
end="<!--role-permissions4-end-->"
rewrite-relative-urls=false
%}

{%
include-markdown "../../business_apps/roles_in_application.md"
start="<!--role-merge-start-->"
end="<!--role-merge-end-->"
rewrite-relative-urls=false
%}

{%
include-markdown "../../business_apps/roles_in_application.md"
start="<!--role-deletion-start-->"
end="<!--role-deletion-end-->"
rewrite-relative-urls=false
%}

--8<-- "related_topics_heading.md"

**[Роли в приложении](roles_in_application.md)**

**[Шаблон роли](role_templates.md)**
