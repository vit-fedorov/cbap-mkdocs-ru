---
title: Установка, запуск, инициализация и остановка ПО
kbId:
---

# Установка, запуск, инициализация и остановка ПО {: #deploy_guide_windows}

## Введение

Для работы **{{ productName }}** требуются операционная система, сервер базы данных, веб-сервер, обратный прокси-сервер и сервер журналирования.

Для быстрого развертывания **{{ productName }}** в Windows компания **{{ companyName }}** предоставляет дистрибутив с установщиком, настраивающим необходимое программное обеспечение.

Здесь представлены инструкции по развёртыванию и инициализации **{{ productName }}** из дистрибутива в ОС Windows.

## Установка {{ productName }} {: #deploy_guide_windows_install_sw}

1. Скачайте и распакуйте архив с дистрибутивом **{{ productName }}**.
2. Запустите _PowerShell_ от имени администратора.
3. Установите неограниченную политику выполнения _PowerShell_:

    ``` sh
    Set-ExecutionPolicy Unrestricted
    ```

4. В запросе на изменение политики выберите вариант «**Да для всех**», введя букву ++a++.
5. Перейдите в папку со скриптами для развёртывания ПО:

    ``` sh
    cd "X:\<path>\X.X-release-ru-X.X.XXXX.X.windows\CMW_Windows\scripts\platform"
    ```

    Здесь: `X:\<path>\X.X-release-ru-X.X.XXXX.X.windows` — путь к распакованному дистрибутиву продукта, а `X.X.XXXX.X` — номер версии ПО.

6. Разблокируйте доступ к скачанным из Интернета установочным файлам:

    ``` sh
    .\files_unblock.ps1
    ```

    !!! tip "Вызов справки для скриптов"

        Для ознакомления с ключами и назначением любого скрипта используйте ключ `-h` без каких-либо других ключей, например:

        ``` sh
        .\files_unblock.ps1 -h
        ```

7. Перейдите в папку со скриптами для развёртывания вспомогательного ПО:

    ``` sh
    cd "X:\<path>\X.X-release-ru-X.X.XXXX.X.windows\CMW_Windows\scripts\prerequisites"
    ```

8. Установите необходимое вспомогательное ПО:

    ``` sh
    .\prerequisites_install.ps1
    ```

9. Перезагрузите машину.
10. Запустите _PowerShell_ от имени администратора.
11. Перейдите в папку со скриптами для развёртывания вспомогательного ПО:

    ``` sh
    cd "X:\<path>\X.X-release-ru-X.X.XXXX.X.windows\CMW_Windows\scripts\prerequisites"
    ```

12. Проверьте, что дополнительные компоненты установлены:

    ``` sh
    .\prerequisites_list.ps1
    ```

    Если какие-либо дополнительные компоненты не были установлены, повторите шаги 8–12.

13. Перейдите в папку со скриптами для развёртывания ПО **{{ productName }}**:

    ``` sh
    cd "X:\<path>\X.X-release-ru-X.X.XXXX.X.windows\CMW_Windows\scripts\platform"
    ```

14. Установите ПО:

    ``` sh
    .\version_install.ps1
    ```

15. Удостоверьтесь, что ПО установлено, вызывав список установленных версий ПО:

    ``` sh
    .\version_list.ps1
    ```

## Создание экземпляра ПО

1. Перейдите в папку со скриптами для развёртывания ПО **{{ productName }}**:

    ``` sh
    cd "X:\<path>\X.X-release-ru-X.X.XXXX.X.windows\CMW_Windows\scripts\platform"
    ```

2. Разверните экземпляр ПО:

    ``` sh
    .\instance_create.ps1 -name <instanceName> -port <portNumber> -version <versionNumber> 
    ```

    Скрипт `instance_create.ps1` поддерживает следующие ключи:

    - `name <instanceName>` — **обязательный** ключ с именем экземпляра ПО.
    - `port <portNumber>` — порт для экземпляра ПО, по умолчанию: 80 (необязательный ключ).
    - `version <versionNumber>` — развернуть  указанной версии вида `X.X.XXXX.X` (например: `5.0.1234.0`) из папки вида `C:\Program Files\Comindware\CBAP\<versionNumber>`.
    - `versionPath <versionPath>` — развернуть ПО из указанной папки `<versionPath>` с версией ПО.
    - `demoDB` — создать экземпляр ПО **{{ productName }}** c демонстрационной базой данных.
    - `fqdn <hostName>` — имя хоста для экземпляра ПО (необязательный ключ). По умолчанию: `localhost`.
    - `h` — вызвать справку по использованию скрипта (этот ключ следует указывать только без остальных ключей).

    !!! tip "Обязательные ключи для скриптов"

        Если не указать обязательный ключ для любого скрипта, он запросит его после запуска.

