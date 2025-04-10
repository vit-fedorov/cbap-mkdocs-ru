---
title: Объявление префикса
kbId: 5042
tags:
  - выражения
  - n3
  - тройки
  - префиксы
  - функции
  - вычисляемые атрибуты
  - проверка значения
  - предиктивный ввод
  - подсказки
  - редактор выражений
  - сценарии
hide:
  - tags
---

# Объявление префикса {: #n3_editor_prefix_autocomplete}

## Инструкции

1. Введите символ `@`.
2. Отобразится список доступных префиксов.
3. Выберите префикс в списке, чтобы просмотреть его описание и URI.
_![Список доступных префиксов N3 с описанием](n3_editor_prefix_autocomplete.png)_
4. Дважды нажмите префикс, например `math`, чтобы вставить его в выражение.

```turtle title="Пример: префикс math для математических функций"
@prefix math: <http://www.w3.org/2000/10/swap/math#>.
```

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Редактор выражений][expression_editor]_
- _[Примеры использования языка N3. База знаний Comindware][n3_use_examples]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
