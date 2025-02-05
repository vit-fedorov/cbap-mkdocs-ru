---
title: Установка, запуск, инициализация и остановка Comindware Platform
kbId: 5063
---

# Установка, запуск, инициализация и остановка {{ productName }} {: #deploy_guide_windows}

## Введение

Для работы **{{ productName }}** требуются операционная система, сервер базы данных, веб-сервер, обратный прокси-сервер и сервер журналирования.

{%
include-markdown ".snippets/elasticsearch_opensearch_configure.md"
rewrite-relative-urls=false
%}

Для быстрого развёртывания **{{ productName }}** в Windows компания **{{ companyName }}** предоставляет дистрибутив с установщиком, настраивающим необходимое программное обеспечение.

Здесь представлены инструкции по развёртыванию и инициализации **{{ productName }}** из дистрибутива в ОС Windows.

## Требования к серверу

Перед установкой ПО убедитесь, что сервер соответствует следующим условиям:

- Сервер работает под управлением _Windows Server_.
- Сервер настраивается от имени пользователя с правами администратора.
- Установлена служба _IIS (Internet Information Services)_.

## Порядок установки ПО

1. Подготовьте сервер к установке ПО.
2. Установите и настройте необходимое вспомогательное ПО.
3. Установите ПО **{{ productName }}**.
4. Создайте экземпляр ПО.
5. Запустите экземпляр ПО.
6. Инициализируйте экземпляр ПО.

## Подготовка сервера к установке ПО

1. Откройте «**Диспетчер сервера**».
2. Добавьте сервер, на котором будет установлено ПО.
3. Чтобы запустить «**Мастер добавления ролей и компонентов**», выберите пункт «**Добавить роли и компоненты**» для данного сервера.
4. На шаге выбора **типа установки** укажите пункт «**Установка ролей или компонентов**».
5. На шаге **выбора сервера** укажите сервер, на котором будет установлено ПО.
6. На шаге **выбора ролей сервера** установите флажок «**Веб-сервер (IIS)**».
7. На шаге **выбора компонентов** для компонента «**Веб-сервер (IIS)**» — «**Веб-сервер**» — «**Разработка приложений**» установите следующие флажки:

    - **ASP.NET 4.8** (или выше);
    - **Расширяемость .NET 4.8** (или выше);
    - **Расширения ISAPI**;
    - **Фильтры ISAPI**.

8. На шаге **подтверждения** нажмите кнопку «**Установить**» и дождитесь завершения процесса.

## Установка вспомогательного ПО {: #deploy_guide_windows_install_prerequisites}

1. Скачайте и распакуйте архив с дистрибутивом вспомогательного ПО для **{{ productName }}**.
2. Запустите _PowerShell_ от имени администратора.
3. Установите неограниченную политику выполнения _PowerShell_:

    ``` powershell
    Set-ExecutionPolicy Unrestricted
    ```

4. В запросе на изменение политики выберите вариант «**Да для всех**», введя букву ++a++.
5. Перейдите в папку со скриптами для развёртывания вспомогательного ПО:

    ``` powershell
    cd "X:\<distPath>\X.X-release-ru-<versionNumber>.prerequisites.windows\CMW_Windows\scripts"
    ```

    Здесь: `X:\<distPath>\X.X-release-ru-<versionNumber>.prerequisites.windows` — путь к распакованному дистрибутиву вспомогательного ПО, а `<versionNumber>` — номер версии ПО.

6. Разблокируйте доступ к скачанным из Интернета установочным файлам:

    ``` powershell
    .\files_unblock.ps1
    ```

    !!! tip "Вызов справки для скриптов"

        Для ознакомления с ключами и назначением любого скрипта используйте ключ `-h` без каких-либо других ключей, например:

        ``` powershell
        .\files_unblock.ps1 -h
        ```

7. Установите необходимое вспомогательное ПО:

    ``` powershell
    .\prerequisites_install.ps1
    ```

8. Перезагрузите машину.
9.  Запустите _PowerShell_ от имени администратора.
10. Перейдите в папку со скриптами для развёртывания вспомогательного ПО:

    ``` powershell
    cd "X:\<distPath>\X.X-release-ru-<versionNumber>.prerequisites.windows\CMW_Windows\scripts"
    ```

11. Проверьте, что дополнительные компоненты установлены:

    ``` powershell
    .\prerequisites_list.ps1
    ```

    Если какие-либо дополнительные компоненты не были установлены, повторите шаги 8–12.

## Установка {{ productName }} {: #deploy_guide_windows_install_sw}

