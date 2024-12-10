---
title: Конфигурация экземпляра, компонентов ПО и служб. Настройка
kbId: 5068
---

# Конфигурация экземпляра, компонентов ПО и служб. Настройка {: #configuration_files_linux }

## Введение

Здесь представлены инструкции по настройке файлов конфигурации после развёртывания и обновления ПО **{{ productName }}**, его компонентов и служб.

## Конфигурация экземпляра ПО

1. Откройте файл конфигурации экземпляра ПО (`<instanceName>` — имя экземпляра ПО) для редактирования:

    ``` sh
    nano /usr/share/comindware/configs/instance/<instanceName>.yml
    ```

2. Измените необходимые параметры, например:

    - `databasePath` — путь к базе данных экземпляра ПО.
    - `backup.config.default.repository.localDisk.path` или `backup.defaultFolder` — директория для хранения резервных копий.
    - `userStorage.localDisk.path` — директория для хранения пользовательских файлов.
    - `mq.server` — адрес сервера Kafka.

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

``` yml
# Федеративная аутентификация отключена (1 — вкл.)
isFederationAuthEnabled: 0
# Путь к базе данных
databasePath: /var/lib/comindware/<instanceName>/Database
# Путь к исполняемым и конфигурационным файлам экземпляра ПО
configPath: /var/www/<instanceName>
# Тип хранилища резервных копий: LocalDisk или S3
backup.config.default.repository.type: LocalDisk
# Путь к директории резервных копий
backup.config.default.repository.localDisk.path: /var/backups/<instanceName>
# Тип хранилища пользовательских файлов: LocalDisk или S3
userStorage.type: LocalDisk
# Путь к директории пользовательских файлов
userStorage.localDisk.path: /var/lib/comindware/<instanceName>/Streams
# Тип хранилища временных файлов: LocalDisk или S3
tempStorage.type: LocalDisk
# Путь к директории временных файлов
tempStorage.localDisk.path: /var/lib/comindware/<instanceName>/Temp
# Адрес и порт сервера очереди сообщений (Kafka)
mq.server: <kafkaBrokerIP>:<kafkaBrokerPort>
# Идентификатор группы очереди сообщений. Должно быть уникальным для каждого экземпляра
mq.group: <instanceName>
# Управление службой adapterhost включено
manageAdapterHost: true
# Адрес и порт сервера Elasticsearch
elasticsearchUri: <elasticsearchIP>:<elasticsearchPort>
# Имя экземпляра ПО
instanceName: <instanceName>
# Версия ПО
version: <versionNumber>
```

## Конфигурация службы apigateway

1. Откройте файл конфигурации `apigateway.json` экземпляра ПО для редактирования:

    ``` sh
    nano /var/www/<instanceName>/apigateway.json
    ```

2. Измените необходимые параметры.
3. Удостоверьтесь, что значение параметра `BootstrapServer` (адрес и порт сервера очереди сообщений) совпадает с `mq.server`, а `GroupId` (идентификатор группы очереди сообщений) — с `mq.group` в [файле конфигурации экземпляра ПО](#пример-yml-файла-конфигурации-экземпляра-по).
4. Сохраните файл конфигурации.
5. Перезапустите службу apigateway:

    ``` sh
    systemctl restart apigateway<instanceName>
    ```

### Пример конфигурации службы apigateway.json

```json
{
   "Instance":{
      "Name":"<instanceName>"
   },
   "Log":{
      "Enabled":true,
      "ConfigurationFile":"/var/www/<instanceName>/logs.config"
   },
   "Kata":{
      "Enabled":false
   },
   "Kafka":{
      "BootstrapServer":"<kafkaBrokerIP>:<kafkaBrokerPort>",
      "GroupId":"<instanceName>"
   },
   "Grpc":{
      "SocketPath":"/var/www/<instanceName>/App_Data/apigateway.socket",
      "Protocol":"Http2"
   }
}
```

## Конфигурация службы adapterhost

1. Откройте файл конфигурации `adapterhost.config` экземпляра ПО для редактирования:

    ``` sh
    nano /var/www/<instanceName>/adapterhost.config
    ```

2. Отредактируйте необходимые параметры.
3. Удостоверьтесь, что значение параметра `BootstrapServers` совпадает с `mq.server`, а `groupId` — с `mq.group` в [файле конфигурации экземпляра](#конфигурация-экземпляра-по).
4. Сохраните файл конфигурации.
5. После внесения изменений перезапустите службу adapterhost:

    ``` sh
    kill -9 $(ps -eo pid,args | grep $<instanceName> | grep Agent | awk {'print $1'}) && systemctl restart comindware<instanceName>
    ```

### Пример файла конфигурации adapterhost.config

``` yml
platformKey: <instanceName>
loaderFolder: /var/log/comindware/.adapterhost/<instanceName>/LoadData
deployRequestQueue: request_queue_<hostname>_<instanceName>_deploy_external
deployReplyQueue: reply_queue_<hostname>_<instanceName>_deploy_external
outgoingRequestQueue: request_queue_<hostname>_<instanceName>_outgoing_external
outgoingReplyQueue: reply_queue_<hostname>_<instanceName>_outgoing_external
incomingRequestQueue: request_queue_<hostname>_<instanceName>_incoming_external
incomingReplyQueue: reply_queue_<hostname>_<instanceName>_incoming_external
bootstrapServers: <kafkaBrokerIP>:<kafkaBrokerPort>
groupId: <instanceName>
exclusiveGroupId:
serverLanguage: ru-RU
securityProtocol: Plaintext
caLocation:
endpointIdentificationEnabled: true
saslMechanism: None
username:
password:
logFolder: /var/log/comindware/<instanceName>/Logs/
archiveFolder: /var/log/comindware/<instanceName>/Logs/Archive/
maxArchiveFiles: 30
archiveAboveSize: 104857600
```

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

3. В случае изменения максимального объёма выделяемой памяти отредактируйте параметр `checkpointPageBufferSize`. Чтобы рассчитать размер значения, разделите размер `maxSize` на четыре, при этом значение не должно в диапазоне 256 МБ — 2 ГБ. Для максимального объёма выделяемой памяти в 8 Гб, значение будет следующим:

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
        # Укажите адрес сервера для доступа к экземпляра ПО.
        server_name <host_name>
        # Укажите номер порта для доступа к экземпляра ПО.
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
