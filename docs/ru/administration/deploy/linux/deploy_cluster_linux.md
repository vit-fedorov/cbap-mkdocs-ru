---
kbId: 5076
title: Развёртывание Comindware Business Application Platform в кластере
---

# Развёртывание {{ productName }} в кластере {: #deploy_cluster_linux}

--8<-- "experimental_feature.md"

## Введение

**{{ productName }}** можно развернуть в кластере для увеличения производительности, улучшения отказоустойчивости и обеспечения бесперебойного функционирования ПО.

Здесь представлены инструкции по развёртыванию кластера в простейшей минимальной конфигурации.

Фактическую продуктивную архитектуру кластера следует определять в рамках разработки ТЗ на целевую систему с учётом всех технических и бизнес-факторов:

- Прежде чем приступать к развёртыванию кластера, определите, какие показатели наиболее важны для бизнеса, а также их приоритетность:
    - производительность;
    - устойчивость;
    - горизонтальное масштабирование;
    - географическая распределённость;
    - RTO (Recovery Time Objective) — время восстановления после сбоя;
    - RPO (Recovery Point Objective) — допустимый объём утраченных данных после сбоя.
- Определите техническую и экономическую целесообразность достижения и поддержания целевых показателей.
- В зависимости от выявленных целевых показателей и бизнес-целей выберите архитектуру кластера на основе одного  следующих подходов или их сочетания:
    - Обеспечение отказоустойчивости
        - Имеется три или более узлов, из которых один является рабочим, а остальные резервными. Также предусмотрены сервер хранения данных и балансировщик нагрузки. ПО работает бесперебойно, пока сохраняют работоспособность как минимум один узел кластера и сервер данных. Показатели RTO/RPO можно свести к минимуму. Для восстановления данных достаточно резервной копии одного узла.
    - Распределение нагрузки
        - Имеется два или более узлов, сервер хранения данных и балансировщик нагрузки. Нагрузка равномерно распределяется между узлами, что сокращает время отклика. ПО работает бесперебойно, пока сохраняют работоспособность все узлы кластера и сервер данных. При равномерной нагрузке время отклика можно рассчитать по формуле: `Y/N+ε`, где `Y` — время отклика при нагрузке только на один узел, `N` — количество узлов, `ε` — погрешность.
    - Обеспечение высокой доступности
        - Имеется три или более узлов, сервер хранения данных и балансировщик нагрузки. ПО работает бесперебойно, пока сохраняют работоспособность два узла кластера и сервер данных. Даже при наличии постоянной нагрузки на балансировщике возможно выполнить поочерёдное обновление каждого из узлов до новой версии ПО.

## Конфигурация кластера

В минимальной конфигурации для распределения нагрузки (горизонтального масштабирования) кластер **{{ productName }}** включает следующие компоненты:

- сервер хранения данных на отдельной машине, к которому будут обращаться узлы кластера (для этого сервера необходимо отдельно обеспечить отказоустойчивость и высокую доступность);
- несколько машин, на каждой из которых установлено ПО **{{ productName }}** одинаковой версии и развёрнут экземпляр ПО с одинаковым именем (`<instanceName>`);
- сервер Elasticsearch на отдельной машине;
- сервер Apache Kafka на отдельной машине;
- балансировщик нагрузки на отдельной машине (при необходимости).

## Настройка сервера хранения данных (NFS)

Для взаимодействия с узлами кластера **{{ productName }}** настройте сервер хранения хранения данных, как указано ниже.

1. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

2. Создайте директорию для хранения файлов экземпляра ПО:

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

5. Добавьте в файл `exports` директиву, открывающую доступ к директории `/share` для узлов кластера:

    ``` sh
    /share <nodeIP>/<netMask>(rw,sync,no_subtree_check)
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

8. Создайте директории для хранения данных экземпляра ПО:

    ``` sh
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

На каждом узле кластера **{{ productName }}** необходимо установить ПО {{ productName }}, развернуть экземпляр ПО и установить бинарные пакеты Apache Ignite, как указано ниже.

### Установка ПО {{ productName }} и бинарных пакетов Apache Ignite

1. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

2. Установите ПО и разверните экземпляр **{{ productName }}** одинаковой версии. См. _«[Установка, запуск, инициализация и остановка ПО][deploy_guide_linux]»_.
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