## Запуск экземпляра ПО

1. Перейдите в папку со скриптами для развёртывания ПО **{{ productName }}**:

    ``` sh
    cd "X:\<path>\X.X-release-ru-X.X.XXXX.X.windows\CMW_Windows\scripts\platform"
    ```

2. Запустите экземпляр ПО:

    ``` sh
    .\instance_start.ps1 -name <instanceName>
    ```

    Здесь: `name <instanceName>` — **обязательный** ключ с именем экземпляра ПО.

## Остановка экземпляра ПО

1. Перейдите в папку со скриптами для развёртывания ПО **{{ productName }}**:

    ``` sh
    cd "X:\<path>\X.X-release-ru-X.X.XXXX.X.windows\CMW_Windows\scripts\platform"
    ```

2. Остановите экземпляр ПО:

    ``` sh
    .\instance_stop.ps1 -name <instanceName>
    ```

    Здесь: `-name <instanceName>` — **обязательный** ключ с именем экземпляра ПО.

## Инициализация {{ productName }}

{%
include-markdown "../linux/deploy_guide.md"
start="<!--initializate-start-->"
end="<!--initializate-end-->"
%}

## Обновление экземпляра ПО

1. Скачайте и установите ПО новой версии согласно инструкциям в параграфе _«[Установка {{ productName }}](#deploy_guide_windows_install_sw)»_.
2. Перейдите в папку со скриптами для развёртывания ПО **{{ productName }}**:

    ``` sh
    cd "X:\<path>\X.X-release-ru-X.X.XXXX.X.windows\CMW_Windows\scripts\platform"
    ```

3. Запустите обновление экземпляра ПО:

    ``` sh
    .\instance_upgrade.ps1 -name <instanceName> -version <versionNumber> 
    ```

    Скрипт `instance_upgrade.ps1` поддерживает следующие ключи:

    - `name <instanceName>` — **обязательный** ключ с именем экземпляра ПО.
    - `version <versionNumber>` — обновить экземпляр ПО до указанной версии вида `X.X.XXXX.X` (например: `5.0.1234.0`) из папки вида `C:\Program Files\Comindware\CBAP\<versionNumber>`.
    - `versionPath <versionPath>` — обновить экземпляр ПО до версии из указанной папки `<versionPath>`.
    - `h` — вызвать справку по использованию скрипта (этот ключ следует указывать только без остальных ключей).

4. Просмотрите список установленных экземпляров ПО:

    ``` sh
    .\instance_list.ps1
    ```

5. Рядом с именем экземпляра ПО отобразится номер версии.

## Удаление экземпляра ПО

1. Перейдите в папку со скриптами для развёртывания ПО **{{ productName }}**:

    ``` sh
    cd "X:\<path>\X.X-release-ru-X.X.XXXX.X.windows\CMW_Windows\scripts\platform"
    ```

2. Удалите экземпляр ПО:

    ``` sh
    .\instance_delete.ps1 -name <instanceName>
    ```

    Скрипт `instance_delete.ps1` поддерживает следующие ключи:

    - `name <instanceName>` — **обязательный** ключ с именем экземпляра ПО. Если не указать другие ключи, будет удалена только служба `comindware<instanceName>`.
    - `deleteData` — удалить базу данных экземпляра ПО. Без указания этого ключа или ключа `clear` база данных экземпляра ПО не удаляется.
    - `clear` — удалить все файлы, папки, базу данных и службы экземпляра ПО.

## Удаление версии ПО

1. Перейдите в папку со скриптами для развёртывания ПО **{{ productName }}**:

    ``` sh
    cd "X:\<path>\X.X-release-ru-X.X.XXXX.X.windows\CMW_Windows\scripts\platform"
    ```

2. Просмотрите список установленных экземпляров ПО:

    ``` sh
    .\instance_list.ps1
    ```

3. Удалите все экземпляры с версией ПО, которую требуется удалить, или обновите их до другой версии. Удалить версию ПО, которая используется в каких-либо экземплярах, не удастся. См. «**[Удаление экземпляра ПО](#удаление-экземпляра-по)**».
4. Удалите версию ПО:

    ``` sh
    .\version_delete.ps1 -version <versionNumber>
    ```

    Здесь: `-version <versionNumber>` — указать номер версии ПО вида `X.X.XXXX.X` (например: `5.0.1234.0`).

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
