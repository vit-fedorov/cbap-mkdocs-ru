---
kbId:
title: Развёртывание Comindware Business Application Platform в кластере
---

# Развёртывание {{ productName }} в кластере

## Введение

Экземпляр ПО **{{ productName }}** можно развернуть в кластере для увеличения производительности, улучшения отказоустойчивости и обеспечения бесперебойного функционирования.

Здесь представлены инструкции по настройке узлов кластера и сервера для хранения данных.

## Конфигурация кластера

Кластер экземпляра ПО включает следующие компоненты:

- сервер хранения данных экземпляра ПО на отдельной машине, к которому будут обращаться узлы кластера;
- несколько машин, на каждой из которых установлено ПО **{{ productName }}** одинаковой версии и развёрнут экземпляр ПО с одинаковым именем (`<instanceName>`);
- сервер Elasticsearch развёрнут на отдельной машине;
- сервер Apache Kafka развёрнут на отдельной машине.

## Настройка сервера хранения данных (NFS)

Выполните следующие инструкции на сервере хранения данных.

1. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

2. Создайте директорию:

    ``` sh
    mkdir /share
    ```

3. Установите NFS-сервер:

    ``` sh
    apt install nfs-kernel-server
    systemctl enable nfs-kernel-server.service
    ```

4. Откройте файл `exports` для редактирования:

    ``` sh
    nano /etc/exports
    ```

5. Добавьте в файл `exports` следующую директиву:

    ``` sh
    /share <clientIP>/<netMask>(rw,sync,no_subtree_check)
    ```

    Здесь:

    - `/share` — директория, к которой предоставляется общий доступ;
    - `<nodeIP>` — неизменная часть IP-адресов узлов кластера;
    - `<netMask>` — маска подсети.

    Например:

    - `192.168.1.100/32` (маска подсети `255.255.255.255`): один компьютер с IP-адресом `192.168.1.100`.
    - `192.168.1.0/24` (маска подсети `255.255.255.0`): все компьютеры с IP-адресами от `192.168.1.1` до `192.168.1.254`.

6. Чтобы применить изменения, выполните следующую команду:

    ``` sh
    exportfs -a
    ```

7. Запустите NFS-сервер:

    ``` sh
    systemctl start nfs-kernel-server.service
    ```

