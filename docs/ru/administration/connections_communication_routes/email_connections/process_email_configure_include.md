
{% if not pdfOutput %}

{%
include-markdown "examples/process_email_configure.md"
rewrite-relative-urls=false
start="<!--include-start-->"
end="<!--include-end-->"
%}

{% endif %}
