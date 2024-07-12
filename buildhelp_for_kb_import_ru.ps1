echo "`nUninstalling the generic em-img2fig-plugin version"

pip uninstall -y mkdocs-em-img2fig-plugin

echo "`nInstalling a custom em-img2fig-plugin version that generates image HTML suitable for the comindware KB"

pip install git+https://github.com/arterm-sedov/mkdocs-em-img2fig-plugin@for_cmw_kb_import

echo "`nBuilding custom help in the for_kb_import_ru folder"

mkdocs build -f mkdocs_for_kb_import_ru.yml

echo "`nUninstalling a custom em-img2fig-plugin version"

pip uninstall -y mkdocs-em-img2fig-plugin

echo "`nReinstalling the generic em-img2fig-plugin version"

pip install mkdocs-em-img2fig-plugin