8. Создайте следующие директории (`<instanceName>` — имя экземпляра ПО):

    `` sh
    mkdir -p /share/<instanceName>/Streams
    mkdir -p /share/<instanceName>/Scripts
    mkdir -p /share/<instanceName>/Temp
    mkdir -p /share/<instanceName>/Localtemp
    ```

9. Настройте права доступа к созданным директориям:

    ``` sh
    chmod -R 777 /share/<instanceName>
    chown -R nobody:nogroup /share
    ```

## Развёртывание узлов кластера

Выполните следующие инструкции на каждом узле кластера **{{ productName }}**.

### Установка ПО **{{ productName }}** и бинарных пакетов Apache Ignite

1. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

2. При необходимости установите ПО и разверните экземпляр **{{ productName }}**. См. _«[Установка, запуск, инициализация и остановка ПО][deploy_guide_linux]»_.
3. Скачайте дистрибутив [Apache Ignite](https://downloads.apache.org/ignite/2.16.0/apache-ignite-2.16.0-bin.zip).
4. Распакуйте дистрибутив (например, в директорию `/usr/share/ignite`):

    ``` sh
    unzip apache-ignite-2.16.0-bin.zip -d /usr/share/
    mv /usr/share/apache-ignite* /usr/share/ignite
    ```

5. Задайте переменную среды `IGNITE_HOME`:

    ``` sh
    export IGNITE_HOME=/usr/share/ignite
    ```

6. Скопируйте файл `Ignite.config` из директории экземпляра ПО в директорию `/usr/share/ignite`:

    ``` sh
    cp /var/www/<instanceName>/Ignite.config /usr/share/ignite/
    ```

7. Перейдите в следующую директорию:

    ``` sh
    cd /usr/share/ignite/bin
    ```

8. Откройте файл `control.sh` для редактирования:

    ``` sh
    nano control.sh
    ```

9. Измените директиву `DEFAULT_CONFIG`:

    ``` ini
    DEFAULT_CONFIG=config/Ignite.config
    ```

10. Проверьте получение списка узлов, зарегистрированных в базовой топологии:

    ``` sh
    bash control.sh --baseline
    ```

    !!! note "Примечание"

        Если работа экземпляра ПО приостановлена, запрос должен вернуть пустую топологию.

### Установка NFS-клиента

1. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

2. Установите службу NFS-клиента:

    ``` sh
    apt install nfs-common
    ```

3. Откройте файл `fstab` для редактирования:

    ``` sh
    nano /etc/fstab
    ```

4. Добавьте в файл `fstab` следующую директиву (`<serverIP>` — адрес [NFS-сервера](#настройка-сервера-хранения-данных-nfss)):

    ``` ini
    `<serverIP>:/share  /mnt/share  nfs  auto  0  0`
    ```

5. Смонтируйте диски:

    ``` sh
    mount -a
    ls -lh /mnt/share
    ```

6. Создайте и настройте следующие директории и ссылки (`<instanceName>` — имя экземпляра ПО):

    ``` sh
    mkdir /db
    mkdir -p /db/<instanceName>/Database/
    mkdir /var/lib/comindware
    ln -s /db/<instanceName> /var/lib/comindware/<instanceName>
    ln -s /mnt/share/<instanceName>/Scripts /db/<instanceName>/Database/Scripts

    chown -R www-data: /var/lib/comindware /db/<instanceName>
    ```

7. Откройте файл `comindware<instanceName>-env` для редактирования:

    ``` sh
    nano /etc/sysconfig/comindware<instanceName>-env
    ```

8. Проверьте значения в следующей директиве и при необходимости отредактируйте её:

    `` ini
    JVM_OPTS=-Xms512m -Xmx4g -XX:MaxDirectMemorySize=1g...
    ```

## Настройка первого узла для работы экземпляра ПО в кластере

### Подготовка первого узла к работе

1. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

2. Создайте [резервную копию][complete_running_instance_backup] экземпляра ПО.
3. Скопируйте резервную копию в директорию `/home/<username>` (`<username>` — имя пользователя, `<backupName>` — имя архива резервной копии, `<pathToBackup>` — путь к архиву резервной копии):

    ``` sh
    cp /<pathToBackup>/<backupName>.cdbbz /home/<username>
    ```

4. Перейдите в директорию `/home/<username>`:

    ``` sh
    cd /home/<username>
    ```

5. Распакуйте архив резервной копии:

    ``` sh
    unzip -q <backupName>.cdbbz
    ```

6. Перенесите и настройте данные резервной копии экземпляра ПО (`<instanceName>` — имя экземпляра ПО):

    ``` sh
    cp -r Scripts/* /mnt/share/<instanceName>/Scripts/
    cp -r Streams/* /mnt/share/<instanceName>/Streams/
    mv Database/* /db/<instanceName>/Database/
    rm -rf Database Scripts Streams
    ```

7. Настройте владельца директории `/db/<instanceName>`:

    ``` sh
    chown -R www-data: /db/<instanceName>
    ```

8. Откройте файл `Ignite.config` для редактирования:

    ``` sh
    nano /var/www/<instanceName>/Ignite.config
    ```

