---
kbId: 5043
tags:
  - выражения
  - n3
  - тройки
  - литерал
  - тип литерала
  - xsd
  - вычисляемые атрибуты
  - проверка значения
  - предиктивный ввод
  - подсказки
  - редактор выражений
  - сценарии
hide:
  - tags
---

# Ввод типа литерала

1. Введите литерал в кавычках, например `"P1D"` (1 день в формате ISO).
2. После кавычек введите символы `^^`.
3. Нажмите клавиши ++ctrl+space++.
4. Отобразится список доступных типов литералов.
*![Список доступных типов литералов](n3_editor_literal_autocomplete.png)*
4. Дважды нажмите тип литерала, например `duration`, чтобы вставить его в выражение.

```turtle title="Пример: выражение, возвращающее конец текущего дня"
@prefix session: <http://comindware.com/ontology/session#>.
@prefix cmwutc: <http://comindware.com/logics/time/utc#>.
@prefix xsd: <http://www.w3.org/2001/XMLSchema#>.
@prefix cmwdur: <http://comindware.com/logics/time/duration#>.
{
  # Текущее время в UTC
  session:context session:requestTime ?nowUTC.
  # Время начала текущего дня
  ?nowUTC cmwutc:startOfDay ?startOfTodayUTC.
  # Начало следующих суток = время начала текущего дня + 1 сутки
  (?startOfTodayUTC "P1D"^^xsd:duration) cmwdur:add ?value.
}
```

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Редактор выражений][expression_editor]_
- _[Примеры использования языка N3. База знаний Comindware][n3_use_examples]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
