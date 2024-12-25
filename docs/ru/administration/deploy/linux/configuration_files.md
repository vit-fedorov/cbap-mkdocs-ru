---
title: Конфигурация экземпляра, компонентов ПО и служб. Настройка
kbId: 5067
---

# Конфигурация экземпляра, компонентов ПО и служб. Настройка {: #configuration_files_linux }

## Введение

Здесь представлены инструкции по настройке файлов конфигурации после развёртывания и обновления ПО **{{ productName }}**, его компонентов и служб.

## Конфигурация экземпляра ПО

1. Откройте файл конфигурации экземпляра ПО (`<instanceName>` — имя экземпляра ПО) для редактирования:

    ``` sh
    nano /usr/share/comindware/configs/instance/<instanceName>.yml
    ```

2. При необходимости измените параметры, например:

    - `journal.server` — адрес сервера Elasticsearch (OpenSearch).
    - `journal.name` — индекс сервера Elasticsearch (OpenSearch).
    - `db.workDir` — директория для хранения базы данных экземпляра ПО.
    - `db.name` — префикс кэшей в базе данных экземпляра ПО.
    - `userStorage.localDisk.path` — директория для хранения пользовательских файлов.
    - `mq.server` — адрес сервера Kafka.
    - `backup.defaultFolder` — директория для хранения резервных копий экземпляра ПО.
    - `backup.defaultFileName` — имя файла резервной копии экземпляра ПО.

    <!--config-warning-start-->
    !!! warning "Внимание!"

        Директивы `isFederationAuthEnabled` и `manageAdapterHost` требуется удалить, если они присутствуют.

        Директивы `mq.server` (адрес и порт сервера очереди сообщений), `mq.group` (идентификатор группы очереди сообщений), `mq.node` (идентификатор узла очереди сообщений) и `cluster.name` / `clusterName` (имя экземпляра ПО) должны совпадать в трёх файлах конфигурации:

        - `/usr/share/comindware/configs/instance/<instanceName>.yml`
        - `/var/www/<instanceName>/adapterhost.yml`
        - `/var/www/<instanceName>/apigateway.yml`
    <!--config-warning-end-->

3. Сохраните файл конфигурации.
4. Убедитесь, что директории, указанные в файле конфигурации, существуют. При необходимости создайте их и задайте права доступа:

    ``` sh
    mkdir -p <path/to/Database>
    mkdir -p <path/to/Streams>
    mkdir -p <path/to/Backup>
    chmod -R 766 <path/to/Database> <path/to/Streams> <path/to/Backup>
    chown -R <User>:<Group> <path/to/Database> <path/to/Streams> <path/to/Backup>
    ```

    Здесь значения `<User>` и `<Group>` должны совпадать с такими же параметрами в файле `/usr/lib/systemd/system/comindware<instanceName>.service`

5. Перезапустите службу экземпляра ПО:

    ``` sh
    systemctl restart comindware<instanceName>
    ```

### Пример YML-файла конфигурации экземпляра ПО

<!--instanceYML-start-->
``` yml
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
<!--instanceYML-end-->

## Конфигурация службы apigateway

1. Откройте файл конфигурации `apigateway.yml` экземпляра ПО для редактирования:

    ``` sh
    nano /var/www/<instanceName>/apigateway.yml
    ```

2. Измените необходимые параметры.
3. Удостоверьтесь, что значение параметра `cluster.name` (имя экземпляра ПО) совпадает с `clusterName` и значение параметров `mq.server` (адрес и порт сервера очереди сообщений), `mq.group` (идентификатор группы очереди сообщений), `mq.node` (идентификатор узла очереди сообщений) — с аналогичными параметрами в [файле конфигурации экземпляра](#конфигурация-экземпляра-по).
4. Сохраните файл конфигурации.
5. Перезапустите службу `apigateway`:

    ``` sh
    systemctl restart apigateway<instanceName>
    ```

### Пример конфигурации службы apigateway.yml

<!--apigatewayYML-start-->
``` yml
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
<!--apigatewayYML-end-->

## Конфигурация службы adapterhost

1. Откройте файл конфигурации `adapterhost.yml` экземпляра ПО для редактирования:

    ``` sh
    nano /var/www/<instanceName>/adapterhost.yml
    ```

