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
3. Удостоверьтесь, что файлы конфигурации соответствуют приведённым ниже образцам, и при необходимости создайте и отредактируйте их.

    - Отредактируйте файл `/usr/share/comindware/configs/instance/<instanceName>.yml` по следующему образцу:

```
#################### Настройка базовых параметров ПО ####################
# Имя экземпляра ПО
# Устаревшая директива: instanceName
clusterName: <instanceName>
# Имя узла экземпляра ПО
#nodeName: <instanceName>
# Путь к экземпляру, по которому ПО находит свою конфигурацию
configPath: <configPath>
# Адрес службы журналирования (Elasticsearch, OpenSearch)
# Устаревшая директива: elasticsearchUri
journal.server: http://<searchHostIP>:<searchHostPort>
# Индекс службы журналирования (Elasticsearch, OpenSearch)
# journal.name: <instanceName>
# URI-адрес экземпляра ПО
fqdn: <hostName>
# Порт экземпляра ПО
port: <portNumber>
# Версия экземпляра ПО
version: <versionNumber>
#################### Настройка базы данных ####################
# Путь к базе данных
# Устаревшая директива: databasePath
db.workDir: /var/lib/comindware/<instanceName>/Database
# Используемый префикс кэшей в базе данных
# Устаревшая директива: databaseName
db.name: <instanceName>
#################### Настройка хранения пользовательских файлов ####################
# Тип хранилища (LocalDisk | S3)
userStorage.type: LocalDisk
# Путь к пользовательским файлам экземпляра
userStorage.localDisk.path: /var/lib/comindware/<instanceName>/Streams
#################### Настройка хранения временных файлов ####################
# Тип хранилища (LocalDisk | S3)
tempStorage.type: LocalDisk
# Путь к временным файлам экземпляра
tempStorage.localDisk.path: /var/lib/comindware/<instanceName>/Temp
# Временная папка
tempWorkingDir: /var/lib/comindware/fooo/LocalTemp
#################### Настройки очереди сообщений ####################
# Адрес и порт сервера очереди сообщений (Kafka)
mq.server: <kafkaBrokerIP>:<kafkaBrokerPort>
# Идентификатор группы очереди сообщений
mq.group: <instanceName>
#################### Конфигурация резервного копирования ####################
# Папка для резервного копирования по умолчанию
# Устаревшая директива: backup.config.default.repository.localDisk.path
backup.defaultFolder: /var/lib/comindware/<instanceName>/Backup
# Имя файла для резервного копирования по умолчанию
backup.defaultFileName: Backup
```

Внимание!

Директивы `isFederationAuthEnabled` и `manageAdapterHost` требуется удалить, если они присутствуют.

Директивы `mq.server` (адрес и порт сервера очереди сообщений), `mq.group` (идентификатор группы очереди сообщений), `mq.node` (идентификатор узла очереди сообщений) и `cluster.name` / `clusterName` (имя экземпляра ПО) должны совпадать в трёх файлах конфигурации:

    - `/usr/share/comindware/configs/instance/<instanceName>.yml`
    - `/var/www/<instanceName>/adapterhost.yml`
    - `/var/www/<instanceName>/apigateway.yml`

    - Отредактируйте файл `/var/www/<instanceName>/adapterhost.yml` по следующему образцу:

```
# Имя экземпляра ПО
clusterName: <instanceName>
# Имя папки загрузчика экземпляра ПО
loaderFolder: <instanceName>
# Язык сервера (en-US | ru-RU )
serverLanguage: ru-RU
# Адрес и порт сервера очереди сообщений (Kafka)
mq.server: <kafkaBrokerIp>:<kafkaBrokerPort>
# Протокол безопасности очереди сообщений. (Plaintext | Ssl | SaslPlaintext | SaslSsl)
mq.securityProtocol: Plaintext
# Тип механизма SASL (None | Plain | ScramSha256 | ScramSha512)
mq.sasl.mechanism: None
# Путь к файлам журналирования экземпляра ПО
log.folder: /var/log/comindware/<instanceName>/Logs/
# Максимальное кол-во файлов журналов
log.maxArchiveFiles: 100
# Максимальный размер файлов журналов (байты)
log.archiveAboveSize: 1048576000
# Путь к архивам журналов
log.archiveFolder: /var/log/comindware/<instanceName>/Logs/Archive/
```

