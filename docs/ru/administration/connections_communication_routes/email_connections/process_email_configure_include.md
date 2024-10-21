
{% if not pdfOutput and not kbExport %}

{%
include-markdown "examples/process_email_configure.md"
rewrite-relative-urls=false
start="<!--include-start-->"
end="<!--include-end-->"
%}

[process_diagram_call_element_menu]: ../../../business_apps/diagrams/process_diagram/index.md#process_diagram_call_element_menu

{% endif %}
