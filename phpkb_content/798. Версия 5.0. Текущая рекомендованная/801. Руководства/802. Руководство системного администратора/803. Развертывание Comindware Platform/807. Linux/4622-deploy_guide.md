---
title: Установка, запуск, инициализация и остановка Comindware Platform
kbId: 4622
---

# Установка, запуск, инициализация и остановка {{ productName }}

## Введение

Для работы **{{ productName }}** требуются операционная система, сервер базы данных, веб-сервер, обратный прокси-сервер и сервер журналов.

Для быстрого развёртывания **{{ productName }}** в Linux компания **Comindware** предоставляет дистрибутив с установщиком, настраивающим необходимое программное обеспечение. См. *[{{ productName }} 5.0. Перечень стороннего программного обеспечения для Linux][auxiliary_software_list]*.

Здесь представлены инструкции по развёртыванию и инициализации **{{ productName }}** из дистрибутива в ОС Linux.

## Порядок развёртывания ПО {{ productName }}

1. Установите и настройте необходимое вспомогательное ПО.
2. Установите ПО **{{ productName }}**.
3. Создайте экземпляр ПО.
4. Запустите экземпляр ПО.
5. Инициализируйте экземпляр ПО.

## Установка вспомогательного ПО

Прежде чем приступать к установке вспомогательного ПО, необходимого для работы **{{ productName }}**, ознакомьтесь с демонстрационным роликом и инструкциями, представленными ниже.

### Видеоинструкция

### Порядок установки вспомогательного ПО

1. Перейдите в режим суперпользователя:

````
sudo -s

````
или

````
su -

````
2. Скачайте и распакуйте дистрибутив с вспомогательным ПО **{{ productName }}**, полученный по ссылке от компании **Comindware** (`X.X`, `<versionNumber>` — номер версии ПО, `<osname>` — название операционной системы):

````
tar -xf X.X-release-ru-<versionNumber>.prerequisites.<osname>.tar.gz

````

Совет

После распаковки архив можно удалить для экономии места:

````
rm -f X.X-release-ru-<versionNumber>.prerequisites.<osname>.tar.gz

````
3. Перейдите в директорию со скриптами для развёртывания вспомогательного ПО:

````
cd <prerequisitesDistPath>/CMW_<osname>/scripts

````
Здесь: `<prerequisitesDistPath>/CMW_<osname>/` — путь к распакованному дистрибутиву со вспомогательным ПО.
4. Установите ПО из дистрибутива:

````
sh prerequisites_install.sh -p [-k] [-e]

````
Скрипт `prerequisites_install.sh` поддерживает следующие ключи:

    - `-p` — установить обязательное вспомогательное ПО.
    - `-k` — установить ПО Kafka (необязательный ключ).
    - `-e` — установить ПО Elasticsearch или OpenSearch (необязательный ключ).
    - `-kh=<hostname>` или `--kafkaHost=<hostname>` — использовать указанный хост для подключения к ПО Kafka (необязательный ключ).
    - `-kp=<portNumber>` или `--kafkaPort=<portNumber>` — использовать указанный порт для подключения к ПО Kafka (необязательный ключ).
    - `-h` — вызов краткой справки по использованию скрипта (указывать только без остальных ключей).
Примечание

Скрипт `prerequisites_install.sh` устанавливает необходимые для **{{ productName }}** компоненты, включая Java, .NET, Mono, NGINX.

Вызов справки для скриптов

Для ознакомления с ключами и назначением любого скрипта используйте ключ `-h` без каких-либо других ключей, например:

````
sh prerequisites_install.sh -h

````

