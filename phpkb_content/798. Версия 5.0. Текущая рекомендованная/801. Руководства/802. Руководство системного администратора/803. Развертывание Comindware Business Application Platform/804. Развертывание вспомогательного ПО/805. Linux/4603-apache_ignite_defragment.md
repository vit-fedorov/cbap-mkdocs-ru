---
title: Дефрагментация данных Apache Ignite
kbId: 4603
---

# Дефрагментация данных Apache Ignite

В данной статье представлены инструкции по дефрагментации хранилища данных Apache Ignite для ПО Comindware Business Application (далее «ПО») под управлением операционных систем семейства Linux. Дефрагментация хранилища Apache Ignite позволяет повысить производительность работы ПО и сократить объем данных хранилища на диске.

Внимание!

Во время дефрагментации хранилища Apache Ignite экземпляр ПО будет недоступен. Поэтому дефрагментацию следует выполнять в нерабочее время.

1. Создайте резервную копию базы данных экземпляра ПО.
2. Скачайте бинарный дистрибутив Apache Ignite, например [apache-ignite-2.16.0-bin.zip](https://downloads.apache.org/ignite/2.16.0/apache-ignite-2.16.0-bin.zip) или более новую версию.
3. Перейдите в режим суперпользователя:

```
su -
```

или

```
sudo -i
```

4. Распакуйте дистрибутив Apache Ignite в домашнюю папку (здесь и далее `username` — имя текущего пользователя):

```
unzip apache-ignite-2.16.0-bin.zip -d /home/username/ignite
```

5. Задайте переменную среды `IGNITE_HOME`:

```
export IGNITE_HOME=/home/username/ignite
```

6. Скопируйте в папку `/home/username/ignite` файл `Ignite.config` из папки `/var/www/instancename` (где `instancename` — имя экземпляра ПО):

```
cp /var/www/instancename/Ignite.config /home/username/ignite/
```

7. Перейдите в папку `bin` Apache Ignite:

```
cd /home/username/ignite/bin
```

8. В файле `control.sh` измените директиву `DEFAULT_CONFIG`:

```
DEFAULT_CONFIG=config/Ignite.config
```

9. Получите список узлов, зарегистрированных в базовой топологии:

```
sh control.sh --baseline
```

10. Назначьте дефрагментацию данных Apache Ignite при перезапуске экземпляра ПО, указав вместо `<id>` идентификаторы узлов, полученные на шаге 9:

```
sh control.sh --defragmentation schedule --nodes <id>
```

11. Деактивируйте кластер Apache Ignite:

```
sh control.sh --set-state INACTIVE --force
```

12. Остановите и запустите экземпляр ПО:

```
systemctl stop comindwareinstancename
systemctl start comindwareinstancename

```

Здесь `instancename` — имя экземпляра ПО.

13. Дождитесь завершения дефрагментации данных. В процессе дефрагментации Apache Ignite будет вносить сведения в файл журнала вида `/var/lib/comindware/instancename/Database/log/ignite-xxxxxxxx.0.log`. Признаком окончания дефрагментации служит появление в журнале Apache Ignite события: `Defragmentation process complete`.
14. Перезапустите экземпляр ПО, чтобы его снова можно было использовать.

```
systemctl restart comindwareinstancename
```

## Решение возможных проблем

Если во время дефрагментации возникнет ошибка «Слишком много открытых файлов» (Too many open files), выполните указанные ниже шаги (пример для Astra Linux).

1. Добавьте в файл `/etc/security/limits.conf` строки:

```
* soft nproc 65535
* hard nproc 65535
* soft nofile 65535
* hard nofile 65535
www-data soft nproc 200000
www-data hard nproc 200000
www-data soft nofile 200000
www-data hard nofile 200000
```
2. Добавьте в файл `/etc/pam.d/common-session` строку:

```
session required pam_limits.so
```
3. Добавьте в файл `/etc/sysctl.conf` строку:

```
fs.file-max = 2097152
```
4. Раскомментируйте строку и задайте значение в файле `/etc/systemd/user.conf`:

```
DefaultLimitNOFILE=65536
```
5. Раскомментируйте строку и задайте значение в файле `/etc/systemd/system.conf`:

```
DefaultLimitNOFILE=65536
```
6. Откройте для редактирования конфигурацию сервиса экземпляра ПО: 

```
systemctl edit comindwareinstancename.service
```
7. Добавьте в него строки:

```
[Service]
LimitNOFILE=65536
LimitNOFILESoft=65536
```
8. Перезагрузите машину и экземпляр ПО.

--8<-- "related_topics_heading.md"

**[Руководство системного администратора. Резервное копирование и восстановление в ОС Linux](https://kb.comindware.ru/category.php?id=812)**
**[Руководство пользователя. Резервное копирование](https://kb.comindware.ru/category.php?id=436)**
**[Дефрагментация персистентного хранилища](https://ignite.apache.org/docs/2.11.1/persistence/native-persistence-defragmentation)** (руководство Apache Ignite, английский язык))
**[Активация, деактивация и управление топологией](https://ignite.apache.org/docs/2.11.1/tools/control-script#activation-deactivation-and-topology-management)** (руководство Apache Ignite, английский язык)

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
