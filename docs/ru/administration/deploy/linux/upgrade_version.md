---
title: Обновление версии экземпляра ПО
kbId: 2499
---

# Обновление версии экземпляра ПО

## Введение

Здесь представлены краткие инструкции по обновлению до 4.7.2XXX версии экземпляра ПО **{{ productName }}** под управлением ОС Linux.

## Порядок обновления версии ПО

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

## Обновление версии ПО

1. Создайте и перенесите во внешнее хранилище резервную копию базы данных экземпляра ПО. См. статью _«[Резервное копирование. Настройка и запуск, просмотр журнала сеансов][backup]»_.
2. Перейдите в режим суперпользователя:

    ``` sh
    sudo -i
    ```

    или

    ``` sh
    su -
    ```

3. Остановите экземпляр ПО и его вспомогательные службы и удостоверьтесь, что они остановлены:


    ``` sh
    systemctl stop apigateway<instanceName> comindware<instanceName>  
    systemctl status apigateway<instanceName> comindware<instanceName> 
    ```

    Здесь `<instanceName>` — имя экземпляра ПО.

4. Проверьте, выполняется ли сервис `Comindware.Adapter.Agent.exe`:

    ``` sh
    ps fax | grep Agent
    ```

    - Если процесс `Comindware.Adapter.Agent.exe`, выполняется, завершите его по `PID`:

        ``` sh
        kill -9 <PID>
        ```

5. Если используется нестандартная конфигурация NGINX для экземпляра ПО, сохраните её резервную копию:
{: #NginxBackup}

    ``` sh
    cp /etc/nginx/sites-available/comindware<instanceName> $HOME            
    ```

    или   

    ``` sh
    cp /etc/nginx/conf.d/comindware<instanceName> $HOME        
    ```

6. Проверьте имя и статус экземпляра:

    ``` sh
    systemctl status comindware*
    ```

7. Удалите (или переместите в резервное хранилище) неиспользуемые предыдущие дистрибутивы ПО (`<osname>` — название операционной системы):

    ``` sh
    rm -rf CMW_<osname>
    ```

## Обновление версии экземпляра ПО {: .pageBreakBerore }

1. Скачайте и распакуйте дистрибутив с новой версией ПО (`X.X.XXX.X` — номер версии ПО, `<osname>` — название операционной системы):

    ``` sh
    tar -xf X.X.XXX.X.<osname>.tar.gz
    ```

2. Перейдите в распакованную папку:

    ``` sh
    cd CMW_<osname>/scripts/cbap
    ```

3.  Запустите установку распакованного дистрибутива ПО:

    ``` sh
    bash install.sh
    ```

4.  Проверьте наличие и имя директории установленной версии ПО:

    ``` sh
    ls /var/www/.cmw_version/
    ```

5. Перейдите в директорию скриптов для работы с экземпляром ПО и запустите его обновление до требуемой версии:

    ``` sh
    cd ../instance/
    bash upgrade.sh -n=<instanceName> -vp=/var/www/.cmw_version/X.X.XXX.X
    ```

    Здесь:

    - `X.X.XXX.X` — номер устанавливаемой версии ПО;
    - `<instanceName>` — имя обновляемого экземпляра ПО.

6.  Проверьте корректность конфигурации NGINX для экземпляра ПО:

    ``` sh
    cat /etc/nginx/sites-available/comindware<instanceName>
    ```

    - При необходимости восстановите конфигурацию NGINX, [сохранённую ранее](#NginxBackup).

7. Откройте для редактирования файл конфигурации `/var/www/<instanceName>/apigateway.json`.

    - Замените в конфигурации адрес сервера Kafka:

        ``` sh
        "Kafka": {  
            "BootstrapServer": "<KAFKAIP>:9092",  
            "GroupId": "<instanceName>"  
        }    
        ```

8. Если выполняется обновление с версии ниже 4.6.1140.0, откройте для редактирования файл конфигурации экземпляра ПО `/usr/share/comindware/configs/instance/<instanceName>.yml`.
    - Замените в конфигурации следующие директивы:
    
        ``` sh
        # исходная директива  
        # backupPath: /var/backups/<instanceName>  
        # заменить на:  
        backup.config.default.repository.type: LocalDisk  
        backup.config.default.repository.localDisk.path: /var/backups/<instanceName> ## backupPath  
        
        # исходная директива  
        # tempPath: /var/lib/comindware/<instanceName>/Temp  
        # заменить на:  
        tempStorage.type: LocalDisk  
        tempStorage.localDisk.path: /var/lib/comindware/<instanceName>/Temp ## tempPath  
        
        # исходная директива  
        # streamsPath: /var/streams/<instanceName>  
        # заменить на:  
        userStorage.type: LocalDisk   
        userStorage.localDisk.path: /var/streams/<instanceName>
        ```

    - Добавьте в конфигурацию следующие директивы:
    
        ``` sh
        # Имя конфигурации   
        configName: <instanceName>    
        
        # Имя базы данных Apache Ignite   
        instanceName: <instanceName>    
        
        manageAdapterHost: true  
        useDataBusNumbers:  
            - 0  
            - 1  
            - 2  
            - 3
        ```

9. Удостоверьтесь, что итоговый файл конфигурации `/usr/share/comindware/configs/instance/<instanceName>.yml` выглядит аналогично следующему примеру:

    ``` sh
    databasePath: /var/lib/comindware/<instanceName>/Database/
    configPath: /var/www/<instanceName>
    backup.config.default.repository.type: LocalDisk
    backup.config.default.repository.localDisk.path: /var/lib/comindware/<instanceName>/Backup
    userStorage.type: LocalDisk
    userStorage.localDisk.path: /var/lib/comindware/<instanceName>/Streams
    tempStorage.type: LocalDisk
    tempStorage.localDisk.path: /var/lib/comindware/<instanceName>/Temp
    elasticsearchUri: XXX.XXX.XXX.XXX:9200 #адрес сервера ElasticSearch
    instanceName: <instanceName>
    configName: <instanceName>
    databaseName: <instanceName>
    nodeName: prod_0
    linuxAuthenticationType: 1
    ldapAuthenticationType: 1
    isFederationAuthEnabled: 0
    manageAdapterHost: true
    isTestEnvironment: false
    mq.enabled: true
    mq.server: XXX.XXX.XXX.XXX:9092 #адрес сервера Kafka
    mq.group: <instanceName> #имя группы в Kafka
    mq.node: prod_0
    mq.name: <instanceName> #имя очереди в Kafka
    mq.adapter.0.enabled: true
    mq.adapter.1.enabled: true
    mq.adapter.2.enabled: true
    mq.adapter.3.enabled: true
    version: 4.7.2XXX.X
    ```

10. Перезапустите сервисы, настройки которых были изменены:

    ``` sh
    systemctl restart apigateway<instanceName> comindware<instanceName>
    ```

    - Проверьте конфигурацию NGINX:

        ``` sh
        nginx -t
        ```

    - Если тест пройден, перезапустите NGINX:
    
        ``` sh
        nginx -s reload
        ```

11. Откройте сайт экземпляра ПО в браузере, дождитесь окончания загрузки, одновременно открыв выдачу журналов экземпляра в терминале:   

    ``` sh
    tail -f /var/log/comindware/<instanceName>/Log/sys*
    ```

--8<-- "related_topics_heading.md"

**[Резервное копирование. Настройка и запуск, просмотр журнала сеансов][backup]**
