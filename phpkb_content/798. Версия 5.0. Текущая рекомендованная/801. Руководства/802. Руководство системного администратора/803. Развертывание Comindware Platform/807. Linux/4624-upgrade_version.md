---
title: Обновление версии экземпляра ПО с его остановкой
kbId: 4624
---

# Обновление версии экземпляра ПО с его остановкой

## Введение

Здесь представлены инструкции по обновлению версии экземпляра ПО **{{ productName }}** на одном и том же сервере с остановкой экземпляра.

Инструкции даны для обновления с версий 4.7.2 до версий 4.7.3–5.0 в ОС Linux.

Совет

Этот способ можно использовать, если ПО **{{ productName }}** развёрнуто на одной машине и нет возможности развернуть новую машину для экземпляра ПО новой версии. Если вы можете развернуть новую машину, то рекомендуется следовать инструкции *«[Обновление версии экземпляра ПО без его остановки][upgrade_version_linux_no_stop]»*.

## Порядок обновления версии экземпляра ПО

1. Подготовьте экземпляр ПО к обновлению:

   - Сохраните резервную копию экземпляра ПО.
   - Остановите экземпляр ПО.
   - Сохраните конфигурацию экземпляра ПО и вспомогательных служб.
   - Удалите компоненты старой версии ПО.
   - Переместите директорию с базой данных экземпляра ПО в резервную директорию.
2. Обновите версию экземпляра ПО:

   - Скачайте и распакуйте два дистрибутива: вспомогательного ПО и новой версии ПО.
   - Обновите версию библиотек `librdkafka`.
   - Установите новую версию ПО.
   - Удалите экземпляр ПО старой версии
   - Создайте экземпляр ПО новой версии.
   - Обновите конфигурацию экземпляра ПО и вспомогательных служб.
   - Перезапустите экземпляр ПО и вспомогательные службы.
   - Инициализируйте экземпляр ПО.
   - Остановите экземпляр ПО.
   - Скопируйте в экземпляр ПО ранее перемещённую директорию с базой данных.
   - Запустите экземпляр ПО.
   - Обновите структуру данных до новой версии.
   - Снова перезапустите экземпляр ПО.

## Подготовка экземпляра ПО к обновлению

Внимание!

Выполните подготовительные действия отдельно для каждого экземпляра ПО, версию которого требуется обновить.

1. Создайте и перенесите во внешнее хранилище резервную копию базы данных экземпляра ПО. См. *«[Резервное копирование. Настройка и запуск, просмотр журнала сеансов][backup_configure]»*.
2. Перейдите в режим суперпользователя:

   ```
   sudo -s

   ```

   или

   ```
   su -

   ```
3. Сохраните резервную копию файлов конфигурации, например в директорию `/var/backups/config_tmp`:

   - **Astra Linux**, **Ubuntu**, **Debian** (DEB-based)

   ```
   mkdir -p /var/backups/config_tmp/
   cd /var/www/<instanceName>/
   cp *.config *.yml *.json /var/backups/config_tmp/
   cp /etc/nginx/sites-available/comindware<instanceName> /var/backups/config_tmp/
   cp /etc/sysconfig/comindware<instanceName>-env /var/backups/config_tmp/
   cp /usr/share/comindware/configs/instance/<instanceName>.yml /var/backups/config_tmp/

   ```

   - **РЕД ОС**, **Rocky** (RPM-based)

   ```
   mkdir -p /var/backups/config_tmp/
   cd /var/www/<instanceName>/
   cp *.config *.yml *.json /var/backups/config_tmp/
   cp /etc/nginx/conf.d/comindware<instanceName> /var/backups/config_tmp/
   cp /etc/sysconfig/comindware<instanceName>-env /var/backups/config_tmp/
   cp /usr/share/comindware/configs/instance/<instanceName>.yml /var/backups/config_tmp/

   ```

   - **Альт Сервер**

   ```
   mkdir -p /var/backups/config_tmp/
   cd /var/www/<instanceName>/
   cp *.config *.yml *.json /var/backups/config_tmp/
   cp /etc/nginx/sites-available.d/comindware<instanceName> /var/backups/config_tmp/
   cp /etc/sysconfig/comindware<instanceName>-env /var/backups/config_tmp/
   cp /usr/share/comindware/configs/instance/<instanceName>.yml /var/backups/config_tmp/

   ```

   Здесь `<instanceName>` — имя экземпляра ПО.
4. Остановите экземпляр ПО и вспомогательные службы и удостоверьтесь, что они остановлены:

   ```
   systemctl stop apigateway<instanceName> adapterhost<instanceName> comindware<instanceName>
   systemctl status apigateway<instanceName> adapterhost<instanceName> comindware<instanceName>

   ```
5. Удалите (или переместите в резервное хранилище) неиспользуемые предыдущие дистрибутивы ПО (`<distPath>` — путь к директории с дистрибутивом, `<osname>` — название операционной системы):

   ```
   rm -rf <distPath>/CMW_<osname>

   ```
