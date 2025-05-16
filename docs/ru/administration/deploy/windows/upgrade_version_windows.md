---
title: 'Обновление версии экземпляра ПО в Windows'
kbId: 
---

# Обновление версии экземпляра ПО в Windows {: #upgrade_version_windows }

## Введение

Здесь представлены инструкции по обновлению версии экземпляра ПО **{{ productName }}** на одном и том же сервере с остановкой экземпляра.

Инструкции даны для обновления с версий 4.7.2 до версий 4.7.3–5.0 в ОС Windows.

!!! tip "Совет"

    Этот способ можно использовать, если ПО **{{ productName }}** развёрнуто на одной машине и нет возможности развернуть новую машину для экземпляра ПО новой версии.

## Примечания {: #upgrade_version_windows_notes }

{%
include-markdown "../linux/deploy_guide.md"
start="<!--windows-deploy-notes-start-->"
end="<!--windows-deploy-notes-end-->"
%}

{%
include-markdown "../linux/deploy_guide.md"
start="<!--powershell-execution-policy-start-->"
end="<!--powershell-execution-policy-end-->"
%}

## Порядок обновления версии экземпляра ПО

1. Подготовьте экземпляр ПО к обновлению:

    - Создайте резервную копию экземпляра ПО.
    - Сохраните конфигурацию экземпляра ПО и вспомогательных служб.
    - Остановите экземпляр ПО и вспомогательные службы.
    - Удалите компоненты старой версии ПО.
    - Переместите директорию с базой данных экземпляра ПО в резервную директорию.

2. Обновите версию экземпляра ПО:

    - Скачайте и распакуйте два дистрибутива: вспомогательного ПО и новой версии ПО.
    - Убедитесь, что установлены все необходимые компоненты вспомогательного ПО.
    - Установите новую версию ПО.
    - Удалите экземпляр ПО старой версии
    - Создайте экземпляр ПО новой версии.
    - Обновите конфигурацию экземпляра ПО и вспомогательных служб.
    - Перезапустите экземпляр ПО и вспомогательные службы.
    - Инициализируйте экземпляр ПО.
    - Остановите экземпляр ПО.
    - Скопируйте в экземпляр ПО ранее перемещённую директорию с базой данных.
    - Запустите экземпляр ПО.
    - Обновите структуру данных до новой версии.
    - Снова перезапустите экземпляр ПО.

## Подготовка экземпляра ПО к обновлению {: .pageBreakBefore }

!!! warning "Внимание!"

    Выполните подготовительные действия отдельно для каждого экземпляра ПО, версию которого требуется обновить.

1. Создайте и перенесите во внешнее хранилище резервную копию базы данных экземпляра ПО. См. _«[Резервное копирование и восстановление {{ productName }}. Краткое руководство для ОС Windows][backup_restore_windows]»_.

2. Запустите _PowerShell_ от имени администратора.

