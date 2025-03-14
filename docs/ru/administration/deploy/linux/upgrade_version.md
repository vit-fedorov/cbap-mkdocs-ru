---
title: Обновление версии экземпляра ПО
kbId: 4624
---

# Обновление версии экземпляра ПО

## Введение

Здесь представлены инструкции по обновлению версии экземпляра ПО **{{ productName }}** с 4.7.2 до версий 4.7.3–5.0 для ОС Linux.

## Порядок обновления версии экземпляра ПО

1. Подготовьте экземпляр ПО к обновлению:

    - Сохраните резервную копию экземпляра ПО.
    - Остановите экземпляр ПО.
    - Сохраните конфигурацию экземпляра ПО и вспомогательных служб.
    - Удалите компоненты старой версии ПО.

2. Обновите версию экземпляра ПО:

    - Скачайте и распакуйте дистрибутив новой версии ПО.
    - Установите новую версию ПО.
    - Обновите экземпляр ПО до новой версии.
    - Обновите конфигурацию экземпляра ПО и вспомогательных служб.
    - Перезапустите экземпляр ПО и вспомогательные службы.

    - Инициализируйте экземпляр ПО.
    - Обновите структуру данных до новой версии.
    - Снова перезапустите запустите экземпляр ПО.

## Подготовка экземпляра ПО к обновлению {: .pageBreakBefore }

!!! warning "Внимание!"

    Выполните подготовительные действия отдельно для каждого экземпляра ПО, версию которого требуется обновить.

1. Создайте и перенесите во внешнее хранилище резервную копию базы данных экземпляра ПО. См. _«[Резервное копирование. Настройка и запуск, просмотр журнала сеансов][backup_configure]»_.
2. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

    {% include-markdown ".snippets/pdfPageBreakHard.md" %}