Конфигурация сервера журналирования (Elasticsearch, OpenSearch)

    - В конфигурации Elasticsearch (OpenSearch) необходимо создать одного пользователя для **{{ productName }}**.
    - В конфигурации экземпляра ПО необходимо указать адрес сервера и уникальный префикс индексов Elasticsearch (OpenSearch). Индекс префикса служит для идентификации данных экземпляра ПО в Elasticsearch (OpenSearch). Поэтому во избежание конфликтов данных для каждого экземпляра ПО следует указывать собственный префикс индекса.
    - При [инициализации экземпляра ПО](#initialize_instance) необходимо указать пользователя **{{ productName }}**, используемого в Elasticsearch (OpenSearch).
    - Экземпляр ПО будет взаимодействовать с Elasticsearch (OpenSearch) под указанным пользователем и создавать, наполнять и читать индексы с заданным префиксом.
5. По окончании установки скрипт выведет информацию об установленных компонентах. Удостоверьтесь, что компоненты успешно установлены (имеют статус `OK`).

Пример результата выполнения скрипта с ключом `-p` без установки Elasticsearch и Kafka:

````
[Done] Creating CBAP Data Dir.
-----------------------------------------
Environment details
Status     | Software   | Version
-----------------------------------------
OK         | mono       | 6.12.0.182
OK         | dotnet     | 6.0.417
OK         | java       | 17.0.7
OK     NGINX installed.
OK     NGINX started.
OK     CBAP version folder created.
OK     CBAP configs folder created.
OK     CBAP data folder created.
OK     CBAP logs folder created.
OK     CBAP dotnet folder created.
OK     Local elasticsearch server installed: No
OK     Local elasticsearch server started: No
OK     Local kafka server installed: No
OK     Local kafka server started: No
OK     Final status.

````
6. Удостоверьтесь, что компоненты установлены:

````
sh prerequisites_list.sh

````

## Установка ПО {{ productName }}

Прежде чем приступать к установке ПО **{{ productName }}**, ознакомьтесь с видеороликом и инструкциями, представленными ниже.

### Видеоинструкция

### Порядок установки ПО {{ productName }}

1. Перейдите в режим суперпользователя:

````
sudo -s

````
или

````
su -

````
2. Скачайте и распакуйте дистрибутив ПО **{{ productName }}**, полученный по ссылке от компании **Comindware**:

````
tar -xf X.X-release-ru-<versionNumber>.<osname>.tar.gz

````

Совет

После распаковки архив можно удалить для экономии места:

````
rm -f X.X-release-ru-<versionNumber>.<osname>.tar.gz

````
3. Перейдите в директорию со скриптами для развёртывания ПО:

````
cd <distPath>/CMW_<osname>_<versionNumber>/scripts

````
Здесь: `<distPath>/CMW_<osname>_<versionNumber>/` — путь к распакованному дистрибутиву со ПО **{{ productName }}**.
4. Установите ПО из дистрибутива:

````
sh version_install.sh

````
5. Если отобразится запрос на перезагрузку ОС, выполните перезагрузку:

````
reboot

````
После перезагрузки ОС перейдите в режим суперпользователя и заново запустите [установку ПО из дистрибутива (шаг 3)](#install_sh).
6. После успешного завершения установки подождите 3–5 минут. Этого времени обычно достаточно для автоматического запуска и инициализации установленных служб (в зависимости от конфигурации машины).
7. Удостоверьтесь, что ПО установлено, просмотрев список установленных версий ПО:

````
sh version_list.sh

````

## Создание экземпляра ПО

Прежде чем приступать к установке экземпляра ПО **{{ productName }}**, ознакомьтесь с видеороликом и инструкциями, представленными ниже.

### Видеоинструкция

### Подготовка к созданию экземпляра ПО

Перед созданием экземпляра ПО проверьте конфигурацию Linux и при необходимости внесите в неё перечисленные ниже изменения.

1. Перейдите в режим суперпользователя:

````
sudo -s

````
или

````
su -

````
2. Откройте для редактирования файл `limits.conf`:

````
nano /etc/security/limits.conf

````
3. Установите следующие директивы:

    - **Astra Linux**, **Ubuntu**, **Debian** (DEB-based)````
www-data soft nproc 200000
www-data hard nproc 200000
www-data soft nofile 200000
www-data hard nofile 200000

````
    - **РЕД ОС**, **Rocky** (RPM-based)````
nginx soft nproc 200000
nginx hard nproc 200000
nginx soft nofile 200000
nginx hard nofile 200000

````
    - **Альт Сервер**````
_nginx soft nproc 200000
_nginx hard nproc 200000
_nginx soft nofile 200000
_nginx hard nofile 200000

````
4. Откройте файл `common-session` для редактирования:

````
nano /etc/pam.d/common-session

````
5. Установите следующую директиву:

````
session required pam_limits.so

````
6. Откройте файл `sysctl.conf` для редактирования:

````
nano /etc/sysctl.conf

````
7. Установите следующие директивы:

````
fs.file-max=2097152
vm.max_map_count=262144
fs.inotify.max_user_instances=524288

````
8. Откройте файл `user.conf` для редактирования:

````
nano /etc/systemd/user.conf

````
9. Установите следующую директиву:

````
DefaultLimitNOFILE=200000

````
10. Откройте файл `system.conf` для редактирования:

````
nano /etc/systemd/system.conf

````
11. Установите следующую директиву:

````
DefaultLimitNOFILE=200000

````
12. После внесения изменений перезапустите демоны:

````
sysctl -p
systemctl daemon-reexec

````

### Создание единственного экземпляра ПО

1. Перейдите в режим суперпользователя:

````
sudo -s

````
или

````
su -

````
2. Перейдите в директорию со скриптами для развёртывания ПО **{{ productName }}**:

````
cd <distPath>/CMW_<osname>_<versionNumber>/scripts

````
Здесь: `<distPath>/CMW_<osname>_<versionNumber>/` — путь к распакованному дистрибутиву ПО.
3. Разверните экземпляр ПО:

````
sh instance_create.sh -n=<instanceName> -v=<versionNumber> [-p=<portNumber>]

````
Скрипт `instance_create.sh` поддерживает следующие ключи:

    - `-n=<instanceName>` — имя экземпляра ПО (**обязательный** ключ).
    - `-v=<versionNumber>` — номер версии ПО вида `X.X.XXXXX.X` (например: 5.0.00000.0, **обязательный** ключ). Версия должна быть установлена, см. *«[Установка {{ productName }}](#deploy_guide_linux_install_sw)»*.
    - `-p=<portNumber>` — порт для экземпляра ПО, по умолчанию: 80 (необязательный ключ).
    - `-fqdn=<hostName>` или `--instance-fqdn=<hostName>` — имя хоста для экземпляра ПО (необязательный ключ). По умолчанию: localhost.
    - `-el=<hostName>` или `--elasticsearch-url=<hostName>` — использовать указанный URL или IP-адрес для подключения к ПО Elasticsearch (OpenSearch).
    - `-kf=<hostName>` или `--kafka-url=<hostName>` — использовать указанный URL или IP-адрес для подключения к ПО Kafka.
    - `-h` — вызов краткой справки по использованию скрипта (указывать только без остальных ключей).
4. По окончании установки скрипт выведет информацию об установленных компонентах. Удостоверьтесь, что компоненты успешно установлены (имеют статус `OK`).

Пример результата выполнения скрипта:

````
OK     Instance folder created.
OK     Instance Web config created.
OK     Instance Ignite config created.
OK     Instance binaries linked.
OK     Instance config created.
OK     Data folder created.
OK     Database folder created: No
OK     Streams folder created: No
OK     Logs folder created: Yes
OK     Used version: 5.0.0000.0
OK     Logs configured.
OK     Sites created.
OK     Sites enabled.
OK     API Gateway configured.
OK     Link to binaries is valid.
OK     Instance service started.
OK     Instance API gateway service started.
OK     Instance adapter host service started.
OK     NGINX started.
OK     Final status.
[Done] Creating a new CBAP instance.

````
5. Удостоверьтесь, что была создана директория с файлами конфигурации экземпляра ПО.

````
ls -lhF /var/www/<instanceName>/

````
6. По выводу команды `ls` удостоверьтесь, что в путях указана корректная версия ПО, например `5.0.0000.0`:

````
lrwxrwxrwx. 1 nginx nginx   36 Oct 11 17:54 bin -> /var/www/.cmw_version/5.0.0000.0/bin/
lrwxrwxrwx. 1 nginx nginx   41 Oct 11 17:54 compiled -> /var/www/.cmw_version/5.0.0000.0/compiled/
lrwxrwxrwx. 1 nginx nginx   37 Oct 11 17:54 data -> /var/www/.cmw_version/5.0.0000.0/data/
lrwxrwxrwx. 1 nginx nginx   44 Oct 11 17:54 favicon.ico -> /var/www/.cmw_version/5.0.0000.0/favicon.ico
lrwxrwxrwx. 1 nginx nginx   44 Oct 11 17:54 Global.asax -> /var/www/.cmw_version/5.0.0000.0/Global.asax
lrwxrwxrwx. 1 nginx nginx   39 Oct 11 17:54 mobile -> /var/www/.cmw_version/5.0.0000.0/mobile/
lrwxrwxrwx. 1 nginx nginx   46 Oct 11 17:54 redirect.aspx -> /var/www/.cmw_version/5.0.0000.0/redirect.aspx
lrwxrwxrwx. 1 nginx nginx   42 Oct 11 17:54 resources -> /var/www/.cmw_version/5.0.0000.0/resources/
lrwxrwxrwx. 1 nginx nginx   43 Oct 11 17:54 robots.txt -> /var/www/.cmw_version/5.0.0000.0/robots.txt
lrwxrwxrwx. 1 nginx nginx   45 Oct 11 17:54 unauthorized -> /var/www/.cmw_version/5.0.0000.0/unauthorized/

````

### Создание дополнительного экземпляра ПО

На одном сервере можно развернуть несколько экземпляров ПО **{{ productName }}**. Для создания второго и последующих экземпляров ПО выполните указанные ниже действия.

1. Перейдите в режим суперпользователя:

````
sudo -s

````
или

````
su -

````
2. Просмотрите список имеющихся экземпляров ПО **{{ productName }}**:

````
cat /usr/share/comindware/configs/instance/* | grep -E '(configPath:)'

````
3. Просмотрите список используемых портов:

````
ss -tunlp

````
Также можно узнать, используется ли определённый порт (`<portNumber>`):

````
ss -tunlp | grep :<portNumber>

````
4. Просмотрите список установленных версий ПО:

````
ls /var/www/.cmw_version/

````
5. Создайте новый экземпляр ПО согласно приведённым выше [инструкциям](#создание-экземпляра-по), указав для него **уникальные имя и порт**.
6. Откройте для редактирования три службы **каждого** из установленных экземпляров ПО (`<instanceName>`):

````
nano /usr/lib/systemd/system/comindware<instanceName>.service
nano /usr/lib/systemd/system/apigateway<instanceName>.service
nano /usr/lib/systemd/system/adapterhost<instanceName>.service

````
7. Если используются локальные службы Kafka и Elasticsearch (OpenSearch), откройте их для редактирования:

````
nano /usr/lib/systemd/system/kafka.service
nano /usr/lib/systemd/system/elasticsearch.service

````
8. В каждом файле службы установите следующие директивы:

````
# Макс. количество открытых файлов
LimitNOFILE=200000
# Макс. количество процессов
LimitNPROC=8192

````

## Запуск экземпляра ПО

1. Перейдите в режим суперпользователя:

````
sudo -s

````
или

````
su -

````
2. Удостоверьтесь, что основные службы установлены, запущены и имеют статус `Active (running)`:

````
systemctl status comindware<instanceName>
systemctl status apigateway<instanceName>
systemctl status adapterhost<instanceName>
systemctl status kafka
systemctl status nginx
systemctl status elasticsearch

````
3. Если какая-либо служба не работает, запустите её:

````
systemctl start comindware<instanceName>
systemctl start apigateway<instanceName>
systemctl start adapterhost<instanceName>
systemctl start kafka
systemctl start nginx
systemctl start elasticsearch

````
4. Выполните инициализацию ПО.

## Инициализация {{ productName }}

1. Запустите веб-браузер и в адресной строке введите URL-адрес, на котором был развёрнут экземпляр ПО:

````
http://<instanceHost>:<portNumber>

````
2. Дождитесь запуска и отображения веб-сайта **{{ productName }}**, что может занять примерно 5 минут.
3. Откроется страница создания аккаунта администратора **{{ productName }}**.

_![Страница создания аккаунта администратора](/platform/v5.0/administration/deploy/linux/img/deploy_guide_admin_account_create.png)_
4. Введите учётные данные аккаунта администратора и нажмите кнопку «**Создать аккаунт**».

Внимание!

    - В экземпляре ПО всегда должен оставаться хотя бы один аккаунт администратора. Он может потребоваться для восстановления системы.
    - Аккаунт администратора, созданный при инициализации экземпляра ПО, не следует удалять, даже если впоследствии аккаунты будут синхронизироваться с Active Directory.
5. При необходимости откроется страница инициализации служб. Выберите службы, которые должны быть запущены, и нажмите кнопку «**Далее**».

_![Страница инициализации служб](/platform/v5.0/administration/deploy/linux/img/deploy_guide_system_initialize.png)_
6. При необходимости откроется страница активации ПО. Выполните **онлайн-** или **ручную активацию** либо нажмите кнопку «**Пропустить**» для первоначального ознакомления с ПО без активации.
7. При необходимости откроется страница настройки подключения к службе Elasticsearch (OpenSearch).

    - В поле «**URI**» введите адрес сервера Elasticsearch (OpenSearch), например: `http://localhost:9200`.
    - При необходимости введите **имя пользователя** и **пароль** Elasticsearch (OpenSearch).
    - Установите уникальный **префикс индекса**, например `mycompanyprefix`.
    - Экземпляр ПО будет взаимодействовать с Elasticsearch (OpenSearch) под указанным пользователем и создавать, наполнять и читать индексы с заданным префиксом.
    - Нажмите кнопку «**Далее**».
8. При необходимости откроется страница инициализации данных в Elasticsearch (OpenSearch).

_![Страница инициализации данных в Elasticsearch](/platform/v5.0/administration/deploy/linux/img/deploy_guide_elasticsearch_initialize.png)_
9. Нажмите кнопку «**Обновить**».
10. Дождитесь открытия начальной страницы **{{ productName }}**.
11. На этом этапе развертывание экземпляра **{{ productName }}** завершено и можно приступать к созданию и использованию приложений.

## Остановка экземпляра ПО

1. Перейдите в режим суперпользователя:

````
sudo -s

````
или

````
su -

````
2. Перед тем как выполнять любые действия с файлами ПО и базы данных, остановите службы, поддерживающие работу ПО:

````
systemctl stop comindware<instanceName>
systemctl stop apigateway<instanceName>
systemctl stop adapterhost<instanceName>
systemctl stop kafka
systemctl stop nginx
systemctl stop elasticsearch

````
3. Удостоверьтесь, что службы остановлены:

````
systemctl status comindware<instanceName>
systemctl status apigateway<instanceName>
systemctl status adapterhost<instanceName>
systemctl status kafka
systemctl status nginx
systemctl status elasticsearch

````

## Удаление версии и экземпляра ПО

Прежде чем приступать к удалению версии и экземпляра ПО **{{ productName }}**, ознакомьтесь с видеороликом и инструкциями, представленными ниже.

### Видеоинструкция

### Удаление экземпляра ПО

1. Перейдите в режим суперпользователя:

````
sudo -s

````
или

````
su -

````
2. Остановите экземпляр ПО согласно [инструкции](#остановка-экземпляра-по).
3. Перейдите в директорию со скриптами для развёртывания ПО **{{ productName }}**:

````
cd <distPath>/CMW_<osname>_<versionNumber>/scripts

````
4. Запустите удаление экземпляра ПО:

````
sh instance_delete.sh -n=<instanceName>

````
Скрипт `delete.sh` поддерживает следующие ключи:

    - `-n=<instanceName>` — удалить экземпляр ПО с указанным именем (**обязательный** ключ).
    - `--delete-data=true` — безвозвратно удалить все файлы базы данных экземпляра ПО (необязательный ключ).
    - `-h` — вызов краткой справки по использованию скрипта (указывать только без остальных ключей).
5. Удостоверьтесь, что экземпляр ПО был успешно удалён, просмотрев список установленных экземпляров ПО:

````
sh instance_list.sh

````

### Удаление версии ПО

1. Перейдите в режим суперпользователя:

````
sudo -s

````
или

````
su -

````
2. Просмотрите список экземпляров ПО с указанием версий:

````
sh instance_list.sh

````
3. Удалите все экземпляры с версией ПО, которую требуется удалить, или обновите их до другой версии. Удалить версию ПО, которая используется в каких-либо экземплярах, не удастся. См. *«[Удаление экземпляра ПО](#удаление-экземпляра-по)»*.
4. Перейдите в директорию со скриптами для развёртывания ПО **{{ productName }}**:

````
cd <distPath>/CMW_<osname>_<versionNumber>/scripts

````
5. Просмотрите список установленных версий ПО:

````
sh version_list.sh

````
6. Удалите версию ПО:

````
sh version_delete.sh -v=<versionNumber>

````
Здесь: `-v=<versionNumber>` — укажите номер версии ПО вида `X.X.XXXX.X` (например: `5.0.0000.0`).
7. Проверьте, что версия ПО была удалена успешно:

````
sh version_list.sh

````
или

````
ls /var/www/.cmw_version

````

--8<-- "related_topics_heading.md"

- *[Пути и содержимое директорий экземпляра ПО][paths]*

[*‌*
 К началу](#)

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