6. Переместите директорию с базой данных экземпляра ПО (`<username>` — имя пользователя Linux):

   ```
   mkdir -p /home/<username>/<instanceName>
   mv /var/lib/comindware/<instanceName> /home/<username>/

   ```

## Обновление версии ПО для экземпляра

Внимание!

Если при обновлении [на шаге 22](#dataUpgrade) будут обнаружены ошибки, не продолжайте обновление, установите старую версию, восстановите экземпляр ПО из резервной копии и обратитесь в службу поддержки **Comindware**.

Обновление нескольких экземпляров ПО

Выполните приведённые ниже шаги 6–18 для каждого экземпляра ПО, версию которого требуется обновить, так как скрипт обновления выполняется отдельно для указанного экземпляра ПО.

После обновления всех экземпляров ПО для экономии места старую версию ПО можно удалить согласно инструкции *«[Удаление версии ПО][deploy_guide_linux]»*.

1. Скачайте и распакуйте дистрибутив с новой версией вспомогательного ПО (`X.X`, `<prerequisitesVersion>` — номер версии):

   ```
   cd <distPath>
   tar -xf X.X-release-ru-<prerequisitesVersion>.prerequisites.<osname>.tar.gz

   ```
2. Перейдите в распакованную директорию библиотек `librdkafka`:

   ```
   cd CMW_<osname>/repo/kafka/librd/

   ```
3. Обновите библиотеки `librdkafka`:

   - **Astra Linux**, **Ubuntu**, **Debian** (DEB-based)

   ```
   dpkg -i *.deb

   ```

   - **РЕД ОС**, **Rocky** (RPM-based)

   ```
   rpm -i *.rpm

   ```

   - **Альт Сервер**

   ```
   apt-get install -y *.rpm

   ```
4. Скачайте и распакуйте дистрибутив с новой версией ПО (`X.X`, `<version>` — номер версии):

   ```
   cd <distPath>
   tar -xf X.X-release-ru-<version>.<osname>.tar.gz

   ```
5. Перейдите в распакованную директорию:

   ```
   cd CMW_<osname>_<version>/scripts/

   ```
6. Установите новую версию ПО:

   ```
   bash version_install.sh

   ```
7. Проверьте наличие и имя директории установленной версии ПО:

   ```
   bash version_list.sh

   ```
8. Отобразится список установленных версий ПО на сервере.
9. Удалите экземпляр ПО старой версии и его данные:

   ```
   bash instance_delete.sh -n=<instanceName> --deleteData

   ```
10. Создайте экземпляр ПО новой версии:

    ```
    bash instance_create.sh -n=<instanceName> -p=<portNumber> -v=<version>

    ```

    Здесь:

    - `-n=<instanceName>` — имя экземпляра ПО;
    - `-p=<portNumber>` - порт для экземпляра ПО, по умолчанию: 80 (необязательный ключ);
    - `-v=<version>` — установленная версия ПО.
11. По окончании создания скрипт выведет информацию о компонентах экземпляра ПО. Удостоверьтесь, что компоненты успешно установлены.

    Пример результата выполнения скрипта:

    ```
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
    OK     Used version: <version>
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

    Если какая-либо из служб имеет статус `FAILED`, исправьте конфигурацию, как указано ниже, и перезапустите службу.
12. Отредактируйте конфигурацию NGINX для экземпляра ПО в соответствии с резервной копией, [сохранённой ранее](#NginxBackup):

    - **Astra Linux**, **Ubuntu**, **Debian** (DEB-based)

      ```
      nano /etc/nginx/sites-available/comindware<instanceName>

      ```
    - **РЕД ОС**, **Rocky** (RPM-based)

      ```
      nano /etc/nginx/conf.d/comindware<instanceName>

      ```
    - **Альт Сервер**

      ```
      nano /etc/nginx/sites-available.d/comindware<instanceName>

      ```
13. Перезапустите службу NGINX для применения изменений:

    ```
    nginx -s reload

    ```
14. Отредактируйте файлы конфигурации в соответствии с резервными копиями, [сохранёнными ранее](#ConfigBackup):

    ```
    nano /etc/sysconfig/comindware<instanceName>-env
    nano /var/www/<instanceName>/adapterhost.yml
    nano /var/www/<instanceName>/apigateway.yml
    nano /var/www/<instanceName>/Ignite.config
    nano /usr/share/comindware/configs/instance/<instanceName>.yml

    ```

    Внимание!

    - В новейших версиях **{{ productName }}** отсутствует файл `Workers.config`.
    - Настройка соответствующих служб выполняется в файле конфигурации экземпляра ПО `<instanceName>.yml`.
15. Перезапустите сервисы **{{ productName }}**:

    ```
    systemctl restart adapterhost<instanceName>.service
    systemctl restart comindware<instanceName>.service
    systemctl restart apigateway<instanceName>.service

    ```
16. Откройте сайт экземпляра ПО в браузере, одновременно открыв выдачу журналов экземпляра в терминале:

    ```
    tail -f /var/log/comindware/<instanceName>/Logs/heartbeat*

    ```
17. В браузере выполните инициализацию экземпляра ПО, выполните вход и проверьте работоспособность ПО.
18. Остановите экземпляр ПО:

    ```
    systemctl stop comindware<instanceName>

    ```
19. Скопируйте в экземпляр ПО директорию с базой данных экземпляра ПО, сохранённую ранее (`<username>` — имя пользователя Linux):

    ```
    cp  -R /home/<username>/<instanceName>/Database /var/lib/comindware/<instanceName>/

    ```
20. Перейдите в папку с экземпляром ПО и поменяйте права для скопированной директории с базой данных:

    ```
    cd /var/lib/comindware/<instanceName>/
    chmod -R 777 Database/
    sudo chown -R www-data:www-data Database/

    ```
21. Запустите экземпляр ПО:

    ```
    systemctl restart comindware<instanceName>

    ```
22. Откройте сайт экземпляра ПО в браузере, дождитесь окончания загрузки, одновременно открыв выдачу журналов экземпляра в терминале:

    ```
    tail -f /var/log/comindware/<instanceName>/Logs/heartbeat*

    ```

    См. *«[Подсистема журналирования][logging_engine]»*.
23. Дождитесь завершения обновления структуры данных и проверьте его успешное выполнение.

    Внимание!

    При обновлении с версии 4.7.2 на версии 4.7.3-5.0 обновляется структура базы данных.

    После этого необходимо вручную удалить некоторые данные кэша в старом формате.

    Поэтому продолжать обновление версии экземпляра ПО можно только после успешного обновления структуры данных.

    - Удостоверьтесь, что появились журналы обновления:
      - `/var/log/comindware/<instanceName>/Logs/UpgradeOntology.log`
      - `/var/log/comindware/<instanceName>/Logs/upgrade<ГГГГ-ММ-ДД>.log`
    - Удостоверьтесь, что в журнале `UpgradeOntology.log` последняя запись содержит строку `Upgrade of ontology completed successfully`.
    - Удостоверьтесь, что в журнале `upgrade<ГГГГ-ММ-ДД>.log` последняя запись содержит строку `Upgrade completed`.
    - Удостоверьтесь, что в журналах отсутствуют ошибки обновления. Найдите их по ключевому слову `error`.
    - Если обновление выполнено успешно, переходите к шагу 24.
    - Если в журнале обновления имеются ошибки:

      1. Не переходите к шагу 24.
      2. Снова установите для экземпляра старую версию ПО.
      3. Восстановите базу данных из резервной копии.
      4. Обратитесь в службу поддержки **Comindware**, предоставив журналы обновления и ошибок для анализа.
24. Создайте резервную копию экземпляра ПО:

    - в формате `.CDBBZ` средствами **{{ productName }}**;

      или
    - c помощью скрипта для создания снимка базы.
25. Остановите экземпляр ПО.
26. Распакуйте резервную копию и удалите из неё следующие директории кэшей:

    ```
    rm -rf cacheGroup-*-TableIdentity
    rm -rf cacheGroup-*-TableIdentityReplicated
    rm -rf cacheGroup-*Value
    rm -rf cacheGroup-*ValueReplicated
    rm -rf cache-ignite-sys-cache
    rm -rf cp
    rm -rf metastorage
    rm -rf cacheGroup-Keys

    ```
27. Очистите директорию с базой данных экземпляра ПО:

    ```
    rm -rf /var/lib/comindware/<instanceName>/Database/*

    ```
28. Скопируйте очищенную резервную копию в директорию с базой данных `/var/lib/comindware/<instanceName>/Database/`.
29. Назначьте владельца директории с базой данных:

    - **Astra Linux, Ubuntu, Debian** (DEB-based)

    ```
    chown -R www-data:www-data /var/lib/comindware/<instanceName>/Database

    ```

    - **РЕД ОС, Rocky** (RPM-based)

    ```
    chown -R nginx:nginx /var/lib/comindware/<instanceName>/Database

    ```

    - **Альт Сервер**

    ```
    chown -R _nginx:_nginx /var/lib/comindware/<instanceName>/Database

    ```
30. Проверьте и при необходимости исправьте конфигурацию экземпляра ПО. См. *«[Проверка и настройка конфигурации экземпляра ПО {{ productName }} после восстановления из резервной копии][restore_test_configure]»*.
31. Проверьте и работоспособность экземпляра ПО.
32. Создайте резервную копию работоспособного экземпляра **{{ productName }}**.

--8<-- "related_topics_heading.md"

- [Обновление версии экземпляра ПО без его остановки][upgrade_version_linux_no_stop]
- [Установка, запуск, инициализация и остановка ПО][deploy_guide_linux]
- [Резервное копирование. Настройка и запуск, просмотр журнала сеансов][backup_configure]
- [Подсистема журналирования][logging_engine]
- [Проверка и настройка конфигурации экземпляра ПО {{ productName }} после восстановления из резервной копии][restore_test_configure]

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