5. Смонтируйте диски и просмотрите содержимое директории NFS-сервера:

    ``` sh
    mount -a
    ls -lh /mnt/share
    ```

6. Удостоверьтесь, что существует директория `/var/lib/comindware/<instanceName>`, и задайте её владельца:

    - **Astra Linux**, **Ubuntu**, **Debian** (DEB-based)

        ``` sh
        chown -R www-data: /var/lib/comindware/<instanceName>
        ```

    - **РЕД ОС**, **Rocky** (RPM-based)

        ``` sh
        chown -R nginx: /var/lib/comindware/<instanceName>
        ```

    - **Альт Сервер**

        ``` sh
        chown -R _nginx: /var/lib/comindware/<instanceName>
        ```

7. Создайте символическую ссылку на директорию со скомпилированными скриптами на NFS-сервере:

    ``` sh
    ln -s /mnt/share/<instanceName>/Scripts /var/lib/comindware/<instanceName>/Database/Scripts
    ```

8. Откройте файл `comindware<instanceName>-env` для редактирования:

    ``` sh
    nano /etc/sysconfig/comindware<instanceName>-env
    ```

9. Проверьте и при необходимости измените лимиты памяти в директиве `JVM_OPTS` — начальный и максимальный размер кучи и максимальный объём области прямого доступа к памяти, например:

    ``` ini
    -Xms512m -Xmx4g -XX:MaxDirectMemorySize=1g
    ```

## Настройка и запуск первого узла кластера

На машине с первым узлом кластера настройте доступ к файлам базы данных и экземпляр ПО.

### Перенос базы данных на NFS-сервер

Если на первом узле был развёрнут экземпляр ПО с базой данных, перенесите её на NFS-сервер.

**Для чистого экземпляра ПО данный этап не требуется.**

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

6. Перенесите данные экземпляра ПО на NFS-сервер:

    ``` sh
    cp -r Scripts/* /mnt/share/<instanceName>/Scripts/
    cp -r Streams/* /mnt/share/<instanceName>/Streams/
    mv Database/* /var/lib/comindware/<instanceName>/Database/
    rm -rf Database Scripts Streams
    ```

### Настройка экземпляра ПО

1. Откройте файл `Ignite.config` для редактирования:

    ``` sh
    nano /var/www/<instanceName>/Ignite.config
    ```

2. Отредактируйте файл `Ignite.config` по следующему образцу:

    ``` xml
    <property name="discoverySpi">
          <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
            <!-- Укажите IP-адрес, порт и диапазон портов первого узла -->
            <property name="localAddress" value="<node_1_IP>" />
            <property name="localPort" value="47510" />
            <property name="localPortRange" value="9" />
            <property name="ipFinder">
              <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
                <property name="addresses">
                  <list>
                    <!-- Укажите IP-адреса всех узлов кластера -->
                    <value><node_1_IP>:47510..47519</value>
                    <value><node_2_IP>:47510..47519</value>
                    ...
                    <value><node_N_IP>:47510..47519</value>
                  </list>
                </property>
              </bean>
            </property>
          </bean>
        </property>
        <property name="communicationSpi">
          <bean class="org.apache.ignite.spi.communication.tcp.TcpCommunicationSpi">
            <property name="localPort" value="47101" />
            <!-- Укажите IP-адрес первого узла -->
            <property name="localAddress" value="<node_1_IP>" />
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
                    <!-- Проверьте и при необходимости отредактируйте объём выделяемой памяти -->
                  <property name="initialSize" value="#{1024L * 1024 * 1024}" />
                  <property name="maxSize" value="#{4L * 1024 * 1024 * 1024}" />
                  <property name="pageEvictionMode" value="RANDOM_2_LRU" />
                  <property name="checkpointPageBufferSize" value="#{1024L * 1024 * 1024}" />
                </bean>
                <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
                  <property name="name" value="InMemory" />
                  <property name="persistenceEnabled" value="false" />
                    <!-- Проверьте и при необходимости отредактируйте объём выделяемой памяти -->
                  <property name="initialSize" value="#{10 * 1024 * 1024}" />
                  <property name="maxSize" value="#{256 * 1024 * 1024}" />
                </bean>
              </list>
            </property>
          </bean>
        </property>
    ```

