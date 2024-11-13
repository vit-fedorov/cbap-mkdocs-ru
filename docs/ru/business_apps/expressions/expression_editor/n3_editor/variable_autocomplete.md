---
tags:
  - выражения
  - n3
  - тройки
  - переменные
  - вычисляемые атрибуты
  - проверка значения
  - предиктивный ввод
  - подсказки
  - редактор выражений
  - сценарии
hide:
  - tags
---

# Ввод имени переменной

1. Введите фигурные скобки `{  }` в пустое выражение (после [префиксов][n3_editor_prefix_autocomplete]).
2. Внутри фигурных скобок введите символ `?`. Этот список также можно вызвать, нажав клавиши ++ctrl+space++ в позиции после символа `?`.
3. Отобразится список доступных переменных.
*![Список доступных переменных](n3_editor_variable_autocomplete.png)*
4. Дважды нажмите имя переменной, например `value`, чтобы вставить его в выражение.

```turtle title="Пример: выражение, возвращающее список всех записей из шаблона аккаунта"
@prefix account: <http://comindware.com/ontology/account#>.
@prefix container: <http://comindware.com/ontology/container#>.
{
  # Получаем ID шаблона аккаунта Zakazchiki
  ?user container:alias "Zakazchiki".
  # Получаем список аккаунтов из шаблона Zakazchiki
  ?value account:extendedBy ?user.
}
```

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Ввод предиката][n3_editor_predicate_autocomplete]_
- _[Ввод префикса][n3_editor_prefix_autocomplete]_
- _[Редактор выражений][expression_editor]_
- _[Примеры использования языка N3. База знаний Comindware][N3_use_examples]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
