!!! warning "Внимание!"

    Директивы `isFederationAuthEnabled` и `manageAdapterHost` требуется удалить, если они присутствуют.

    Директивы `mq.server` (адрес и порт сервера очереди сообщений), `mq.group` (идентификатор группы очереди сообщений), `mq.node` (идентификатор узла очереди сообщений) и `cluster.name` / `clusterName` (имя экземпляра ПО) должны совпадать в трёх файлах конфигурации:

    - `/usr/share/comindware/configs/instance/<instanceName>.yml`
    - `/var/www/<instanceName>/adapterhost.yml`
    - `/var/www/<instanceName>/apigateway.yml`