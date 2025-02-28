---
title: 'Просмотр диаграмм процессов и бизнес-способностей'
kbId: 4830
tags:
    - процессная архитектура
    - диаграмма процесса
    - диаграмма бизнес-способностей
    - навигация по диаграмме
    - просмотр диаграммы
    - навигация по элементам диаграммы
hide:
    - tags
---

# Просмотр диаграмм процессов и бизнес-способностей {: #architect_process_architecture_diagram_view }

## Открытие диаграммы для просмотра

1. Выберите элемент процессной архитектуры в [панели навигации][navigation_panel] или дважды нажмите его строку в [реестре процессов][architect_process_architecture_design].
2. Откроется диаграмма процесса или бизнес-способностей в режиме просмотра.
3. При необходимости [отредактируйте диаграмму][architect_edit_diagram].

## Функции при просмотре диаграммы

*![Диаграмма в режиме просмотра](process_architecture_modeling_view_diagram.png)*

1. **Кнопки типовых операций**

    - **Редактировать** <i class="fa-light fa-pen-nib"></i> — переход в режим просмотра диаграммы.
    - **Обсуждение** <i class="fa-light fa-comment-dots"></i> — отображение чата для обсуждения диаграммы.
    - **Версии** <i class="fa-light fa-code-branch"></i> — просмотр версий диаграммы.
    - **Свойства** <i class="fa-light fa-sidebar-flip"></i> — просмотр свойств диаграммы.

--8<-- "process_architecture_diagram_zoom_controls.md"
4. **Панель свойств** — здесь отображаются свойства выбранного элемента, а также панель обсуждения и панель версий диаграммы.

<!--navigating-to-child-start-->
{% if not pdfOutput %}
## Переход к дочерним элементам диаграммы {: .pageBreakBefore }

Для перехода к диаграмме подпроцесса или дочерней группы процессов нажмите значок перехода к дочернему элементу:

- <i class="fa-light fa-diagram-subtask"></i> <i class="fa-light fa-square-plus"></i> — переход к диаграмме бизнес-способностей по ссылке;
- <i class="fa-light fa-list-tree"></i> <i class="fa-light fa-square-plus"></i> — переход к диаграмме бизнес-способностей.
- <i class="fa-light fa-diagram-nested"></i> — переход к диаграмме процесса;
- <i class="fa-light fa-code-compare"></i> — переход к диаграмме процесса по ссылке;
- <i class="fa-light fa-square-plus"></i> — переход к подпроцессу с диаграммы процесса.

*![Переход к дочернему элементу с диаграммы бизнес-способностей](img/diagram_navigating_to_child_element.png)*

*![Переход к диаграмме подпроцесса с диаграммы процесса](img/diagram_navigating_to_subprocess.png)*
{% endif %}
<!--navigating-to-child-end-->

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Просмотр реестра процессов][architect_process_architecture_design]_
- _[Редактирование диаграммы][architect_edit_diagram]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
