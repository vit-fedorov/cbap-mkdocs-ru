---
title:
kbId:
---

# Файлы конфигурации

## Настройка конфигурации файла конфигурации экземпляра ПО

1. Откройте для редактирования файл конфигурации экземпляра ПО (`<instanceName>` — имя экземпляра ПО):

    ``` sh
    nano /usr/share/comindware/configs/instance/<instanceName>.yml
    ```

2. Отредактируйте необходимые параметры и сохраните. Для редактирования доступны:

    - `databasePath` — директория для хранения базы данных экземпляра.
    - `backup.config.default.repository.localDisk.path` или `backup.defaultFolder` — директория для хранения данных резервного копирования.
    - `userStorage.localDisk.path` — директория для хранения загружаемых файлов.
    - `mq.server` — адрес подключения к службе Kafka.

3. Убедитесь, что папки, указанные в файле конфигурации, существуют. При необходимости создайте их и задайте права доступа:

    ``` sh
    mkdir -p <path/to/Database>
    mkdir -p <path/to/Streams>
    mkdir -p <path/to/Backup>
    chmod -R 766 <path/to/Database> <path/to/Streams> <path/to/Backup>
    chown -R <User>:<Group> <path/to/Database> <path/to/Streams> <path/to/Backup>
    ```

    Здесь: значения `<User>` и `<Group>` должны совпадать с такими же параметрами в `/usr/lib/systemd/system/comindware<instanceName>.service`

4. После внесения изменений перезапустите службу экземпляра ПО:

    ``` sh
    systemctl restart comindware<instanceName>
    ```

### Пример YML-файла конфигурации экземпляра ПО

``` yml
isFederationAuthEnabled: 0
databasePath: /var/lib/comindware/<instanceName>/Database
configPath: /var/www/<instanceName>
backup.config.default.repository.type: LocalDisk
backup.config.default.repository.localDisk.path: /var/backups/<instanceName>
userStorage.type: LocalDisk
userStorage.localDisk.path: /var/lib/comindware/<instanceName>/Streams
tempStorage.type: LocalDisk
tempStorage.localDisk.path: /var/lib/comindware/<instanceName>/Temp
mq.server: <kafkaBrokerIP>:<kafkaBrokerPort>
mq.group: <instanceName>
manageAdapterHost: true
elasticsearchUri: http://localhost:9200
instanceName: <instanceName>
version: 4.7.XXXX.0
```

## Настройка конфигурации apigateway.json

1. Откройте для редактирования файл конфигурации `apigateway.json` экземпляра ПО:

    ``` sh
    nano /var/www/<instanceName>/apigateway.json
    ```

2. Отредактируйте необходимые параметры и сохраните. Удостоверьтесь, что значение параметра `BootstrapServer` совпадает с `mq.server`, а `GroupId` — с `mq.group` в [файле конфигурации экземпляра ПО](#пример-yml-файла-конфигурации-экземпляра-по).
3. После внесения изменений перезапустите службу:

    ``` sh
    systemctl restart apigateway<instanceName>
    ```

### Пример конфигурации apigateway.json

```json
{
"Instance": {
    "Name": "<instanceName>"
},
"Log": {
    "Enabled": true,
    "ConfigurationFile": "/var/www/<instanceName>/logs.config"
},
"Kata": {
    "Enabled": false
},
"Kafka": {
    "BootstrapServer": "<kafkaBrokerIP>:<kafkaBrokerPort>",
    "GroupId": "<instanceName>"
},
"Grpc": {
    "SocketPath": "/var/www/<instanceName>/App_Data/apigateway.socket",
    "Protocol": "Http2"
}
}
```

## Настройка конфигурации adapterhost

1. Откройте для редактирования файл конфигурации `adapterhost.config` экземпляра ПО:

    ``` sh
    nano /var/www/<instanceName>/adapterhost.config
    ```

2. Отредактируйте необходимые параметры и сохраните. Удостоверьтесь, что значение параметра `BootstrapServers` совпадает с `mq.server`, а `groupId` — с `mq.group` в [файле конфигурации экземпляра](#настройка-конфигурации-файла-конфигурации-экземпляра-по).
3. После внесения изменений перезапустите службу:

    ``` sh
    kill -9 $(ps -eo pid,args | grep $<instanceName> | grep Agent | awk {'print $1'}) && systemctl restart comindware<instanceName>
    ```

### Пример конфигурации adapterhost

```yml
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

## Настройка конфигурации Ignite

1. Откройте файл конфигурации Ignite для редактирования:

    ``` sh
    nano /var/www/<instanceName>/Ignite.config
    ```

2. В блоке `<bean class="org.apache.ignite.configuration.DataRegionConfiguration">` настройте максимальный объём выделяемой памяти:

    - 3 Гб:
    
        ``` xml
        <property name="maxSize" value="#{3L * 1024 * 1024 * 1024}" />
        ```
    
    - 8 Гб:

        ``` xml
        <property name="maxSize" value="#{8L * 1024 * 1024 * 1024}" />
        ```

3. В случае изменения максимального объёма выделяемой памяти отредактируйте параметр `checkpointPageBufferSize`. Чтобы рассчитать размер значения, разделите размер `maxSize` на четыре, но при это значение не должно быть менее 256 Мб и более 2 Гб. Для максимального объёма выделяемой памяти в 8 Гб, значение будет следующим:

    ``` xml
    <property name="checkpointPageBufferSize" value="#{2L * 1024 * 1024 * 1024}" />
    ```

4. После внесения изменений перезапустите службу экземпляра ПО:

    ``` sh
    systemctl restart comindware<instanceName>
    ```

## Настройка конфигурации памяти кучи Java

В зависимости от размера оперативной памяти на сервере следует отредактировать конфигурацию памяти Java.

1. Откройте конфигурацию кучи Java экземпляра ПО для редактирования:

    ```sh
    nano /etc/sysconfig/comindware<instanceName>-env
    ```

2. Отредактируйте объём памяти, который выделяется для кучи Java:

    ``` sh
    ...
    JVM_OPTS=-Xms512m -Xmx16g -XX:MaxDirectMemorySize=1g ...
    ...
    ```

    Здесь:

    - `-Xms` — начальный размер кучи;
    - `-Xmx` — максимальный размер кучи.

3. После внесения изменений перезапустите службу экземпляра ПО:

    ```sh
    systemctl daemon-reload
    systemctl restart comindware<instanceName>
    ```

## Настройка конфигурации NGINX

1. Откройте конфигурацию NGINX для редактирования:

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
    ...
            }
        error_log /var/log/nginx/<instanceName>-error.log;
        access_log /var/log/nginx/<instanceName>-access.log;
    }
    ```

4. Проверьте, что изменения работают корректно:

    ```sh
    nginx -t
    ```

5. При успешном вступлении изменений в силу перезагрузите NGINX:

    ```sh
    nginx -s reload
    ```

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Пути и содержимое директорий экземпляра ПО][paths]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
