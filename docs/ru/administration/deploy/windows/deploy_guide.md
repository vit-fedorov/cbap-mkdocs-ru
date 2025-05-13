---
title: 'Установка, запуск, инициализация и остановка Comindware Platform в Windows'
kbId: 5063
---

# Установка, запуск, инициализация и остановка {{ productName }} в Windows {: #deploy_guide_windows}

## Введение {: #deploy_guide_windows_intro }

Для быстрого развёртывания **{{ productName }}** в Windows компания **{{ companyName }}** предоставляет дистрибутив с установщиком, настраивающим необходимое программное обеспечение.

Здесь представлены инструкции по развёртыванию и инициализации **{{ productName }}** из дистрибутива в ОС Windows.

## Требования к серверу {: #deploy_guide_windows_requirements }

Для работы **{{ productName }}** требуются операционная система, сервер базы данных, веб-сервер, обратный прокси-сервер и сервер журналирования.

Перед установкой ПО убедитесь, что сервер соответствует следующим требованиям:

- сервер работает под управлением _Windows Server_;
- сервер настраивается от имени пользователя с правами администратора;
- установлена служба _IIS (Internet Information Services)_.

{%
include-markdown ".snippets/elasticsearch_opensearch_configure.md"
rewrite-relative-urls=false
%}

## Порядок установки ПО {: #deploy_guide_windows_order }

1. Подготовьте сервер к установке ПО.
2. Установите и настройте необходимое вспомогательное ПО.
3. Установите ПО **{{ productName }}**.
4. Создайте экземпляр ПО.
5. Запустите экземпляр ПО.
6. Инициализируйте экземпляр ПО.

## Подготовка сервера к установке ПО {: #deploy_guide_windows_server_prepare }

1. Откройте **Диспетчер сервера**.
2. Добавьте в список серверов компьютер, на котором будет установлено ПО **{{ productName }}**.
3. Запустите **Мастер добавления ролей и компонентов**, выбрав пункт «**Добавить роли и компоненты**» для данного сервера.
4. На шаге «**Тип установки**» выберите пункт «**Установка ролей или компонентов**».
5. На шаге «**Выбор сервера**» укажите сервер, на котором будет установлено ПО.
6. На шаге «**Роли сервера**» установите флажок «**Веб-сервер (IIS)**».
7. На шаге «**Компоненты**» для компонента «**Веб-сервер (IIS)** — **Веб-сервер** — **Разработка приложений**» установите следующие флажки:

    - **ASP.NET 4.8** (или выше);
    - **Расширяемость .NET 4.8** (или выше);
    - **Расширения ISAPI**;
    - **Фильтры ISAPI**.

8. На шаге «**Подтверждение**» нажмите кнопку «**Установить**» и дождитесь завершения процесса.

## Установка вспомогательного ПО {: #deploy_guide_windows_install_prerequisites }