Внимание!

Файл `adapterhost.yml` не должен содержать пустых строк.

    - Отредактируйте файл `/var/www/<instanceName>/apigateway.yml` по следующему образцу:

```
# Имя экземпляра ПО
cluster.name: <instanceName>
# Имя узла экземпляра
# nodeName:
# Включение/выключение конфигурации журналирования экземпляра (true | false)
log.enabled: true
# Путь к файлу конфигурации журналирования экземпляра
log.configurationFile: /var/www/<instanceName>/logs.config
kata.enabled: false
# Адрес сервера очереди сообщений (Kafka) с портом.
mq.server: <kafkaBrokerIp>:<kafkaBrokerPort>
# Идентификатор группы очереди сообщений
mq.group: <instanceName>
# Идентификатор узла очереди сообщений
mq.node: <instanceName>
# Тип механизма SASL. (None | Plain | ScramSha256 | ScramSha512)
mq.sasl.mechanism: None
# Протокол безопасности очереди сообщений. (Plaintext | Ssl | SaslPlaintext | SaslSsl)
mq.securityProtocol: Plaintext
# Путь к сокету apigateway
listen.socketPath: /var/www/<instanceName>/App_Data/apigateway.socket
# Включение/выключение файлового хранилища  (true | false)
fileStorage.enabled: true
# Тип файлового хранилища (Platform — встроенное | Custom — особая DLL-библиотека )
fileStorage.type: Platform
# IP-адрес сервера для загрузки файлов
fileStorage.attachmentServerUri: http://local.host.ip.address/
# Путь к загружаемым файлам
fileStorage.uploadAttachment.path: /api/Attachment/Upload
# Путь к скачанным файлам
fileStorage.downloadAttachment.path: /api/Attachment/GetReferenceContent/{0}
# Путь к удалённым файлам
fileStorage.removeAttachment.path: /api/Attachment/Remove/{0}
# Префиксы служб API
services:
- apiPrefix: conversation
- apiPrefix: useractivity
- apiPrefix: notification
- apiPrefix: architect
```
4. Сохраните резервную копию конфигурационных файлов, например в директорию `/var/backups/config_tmp`:

    - **Astra Linux**, **Ubuntu**, **Debian** (DEB-based)

```
mkdir -p /var/backups/config_tmp/
cd /var/www/<instanceName>/
cp *.config *.yml /var/backups/config_tmp/
cp /etc/nginx/sites-available/comindware<instanceName> /var/backups/config_tmp/
```

    - **РЕД ОС**, **Rocky** (RPM-based)

```
mkdir -p /var/backups/config_tmp/
cd /var/www/<instanceName>/
cp *.config *.yml /var/backups/config_tmp/
cp /etc/nginx/conf.d/comindware<instanceName> /var/backups/config_tmp/
```

    - **Альт Сервер**

```
mkdir -p /var/backups/config_tmp/
cd /var/www/<instanceName>/
cp *.config *.yml /var/backups/config_tmp/
cp /etc/nginx/sites-available.d/comindware<instanceName> /var/backups/config_tmp/
```

Здесь `<instanceName>` — имя экземпляра ПО.
5. Остановите экземпляр ПО и вспомогательные службы и удостоверьтесь, что они остановлены:

```
systemctl stop apigateway<instanceName> comindware<instanceName>
systemctl status apigateway<instanceName> comindware<instanceName>
```
6. Проверьте, выполняется ли сервис `Comindware.Adapter.Agent.exe`:

```
ps fax | grep Agent
```

    - Если процесс `Comindware.Adapter.Agent.exe`, выполняется, завершите его по `PID`:
    
    
    
    
    ```
    kill -9 <PID>
    ```
7. Проверьте имя и статус экземпляра:

```
systemctl status comindware*
```
8. Удалите (или переместите в резервное хранилище) неиспользуемые предыдущие дистрибутивы ПО (`<distPath>` — путь к директории с дистрибутивом, `<osname>` — название операционной системы):