9.  Отредактируйте файл `Ignite.config` следующим образом:

    ``` xml
    <property name="discoverySpi">
          <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
            <!-- укажите IP-адрес машины -->
            <property name="localAddress" value="<clientIP>" />
            <property name="localPort" value="47510" />
            <property name="localPortRange" value="9" />
            <property name="ipFinder">
              <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
                <property name="addresses">
                  <list>
                    <!-- перечислите все IP-адреса машин, которые составляют кластер -->
                    <value><clientIP>:47510..47519</value>
                    <value><clientIP_1>:47510..47519</value>
                    ...
                    <value><clientIP_n>:47510..47519</value>
                  </list>
                </property>
              </bean>
            </property>
          </bean>
        </property>
        <property name="communicationSpi">
          <bean class="org.apache.ignite.spi.communication.tcp.TcpCommunicationSpi">
            <property name="localPort" value="47101" />
            <!-- укажите IP-адрес машины -->
            <property name="localAddress" value="<clientIP>" />
            <property name="messageQueueLimit" value="1024" />
          </bean>
        </property>
    ...
    ...
    <property name="dataRegionConfigurations">
              <list>
                <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
                  <property name="warmUpConfiguration">
                    <bean class="org.apache.ignite.configuration.NoOpWarmUpConfiguration" />
                  </property>
                  <property name="name" value="Persistent" />
                  <property name="persistenceEnabled" value="true" />
                    <!-- проверьте и при необходимости отредактируйте размер выделяемой памяти -->
                  <property name="initialSize" value="#{1024L * 1024 * 1024}" />
                  <property name="maxSize" value="#{4L * 1024 * 1024 * 1024}" />
                  <property name="pageEvictionMode" value="RANDOM_2_LRU" />
                  <property name="checkpointPageBufferSize" value="#{1024L * 1024 * 1024}" />
                </bean>
                <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
                  <property name="name" value="InMemory" />
                  <property name="persistenceEnabled" value="false" />
                    <!-- проверьте и при необходимости отредактируйте размер выделяемой памяти -->
                  <property name="initialSize" value="#{10 * 1024 * 1024}" />
                  <property name="maxSize" value="#{256 * 1024 * 1024}" />
                </bean>
              </list>
            </property>
          </bean>
        </property>
    ```

10. Откройте файл конфигурации экземпляра ПО для редактирования:

    ``` sh
    nano /usr/share/comindware/configs/instance/<instanceName>.yml
    ```

11. Отредактируйте файл конфигурации экземпляра ПО следующим образом:

    ``` yml
    isFederationAuthEnabled: 0
    databasePath: /var/lib/comindware/<instanceName>/Database
    configPath: /var/www/<instanceName>
    backup.config.default.repository.type: LocalDisk
    backup.config.default.repository.localDisk.path: /var/lib/comindware/<instanceName>/Backup
    userStorage.type: LocalDisk
    userStorage.localDisk.path: /mnt/share/<instanceName>/Streams
    tempStorage.type: LocalDisk
    tempStorage.localDisk.path: /mnt/share/<instanceName>/Temp
    
    instanceName: <instanceName>
    databaseName: <instanceName>
    configName: <instanceName>
    # У каждого узла должно быть своё название
    nodeName: <instanceName><nodeNumber>
    
    # Адрес и порт сервера очереди сообщений (Kafka)
    mq.server: <kafkaBrokerIP>:<kafkaBrokerPort>
    mq.group: <instanceName>
    manageAdapterHost: true
    # Адрес и порт сервера Elasticsearch
    elasticsearchUri: <elasticsearchIP>:<elasticsearchPort>
    # Версия ПО
    version: <versionNumber>
    ```

12. При наличии файла `Workers.config` удалите его:

    ```sh
    rm -f /var/www/npportalid/Workers.config
    ```

### Запуск первого узла кластера

1. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

2. Запустите службу экземпляра ПО:

    ``` sh
    systemctl start comindware<instanceName>
    ```

3. В веб-браузере запустите сайт экземпляра ПО и выполните вход.
4. Откройте файл `Workers.config` для редактирования (`<instanceName>` — имя экземпляра ПО):

    ``` sh
    nano /var/www/<instanceName>/Workers.config
    ```