3. Сохраните резервную копию файлов конфигурации:
{: #ConfigBackup }

- **Создаём папку для сбора резервных копий файлов конфигурации:**

    ``` powershell
    New-Item -Path "X:\backups\config_tmp" -ItemType "Directory"
    ```

    Здесь и далее:
    `X:\backups\config_tmp` — путь к папке, в которую будем копировать резервные копии файлов конфигурации

- **Переходим в папку с экземпляром ПО:**

    ``` powershell
    cd C:\ProgramData\сomindware\Instances\<instanceName>
    ```

- **Копируем все файлы .yml и .config в резервную папку:**

    ``` powershell
    Copy-Item -Path "C:\ProgramData\сomindware\Instances\<instanceName>\сonfig\*" -Destination "X:\backups\config_tmp" -Recurse -Include "*.yml", "*.config"
    ```

- **Скопируйте настройки IIS.**

  - Откройте командную строку в качестве администратора
  - Cоздайте резервную копию конфигурации IIS:

    ``` powershell
    cd c:\Windows\system32\inetsrv
    appcmd add backup iis-backup-conf
    ```

    `iis-backup-conf` — это резервная папка.

    После выполнения команды в `c:\Windows\system32\inetsrv\backup` появляется папка с вашими резервными файлами настроек.


- **Копируем настройки Java:**
    Перейдите в локальные переменные среды и сформируйте их по приведённому ниже образцу, подставив свои фактические пути и значения.

    В переменных среды Windows должна быть заданы следующие переменные для Open JDK (здесь `<version>` — номер версии Open JDK):
    - `JAVA_HOME` — путь к исполняемым файлам Open JDK 17, например `C:\Program Files\jdk\jdk-<version>`
    - `JAVA_HOME_DLL` — путь к DLL-файлу Open JDK 17, например `C:\Program Files\jdk\jdk-<version>\bin\server\jvm.dll`
    - `JAVA_OPTS` — начальный и максимальный объёмы памяти, выделенные для Java, например `-Xms512m -Xmx3g`
    - `JVM_OPTS`  — конфигурация запуска виртуальной машины Java, рекомендуется использовать следующий набор настроек:
    {: .pageBreakBefore }
    
    ``` powershell
    -Xms512m -Xmx16g -XX:MaxDirectMemorySize=1g -Djava.net.preferIPv4Stack=true -XX:+AlwaysPreTouch -XX:+UseG1GC -XX:+ScavengeBeforeFullGC -XX:+DisableExplicitGC --add-opens=java.base/sun.nio.ch=ALL-UNNAMED --add-opens=java.base/java.io=ALL-UNNAMED --add-opens=java.base/java.nio=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED --add-opens=java.base/java.lang=ALL-UNNAMED --add-exports=java.base/jdk.internal.misc=ALL-UNNAMED --add-exports=java.base/sun.nio.ch=ALL-UNNAMED --add-exports=java.management/com.sun.jmx.mbeanserver=ALL-UNNAMED --add-exports=jdk.internal.jvmstat/sun.jvmstat.monitor=ALL-UNNAMED --add-exports=java.base/sun.reflect.generics.reflectiveObjects=ALL-UNNAMED --add-opens=jdk.management/com.sun.management.internal=ALL-UNNAMED -DIGNITE_QUIET=false -DIGNITE_NO_ASCII=true
    ```


- **Копируем основной конфиг экземпляра ПО:**
    ``` powershell
    Copy-Item -Path "C:\ProgramData\comindware\configs\instance\<instanceName>.yml" -Destination "X:\backups\config_tmp"
    ```

    Здесь `<instanceName>` — имя экземпляра ПО.


4. Остановите экземпляр ПО и вспомогательные службы и удостоверьтесь, что они остановлены

- Перейдите в папку со скриптами для развёртывания ПО **{{ productName }}**:
    ``` powershell
    cd "X:\<distPath>\X.X-release-ru-<versionNumber>.windows\CMW_Windows<versionNumber>\scripts"
    ``` 

- Остановите экземпляр ПО:

    ``` powershell
    .\instance_stop.ps1 -name <instanceName>
    ``` 
- Остановите adapterhost для экземпляра ПО:

    ``` powershell
    .\adapterhost_stop.ps1 <instanceName>
    ``` 
- Остановите apigateway для экземпляр ПО:

    ``` powershell
    .\apigateway_stop.ps1 <instanceName>
    ``` 

Здесь: `-name <instanceName>` — **обязательный** ключ с именем экземпляра ПО.


5. Проверьте статус экземпляра в IIS

    Запустите **Диспетчер служб IIS** (IIS Manager):

     - В левой древовидной панеле **«Подключения»** (Connections), разверните меню с названием своего сервера, 
     - Зайдите в **«Пулы приложений»** (Application Pools) 
     - Убедитесь, что напротив сервисов `Comindware <InstanceName>`, `Comindware <InstanceName>_adapterhost`, `Comindware <InstanceName>_apigateway` стоит статус «Остановлен» (Stopped).


6. Удалите (или переместите в резервное хранилище) неиспользуемые предыдущие дистрибутивы ПО (`<distPath>` — путь к директории с дистрибутивом, `<versionNumber>` — версия ПО):

    ``` powershell
    Remove-Item X:\<distPath>\X.X-release-ru-<versionNumber>.windows\CMW_Windows<versionNumber> -Recurse
    ```

7. Скопируйте директорию с базой данных экземпляра ПО

    ``` powershell
    Copy-Item -Path "C:\ProgramData\сomindware\Instances\<instanceName>\Database" -Destination "X:\backups\config_tmp" -Recurse
    ```

Путь до файлов базы данных экземпляра ПО:
    `C:\ProgramData\сomindware\Instances\<instanceName>\Database`


## Обновление версии ПО для экземпляра {: .pageBreakBefore }

!!! warning "Внимание!"

    Если при обновлении [на шаге 26](#dataUpgrade) будут обнаружены ошибки, не продолжайте обновление, установите старую версию, восстановите экземпляр ПО из резервной копии и обратитесь в службу поддержки **{{ companyName }}**.

!!! note "Обновление нескольких экземпляров ПО"

    Выполните приведённые ниже шаги 9–21 для каждого экземпляра ПО, версию которого требуется обновить, так как скрипт обновления выполняется отдельно для указанного экземпляра ПО.

    После обновления всех экземпляров ПО для экономии места старую версию ПО можно удалить согласно инструкции _«[Удаление версии ПО][deploy_guide_windows_delete_version]»_.


1. Скачайте и распакуйте дистрибутив с новой версией вспомогательного ПО.

2. Проверьте, что установлены все компоненты вспомогательного ПО:

    ``` powershell
    .\prerequisites_list.ps1
    ```

Важно, чтобы были установлены все компоненты вспомогательного ПО.

!!! warning "Внимание!"

    Если каких-то компонентов не хватает, то установите соответствующую версию вспомогательного ПО согласно инструкции _«[Установка вспомогательного ПО](#deploy_guide_windows_install_prerequisites)»_.

3. Скачайте и распакуйте архив с дистрибутивом новой версией ПО.
4. Запустите _PowerShell_ от имени администратора.

5. При необходимости установите неограниченную политику выполнения _PowerShell_. См. _«[Политика выполнения PowerShell](#powershell_execution_policy)»_.
6. В запросе на изменение политики выберите вариант «**Да для всех**», введя букву A.
7. Перейдите в папку со скриптами для развёртывания ПО **{{ productName }}**:

    ``` powershell
    cd "X:\<distPath>\X.X-release-ru-<versionNumber>.windows\CMW_Windows<versionNumber>\scripts"
    ``` 

Здесь: `X:\<distPath>\X.X-release-ru-<versionNumber>.windows` — путь к распакованному дистрибутиву продукта, а `<versionNumber>` — номер версии ПО.

8. Разблокируйте доступ к скачанным из Интернета установочным файлам:

    ``` powershell
    .\files_unblock.ps1 
    ``` 

!!! note "Вызов справки для скриптов"
    Для ознакомления с ключами и назначением любого скрипта используйте ключ `-h` без каких-либо других ключей, например:
    ```.\files_unblock.ps1 -h``` 

9. Установите новую версию ПО:

    ``` powershell
    .\version_install.ps1
    ``` 

10. Удостоверьтесь, что ПО установлено, вызвав список установленных версий ПО:

    ``` powershell
    .\version_list.ps1
    ``` 

Отобразится список установленных версий ПО на сервере.

11. Удалите экземпляр ПО старой версии:

    ``` powershell
    .\instance_delete.ps1 -name <instanceName> -clear
    ``` 

    Ключи:

    - `-name` — имя экземпляра.

        Если не указать другие ключи, будет удалена только служба `comindware<instanceName>`.

    - `-deleteData` (необязательно) — удалить следующие объекты:
        - базу данных из папки вида `C:\ProgramData\Comindware\Instances\<instanceName>\Data`;
        - пользовательские файлы экземпляра ПО из папки вида `C:\ProgramData\Comindware\Instances\<instanceName>\Streams`.

        Без указания этого ключа или ключа `-clear` база данных экземпляра ПО не будет удалена.

    - `-clear` (необязательно)  — удалить следующие объекты:
        - все файлы, папки, базу данных и пользовательские файлы экземпляра ПО;
        - папку экземпляра ПО вида `C:\ProgramData\Comindware\Instances\<instanceName>`;
        - все службы экземпляра ПО;
        - сайт и пул приложения из IIS.

12. Создайте экземпляр ПО новой версии:

    ``` powershell
    .\instance_create.ps1 -name <instanceName> -port <portNumber> -version <versionNumber>
    ```  

    Ключи:

    - `-name` — имя экземпляра;
    - `-version` — номер версии ПО;
    - `-port` (необязательно) — порт для экземпляра ПО (по умолчанию: 80).

13. По окончании создания скрипт выведет информацию о компонентах экземпляра ПО. Удостоверьтесь, что компоненты успешно установлены.

Если какая-либо из служб имеет статус `FAILED`, перезапустите её.
Например для экземпляра ПО:

    ``` powershell
    .\instance_stop.ps1 -name <instanceName>
    .\instance_start.ps1 -name <instanceName>
    ``` 

Для apigateway: `apigateway_stop.ps1` и `apigateway_start.ps1`
Для adapterhost: `adapterhost_stop.ps1` и `adapterhost_start.ps1`

14. Отредактируйте конфигурацию IIS для экземпляра ПО в соответствии с резервной копией, [сохранённой ранее](#IIS_Backup):

Запуск через строку поиска или «Выполнить» (Win + R)

    ``` r
    InetMgr.exe
    ```

15. Перезапустите службу IIS для применения изменений:

    ``` powershell
    Restart-WebAppPool -Name <DefaultAppPool>
    ```
Замените `<DefaultAppPool>` на имя нужного пула приложений

16. Отредактируйте файлы конфигурации в соответствии с резервными копиями, [сохранёнными ранее](#ConfigBackup):

| **Путь** | **Служба** |
| --- | --- |
| `C:\ProgramData\сomindware\Instances\<instanceName>\сonfig\adapterhost.yml` | Adapterhost |
| `C:\ProgramData\сomindware\Instances\<instanceName>\сonfig\apigateway.yml` | Apigateway |
| `C:\ProgramData\сomindware\Instances\<instanceName>\сonfig\Ignite.config` | Ignite |
| `C:\ProgramData\сomindware\configs\instance\<instanceName>.yml` | файл конфигурации |

Здесь `<instanceName>` — имя экземпляра ПО.

17. Отредактируйте настройки локальной переменной среды.

Открыть настройки локальной переменной среды можно через Powershell:
    ``` powershell
    rundll32 sysdm.cpl,EditEnvironmentVariables
    ```

18. Перезапустите сервисы, настройки которых были изменены:

    Перейдите в папку со скриптами для развёртывания ПО ** {{ productName }}**:

    ``` powershell
    cd "X:\<distPath>\CMW_Windows<versionNumber>\scripts"
    ```

    Здесь: `X:\<distPath>` — путь к распакованному дистрибутиву продукта, а `<versionNumber>` — номер версии ПО.

    Запустите необходимые для перезапуска скрипты.

    Перезапуск экземпляра ПО:

    ``` powershell
    .\instance_stop.ps1 -name <instanceName>
    .\instance_start.ps1 -name <instanceName>
    ``` 

    Перезапуск Apigateway:

    ``` powershell
    .\apigateway_stop.ps1 -name <instanceName>
    .\apigateway_start.ps1 -name <instanceName>
    ```

    Перезапуск Adapterhost:

    ``` powershell
    .\adapterhost_stop.ps1 -name <instanceName>
    .\adapterhost_start.ps1 -name <instanceName>
    ```

19. Откройте сайт экземпляра ПО в браузере, одновременно открыв выдачу журналов экземпляра в _PowerShell_:

    ```powershell
    Get-Content "C:\ProgramData\comindware\Instances\<instanceName>\Logs\heartbeat_<ГГГГ-ММ-ДД>.log" -Wait
    ```
Здесь:
    `<instanceName>` — имя экземпляра ПО
    `<ГГГГ-ММ-ДД>` — Текущая дата


20. В браузере выполните инициализацию экземпляра ПО, выполните вход и проверьте работоспособность ПО.

21. Остановите экземпляр ПО:

    ``` powershell
    .\instance_stop.ps1 -name <instanceName>
    ``` 

22. Удалите или переименуйте папку `Database` в  директории  экземпляра ПО (`C:\ProgramData\сomindware\Instances\<instanceName>`)

Удаление папки Database через Powershell:

    ``` powershell
    Remove-Item -Path "C:\ProgramData\comindware\Instances\<instanceName>\Database" -Recurse
    ```

`<instanceName>` — имя экземпляра ПО

23. Скопируйте в экземпляр ПО директорию с базой данных экземпляра ПО, сохранённую ранее:

    ``` powershell
    Copy-Item -Path "X:\backups\config_tmp\Database" -Destination "C:\ProgramData\сomindware\Instances\<instanceName>" -Recurse -Force
    ```
Здесь:
    `C:\ProgramData\сomindware\Instances\<instanceName>` — путь до файлов экземпляра ПО
     `<X:\backups\config_tmp>` — путь до папки с резервными копиями файлов экземпляра ПО


24. Запустите экземпляр ПО:

    ``` powershell
    .\instance_start.ps1 -name <instanceName>
    ``` 

25. Откройте сайт экземпляра ПО в браузере, дождитесь окончания загрузки, одновременно открыв выдачу журналов экземпляра в _PowerShell_:

    ``` powershell
    Get-Content "C:\ProgramData\comindware\Instances\<instanceName>\Logs\heartbeat_<date>.log" -Wait
    ```
Здесь:
    `<instanceName>` — имя экземпляра ПО
    `<date>` — Текущая дата

26. Дождитесь завершения обновления структуры данных и проверьте его успешное выполнение.
{: #dataUpgrade }

!!! warning "Внимание!"

    При обновлении с версии 4.7.2 на версии 4.7.3-5.0 обновляется структура базы данных.

    После этого необходимо вручную удалить некоторые данные кэша в старом формате.

    Поэтому продолжать обновление версии экземпляра ПО можно только после успешного обновления структуры данных. 


- Удостоверьтесь, что появились журналы обновления:
    - `C:\ProgramData\сomindware\Instances\<instanceName>\Logs\UpgradeOntology_<ГГГГ-ММ-ДД>.log`
    - `C:\ProgramData\сomindware\Instances\<instanceName>\Logs\upgrade<ГГГГ-ММ-ДД>.log`
- Удостоверьтесь, что в журнале `UpgradeOntology_<ГГГГ-ММ-ДД>.log` последняя запись содержит строку `Upgrade of ontology completed successfully`.
- Удостоверьтесь, что в журнале `upgrade<ГГГГ-ММ-ДД>.log` последняя запись содержит строку `Upgrade completed`.
- Удостоверьтесь, что в журналах отсутствуют ошибки обновления. Найдите их по ключевому слову `error`.
- Если обновление выполнено успешно, переходите к шагу 27.
- Если в журнале обновления имеются ошибки:
    1. Не переходите к шагу 27.
    2. Снова установите для экземпляра старую версию ПО.
    3. Восстановите базу данных из резервной копии.
    4. Обратитесь в службу поддержки **{{ companyName }}**, предоставив журналы обновления и ошибок для анализа.


27. Создайте резервную копию экземпляра ПО:

- в формате `.CDBBZ` средствами ** {{ productName }}**;
или
- c помощью скрипта для создания снимка базы.

28. Остановите экземпляр ПО.

29. Распакуйте резервную копию и удалите из неё лишний кэш.
    В директории базы-данных найдите папку `Database\db\node*` и удалите из неё следующие директории кэшей::

    ``` powershell
    Remove-Item cacheGroup-*-TableIdentity -Recurse -Force
    Remove-Item cacheGroup-*-TableIdentityReplicated -Recurse -Force
    Remove-Item cacheGroup-*Value -Recurse -Force
    Remove-Item cacheGroup-*ValueReplicated -Recurse -Force
    Remove-Item cache-ignite-sys-cache -Recurse -Force
    Remove-Item cp -Recurse -Force
    Remove-Item metastorage -Recurse -Force
    Remove-Item cacheGroup-Keys -Recurse -Force
    ```

30. Очистите директорию с базой данных экземпляра ПО:

    ``` powershell
    Remove-Item -Path "C:\ProgramData\comindware\Instances\<instanceName>\Database\*" -Recurse -Force
    ```

31. Скопируйте очищенную резервную копию в директорию с базой данных: 

    ``` powershell
    Copy-Item -Path "X:\<backupFolder>\Database\*" -Destination "C:\ProgramData\comindware\Instances\<instanceName>\Database" -Recurse -Force
    ```
Здесь:
`X:\<backupFolder>` - Путь до папки с распакованной резервной копией экземпляра ПО

32. Запустите экземпляр ПО

33. Откройте сайт экземпляра ПО в браузере, дождитесь его инициализации и выполните вход.




<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Установка вспомогательного ПО](#deploy_guide_windows_install_prerequisites)_
- _[Резервное копирование и восстановление Comindware Platform. Краткое руководство для ОС Windows](backup_restore_windows)_
- _[Установка, запуск, инициализация и остановка Comindware Platform в Windows](#deploy_guide_windows)_

</div>




{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