1. Скачайте и распакуйте архив с дистрибутивом **{{ productName }}**.
2. Запустите _PowerShell_ от имени администратора.
3. Установите неограниченную политику выполнения _PowerShell_:

    ``` powershell
    Set-ExecutionPolicy Unrestricted
    ```

4. В запросе на изменение политики выберите вариант «**Да для всех**», введя букву ++a++.
5. Перейдите в папку со скриптами для развёртывания ПО **{{ productName }}**:

    ``` powershell
    cd "X:\<distPath>\X.X-release-ru-<versionNumber>.windows\CMW_Windows\scripts"
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

## Создание экземпляра ПО

1. Перейдите в папку со скриптами для развёртывания ПО **{{ productName }}**:

    ``` powershell
    cd "X:\<distPath>\X.X-release-ru-<versionNumber>.windows\CMW_Windows\scripts"
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

## Запуск экземпляра ПО

1. Перейдите в папку со скриптами для развёртывания ПО **{{ productName }}**:

    ``` powershell
    cd "X:\<distPath>\X.X-release-ru-<versionNumber>.windows\CMW_Windows\scripts"
    ```

2. Запустите экземпляр ПО:

    ``` powershell
    .\instance_start.ps1 -name <instanceName>
    ```

    Здесь: `name <instanceName>` — **обязательный** ключ с именем экземпляра ПО.

## Остановка экземпляра ПО

1. Перейдите в папку со скриптами для развёртывания ПО **{{ productName }}**:

    ``` powershell
    cd "X:\<distPath>\X.X-release-ru-<versionNumber>.windows\CMW_Windows\scripts"
    ```

2. Остановите экземпляр ПО:

    ``` powershell
    .\instance_stop.ps1 -name <instanceName>
    ```

    Здесь: `-name <instanceName>` — **обязательный** ключ с именем экземпляра ПО.

## Инициализация {{ productName }} {: #initialize_instance}

{%
include-markdown "../linux/deploy_guide.md"
start="<!--initialize-start-->"
end="<!--initialize-end-->"
%}

## Обновление экземпляра ПО

1. Скачайте и установите ПО новой версии согласно инструкциям в параграфе _«[Установка {{ productName }}](#deploy_guide_windows_install_sw)»_.
2. Перейдите в папку со скриптами для развёртывания ПО **{{ productName }}**:

    ``` powershell
    cd "X:\<distPath>\X.X-release-ru-<versionNumber>.windows\CMW_Windows\scripts"
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

## Удаление экземпляра ПО

1. Перейдите в папку со скриптами для развёртывания ПО **{{ productName }}**:

    ``` powershell
    cd "X:\<distPath>\X.X-release-ru-<versionNumber>.windows\CMW_Windows\scripts"
    ```

2. Удалите экземпляр ПО:

    ``` powershell
    .\instance_delete.ps1 -name <instanceName>
    ```

    Скрипт `instance_delete.ps1` поддерживает следующие ключи:

    - `name <instanceName>` — **обязательный** ключ с именем экземпляра ПО. Если не указать другие ключи, будет удалена только служба `comindware<instanceName>`.
    - `deleteData` — удалить базу данных из папки вида `C:\ProgramData\Comindware\Instances\<instanceName>\Data` и пользовательские файлы экземпляра ПО из папки вида `C:\ProgramData\Comindware\Instances\<instanceName>\Streams`. Без указания этого ключа или ключа `clear` база данных экземпляра ПО не будет удалена.
    - `clear` — удалить все файлы, папки, базу данных и пользовательские файлы вместе с папкой вида `C:\ProgramData\Comindware\Instances\<instanceName>`, а также службы экземпляра ПО, сайт и пул приложения из IIS.

## Удаление версии ПО

1. Перейдите в папку со скриптами для развёртывания ПО **{{ productName }}**:

    ``` powershell
    cd "X:\<distPath>\X.X-release-ru-<versionNumber>.windows\CMW_Windows\scripts"
    ```

2. Просмотрите список установленных экземпляров ПО:

    ``` powershell
    .\instance_list.ps1
    ```

3. Удалите все экземпляры с версией ПО, которую требуется удалить, или обновите их до другой версии. Удалить версию ПО, которая используется в каких-либо экземплярах, не удастся. См. _«[Удаление экземпляра ПО](#удаление-экземпляра-по)»_.
4. Удалите версию ПО:

    ``` powershell
    .\version_delete.ps1 -version <versionNumber>
    ```

    Здесь: `-version <versionNumber>` — указать номер версии ПО вида `X.X.XXXX.X` (например: `5.0.1234.0`).

<div class="relatedTopics" markdown="block">

--8<-- "related_topics_heading.md"

- _[Пути и содержимое директорий экземпляра ПО][paths]_

</div>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
