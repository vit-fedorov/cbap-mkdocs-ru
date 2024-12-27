---
title: Kafka. Установка в базовой конфигурации
kbId: 5074
---

# Kafka. Установка в базовой конфигурации {: #kafka_deploy_linux}

## Введение

Для работы **{{ productName }}** требуется сервер Kafka. См. [системные требования][system_requirements].

Здесь представлены инструкции по установке Kafka с помощью дистрибутива **{{ productName }}** для ОС Linux в простейшей базовой конфигурации.

Инструкция по установке Kafka в иных конфигурациях на _[официальном сайте Kafka](https://kafka.apache.org/quickstart)_.

Здесь представлены требования к техническому обеспечению и инструкции по развёртыванию сервера Kafka в ОС Linux, а также приведён пример типового файла конфигурации. Инструкции представлены для версии Kafka 3.2.0, для других версий содержимое файлов конфигурации и порядок установки могут быть иными.

## Требования к серверу

Kafka создает значительную нагрузку на вычислительные ресурсы компьютера, поэтому рекомендуется:

- использовать отдельный SSD-диск для хранения журналов и данных сервера Kafka;
- использовать высокопроизводительный компьютер с достаточным объемом ОЗУ и количеством ядер ЦП.

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

1. Откройте файл конфигурации Kafka:

    ``` sh
    nano /usr/share/kafka/config/kraft/server.properties
    ```

2. Отредактируйте файл по следующему образцу:

    ``` yml
    # Укажите роли, в которых должен выступать сервер Kafka
    process.roles=broker,controller
    node.id=1
    # Укажите IP-адрес сервера Kafka
    controller.quorum.voters=1@<KafkaIP>:9093
    # Укажите IP-адрес сервера Kafka
    listeners=PLAINTEXT://<KafkaIP>:9092,CONTROLLER://<KafkaIP>:9093
    inter.broker.listener.name=PLAINTEXT
    controller.listener.names=CONTROLLER
    listener.security.protocol.map=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT,SSL:SSL,SASL_PLAINTEXT:SASL_PLAINTEXT,SASL_SSL:SASL_SSL
    num.network.threads=3
    num.io.threads=8
    socket.send.buffer.bytes=102400
    socket.receive.buffer.bytes=102400
    socket.request.max.bytes=104857600
    # Укажите путь к файлам журналирования
    log.dirs=/var/log/comindware/.kafka
    num.partitions=4
    num.recovery.threads.per.data.dir=1
    offsets.topic.replication.factor=1
    transaction.state.log.replication.factor=1
    transaction.state.log.min.isr=1
    log.retention.hours=168
    log.segment.bytes=1073741824
    log.retention.check.interval.ms=300000
    max.request.size=104857600
    max.message.bytes=104857600
    message.max.bytes=104857600
    fetch.message.max.bytes=104857600
    replica.fetch.max.bytes=104857600
    ```

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Настройка конфигурации вспомогательного ПО для оптимизации работы {{ productName }}][auxiliary_software_optimize]_
- _[Конфигурация экземпляра, компонентов ПО и служб. Настройка][configuration_files_linux]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
