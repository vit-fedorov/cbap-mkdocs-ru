---
title: Восстановление базы данных из файла резервной копии в формате .CDBBZ
kbId: 4647
tags: 
    - развёртывание
    - резервное копирование
    - восстановление
---

# Восстановление базы данных из файла резервной копии в формате .CDBBZ {: #backup_restore_cdbbz}

## Введение

Здесь представлены инструкции по восстановлению базы данных **{{ productName }}** для следующего сценария:

- используется ранее настроенный экземпляр ПО **{{ productName }}** под управлением ОС Linux;
- имеется файл резервной копии базы данных с расширением `.CDBBZ`;
- резервная копия создана с помощью встроенной в ПО функции «**Резервное копирование**» (см. *«[Резервное копирование. Настройка и запуск, просмотр журнала сеансов][backup_configure]»*);
- индексы {{ openSearchVariants }} восстанавливаются отдельно от восстановления базы данных экземпляра ПО.

Прежде чем приступать к восстановлению экземпляра ПО **{{ productName }}** из резервной копии, ознакомьтесь с видеороликом и инструкциями, представленными ниже.

### Видеоинструкция

Ссылка на видеоролик: <https://kb.comindware.ru/platform/v5.0/administration/deploy/linux/img/restore_complete_backup_linux.mp4>

<video controls="controls" width="100%" height="100%">
<source src="https://kb.comindware.ru/platform/v5.0/administration/deploy/linux/img/restore_complete_backup_linux.mp4" type="video/mp4" />
</video>

## Восстановление базы данных и скриптов

1. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

2. Остановите службы экземпляра ПО (где `<instanceName>` — имя экземпляра ПО):

    ``` sh
    systemctl stop comindware<instanceName>
    systemctl stop apigateway<instanceName>
    ```

    ``` sh
    ps -fax | grep <instanceName> | grep Agent
    kill -9 $(ps -eo pid,args | grep <instanceName> | grep Agent | awk {'print $1'}) 
    #или 
    systemctl stop adapterhost<instanceName>
    ```

3. С помощью команды `systemctl status <serviceName>` удостоверьтесь, что службы остановлены.
4. Перейдите в директорию с резервной копией, например `/home/<user>`

    ```sh
    cd /home/<user>
    ```

5. Создайте временную директорию для распакованной резервной копии (например, `tmp`):

    ```sh
    mkdir tmp
    ```

6. <a id="unpack_backup"></a>Распакуйте архив резервной копии в директорию `tmp`:

    ``` sh
    unzip -q <backupName>.cdbbz -d tmp/
    ```

7. Перейдите в директорию `tmp` и просмотрите её содержимое:

    ``` sh
    cd tmp
    ls
    ```

8. После распаковки архива в директории быть 3 директории: `Database`, `Scripts`, `Streams`.

    !!! note "Примечание"

        Если в распакованной резервной копии имеется директория `Ignite` вместо `Database`, переименуйте её в `Database`:

        ```
        mv Ignite Database
        ```

9. Для восстановления резервной копии используйте следующие параметры из YML-файла конфигурации экземпляра ПО `/usr/share/comindware/configs/instance/<instanceName>.yml`:

    `#!yml databasePath: <path/to/Database>` — путь к директории базы данных;
    `#!yml userStorage.localDisk.path: <path/to/Streams>` — путь к директории пользовательских файлов;

    Просмотрите откройте файл конфигурации с помощью следующей команды:

    ``` sh
    cat /usr/share/comindware/configs/instance/<instanceName>.yml
    ```

10. Убедитесь в наличии директорий `<path/to/Database>` и `<path/to/Streams>`:

    ``` sh
    ls -lh <path/to/Database>
    ls -lh <path/to/Streams>
    ```

    - Если папки отсутствуют, создайте их:

        ``` sh
        mkdir -p <path/to/Database>
        mkdir -p <path/to/Streams>
        ```

11. Перейдите в директорию распакованной резервной копии (например, `/home/<user>/temp/`).
12. Переместите директорию `Scripts` в `Database`:

    ```
    mv Scripts Database
    ```

