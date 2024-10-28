---
title: Восстановление базы данных из файла резервной копии в формате .CDBBZ
kbId: 2500
---

# Восстановление базы данных из файла резервной копии в формате .CDBBZ {: #backup_restore_cdbbz}

## Введение

В данном разделе представлены инструкции по восстановлению на чистом экземпляре ПО **{{ productName }}** (далее — ПО, экземпляр ПО) под управлением ОС Linux  базы данных из файла резервной копии с расширением `.CDBBZ`  , созданного с помощью встроенной в ПО функции «**Резервное копирование** ». См. *«[Резервное копирование. Настройка и запуск, просмотр журнала сеансов][backup]**»**.* 

См. также инструкции по полному резервному копированию и восстановлению базы данных внешними средствами:

- *[Создание полной резервной копии (базы данных, вложенных файлов и журналов) без остановки экземпляра ПО][complete_running_instance_backup]*
- *[Восстановление базы данных, вложенных файлов и журналов из полной резервной копии][restore_complete_backup]*

## Восстановление базы данных и скриптов

1. Перейдите в режим суперпользователя:

    ```
    su -
    ```

    или

    ```
    sudo -i
    ```

2. Разверните чистый экземпляр ПО {{ productName }} *без демонстрационной базы данных* (с параметром `-d=clear`). См. «[**Развертывание {{ productName }}**](https://kb.comindware.ru/category.php?id=491)». Например:

    ``` shell
    sh install.sh -k -p [-i=<instanceName>] [-e] -d=clear [-u=www-data] [-g=www-data]
    ```

    Скрипт `install.sh` поддерживает следующие ключи:

        - `k` — установить ПО Kafka;
        - `e` — установить ПО {{ productName }}
        - `p` — установить ПО Comindware Bus{{ productName }}
        - `d=clear` *— создать экземпляр П{{ productName }}rm без демонстрационной базы данных;*
        - `d=demo` — создать экземпляр ПО Comindware Business Application Platform c демонстрационной базой данных (не обязательный ключ по умолчанию);
        - `u` — пользователь (необязательный ключ);
        - `g` — группа (необязательный ключ);
        - `h` — вызов краткой справки по использованию скрипта (этот ключ следует указывать без остальных ключей);
        - `kh=hostname` — использовать указанный хост для подключения к ПО Kafka (необязательный ключ);
        - `kp=portnumber` — использовать указанный порт для подключения к ПО Kafka (необязательный ключ);
        - `i=<instanceName>` — создать экземпляр ПО с указанным именем (необязательный ключ). Имя экземпляра п{{ productName }}
3. Инициализируйте экземпляр ПО. См. *«[Развертывание](https://kb.comindware.ru/category.php?id=491)*[*Comindware Business Application Platform*](https://kb.comindware.ru/category.php?id=491)*»*.
4. Остановите сервисы NGINX и comindware`<instanceName>` (где `<instanceName>` — имя экземпляра ПО) и удостоверьтесь, что они остановлены:

    ```
    systemctl stop nginx comindware<instanceName>   
    systemctl status nginx comindware<instanceName>
    ```

<a id="unpack_backup"></a>
5. Распакуйте архив резервной копии в каталог `/var/lib/comindware/<instanceName>/`:

```
unzip /tmp/BackupFileName.202302161625.cdbbz -d /var/lib/comindware/<instanceName>/
```
6. Если в папке резервной копии (`/var/lib/comindware/<instanceName>/`) имеется каталог `Ignite`, переименуйте его в `Database`:

    ```
    cd /var/lib/comindware/<instanceName>/   
    mv Ignite Database
    ```

7. Перенесите каталог `Scripts` резервной копии в каталог `Database`:

    ```
    mv Scripts /var/lib/comindware/<instanceName>/Database/
    ```

8. Назначьте перенесённым каталогам права `rwxrw-rw-`:

    ```
    chmod -R 766 /var/lib/comindware/<instanceName>
    ```

9. Назначьте перенесенным каталогам владельца:

    **Astra Linux, Ubuntu, Rocky**

    ```
    chown -R www-data:www-data /var/lib/comindware/<instanceName>
    ```

    **Альт Сервер**

    ```
    chown -R _nginx:_nginx /var/lib/comindware/<instanceName>
    ```

## Восстановление индексов Elasticsearch из файла резервной копии репозитория

1. Остановите службу Elasticsearch и удостоверьтесь, что она остановлена:

	```
	systemctl stop elasticsearch   
	systemctl status elasticsearch
	```

2. Создайте папку репозитория Elasticsearch (например, `/var/www/backups/elasticsearch/`) и перенесите в неё файлы из каталога `History` ранее [распакованной резервной копии](#unpack_backup):

	```
	mkdir /var/www/backups/elasticsearch/   
	mv /var/lib/comindware/<instanceName>/History/* /var/www/backups/elasticsearch/
	```

3. Назначьте папке репозитория и её содержимому права `rwxr-xr-x`:

	```
	chmod -R 755 /var/www/backups/ 
	```

4. Назначьте владельца `elasticsearch` папке репозитория и её содержимому:

	```
	chown -R elasticsearch:elasticsearch /var/www/backups/ 
	```

5. В файле конфигурации `/etc/elasticsearch/elasticsearch.yml` укажите путь к созданному репозиторию:

	```
	path.repo: /var/www/backups/elasticsearch
	```

6. Запустите службу Elasticsearch:

	```
	systemctl start elasticsearch.service 
	```

7. Зарегистрируйте репозиторий (например, `repostory_backup`) с резервной копией снимка Elasticsearch:

	```
	curl -X PUT "localhost:9200/_snapshot/repostory_backup?pretty" -H ’Content-Type: application/json’ -d’  
	{  
	"type": "fs",  
	"settings": {  
				"location": "/var/www/backups/elasticsearch"  
				}  
	}  

	```

	<a id="s3_repository"></a>
	!!! note "Примечание"

		Шаги 7 и 8 не требуются при восстановлении снимка из хранилища S3.

		Для восстановления снимка из хранилища S3 используйте репозиторий с именем, совпадающим с префиксом индекса Elasticsearch.

		Этот репозиторий создаётся автоматически при запуске резервного копирования

		Префикс индекса задаётся в [свойствах подключения к Elasticsearch][elasticsearch_connection], используемого по умолчанию.

8. Проверьте содержимое зарегистрированного репозитория:

	```
	curl -X GET "localhost:9200/_cat/snapshots/repostory_backup?pretty"
	```

9. Восстановите снимок Elasticsearch:

	```
	curl -X POST "localhost:9200/_snapshot/repostory_backup/backupSession123/_restore?pretty" 
	```

    - В качестве репозитория укажите имя репозитория, созданного на шаге 7, или префикс индекса Elasticsearch (см. [примечание](#s3_repository) выше).
    - В качестве имени снимка укажите идентификатор резервной копии **без точки перед номером** (например, `backupSession``.123` указывайте как `backupSession``123`) со страницы [«Администрирование» – «Инфраструктура» – «Резервное копирование» – «Журнал»]({{ kbArticleURLPrefix }}2190#mcetoc_1gjrihkcn1):

10. Проверьте наличие индексов в восстановленном каталоге:

	```
	curl -X GET "localhost:9200/_cat/indices?pretty"
	```

## Запуск и проверка конфигурации экземпляра ПО

1. Запустите необходимые службы и проверьте их статус:

	```
	systemctl start nginx comindware<instanceName>   
	systemctl status nginx comindware<instanceName>
	```

2. Откройте веб-сайт экземпляра ПО.
3. Дождитесь инициализации экземпляра ПО. Этот процесс может занять некоторое время. Может потребоваться обновить страницу браузера.
4. Удостоверьтесь, что все данные из резервной копии восстановлены.
5. Проверьте и исправьте конфигурацию экземпляра. См. *«[Проверка и настройка конфигурации экземпляра ПО {{ productName }} после восстановления из резервной копии][restore_test_configure]».*

--8<-- "related_topics_heading.md"

**[Создание полной резервной копии (базы данных, вложенных файлов и журналов) без остановки экземпляра ПО][complete_running_instance_backup]**

**[Восстановление базы данных, вложенных файлов и журналов из полной резервной копии][restore_complete_backup]**

**[Резервное копирование. Настройка и запуск, просмотр журнала сеансов][backup]**

**[Установка и запуск {{ productName }}][deploy_guide]**

**[Регистрация репозитория Elasticsearch (официальное руководство, английский язык)](https://www.elastic.co/guide/en/elasticsearch/reference/current/snapshots-filesystem-repository.html)**

**[Восстановление снимка Elasticsearch (официальное руководство, английский язык)](https://www.elastic.co/guide/en/elasticsearch/reference/current/restore-snapshot-api.html)**

**[Elasticsearch. Настройка подключения][elasticsearch_connection]**

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
