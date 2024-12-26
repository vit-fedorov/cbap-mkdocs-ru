---
title: Kafka. Установка в базовой конфигурации
kbId:
---

# Kafka. Установка в базовой конфигурации {: #kafka_deploy_Linux}

## Введение

Для работы **{{ productName }}** требуется сервер Kafka. См. [системные требования][system_requirements].

Здесь представлены инструкции по установке Kafka с помощью дистрибутива **{{ productName }}** для ОС Linux в простейшей базовой конфигурации.

Инструкции по установке Kafka в иных конфигурациях:

- _[Официальный сайт Elasticsearch](https://kafka.apache.org/quickstart)_

Здесь представлены инструкции по развёртыванию сервера Kafka в ОС Linux, а также приведён пример типового файла конфигурации. Инструкции представлены для версии Kafka 3.2.0, для других версий содержимое файлов конфигурации и порядок установки могут быть иными.

## Установка Kafka

1. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

2. Скачайте и распакуйте дистрибутив с вспомогательным ПО **{{ productName }}**, полученный по ссылке от компании **{{ companyName }}** (`X.X`, `<versionNumber>` — номер версии ПО, `<osname>` — название операционной системы):

    ``` sh
    tar -xf X.X-release-ru-<versionNumber>.prerequisites.<osname>.tar.gz
    ```

    !!! tip "Совет"

        После распаковки архив можно удалить для экономии места:

        ``` sh
        rm -f X.X-release-ru-<versionNumber>.prerequisites.<osname>.tar.gz
        ```

3. Перейдите в директорию со скриптами для развёртывания вспомогательного ПО:

    ``` sh
    cd <prerequisitesDistPath>/CMW_<osname>/scripts
    ```

    Здесь:  `<prerequisitesDistPath>/CMW_<osname>/` — путь к распакованному дистрибутиву со вспомогательным ПО.

4. Установите Kafka из дистрибутива с помощью ключа `-k`:

    ``` sh
    sh prerequisites_install.sh -k
    ```

5. После установки удостоверьтесь, что сервер Kafka запущен и имеет статус `Active (running)`:

    ``` sh
    systemctl status kafka
    ```

6. Если сервер Kafka не работает, запустите его:

    ``` sh
    systemctl start kafka
    ```

## Подключение экземпляра ПО к Kafka

1. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

2. Отредактируйте настройки подключения к Kafka в файле `/usr/share/comindware/configs/instance/<instanceName>.yml`, где `<instanceName>` — имя экземпляра ПО:

    ``` yml
    # Адрес и порт сервера очереди сообщений (Kafka)
    mq.server: <kafkaBrokerIP>:<kafkaBrokerPort>
    # Идентификатор группы очереди сообщений
    mq.group: <instanceName>
    # Идентификатор узла очереди сообщений
    #mq.node: <instanceName>
    ```

    !!! warning "Внимание!"

        - Для корректной работы экземпляра ПО адрес и порт Kafka должны быть обязательно прописаны цифрами.
        - Для корректной работы экземпляра ПО значение параметров `mq.server` (адрес и порт сервера очереди сообщений), `mq.group` (идентификатор группы очереди сообщений), `mq.node` (идентификатор узла очереди сообщений) должно совпадать во всех файлах конфигурации:
            - `/usr/share/comindware/configs/instance/<instanceName>.yml`
            - `/var/www/<instanceName>/apigateway.yml`
            - `/var/www/<instanceName>/adapterhost.yml`

3. Отредактируйте настройки подключения к Kafka в файле `/var/www/<instanceName>apigateway.yml`:

    ``` yml
    # Адрес сервера очереди сообщений (Kafka) с портом.
    mq.server: <kafkaBrokerIp>:<kafkaBrokerPort>
    # Идентификатор группы очереди сообщений
    mq.group: <instanceName>
    # Идентификатор узла очереди сообщений
    mq.node: <instanceName>
    ```

4. Отредактируйте файл `/var/www/<instanceName>/adapterhost.yml` по следующему образцу:

    ``` yml
    # Адрес и порт сервера очереди сообщений (Kafka)
    mq.server: <kafkaBrokerIp>:<kafkaBrokerPort>
    ```

## Пример типового файла конфигурации Kafka

``` yml
############################# Server Basics #############################
# The role of this server. Setting this puts us in KRaft mode
process.roles=broker,controller
# The node id associated with this instance's roles
node.id=1
# The connect string for the controller quorum
controller.quorum.voters=1@10.9.9.113:9093
############################# Socket Server Settings #############################
# The address the socket server listens on.
# Combined nodes (i.e. those with `process.roles=broker,controller`) must list the controller listener here at a minimum.
# If the broker listener is not defined, the default listener will use a host name that is equal to the value of java.net.InetAddress.getCanonicalHostName(),
# with PLAINTEXT listener name, and port 9092.
#   FORMAT:
#     listeners = listener_name://host_name:port
#   EXAMPLE:
#     listeners = PLAINTEXT://your.host.name:9092
listeners=PLAINTEXT://10.9.9.113:9092,CONTROLLER://10.9.9.113:9093
# Name of listener used for communication between brokers.
inter.broker.listener.name=PLAINTEXT
# Listener name, hostname and port the broker will advertise to clients.
# If not set, it uses the value for "listeners".
#advertised.listeners=PLAINTEXT://10.9.9.113:9092
# A comma-separated list of the names of the listeners used by the controller.
# If no explicit mapping set in `listener.security.protocol.map`, default will be using PLAINTEXT protocol
# This is required if running in KRaft mode.
controller.listener.names=CONTROLLER
# Maps listener names to security protocols, the default is for them to be the same. See the config documentation for more details
listener.security.protocol.map=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT,SSL:SSL,SASL_PLAINTEXT:SASL_PLAINTEXT,SASL_SSL:SASL_SSL
# The number of threads that the server uses for receiving requests from the network and sending responses to the network
num.network.threads=3
# The number of threads that the server uses for processing requests, which may include disk I/O
num.io.threads=8
# The send buffer (SO_SNDBUF) used by the socket server
socket.send.buffer.bytes=102400
# The receive buffer (SO_RCVBUF) used by the socket server
socket.receive.buffer.bytes=102400
# The maximum size of a request that the socket server will accept (protection against OOM)
socket.request.max.bytes=104857600
############################# Log Basics #############################
# A comma separated list of directories under which to store log files
log.dirs=/var/log/comindware/.kafka
# The default number of log partitions per topic. More partitions allow greater
# parallelism for consumption, but this will also result in more files across
# the brokers.
num.partitions=4
# The number of threads per data directory to be used for log recovery at startup and flushing at shutdown.
# This value is recommended to be increased for installations with data dirs located in RAID array.
num.recovery.threads.per.data.dir=1
############################# Internal Topic Settings  #############################
# The replication factor for the group metadata internal topics "__consumer_offsets" and "__transaction_state"
# For anything other than development testing, a value greater than 1 is recommended to ensure availability such as 3.
offsets.topic.replication.factor=1
transaction.state.log.replication.factor=1
transaction.state.log.min.isr=1
############################# Log Retention Policy #############################
# The following configurations control the disposal of log segments. The policy can
# be set to delete segments after a period of time, or after a given size has accumulated.
# A segment will be deleted whenever *either* of these criteria are met. Deletion always happens
# from the end of the log.
# The minimum age of a log file to be eligible for deletion due to age
log.retention.hours=168
# A size-based retention policy for logs. Segments are pruned from the log unless the remaining
# segments drop below log.retention.bytes. Functions independently of log.retention.hours.
#log.retention.bytes=1073741824
# The maximum size of a log segment file. When this size is reached a new log segment will be created.
log.segment.bytes=1073741824
# The interval at which log segments are checked to see if they can be deleted according
# to the retention policies
log.retention.check.interval.ms=300000
# Max message size
max.request.size=104857600
max.message.bytes=104857600
message.max.bytes=104857600
fetch.message.max.bytes=104857600
replica.fetch.max.bytes=104857600
```