!!! tip "Необходимое вспомогательное ПО"

    Для работы {{ productName }} требуется следующее вспомогательное ПО:

    - [.NET 8.0 SDK 8.0.408](https://dotnet.microsoft.com/en-us/download/dotnet/8.0)+
    -  [ASP.NET Core 8.0 Runtime - Windows Hosting Bundle Installer](https://dotnet.microsoft.com/ru-ru/download/dotnet/thank-you/runtime-aspnetcore-8.0.15-windows-hosting-bundle-installer)
    - [Microsoft Build of OpenJDK 17](https://learn.microsoft.com/en-us/java/openjdk/download#openjdk-17)+

    Вы можете скачать и установить их самостоятельно, либо используя наш дистрибутив вспомогательного ПО согласно инструкции.
    
    Также могут потребоваться:

    - [7-Zip](https://www.7-zip.org/) 
    - [VSCode](https://code.visualstudio.com/Download)

1. Скачайте и распакуйте архив с дистрибутивом вспомогательного ПО для **{{ productName }}**.
2. Запустите _PowerShell_ от имени администратора.
3. Установите неограниченную политику выполнения _PowerShell_:

    ``` powershell
    Set-ExecutionPolicy Unrestricted
    ```

    В запросе на изменение политики выберите вариант «**Да для всех**», введя букву ++a++.

4. Перейдите в папку со скриптами для развёртывания вспомогательного ПО:

    ``` powershell
    cd "X:\<distPath>\X.X-release-ru-<versionNumber>.prerequisites.windows\CMW_Windows<versionNumber>\scripts"
    ```

    Здесь: `X:\<distPath>\X.X-release-ru-<versionNumber>.prerequisites.windows` — путь к распакованному дистрибутиву вспомогательного ПО, а `<versionNumber>` — номер версии ПО.

5. Разблокируйте доступ к скачанным из Интернета установочным файлам:

    ``` powershell
    .\files_unblock.ps1
    ```

    !!! tip "Вызов справки для скриптов"

        Для ознакомления с ключами и назначением любого скрипта используйте ключ `-h` без каких-либо других ключей, например:

        ``` powershell
        .\files_unblock.ps1 -h
        ```

6. Установите необходимое вспомогательное ПО:

    ``` powershell
    .\prerequisites_install.ps1
    ```

7. Перезагрузите машину.
8. Запустите _PowerShell_ от имени администратора.
9. Перейдите в папку со скриптами для развёртывания вспомогательного ПО:

    ``` powershell
    cd "X:\<distPath>\X.X-release-ru-<versionNumber>.prerequisites.windows\CMW_Windows<versionNumber>\scripts"
    ```

10. Проверьте, что дополнительные компоненты установлены:

    ``` powershell
    .\prerequisites_list.ps1
    ```
    Если какие-либо дополнительные компоненты не были установлены, повторите шаги 6–10.

## Установка {{ productName }} {: #deploy_guide_windows_install_sw }

1. Скачайте и распакуйте архив с дистрибутивом **{{ productName }}**.
2. Запустите _PowerShell_ от имени администратора.
3. Установите неограниченную политику выполнения _PowerShell_:

    ``` powershell
    Set-ExecutionPolicy Unrestricted
    ```

4. В запросе на изменение политики выберите вариант «**Да для всех**», введя букву ++a++.
5. Перейдите в папку со скриптами для развёртывания ПО **{{ productName }}**:

    ``` powershell
    cd "X:\<distPath>\X.X-release-ru-<versionNumber>.windows\CMW_Windows<versionNumber>\scripts"
    ```

    Здесь: `X:\<distPath>\X.X-release-ru-<versionNumber>.windows` — путь к распакованному дистрибутиву продукта, а `<versionNumber>` — номер версии ПО.

6. Разблокируйте доступ к скачанным из Интернета установочным файлам:

    ``` powershell
    .\files_unblock.ps1
    ```

    !!! tip "Вызов справки для скриптов"

        Для ознакомления с ключами и назначением любого скрипта используйте ключ `-h` без каких-либо других ключей, например:

        ``` powershell
        .\files_unblock.ps1 -h
        ```

7. Установите версию ПО:

    ``` powershell
    .\version_install.ps1
    ```

15. Удостоверьтесь, что ПО установлено, вызывав список установленных версий ПО:

    ``` powershell
    .\version_list.ps1
    ```

## Создание экземпляра ПО {: #deploy_guide_windows_instance_create }

1. Перейдите в папку со скриптами для развёртывания ПО **{{ productName }}**:

    ``` powershell
    cd "X:\<distPath>\X.X-release-ru-<versionNumber>.windows\CMW_Windows<versionNumber>\scripts"
    ```

2. Разверните экземпляр ПО:

    ``` powershell
    .\instance_create.ps1 -name <instanceName> -port <portNumber> -version <versionNumber> 
    ```

    Скрипт `instance_create.ps1` поддерживает следующие ключи:

    - `name <instanceName>` — **обязательный** ключ с именем экземпляра ПО.
    - `port <portNumber>` — порт для экземпляра ПО, по умолчанию: 80 (необязательный ключ).
    - `version <versionNumber>` — развернуть ПО указанной версии вида `X.X.XXXX.X` (например: `5.0.1234.0`) из папки вида `C:\Program Files\Comindware\CBAP\<versionNumber>`.
    - `versionPath <versionPath>` — развернуть ПО из указанной папки `<versionPath>` с версией ПО.
    - `demoDB` — создать экземпляр ПО **{{ productName }}** c демонстрационной базой данных.
    - `fqdn <hostName>` — имя хоста для экземпляра ПО (необязательный ключ). По умолчанию: `localhost`.
    - `h` — вызвать справку по использованию скрипта (этот ключ следует указывать только без остальных ключей).

    !!! tip "Обязательные ключи для скриптов"

        Если не указать обязательный ключ для любого скрипта, он запросит его после запуска.

## Запуск экземпляра ПО {: #deploy_guide_windows_instance_start }

1. Перейдите в папку со скриптами для развёртывания ПО **{{ productName }}**:

    ``` powershell
    cd "X:\<distPath>\X.X-release-ru-<versionNumber>.windows\CMW_Windows<versionNumber>\scripts"
    ```

2. Запустите экземпляр ПО:

    ``` powershell
    .\instance_start.ps1 -name <instanceName>
    ```

    Здесь: `name <instanceName>` — **обязательный** ключ с именем экземпляра ПО.

## Остановка экземпляра ПО {: #deploy_guide_windows_instance_stop }

1. Перейдите в папку со скриптами для развёртывания ПО **{{ productName }}**:

    ``` powershell
    cd "X:\<distPath>\X.X-release-ru-<versionNumber>.windows\CMW_Windows<versionNumber>\scripts"
    ```

2. Остановите экземпляр ПО:

    ``` powershell
    .\instance_stop.ps1 -name <instanceName>
    ```

    Здесь: `-name <instanceName>` — **обязательный** ключ с именем экземпляра ПО.

## Инициализация {{ productName }} {: #instance_initialize}

{%
include-markdown "../linux/deploy_guide.md"
start="<!--initialize-start-->"
end="<!--initialize-end-->"
%}

## Подготовка экземпляра ПО к разработке приложений {: #deploy_guide_windows_instance_prepare .pageBreakBefore }

{%
include-markdown "../linux/deploy_guide.md"
start="<!--instance-prepare-start-->"
end="<!--instance-prepare-end-->"
%}

## Обновление экземпляра ПО {: #deploy_guide_windows_instance_upgrade }

1. Скачайте и установите ПО новой версии согласно инструкциям в параграфе _«[Установка {{ productName }}](#deploy_guide_windows_install_sw)»_.
2. Перейдите в папку со скриптами для развёртывания ПО **{{ productName }}**:

    ``` powershell
    cd "X:\<distPath>\X.X-release-ru-<versionNumber>.windows\CMW_Windows<versionNumber>\scripts"
    ```

3. Запустите обновление экземпляра ПО:

    ``` powershell
    .\instance_upgrade.ps1 -name <instanceName> -version <versionNumber> 
    ```

    Скрипт `instance_upgrade.ps1` поддерживает следующие ключи:

    - `name <instanceName>` — **обязательный** ключ с именем экземпляра ПО.
    - `version <versionNumber>` — обновить экземпляр ПО до указанной версии вида `X.X.XXXX.X` (например: `5.0.1234.0`) из папки вида `C:\Program Files\Comindware\CBAP\<versionNumber>`.
    - `versionPath <versionPath>` — обновить экземпляр ПО до версии из указанной папки `<versionPath>`.
    - `h` — вызвать справку по использованию скрипта (этот ключ следует указывать только без остальных ключей).

4. Просмотрите список установленных экземпляров ПО:

    ``` powershell
    .\instance_list.ps1
    ```

5. Рядом с именем экземпляра ПО отобразится номер версии.

## Удаление экземпляра ПО {: #deploy_guide_windows_instance_delete }

1. Перейдите в папку со скриптами для развёртывания ПО **{{ productName }}**:

    ``` powershell
    cd "X:\<distPath>\X.X-release-ru-<versionNumber>.windows\CMW_Windows<versionNumber>\scripts"
    ```

2. Удалите экземпляр ПО:

    ``` powershell
    .\instance_delete.ps1 -name <instanceName>
    ```

    Скрипт `instance_delete.ps1` поддерживает следующие ключи:

    - `name <instanceName>` — **обязательный** ключ с именем экземпляра ПО. Если не указать другие ключи, будет удалена только служба `comindware<instanceName>`.
    - `deleteData` — удалить базу данных из папки вида `C:\ProgramData\Comindware\Instances\<instanceName>\Data` и пользовательские файлы экземпляра ПО из папки вида `C:\ProgramData\Comindware\Instances\<instanceName>\Streams`. Без указания этого ключа или ключа `clear` база данных экземпляра ПО не будет удалена.
    - `clear` — удалить все файлы, папки, базу данных и пользовательские файлы вместе с папкой вида `C:\ProgramData\Comindware\Instances\<instanceName>`, а также службы экземпляра ПО, сайт и пул приложения из IIS.

## Удаление версии ПО {: #deploy_guide_windows_version_delete }

1. Перейдите в папку со скриптами для развёртывания ПО **{{ productName }}**:

    ``` powershell
    cd "X:\<distPath>\X.X-release-ru-<versionNumber>.windows\CMW_Windows<versionNumber>\scripts"
    ```

2. Просмотрите список установленных экземпляров ПО:

    ``` powershell
    .\instance_list.ps1
    ```

3. Удалите все экземпляры с версией ПО, которую требуется удалить, или обновите их до другой версии. Удалить версию ПО, которая используется в каких-либо экземплярах, не удастся. См. _«[Удаление экземпляра ПО](#deploy_guide_windows_instance_delete)»_.
4. Удалите версию ПО:

    ``` powershell
    .\version_delete.ps1 -version <versionNumber>
    ```

    Здесь: `-version <versionNumber>` — указать номер версии ПО вида `X.X.XXXX.X` (например: `5.0.1234.0`).

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- [Пути и содержимое директорий экземпляра ПО][paths]
- [Резервное копирование. Настройка, запуск и просмотр журнала сеансов][backup_configure]
- [Отправка почты из процесса. Настройка подключения][process_sending_connection]

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