3. Удостоверьтесь, что файлы конфигурации соответствуют приведённым ниже образцам, и при необходимости создайте и отредактируйте их.
{: #config_samples }

    - Отредактируйте файл `/usr/share/comindware/configs/instance/<instanceName>.yml` по следующему образцу:

    {%
    include-markdown "./configuration_files.md"
    start="<!--instanceYML-start-->"
    end="<!--instanceYML-end-->"
    %}

    --8<-- "instance_config_warning.md"

    {% include-markdown ".snippets/pdfPageBreakHard.md" %}

    - Отредактируйте файл `/var/www/<instanceName>/adapterhost.yml` по следующему образцу:

    {%
    include-markdown "./configuration_files.md"
    start="<!--adapterhostYML-start-->"
    end="<!--adapterhostYML-end-->"
    %}

    !!! warning "Внимание!"

        Файл `adapterhost.yml` не должен содержать пустых строк.

    {% include-markdown ".snippets/pdfPageBreakHard.md" %}

    - Отредактируйте файл `/var/www/<instanceName>/apigateway.yml` по следующему образцу:

    {%
    include-markdown "./configuration_files.md"
    start="<!--apigatewayYML-start-->"
    end="<!--apigatewayYML-end-->"
    %}

    {% include-markdown ".snippets/pdfPageBreakHard.md" %}

4. Сохраните резервную копию конфигурационных файлов, например в директорию `/var/backups/config_tmp`:
{: #NginxBackup}

    - **Astra Linux**, **Ubuntu**, **Debian** (DEB-based)

    ``` sh
    mkdir -p /var/backups/config_tmp/
    cd /var/www/<instanceName>/
    cp *.config *.yml /var/backups/config_tmp/
    cp /etc/nginx/sites-available/comindware<instanceName> /var/backups/config_tmp/
    ```

    - **РЕД ОС**, **Rocky** (RPM-based)

    ``` sh
    mkdir -p /var/backups/config_tmp/
    cd /var/www/<instanceName>/
    cp *.config *.yml /var/backups/config_tmp/
    cp /etc/nginx/conf.d/comindware<instanceName> /var/backups/config_tmp/
    ```

    - **Альт Сервер**

    ``` sh
    mkdir -p /var/backups/config_tmp/
    cd /var/www/<instanceName>/
    cp *.config *.yml /var/backups/config_tmp/
    cp /etc/nginx/sites-available.d/comindware<instanceName> /var/backups/config_tmp/
    ```

    Здесь `<instanceName>` — имя экземпляра ПО.

5. Остановите экземпляр ПО и вспомогательные службы и удостоверьтесь, что они остановлены:

    ``` sh
    systemctl stop apigateway<instanceName> comindware<instanceName>
    systemctl status apigateway<instanceName> comindware<instanceName>
    ```

6. Проверьте, выполняется ли сервис `Comindware.Adapter.Agent.exe`:

    ``` sh
    ps fax | grep Agent
    ```

    - Если процесс `Comindware.Adapter.Agent.exe`, выполняется, завершите его по `PID`:

        ``` sh
        kill -9 <PID>
        ```

7. Проверьте имя и статус экземпляра:

    ``` sh
    systemctl status comindware*
    ```

8. Удалите (или переместите в резервное хранилище) неиспользуемые предыдущие дистрибутивы ПО (`<distPath>` — путь к директории с дистрибутивом, `<osname>` — название операционной системы):

    ``` sh
    rm -rf <distPath>/CMW_<osname>
    ```
    {% include-markdown ".snippets/pdfEndOfBlockHack.md" %}

## Обновление версии ПО для экземпляра {: .pageBreakBefore }

!!! warning "Внимание!"

    Если при обновлении [на шаге 12](#dataUpgrade) будут обнаружены ошибки, не продолжайте обновление, установите старую версию, восстановите экземпляр ПО из резервной копии и обратитесь в службу поддержки **{{ companyName }}**.

!!! note "Обновление нескольких экземпляров ПО"

    Выполните приведённые ниже шаги 6–18 для каждого экземпляра ПО, версию которого требуется обновить, так как скрипт обновления выполняется отдельно для указанного экземпляра ПО.

    После обновления всех экземпляров ПО для экономии места старую версию ПО можно удалить согласно инструкции _«[Удаление версии ПО][deploy_guide_linux_delete_version]»_.

1. Скачайте и распакуйте дистрибутив с новой версией ПО (`X.X`, `<versionNumber>` — номер версии ПО):

    ``` sh
    cd <distPath>
    tar -xf X.X-release-ru-<versionNumber>.<osname>.tar.gz
    ```

2. Перейдите в распакованную директорию:

    ``` sh
    cd CMW_<osname>_<versionNumber>/scripts/
    ```

3. Запустите установку распакованного дистрибутива ПО:

    ``` sh
    bash version_install.sh
    ```

4. Проверьте наличие и имя директории установленной версии ПО:

    ``` sh
    bash version_list.sh
    ```

5. Отобразится список установленных версий ПО на сервере.
6. Перейдите в директорию скриптов для работы с экземпляром ПО и запустите его обновление до требуемой версии:

    ``` sh
    bash instance_upgrade.sh -n=<instanceName> -vp=/var/www/.cmw_version/<versionNumber>
    ```

    Здесь:

    - `-n=<instanceName>` — имя обновляемого экземпляра ПО;
    - `-vp=/var/www/.cmw_version/<versionNumber>` — укажите путь к директории с установленной версией ПО, где `<versionNumber>` — номер версии ПО.

    {% include-markdown ".snippets/pdfPageBreakHard.md" %}

7. По окончании обновления скрипт выведет информацию о компонентах экземпляра ПО. Удостоверьтесь, что компоненты успешно обновлены.

    Пример результата выполнения скрипта:

    ``` sh
    ...
    [Done] Creating Log Directories.
    OK     Instance folder created.
    OK     Instance Web config created.
    OK     Instance Ignite config created.
    OK     Instance binaries linked.
    OK     Instance config created.
    OK     Data folder created.
    OK     Database folder created: Yes
    OK     Streams folder created: No 
    OK     Logs folder created: Yes
    OK     Used version: <versionNumber>
    OK     Logs configured.
    OK     Sites created.
    OK     Sites enabled.
    OK     API Gateway configured.
    OK     Link to binaries is valid.
    OK     Instance service started.
    OK     Instance API gateway service started.
    OK     NGINX started.
    OK     Final status.
    [Done] Upgrade CBAP instance.
    ```

    Если какая-либо из служб имеет статус `FAILED`, перезапустите её (`<serviceName>` — имя службы):

    ``` sh
    systemctl restart comindware<instanceName>.service
    systemctl restart apigateway<instanceName>.service
    systemctl restart adaperhost<instanceName>.service
    systemctl restart kafka.service
    systemctl restart elasticsearch.service 
    ```

8. Проверьте корректность конфигурации NGINX для экземпляра ПО:

    - **Astra Linux**, **Ubuntu**, **Debian** (DEB-based)

        ``` sh
        cat /etc/nginx/sites-available/comindware<instanceName>
        ```

    - **РЕД ОС**, **Rocky** (RPM-based)

        ``` sh
        nano /etc/nginx/conf.d/comindware<instanceName>
        ```

    - **Альт Сервер**

        ``` sh
        nano /etc/nginx/sites-available.d/comindware<instanceName>
        ```

    - При необходимости восстановите конфигурацию NGINX, [сохранённую ранее](#NginxBackup).

        - **Astra Linux**, **Ubuntu**, **Debian** (DEB-based)

        ``` sh
        cp /var/backups/config_tmp/comindware<instanceName> /etc/nginx/sites-available/
        nginx -t && nginx -s reload
        ```

        - **РЕД ОС**, **Rocky** (RPM-based)

        ``` sh
        cp /var/backups/config_tmp/comindware<instanceName> /etc/nginx/conf.d/
        nginx -t && nginx -s reload
        ```

        - **Альт Сервер**

        ``` sh
        cp /var/backups/config_tmp/comindware<instanceName> /etc/nginx/sites-available.d/
        nginx -t && nginx -s reload
        ```

9. Удостоверьтесь, что файлы конфигурации соответствуют [приведённым выше образцам](#config_samples).
10. Перезапустите сервисы, настройки которых были изменены:

    ``` sh
    systemctl restart apigateway<instanceName> comindware<instanceName>
    ```

11. Откройте сайт экземпляра ПО в браузере, дождитесь окончания загрузки, одновременно открыв выдачу журналов экземпляра в терминале:

    ``` sh
    tail -f /var/log/comindware/<instanceName>/Log/sys*
    ```

12. Подтвердите успешное обновление структуры данных.
{: #dataUpgrade }

    !!! warning "Внимание!"

        При обновлении с версии 4.7.2 на версии 4.7.3-5.0 обновляется структура базы данных.

        После этого необходимо вручную удалить некоторые данные кэша в старом формате.

        Поэтому продолжать обновление версии экземпляра ПО можно только после успешного обновления структуры данных. 

    - Удостоверьтесь, что появились журналы обновления:
        - `/var/log/comindware/<instanceName>/Log/UpgradeOntology.log`
        - `/var/log/comindware/<instanceName>/Log/upgrade<ГГГГ-ММ-ДД>.log`
    - Удостоверьтесь, что в журнале `UpgradeOntology.log` последняя запись содержит строку `Upgrade of ontology completed successfully`.
    - Удостоверьтесь, что в журнале `upgrade<ГГГГ-ММ-ДД>.log` последняя запись содержит строку `Upgrade completed`.
    - Удостоверьтесь, что в журналах отсутствуют ошибки обновления. Найдите их по ключевому слову `error`.
    - Если обновление выполнено успешно, переходите к шагу 13.
    - Если в журнале обновления имеются ошибки:

        1. Не переходите к шагу 13.
        2. Снова установите для экземпляра старую версию ПО.
        3. Восстановите базу данных из резервной копии.
        4. Обратитесь в службу поддержки **{{ companyName }}**, предоставив журналы обновления и ошибок для анализа.

13. Создайте резервную копию экземпляра ПО:

    - в формате `.CDBBZ` средствами **{{ productName }}**;

        или

    - c помощью скрипта для создания снимка базы.

14. Остановите экземпляр ПО.
15. Распакуйте резервную копию и удалите из неё следующие директории кэшей:

    ``` sh
    rm -rf cacheGroup-*-TableIdentity
    rm -rf cacheGroup-*-TableIdentityReplicated
    rm -rf cacheGroup-*Value
    rm -rf cacheGroup-*ValueReplicated
    rm -rf cache-ignite-sys-cache
    rm -rf cp
    rm -rf metastorage
    rm -rf cacheGroup-Keys
    ```

16. Очистите директории с базой данных экземпляра ПО:

    ``` sh
    rm -rf /var/lib/comindware/<instanceName>/Database/db
    rm -rf /var/lib/comindware/<instanceName>/Database/wal*
    ```

17. Скопируйте очищенную резервную копию в директорию с базой данных `/var/lib/comindware/<instanceName>/Database/`.
18. Запустите экземпляр ПО и войдите в систему.

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Установка, запуск, инициализация и остановка ПО][deploy_guide_linux]_
- _[Резервное копирование. Настройка и запуск, просмотр журнала сеансов][backup_configure]_
- _[Подсистема журналирования][logging_engine]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