3. Откройте файл конфигурации экземпляра ПО для редактирования:

    ``` sh
    nano /usr/share/comindware/configs/instance/<instanceName>.yml
    ```

4. Отредактируйте файл конфигурации экземпляра ПО по следующему образцу (см. _«[Конфигурация экземпляра, компонентов ПО и служб. Настройка][configuration_files_linux]»_):

    ``` yml
    isFederationAuthEnabled: 0
    databasePath: /var/lib/comindware/<instanceName>/Database
    configPath: /var/www/<instanceName>
    # Укажите примонтированные директории NFS-сервера с файлами экземпляра ПО
    backup.config.default.repository.type: LocalDisk
    backup.config.default.repository.localDisk.path: /mnt/share/comindware/Backup
    userStorage.type: LocalDisk
    userStorage.localDisk.path: /mnt/share/<instanceName>/Streams
    tempStorage.type: LocalDisk
    tempStorage.localDisk.path: /mnt/share/<instanceName>/Temp

    instanceName: <instanceName>
    databaseName: <instanceName>
    configName: <instanceName>
    # У каждого узла должно быть уникальное имя
    nodeName: <instanceName><nodeNumber>

    mq.server: <kafkaBrokerIP>:<kafkaBrokerPort>
    mq.group: <instanceName>
    manageAdapterHost: true
    elasticsearchUri: <elasticsearchIP>:<elasticsearchPort>
    version: <versionNumber>
    ```

5. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

6. При наличии файла `Workers.config` удалите его:

    ```sh
    rm -f /var/www/npportalid/Workers.config
    ```

7. Запустите службу экземпляра ПО:

    ``` sh
    systemctl start comindware<instanceName>
    ```

8. В веб-браузере запустите сайт экземпляра ПО и выполните вход.
9. Откройте файл `Workers.config` для редактирования:

    ``` sh
    nano /var/www/<instanceName>/Workers.config
    ```

10. Отредактируйте файл `Workers.config` по следующему образцу:

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
        <!-- Значение ConfigurationId должно совпадать на всех узлах -->
      <ConfigurationId>XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX</ConfigurationId>
    </WorkerEngine>
    ```

11. Настройте владельца файла `Workers.config`:

    - **Astra Linux**, **Ubuntu**, **Debian** (DEB-based)

        ``` sh
        chown www-data: /var/www/<instanceName>/Workers.config
        ```

    - **РЕД ОС**, **Rocky** (RPM-based)

        ``` sh
        chown nginx: /var/www/<instanceName>/Workers.config
        ```

    - **Альт Сервер**

        ``` sh
        chown _nginx: /var/www/<instanceName>/Workers.config
        ```

12. Перезапустите экземпляр ПО:

    ``` sh
    systemctl restart comindware<instanceName>
    ```

13. Настройте директорию `LocalTemp`. См. _«[Создание директории LocalTemp после запуска узлов кластера](#создание-директории-localtemp-после-запуска-узлов-кластера)»_.

## Настройка и запуск второго и последующих узлов кластера

На машине со вторым и последующими узлами кластера настройте конфигурацию экземпляра ПО.

1. Перейдите в режим суперпользователя:

    --8<-- "linux_sudo.md"

2. Откройте файл `Ignite.config` для редактирования:

    ``` sh
    nano /var/www/<instanceName>/Ignite.config
    ```

3. Отредактируйте файл `Ignite.config` по следующему образцу:

    ``` xml
    <property name="discoverySpi">
          <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
            <!-- Укажите IP-адрес, порт и диапазон портов узла N -->
            <property name="localAddress" value="<node_N_IP>" />
            <property name="localPort" value="47510" />
            <property name="localPortRange" value="9" />
            <property name="ipFinder">
              <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
                <property name="addresses">
                  <list>
                    <!-- Укажите IP-адреса всех узлов кластера -->
                    <value><node_1_IP>:47510..47519</value>
                    <value><node_2_IP>:47510..47519</value>
                    ...
                    <value><node_N_IP>:47510..47519</value>
                  </list>
                </property>
              </bean>
            </property>
          </bean>
        </property>
        <property name="communicationSpi">
          <bean class="org.apache.ignite.spi.communication.tcp.TcpCommunicationSpi">
            <property name="localPort" value="47101" />
            <!-- укажите IP-адрес узла -->
            <property name="localAddress" value="<nodeIP_n>" />
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
                    <!-- Проверьте и при необходимости отредактируйте размер выделяемой памяти -->
                  <property name="initialSize" value="#{1024L * 1024 * 1024}" />
                  <property name="maxSize" value="#{4L * 1024 * 1024 * 1024}" />
                  <property name="pageEvictionMode" value="RANDOM_2_LRU" />
                  <property name="checkpointPageBufferSize" value="#{1024L * 1024 * 1024}" />
                </bean>
                <bean class="org.apache.ignite.configuration.DataRegionConfiguration">
                  <property name="name" value="InMemory" />
                  <property name="persistenceEnabled" value="false" />
                    <!-- Проверьте и при необходимости отредактируйте размер выделяемой памяти -->
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