5. Отредактируйте файл `Workers.config` следующим образом:

    ``` xml
    <?xml version="1.0" encoding="utf-8"?>
    <WorkerEngine xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-i>
      <RebuildThreadWorker>false</RebuildThreadWorker>
      <BackupSessionsQueue>true</BackupSessionsQueue>
      <SessionManagerWorker>false</SessionManagerWorker>
      <NotificationWorker>false</NotificationWorker>
      <EmailListener>false</EmailListener>
      <IndexTasksQueue>false</IndexTasksQueue>
      <ProcessEngineQueueProcessing>false</ProcessEngineQueueProcessing>
      <ProcessEngineTimerProcessing>false</ProcessEngineTimerProcessing>
      <SyncThread>false</SyncThread>
      <SwitchOnFullTextSearch>false</SwitchOnFullTextSearch>
      <PerformanceMonitoring>false</PerformanceMonitoring>
      <ConfigurationId>XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX</ConfigurationId>
    </WorkerEngine>
    ```

6. Скопируйте и сохраните значение из следующей строки:
{: #ConfigurationId}

    ``` xml
    <ConfigurationId>XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX</ConfigurationId>
    ```

7. Настройте владельца файла `Workers.config`:

    ``` sh
    chown www-data: /var/www/<instanceName>/Workers.config
    ```

## Настройка и запуск последующих экземпляров ПО

1. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

2. Откройте файл `Ignite.config` для редактирования:

    ``` sh
    nano /var/www/<instanceName>/Ignite.config
    ```

3. Отредактируйте файл `Ignite.config` следующим образом:

    ``` xml
    <property name="discoverySpi">
          <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
            <!-- укажите IP-адрес машины -->
            <property name="localAddress" value="<clientIP>" />
            <property name="localPort" value="47510" />
            <property name="localPortRange" value="9" />
            <property name="ipFinder">
              <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
                <property name="addresses">
                  <list>
                    <!-- перечислите все IP-адреса машин, которые составляют кластер -->
                    <value><clientIP>:47510..47519</value>
                    <value><clientIP_1>:47510..47519</value>
                    ...
                    <value><clientIP_n>:47510..47519</value>
                  </list>
                </property>
              </bean>
            </property>
          </bean>
        </property>
        <property name="communicationSpi">
          <bean class="org.apache.ignite.spi.communication.tcp.TcpCommunicationSpi">
            <property name="localPort" value="47101" />
            <!-- укажите IP-адрес машины -->
            <property name="localAddress" value="<clientIP>" />
            <property name="messageQueueLimit" value="1024" />
          </bean>
        </property>
    ...
    ...
    <property name="dataRegionConfigurations">
              <list>
                <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
                  <property name="warmUpConfiguration">
                    <bean class="org.apache.ignite.configuration.NoOpWarmUpConfiguration" />
                  </property>
                  <property name="name" value="Persistent" />
                  <property name="persistenceEnabled" value="true" />
                    <!-- проверьте и при необходимости отредактируйте размер выделяемой памяти -->
                  <property name="initialSize" value="#{1024L * 1024 * 1024}" />
                  <property name="maxSize" value="#{4L * 1024 * 1024 * 1024}" />
                  <property name="pageEvictionMode" value="RANDOM_2_LRU" />
                  <property name="checkpointPageBufferSize" value="#{1024L * 1024 * 1024}" />
                </bean>
                <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
                  <property name="name" value="InMemory" />
                  <property name="persistenceEnabled" value="false" />
                    <!-- проверьте и при необходимости отредактируйте размер выделяемой памяти -->
                  <property name="initialSize" value="#{10 * 1024 * 1024}" />
                  <property name="maxSize" value="#{256 * 1024 * 1024}" />
                </bean>
              </list>
            </property>
          </bean>
        </property>
    ```

4. Откройте файл конфигурации экземпляра ПО для редактирования:

    ``` sh
    nano /usr/share/comindware/configs/instance/<instanceName>.yml
    ```

5. Отредактируйте файл конфигурации экземпляра ПО следующим образом:

    ``` yml
    isFederationAuthEnabled: 0
    databasePath: /var/lib/comindware/<instanceName>/Database
    configPath: /var/www/<instanceName>
    backup.config.default.repository.type: LocalDisk
    backup.config.default.repository.localDisk.path: /var/lib/comindware/<instanceName>/Backup
    userStorage.type: LocalDisk
    userStorage.localDisk.path: /mnt/share/<instanceName>/Streams
    tempStorage.type: LocalDisk
    tempStorage.localDisk.path: /mnt/share/<instanceName>/Temp
    
    instanceName: <instanceName>
    databaseName: <instanceName>
    configName: <instanceName>
    # У каждого узла должно быть своё название
    nodeName: <instanceName><nodeNumber>
    
    # Адрес и порт сервера очереди сообщений (Kafka)
    mq.server: <kafkaBrokerIP>:<kafkaBrokerPort>
    mq.group: <instanceName>
    manageAdapterHost: true
    # Адрес и порт сервера Elasticsearch
    elasticsearchUri: <elasticsearchIP>:<elasticsearchPort>
    # Версия ПО
    version: <versionNumber>
    ```

6. Откройте файл `Workers.config` для редактирования:

    ``` sh
    nano /var/www/<instanceName>/Workers.config
    ```

7. Отредактируйте файл `Workers.config`, изменив статус служб и подставив значение параметра  `<ConfigurationId>` из [конфигурации первого узла](#ConfigurationId):

    ``` xml
    <?xml version="1.0" encoding="utf-8"?>
    <WorkerEngine xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-i>
      <RebuildThreadWorker>false</RebuildThreadWorker>
      <BackupSessionsQueue>false</BackupSessionsQueue>
      <SessionManagerWorker>false</SessionManagerWorker>
      <NotificationWorker>false</NotificationWorker>
      <EmailListener>true</EmailListener>
      <IndexTasksQueue>false</IndexTasksQueue>
      <ProcessEngineQueueProcessing>true</ProcessEngineQueueProcessing>
      <ProcessEngineTimerProcessing>false</ProcessEngineTimerProcessing>
      <SyncThread>false</SyncThread>
      <SwitchOnFullTextSearch>false</SwitchOnFullTextSearch>
      <PerformanceMonitoring>false</PerformanceMonitoring>
      <ConfigurationId>XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX</ConfigurationId>
    </WorkerEngine>
    ```

8. Запустите экземпляр ПО:

    ``` sh
    systemctl start comindware<instanceName>
    ```

9. В веб-браузере запустите сайт экземпляра ПО и выполните вход.
10. На машине, на которой развёрнут первый узел, перейдите в директорию со скриптами Apache Ignite:

    ``` sh
    cd /home/username/ignite/bin
    ```

11. Выполните запрос топологии, пока не отобразится сообщение о наличи стороннего узла:

    ``` sh
    bash control.sh --baseline
    ```

12. Выполните запрос на включение узла в топологию:

    ``` sh
    bash control.sh --baseline add <nodeConsistenceId> -y
    ```

13. На машине с новым узлом кластера перейдите в директорию со скриптами Apache Ignite:

    ``` sh
    cd /home/username/ignite/bin
    ```

14. Выполните запрос топологии:

    ``` sh
    watch bash control.sh --baseline
    ```

15. Дождитесь включения нового узла в топологию.
16. Дождитесь запуска страницы входа на сайт в веб-браузере.

## Настройка кластера после запуска

1. На машине, где развёрнут первый узел, удалите директорию `LocalTemp`:

    ``` sh
    rf -rf /var/lib/comindware/<instanceName>/LocalTemp
    ```

2. Создайте новую директорию `LocalTemp` и назначьте ей владельца:

    ``` sh
    mkdir /mnt/share/<instanceName>/LocalTemp
    chown -R www-data:www-data /mnt/storage/<instanceName>/LocalTemp
    ```

3. На каждой машине, на которой развёрнуты узлы кластера, создайте символьную ссылку на директорию `LocalTemp`:

    ``` sh
    ln -s /mnt/storage/<instanceName>/LocalTemp /var/lib/comindware/<instanceName>/LocalTemp
    ```
<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Установка, запуск, инициализация и остановка ПО][deploy_guide_linux]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}