```
rm -rf <distPath>/CMW_<osname>
```

## Обновление версии ПО для экземпляра

Выполните шаги 6–13 для каждого экземпляра ПО, версию которого требуется обновить, так как скрипт обновления выполняется отдельно для указанного экземпляра ПО.

1. Скачайте и распакуйте дистрибутив с новой версией ПО (`X.X`, `<versionNumber>` — номер версии ПО):

```
cd <distPath>
tar -xf X.X-release-ru-<versionNumber>.<osname>.tar.gz
```
2. Перейдите в распакованную папку:

```
cd CMW_<osname>_<versionNumber>/scripts/
```
3. Запустите установку распакованного дистрибутива ПО:

```
bash version_install.sh
```
4. Проверьте наличие и имя директории установленной версии ПО:

```
bash version_list.sh
```
5. Отобразится список установленных версий ПО на сервере.
6. Перейдите в директорию скриптов для работы с экземпляром ПО и запустите его обновление до требуемой версии:

```
bash instance_upgrade.sh -n=<instanceName> -vp=/var/www/.cmw_version/<versionNumber>
```

Здесь:

    - `-n=<instanceName>` — имя обновляемого экземпляра ПО;
    - `-vp=/var/www/.cmw_version/<versionNumber>` — укажите путь к папке с установленной версией ПО, где `<versionNumber>` — номер версии ПО.
7. По окончании обновления скрипт выведет информацию о компонентах экземпляра ПО. Удостоверьтесь, что компоненты успешно обновлены.

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

```
systemctl restart comindware<instanceName>.service
systemctl restart apigateway<instanceName>.service
systemctl restart adaperhost<instanceName>.service
systemctl restart kafka.service
systemctl restart elasticsearch.service
```
8. Проверьте корректность конфигурации NGINX для экземпляра ПО:

    - **Astra Linux**, **Ubuntu**, **Debian** (DEB-based)
    
    
    
    
    ```
    cat /etc/nginx/sites-available/comindware<instanceName>
    ```
    - **РЕД ОС**, **Rocky** (RPM-based)
    
    
    
    
    ```
    nano /etc/nginx/conf.d/comindware<instanceName>
    ```
    - **Альт Сервер**
    
    
    
    
    ```
    nano /etc/nginx/sites-available.d/comindware<instanceName>
    ```
    - При необходимости восстановите конфигурацию NGINX, [сохранённую ранее](#NginxBackup).
    
    
        - **Astra Linux**, **Ubuntu**, **Debian** (DEB-based)
    
    ```
    cp /var/backups/config_tmp/comindware<instanceName> /etc/nginx/sites-available/
    nginx -t && nginx -s reload
    ```
    
    
        - **РЕД ОС**, **Rocky** (RPM-based)
    
    ```
    cp /var/backups/config_tmp/comindware<instanceName> /etc/nginx/conf.d/
    nginx -t && nginx -s reload
    ```
    
    
        - **Альт Сервер**
    
    ```
    cp /var/backups/config_tmp/comindware<instanceName> /etc/nginx/sites-available.d/
    nginx -t && nginx -s reload
    ```
9. Удостоверьтесь, что файлы конфигурации соответствуют [приведённым выше образцам](#config_samples).
10. Перезапустите сервисы, настройки которых были изменены:

```
systemctl restart apigateway<instanceName> comindware<instanceName>
```
11. Откройте сайт экземпляра ПО в браузере, дождитесь окончания загрузки, одновременно открыв выдачу журналов экземпляра в терминале:

```
tail -f /var/log/comindware/<instanceName>/Log/sys*
```
12. После обновления всех экземпляров ПО, старую версию ПО можно удалить согласно инструкции *«[Удаление версии ПО](deploy_guide.html#deploy_guide_linux_delete_version)»*.

--8<-- "related_topics_heading.md"

- *[Установка, запуск, инициализация и остановка ПО][deploy_guide_linux]*
- *[Резервное копирование. Настройка и запуск, просмотр журнала сеансов][backup_configure]*


{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
