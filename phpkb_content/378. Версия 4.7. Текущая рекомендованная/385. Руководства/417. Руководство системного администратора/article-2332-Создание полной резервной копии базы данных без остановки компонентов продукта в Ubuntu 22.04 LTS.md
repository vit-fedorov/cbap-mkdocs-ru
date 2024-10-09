---
title: Создание полной резервной копии базы данных без остановки компонентов продукта в Ubuntu 22.04 LTS
kbId: 2332
---

# Создание полной резервной копии базы данных без остановки компонентов продукта в Ubuntu 22.04 LTS

## Введение

В этой статье представлены инструкции по созданию резервной копии базы данных экземпляра ПО **Comindware Business Application Platform** версии 4.3.0.203, развёрнутого в среде Ubuntu 22.04 LTS.

Для создания полной резервной копии базы данных в ОС Linux необходимо с помощью терминала выполнить следующие действия:

- создать снимки состояния памяти Apache Ignite и Elasticsearch;
- скопировать содержимое папок со скриптами и вложенными файлами.

Сведения о восстановлении данных см. в статье «**[Полное восстановление базы данных, вложенных файлов и журналов из резервной копии в Ubuntu 22.04 LTS](https://kb.comindware.ru/article.php?id=2335)**».

## Определения

- ***ПО*** — программное обеспечение **Comindware Business Application Platform**.
- ***Экземпляр ПО*** — установленный веб-сайт на основе ПО.
- ***База данных экземпляра ПО*** — набор папок и файлов, содержащий все данные и конфигурацию экземпляра ПО.
- ***Система*** — развёрнутый программно-аппаратный комплекс на основе ПО.

## 1. Сбор данных об экземпляре ПО

Для создания резервной копии соберите перечисленные ниже данные об экземпляре ПО.

1.1. `InstanceName` — имя экземпляра ПО, можно получить в ответе на запрос `localhost:9200/_cat/indices`, например `cmw_cmw-study`.

_![Определение имени экземпляра ПО](https://kb.comindware.ru/assets/Pasted image 20221229181253.png)_

1.2. Папка с базой данных экземпляра ПО. По умолчанию используется папка `/var/www/comindware/data/Database/`. Но может быть задан другой путь с помощью директивы `<workDirectory>` в файле конфигурации `/var/www/comindware/Ignite.config`. Если в файле конфигурации директива `<workDirectory>` не содержит пути, используется путь по умолчанию.

1.3. Путь для сохранения снимков базы данных Apache Ignite, по умолчанию: `/var/www/comindware/data/Database/snapshots/`

1.4 `elastic_search_repo_name` — имя репозитория Elasticsearch, заданное при его регистрации.

1.5. Путь для сохранения резервных копий Elasticsearch. Должен быть указан в директиве `path.repo:` в файле `/etc/elasticsearch/elasticsearch.yml`, например `/var/www/backups/elasticsearch`

_![Определение пути для резервных копий Elasticsearch](https://kb.comindware.ru/assets/Pasted image 20221229181640.png)_

1.6. `snapshot_name` — выбранное пользователем имя снимка, лучше в формате `<InstanceName><Date><Time>`

## 2. Установка и настройка исполняемых скриптов Apache Ignite

2.1. Для установки исполняемых скриптов перейдите в режим суперпользователя `root`:

```
sudo -i 
```

2.2. Проверьте наличие пакета `apache-ignite` на машине:

```
dpkg -s apache-ignite 
```

Если пакет имеется, пропустите шаги 2.3–2.7.

2.3. Если пакета нет, загрузите zip-архив со скриптами:

```
wget -P /tmp/ https://archive.apache.org/dist/ignite/2.14.0/apache-ignite-2.14.0-bin.zip 
```

2.4. Если на машине ранее не был установлен пакет `zip`, установите его:

```
apt install zip 
```

2.5. Разархивируйте пакет в папку `/var/www/`:

```
unzip /tmp/apache-ignite-2.14.0-bin.zip -d /var/www 
```

2.6. Переименуйте получившуюся папку со скриптами `Apache Ignite` в `apache-ignite`:

```
mv /var/www/apache-ignite-2.14.0-bin /var/www/apache-ignite 
```

2.7. Прейдите в папку `/var/www/`:

```
cd /var/www/ 
```

2.8. Назначьте папке `apache-ignite` права на чтение-запись `rwxrwxrwx`:

```
chmod -R 777 apache-ignite/ 
```

2.9. Смените владельца папки `apache-ignite` на `www-data`:

```
chown -R www-data:www-data apache-ignite/ 
```

_![Смена владельца папки apache-ignite](https://kb.comindware.ru/assets/Pasted image 20221226120157.png)_

2.10. Создайте папки для сохранения резервных копий:

```
mkdir /var/www/backups/ 
```

2.11. Создайте папку репозитория Elasticsearch:

```
mkdir /var/www/backups/elasticsearch 
```

2.12. Присвойте папке `backups` права на чтение-запись `rwxrwxrwx`:

```
chmod -R 777 backups/ 
```

2.13. Смените владельца папки `backups` на `www-data`:

```
chown -R www-data:www-data backups/ 
```

## 3. Создание резервной копии

При создании снимка после перезагрузки машины необходимо убедиться в том, что экземпляр ПО запущен и Apache Ignite работает. Для этого достаточно в браузере открыть веб-сайт с экземпляром ПО.

3.1. Задайте переменную `now`:

```
now=$(date  %Y_%m_%d_%H_%M) 
```

3.2. Проверьте окружение и сделайте снимок состояния Apache Ignite:

```
bash /var/www/apache-ignite/bin/control.sh —baseline bash /var/www/apache-ignite/bin/control.sh —snapshot create snapshot_$now 
```

3.3. Зарегистрируйте репозиторий Elasticsearch. Вместо `elastic_search_repo_name` и `/var/www/backups/elasticsearch` подставьте своё имя репозитория и путь к его папке:

```
curl -X PUT "localhost:9200/_snapshot/elastic_search_repo_name?pretty" -H 'Content-Type: application/json' -d' {"type": "fs", "settings": {"location": "/var/www/backups/elasticsearch"}}' 
```

3.4. Сделайте снимок состояния Elasticsearch, заменив `elastic_search_repo_name`, `snapshot-$now` и `InstanceName` на свои значения:

```
curl -X PUT "localhost:9200/_snapshot/elastic_search_repo_name/snapshot-$now?wait_for_completion=true&pretty" -H 'Content-Type: application/json' -d' {"indices": "InstanceName*", "ignore_unavailable": true, "include_global_state": false}' 
```

3.5. Создайте папки для хранения компонентов резервной копии:

```
mkdir /var/www/backups/backup_$now mkdir /var/www/backups/backup_$now/Database mkdir /var/www/backups/backup_$now/elastic mkdir /var/www/backups/backup_$now/Streams mkdir /var/www/backups/backup_$now/Scripts mkdir /var/www/backups/backup_$now/wal 
```

3.6. Перенесите и скопируйте компоненты в папку резервной копии:

```
mv /var/www/comindware/data/Database/snapshots/snapshot_$now /var/www/backups/backup_$now/Database cp -r /var/www/backups/elasticsearch/* /var/www/backups/backup_$now/elastic cp -r /var/www/comindware/data/Database/wal/* /var/www/backups/backup_$now/wal cp -r /var/www/comindware/data/Database/Scripts/* /var/www/backups/backup_$now/Scripts cp -r /var/www/comindware/data/Streams/* /var/www/backups/backup_$now/Streams 
```

3.7. Создайте архив с резервной копией:

```
tar -cvjf backup_$now.tar.bz2 /var/www/backups/backup_$now 
```

3.8. Перенесите архив с резервной копией во внешнее хранилище.



 
{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