5. Скопируйте содержимое файла конфигурации первого узла и в директиве `nodeName` укажите уникальное имя узла.
6. Откройте файл `Workers.config` для редактирования:

    ``` sh
    nano /var/www/<instanceName>/Workers.config
    ```

7. Скопируйте содержимое файла `Workers.config` первого узла.
8. Удостоверьтесь, что значение директивы `<ConfigurationId>` совпадает на всех узлах.
9. Запустите экземпляр ПО:

    ``` sh
    systemctl start comindware<instanceName>
    ```

10. В браузере запустите сайт экземпляра ПО.
11. На машине, на которой развёрнут первый узел, перейдите в директорию со скриптами Apache Ignite:

    ``` sh
    cd /home/username/ignite/bin
    ```

12. Выполняйте запрос топологии до тех пор, пока не отобразится сообщение о наличии стороннего узла:

    ``` sh
    bash control.sh --baseline
    ```

13. Выполните запрос на включение узла N в топологию (`<nodeNConsistenceId>` — идентификатор узла N в Ignite):

    ``` sh
    bash control.sh --baseline add <nodeNConsistenceId> -y
    ```

14. На машине с узлом N кластера перейдите в директорию со скриптами Apache Ignite:

    ``` sh
    cd /home/username/ignite/bin
    ```

15. Выполните запрос топологии:

    ``` sh
    watch bash control.sh --baseline
    ```

16. Дождитесь включения узла N в топологию.
17. Дождитесь отображения страницы входа в экземпляр ПО в браузере.

## Создание директории LocalTemp после запуска узлов кластера

При каждом запуске экземпляра ПО заново создаётся локальная папка `/var/lib/comindware/<instanceName>/LocalTemp` и удаляется символьная ссылка на неё на NFS-сервере. После этого необходимо удалить директорию `/var/lib/comindware/<instanceName>/LocalTemp` и пересоздавать символьную ссылку на директорию `LocalTemp` на NFS-сервере.

1. На каждом узле удалите локальную директорию `LocalTemp`:

    ``` sh
    rm -rf /var/lib/comindware/<instanceName>/LocalTemp
    ```

2. С любого узла создайте директорию `LocalTemp` на NFS-сервере:

        ``` sh
        mkdir /mnt/share/<instanceName>/LocalTemp
        ```

3. На каждом узле назначьте владельца директории `LocalTemp` на NFS-сервере:

    - **Astra Linux**, **Ubuntu**, **Debian** (DEB-based)

        ``` sh
        chown -R www-data:www-data /mnt/share/<instanceName>/LocalTemp
        ```

    - **РЕД ОС**, **Rocky** (RPM-based)

        ``` sh
        chown -R nginx:nginx /mnt/share/<instanceName>/LocalTemp
        ```

    - **Альт Сервер**

        ``` sh
        chown -R _nginx:_nginx /mnt/share/<instanceName>/LocalTemp
        ```

4. На каждом узле создайте символьную ссылку на директорию `LocalTemp` с NFS-сервера:

    ``` sh
    ln -s /mnt/share/<instanceName>/LocalTemp /var/lib/comindware/<instanceName>/LocalTemp
    ```

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Установка, запуск, инициализация и остановка ПО][deploy_guide_linux]_
- _[Пути и содержимое директорий экземпляра ПО][paths]_
- _[Конфигурация экземпляра, компонентов ПО и служб. Настройка][configuration_files_linux]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}