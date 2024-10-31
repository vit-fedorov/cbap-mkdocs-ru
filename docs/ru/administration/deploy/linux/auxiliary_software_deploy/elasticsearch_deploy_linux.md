---
title: Установка Elasticsearch. Краткое руководство для Linux
kbId: 
---

# Установка Elasticsearch. Краткое руководство для Linux {: #elasticsearch_deploy_Linux}

## Введение

Для работы **{{ productName }}** требуется сервер Elasticsearch. См. [системные требования][system_requirements].

При установке **{{ productName }}** версии для ОС Linux одновременно с экземпляром ПО можно развернуть сервер Elasticsearch. Для этого укажите ключ `-e` при запуске скрипта.

Служба Elasticsearch имеет базовую конфигурацию и доступна по адресу `localhost:9200`. Вы можете использовать имеющуюся службу Elasticsearch или развернуть её на отдельном сервере.

Здесь представлены требования к конфигурации компьютера для сервера Elasticsearch, инструкции по установке и настройке конфигурации сервера и службы Elasticsearch в ОС Linux, а также приведен пример типового файла конфигурации. Инструкции представлены для версии 8.10.2, для других версий содержимое файлов конфигурации и порядок установки могут быть иными.

## Требования к компьютеру

Сервер Elasticsearch создает значительную нагрузку на вычислительные ресурсы компьютера, поэтому рекомендуется:

- использовать отдельный SSD-диск для хранения журналов и данных сервера Elasticsearch;
- осуществлять мониторинг свободного места на диске, так как сервер перестает записывать данные, если на диске мало свободного места;
- использовать высокопроизводительный компьютер с достаточным объемом ОЗУ и количеством ядер ЦП, так как для обработки каждого индекса создается отдельный поток, а индексов может быть много.

## Установка Elasticsearch

Здесь представлена инструкция по установке Elasticsearch с помощью дистрибутива **{{ productName }}**. Для установки Elasticsearch без помощи дистрибутива воспользуйтесь [инструкцией с официального сайта](https://www.elastic.co/guide/en/elasticsearch/reference/current/targz.html).

1. Перейдите в режим суперпользователя:

    ``` sh
    sudo -i
    ```

    или

    ``` sh
    su -
    ```

2. Скачайте и распакуйте дистрибутив **{{ productName }}** по ссылке, предоставленной компанией **{{ companyName }}** (`X.X.XXXX.X` — номер версии ПО, `<osname>` — название операционной системы):

    ``` sh
    tar -xf X.X-release-ru-X.X.XXXX.X.<osname>.tar.gz
    ```

3. Перейдите в распакованную папку:

    ``` sh
    cd CMW_<osname>/
    ```

4. Установите Elasticsearch из дистрибутива:

    ``` sh
    sh install.sh -e 
    ```

5. После установки удостоверьтесь, что Elasticsearch запущен и имеет статус Active (running):

    ``` sh
    systemctl status elasticsearch
    ```

6. Если сервис Elasticsearch не работает, запустите его:

    ``` sh
    systemctl start elasticsearch
    ```

Для развёртывания кластера Elasticsearch см. _«[Установка Elasticsearch и настройка кластера Elasticsearch без сертификатов подлинности][elasticsearch_cluster_deploy_no_certificates]»_.

## Пример типового файла конфигурации Elasticsearch

Ниже приведен пример файла `elasticsearch.yml` для следующей конфигурации сервера:

- сервер Elasticsearch состоит из единственного узла;
- служба работает в локальной сети;
- включена аутентификация;
- служба доступна через порт `9200`;
- адрес сервера `http://localhost:9200`;
- путь к файлу конфигурации: `/etc/elasticsearch/elasticsearch.yml`

``` sh
#======================== Elasticsearch Configuration =========================
cluster.name: my-application
# ------------------------------------ Node ------------------------------------
node.name: node-1
# ----------------------------------- Paths ------------------------------------
path.data: /var/lib/elasticsearch # database path Elasticsearch
path.logs: /var/log/elasticsearch # путь к файлам журнала Elasticsearch
#path.repo: /var/backups/elasticsearch # путь к репозиторию резервных копий Elasticsearch
# ----------------------------------- Memory -----------------------------------
bootstrap.memory_lock: false
# ---------------------------------- Network -----------------------------------
# укажите IP сервера Elasticsearch или 127.0.0.1, если Elasticsearch и 
# Comindware Business Application Platform развёрнуты на одной машине
network.host: 127.0.0.1  
http.port: 9200 # порт по умолчанию
# --------------------------------- Discovery ----------------------------------
discovery.type: single-node # директива для работы в режиме одного узла
#discovery.seed_hosts: ["192.168.12.1"] # директива для работы кластера
#cluster.initial_master_nodes: ["192.168.12.1"] # директива для работы кластера
# ---------------------------------- Various -----------------------------------
search.allow_expensive_queries: true
action.destructive_requires_name: true
indices.id_field_data.enabled: true
# ---------------------------------- Security ----------------------------------
xpack.security.enabled: false
xpack.security.enrollment.enabled: false
xpack.security.http.ssl:
  enabled: false
  #  keystore.path: certs/http.p12
xpack.security.transport.ssl:
  enabled: false
  #  verification_mode: certificate
  #  keystore.path: certs/transport.p12
  #  truststore.path: certs/transport.p12
http.host: 0.0.0.0 # IP - слушать внешний интерфейс, 127.0.0.1 - localhost, 0.0.0.0 - все
```

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