2. Измените необходимые параметры.
3. Удостоверьтесь, что значения параметров `mq.server` (адрес и порт сервера очереди сообщений), `mq.group` (идентификатор группы очереди сообщений), `mq.node` (идентификатор узла очереди сообщений) и `clusterName` (имя экземпляра ПО) совпадают с аналогичными параметрами в [файле конфигурации экземпляра ПО](#пример-yml-файла-конфигурации-экземпляра-по).
4. Сохраните файл конфигурации.
5. После внесения изменений перезапустите службу `adapterhost`:

    ``` sh
    kill -9 $(ps -eo pid,args | grep $<instanceName> | grep Agent | awk {'print $1'}) && systemctl restart comindware<instanceName>
    ```

### Пример файла конфигурации adapterhost.yml

<!--adapterhostYML-start-->
``` yml
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
<!--adapterhostYML-end-->

## Конфигурация Apache Ignite

1. Откройте файл конфигурации Ignite для редактирования:

    ``` sh
    nano /var/www/<instanceName>/Ignite.config
    ```

2. В блоке `<bean class="org.apache.ignite.configuration.DataRegionConfiguration">` задайте максимальный объём выделяемой памяти:

    - 3 ГБ:

        ``` xml
        <property name="maxSize" value="#{3L * 1024 * 1024 * 1024}" />
        ```

    - 8 ГБ:

        ``` xml
        <property name="maxSize" value="#{8L * 1024 * 1024 * 1024}" />
        ```

3. В случае изменения максимального объёма выделяемой памяти отредактируйте параметр `checkpointPageBufferSize`. Чтобы рассчитать размер значения, разделите размер `maxSize` на четыре, при этом значение должно быть в диапазоне 256 МБ — 2 ГБ.

    - 8 ГБ:

        ``` xml
        <property name="checkpointPageBufferSize" value="#{2L * 1024 * 1024 * 1024}" />
        ```

4. Перезапустите службу экземпляра ПО:

    ``` sh
    systemctl restart comindware<instanceName>
    ```

## Конфигурация кучи Java

В зависимости от объёма оперативной памяти на сервере следует отредактировать конфигурацию области памяти для кучи Java.

1. Откройте файл конфигурации среды экземпляра ПО для редактирования:

    ``` sh
    nano /etc/sysconfig/comindware<instanceName>-env
    ```

2. Задайте объём памяти, который выделяется для кучи Java:

    ``` ini
    JVM_OPTS=-Xms512m -Xmx16g -XX:MaxDirectMemorySize=1g ...
    ```

    Здесь:

    - `-Xms` — начальный размер кучи;
    - `-Xmx` — максимальный размер кучи.

3. Сохраните файл конфигурации.
4. Перезапустите службу экземпляра ПО:

    ``` sh
    systemctl daemon-reload
    systemctl restart comindware<instanceName>
    ```

## Конфигурация NGINX

1. Откройте файл конфигурации NGINX для редактирования:

    - **Astra Linux**, **Ubuntu**, **Debian** (DEB-based)

        ``` sh
        nano /etc/nginx/sites-available/comindware<instanceName>
        ```

    - **РЕД ОС**, **Rocky** (RPM-based)

        ``` sh
        nano /etc/nginx/conf.d/comindware<instanceName>
        ```

    - **Альт Сервер**

        ``` sh
        nano /etc/nginx/sites-available.d/comindware<instanceName>
        ```

2. В директиве `server` задайте номер порта и адрес сервера, по которым будет доступен экземпляр ПО:

    ``` sh
    server {
        # Адрес сервера для доступа к экземпляру ПО.
        server_name <hostName>
        # Номер порта для доступа к экземпляру ПО.
        listen <portNumber>
    }
    ```

3. Для записи событий в отдельные журналы укажите их:

    ``` sh
        error_log /var/log/nginx/<instanceName>-error.log;
        access_log /var/log/nginx/<instanceName>-access.log;
    ```

4. Сохраните файл конфигурации.
5. Проверьте, что изменения работают корректно:

    ``` sh
    nginx -t
    ```

6. При успешном вступлении изменений в силу перезагрузите NGINX:

    ``` sh
    nginx -s reload
    ```

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Пути и содержимое директорий экземпляра ПО][paths]_
- _[Настройка конфигурации вспомогательного ПО для оптимизации работы {{ productName }}][auxiliary_software_optimize]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
