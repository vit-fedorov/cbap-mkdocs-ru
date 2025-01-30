---
title: Обновление версии экземпляра ПО
kbId: 4624
---

# Обновление версии экземпляра ПО

## Введение

Здесь представлены краткие инструкции по обновлению версии экземпляра ПО **{{ productName }}** c 4.7 до 5.X для ОС Linux.

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

Прежде чем приступать к установке вспомогательного ПО, необходимого для работы **{{ productName }}**, ознакомьтесь с демонстрационным роликом и инструкциями, представленными ниже.

### Видеоинструкция

<video controls="controls" width="100%" height="100%">
<source src="https://kb.comindware.ru/platform/v5.0/administration/deploy/linux/img/upgrade_version_linux.mp4" type="video/mp4" />
</video>

## Подготовка экземпляра ПО к обновлению

!!! warning "Внимание!"

    Выполните подготовительные действия отдельно для каждого экземпляра ПО, версию которого требуется обновить.

1. Создайте и перенесите во внешнее хранилище резервную копию базы данных экземпляра ПО. См. _«[Резервное копирование. Настройка и запуск, просмотр журнала сеансов][backup]»_.
2. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

3. Удостоверьтесь, что файлы конфигурации соответствуют приведённым ниже образцам, и при необходимости создайте и отредактируйте их.
{: #config_samples }

    - Отредактируйте файл `/usr/share/comindware/configs/instance/<instanceName>.yml` по следующему образцу:

    {%
    include-markdown "./configuration_files.md"
    start="<!--instanceYML-start-->"
    end="<!--instanceYML-end-->"
    %}

    --8<-- "instance_config_warning.md"

    - Отредактируйте файл `/var/www/<instanceName>/adapterhost.yml` по следующему образцу:

    {%
    include-markdown "./configuration_files.md"
    start="<!--adapterhostYML-start-->"
    end="<!--adapterhostYML-end-->"
    %}

    !!! warning "Внимание!"

        Файл `adapterhost.yml` не должен содержать пустых строк.

    - Отредактируйте файл `/var/www/<instanceName>/apigateway.yml` по следующему образцу:

    {%
    include-markdown "./configuration_files.md"
    start="<!--apigatewayYML-start-->"
    end="<!--apigatewayYML-end-->"
    %}

1. Сохраните резервную копию конфигурационных файлов, например в директорию `/var/backups/config_tmp`:
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

1. Остановите экземпляр ПО и вспомогательные службы и удостоверьтесь, что они остановлены:

    ``` sh
    systemctl stop apigateway<instanceName> comindware<instanceName>
    systemctl status apigateway<instanceName> comindware<instanceName>
    ```

2. Проверьте, выполняется ли сервис `Comindware.Adapter.Agent.exe`:

    ``` sh
    ps fax | grep Agent
    ```

    - Если процесс `Comindware.Adapter.Agent.exe`, выполняется, завершите его по `PID`:

        ``` sh
        kill -9 <PID>
        ```

3. Проверьте имя и статус экземпляра:

    ``` sh
    systemctl status comindware*
    ```

4. Удалите (или переместите в резервное хранилище) неиспользуемые предыдущие дистрибутивы ПО (`<distPath>` — путь к директории с дистрибутивом, `<osname>` — название операционной системы):

    ``` sh
    rm -rf <distPath>/CMW_<osname>
    ```

## Обновление версии ПО для экземпляра {: .pageBreakBefore }

Выполните шаги 6–13 для каждого экземпляра ПО, версию которого требуется обновить, так как скрипт обновления выполняется отдельно для указанного экземпляра ПО.

1. Скачайте и распакуйте дистрибутив с новой версией ПО (`X.X`, `<versionNumber>` — номер версии ПО):

    ``` sh
    cd <distPath>
    tar -xf X.X-release-ru-<versionNumber>.<osname>.tar.gz
    ```

2. Перейдите в распакованную папку:

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
    - `-vp=/var/www/.cmw_version/<versionNumber>` — укажите путь к папке с установленной версией ПО, где `<versionNumber>` — номер версии ПО.

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

12. После обновления всех экземпляров ПО, старую версию ПО можно удалить согласно инструкции _«[Удаление версии ПО][deploy_guide_linux_delete_version]»_.

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Установка, запуск, инициализация и остановка ПО][deploy_guide_linux]_
- _[Резервное копирование. Настройка и запуск, просмотр журнала сеансов][backup]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