13. Переместите содержимое резервной копии в директории экземпляра ПО:

    ``` sh
    mv Database/* <path/to/Database>
    mv Streams/* <path/to/Streams>
    ```

14. Назначьте перенесённым директориям права `rwxrw-rw-`:

    ``` sh
    chmod -R 766 <path/to/Database/folder> <path/to/Streams> /var/lib/comindware/<instanceName>

    ```

    {% include-markdown ".snippets/pdfPageBreakHard.md" %}

15. Назначьте перенесенным директориям владельца:

    ``` sh
    chown -R <User>:<Group> <path/to/database/folder> <path/to/streams/folder> /var/lib/comindware/<instanceName>
    ```

    Здесь `<User>`, `<Group>` — значения соответствующих параметров из файла `/usr/lib/systemd/system/comindware<instanceName>.service`

16. Если в файле конфигурации экземпляра ПО отсутствует параметр `nodeName` (имя узла экземпляра ПО), добавьте его:

    - Откройте файл конфигурации для редактирования:
        ``` sh
        nano /usr/share/comindware/configs/instance/<instanceName>.yml
        ```

    - Добавьте директиву:

        ``` yml
        nodeName: <instanceName>
        ```

    !!! warning "Имя узла и лицензионные ключи"

        Чтобы использовать на восстановленном экземпляре ПО прежние лицензионные ключи, скопируйте имя узла из конфигурации исходного экземпляра ПО.

        См. _«[Восстановление лицензионных ключей](#backup_restore_cdbbz_license_keys)»_.

17. При необходимости [восстановите индексы {{ openSearchVariants }}](#backup_restore_cdbbz_indexes) из резервной копии.
18. Запустите службы экземпляра ПО и проверьте их статус:

    ``` sh
    systemctl start comindware<instanceName> 
    systemctl start apigateway<instanceName>
    systemctl start adapterhost<instanceName>
    ```

    ``` sh
    systemctl status comindware<instanceName>
    systemctl status apigateway<instanceName>
    systemctl status adapterhost<instanceName>
    ```

19. Откройте веб-сайт экземпляра ПО.
20. Дождитесь инициализации экземпляра ПО. Этот процесс может занять некоторое время. Может потребоваться обновить страницу браузера. См. _«[Инициализация {{ productName }}][deploy_guide_linux_initialize]»_.
21. Удостоверьтесь, что все данные из резервной копии восстановлены.
22. Проверьте и исправьте конфигурацию экземпляра ПО. См. *«[Проверка и настройка конфигурации экземпляра ПО {{ productName }} после восстановления из резервной копии][restore_test_configure]»*.
23. Удалите временную директорию с распакованной резервной копией:

    ``` sh
    rm -r /home/<user>/tmp
    ```

## Восстановление лицензионных ключей {: #backup_restore_cdbbz_license_keys }

Чтобы использовать на восстановленном экземпляре ПО прежние лицензионные ключи, выполните указанные ниже действия.

1. Откройте файл конфигурации для редактирования:

    ``` sh
    nano /usr/share/comindware/configs/instance/<instanceName>.yml
    ```

2. Укажите такое же значение `nodeName` (имя узла экземпляра ПО), как в конфигурации исходного экземпляра ПО:

    ``` yml
    nodeName: <instanceName>
    ```

3. Включите директиву `isContainerEnvironment`:

    ``` yml
    isContainerEnvironment: true
    ```

4. Перезапустите экземпляр ПО:

    ``` sh
    systemctl restart comindware<instanceName>
    ```

5. Удостоверьтесь, что лицензионные ключи присутствуют на странице «**Администрирование**» — «**[Лицензирование][licensing]**».
6. Назначьте лицензионные ключи аккаунтам и группам.

## Восстановление индексов {{ openSearchVariants }} из файла резервной копии репозитория {: #backup_restore_cdbbz_indexes }

1. Остановите службу {{ openSearchVariants }} и удостоверьтесь, что она остановлена:

    ```
    systemctl stop elasticsearch
    systemctl status elasticsearch
    ```

2. Создайте папку репозитория {{ openSearchVariants }} (например, `/var/www/backups/elasticsearch/`) и перенесите в неё файлы из каталога `History` ранее [распакованной резервной копии](#unpack_backup):

    ```
    mkdir /var/www/backups/elasticsearch/
    mv /var/lib/comindware/<instanceName>/History/* /var/www/backups/elasticsearch/
    ```

3. Назначьте папке репозитория и её содержимому права `rwxr-xr-x`:

    ```
    chmod -R 755 /var/www/backups/
    ```

4. Назначьте владельца `elasticsearch` папке репозитория и её содержимому:

    ```
    chown -R elasticsearch:elasticsearch /var/www/backups/
    ```

5. В файле конфигурации `/etc/elasticsearch/elasticsearch.yml` укажите путь к созданному репозиторию:

    ```
    path.repo: /var/www/backups/elasticsearch
    ```

6. Запустите службу {{ openSearchVariants }}:

    ```
    systemctl start elasticsearch.service
    ```

    {% include-markdown ".snippets/pdfPageBreakHard.md" %}

7. Зарегистрируйте репозиторий (например, `repository_backup`) с резервной копией снимка {{ openSearchVariants }}:

    ```
    curl -X PUT "localhost:9200/_snapshot/repository_backup?pretty" \
    -H 'Content-Type: application/json' -d \
    '{
        "type": "fs",
        "settings": {
            "location": "/var/www/backups/elasticsearch"
        }
    }'

    ```

    <a id="s3_repository"></a>
    !!! note "Примечание"

        Шаги 7 и 8 не требуются при восстановлении снимка из хранилища S3.

        Для восстановления снимка из хранилища S3 используйте репозиторий с именем, совпадающим с префиксом индекса {{ openSearchVariants }}.

        Этот репозиторий создаётся автоматически при запуске резервного копирования

        Префикс индекса задаётся в [свойствах подключения к {{ openSearchVariants }}][elasticsearch_connection], используемого по умолчанию.

8. Проверьте содержимое зарегистрированного репозитория:

    ```
    curl -X GET "localhost:9200/_cat/snapshots/repostory_backup?pretty"
    ```

9. Восстановите снимок {{ openSearchVariants }}:

    ```
    curl -X POST "localhost:9200/_snapshot/repostory_backup/backupSession123/_restore?pretty"
    ```

    - В качестве репозитория укажите имя репозитория, созданного на шаге 7, или префикс индекса {{ openSearchVariants }} (см. [примечание](#s3_repository) выше).
    - В качестве имени снимка укажите идентификатор резервной копии **без точки перед номером** (например, `backupSession.123` указывайте как `backupSession123`) со страницы [«Администрирование» – «Инфраструктура» – «Резервное копирование» – «Журнал»][backup_configure].

10. Проверьте наличие индексов в восстановленном каталоге:

    ```
    curl -X GET "localhost:9200/_cat/indices?pretty"
    ```

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Резервное копирование. Настройка и запуск, просмотр журнала сеансов][backup_configure]_
- _[Установка, запуск, инициализация и остановка ПО][deploy_guide_linux]_
- _[Пути и содержимое директорий экземпляра ПО][paths]_
- _[Проверка и настройка конфигурации экземпляра ПО {{ productName }} после восстановления из резервной копии][restore_test_configure]_
- _[Регистрация репозитория {{ openSearchVariants }} (официальное руководство, английский язык)](https://www.elastic.co/guide/en/elasticsearch/reference/current/snapshots-filesystem-repository.html)_
- _[Восстановление снимка {{ openSearchVariants }} (официальное руководство, английский язык)](https://www.elastic.co/guide/en/elasticsearch/reference/current/restore-snapshot-api.html)_
- _[{{ openSearchVariants }}. Настройка подключения][elasticsearch_connection]_
- _[Создание полной резервной копии (базы данных, вложенных файлов и журналов) без остановки экземпляра ПО][complete_running_instance_backup]_
- _[Восстановление базы данных, вложенных файлов и журналов из полной резервной копии][restore_complete_backup]_
- _[Лицензирование. Активация, назначение, отзыв и продление лицензий][licensing]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
