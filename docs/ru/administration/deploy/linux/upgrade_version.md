---
title: Обновление версии экземпляра ПО
kbId: 2499
---

# Обновление версии экземпляра ПО

## Введение

В данной статье представлены краткие инструкции по обновлению до 4.7.2285 версии экземпляра ПО **{{ productName }}** (далее — ПО, экземпляр ПО) под управлением ОС Альт Сервер, Astra Linux, РЕД ОС, Rocky Linux и Ubuntu.

## Обновление версии ПО

1. Создайте и перенесите во внешнее хранилище резервную копию базы данных экземпляра ПО. См. статью *«[Резервное копирование. Настройка и запуск, просмотр журнала сеансов](https://kb.comindware.ru/article.php?id=2190)»*.
2. Перейдите в режим суперпользователя:


```
sudo -i
```


или


```
su -
```
3. Остановите экземпляр ПО и его вспомогательные службы и удостоверьтесь, что они остановлены:


```
systemctl stop apigateway<instanceName> comindware<instanceName>  
systemctl status apigateway<instanceName> comindware<instanceName> 
```

Здесь *`<instanceName>`*— имя экземпляра ПО.
4. Проверьте, выполняется ли сервис `Comindware.Adapter.Agent.exe`:


```
ps fax | grep Agent
```

	- Если процесс `Comindware.Adapter.Agent.exe`, выполняется, завершите его по `PID`:

	
	```
	kill -9 <PID>
	```
5. Удалите (или переместите в резервное хранилище) неиспользуемые предыдущие дистрибутивы ПО:


```
rm -rf CMW_Alt
```


или


```
rm -rf CMW_Astra
```


или   

```
rm -rf CMW_Redos
```


или   

```
rm -rf CMW_Rocky
```


или


```
rm -rf CMW_Ubuntu_22.04
```
6. Скачайте и распакуйте дистрибутив с новой версией ПО (`X.X.XXX.X` — номер версии ПО):


```
tar -xf X.X.XXX.X.alt.tar.gz
```

или


```
tar -xf X.X.XXX.X.astra.tar.gz
```

или

```
tar -xf X.X.XXX.X.redos.tar.gz
```

или

```
tar -xf X.X.XXX.X.rocky.tar.gz
```

или

```
tar -xf X.X.XXX.X.ubuntu.tar.gz
```
7. Перейдите в распакованную папку:


```
cd CMW_Alt/scripts/cbap
```

или


```
cd CMW_Astra/scripts/cbap
```

или

```
cd CMW_Rocky/scripts/cbap
```

или

```
cd CMW_Redos/scripts/cbap
```

или

```
cd CMW_Ubuntu22.04/scripts/cbap
```
8. Если используется нестандартная конфигурация NGINX для экземпляра ПО, cохраните её резервную копию:   

```
cp /etc/nginx/sites-available/comindware<instanceName> $HOME            
```


или   

```
cp /etc/nginx/conf.d/comindware<instanceName> $HOME        
```
9. 
10. Проверьте имя и статус экземпляра:   

```
systemctl status comindware*
```
11. Запустите установку распакованного дистрибутива ПО:


```
bash install.sh        
```
12. Проверьте наличие и имя директории установленной версии ПО:   

```
ls /var/www/.cmw_version/
```
13. Перейдите в директорию скриптов для работы с экземпляром ПО и запустите его обновление до требуемой версии:


```
cd ../instance/   
bash upgrade.sh -n=<instanceName> -vp=/var/www/.cmw_version/X.X.XXX.X
```

Здесь:

	- `X.X.XXX.X` — номер устанавливаемой версии ПО;
	- `<instanceName>` — имя обновляемого экземпляра ПО.
14. Проверьте корректность конфигурации NGINX для экземпляра ПО:   

```
cat /etc/nginx/sites-available/comindware<instanceName>
```

	- При необходимости восстановите конфигурацию NGINX, [сохранённую ранее](#NginxBackup).
15. Откройте для редактирования файл конфигурации `/var/www/<instanceName>/apigateway.json`.

	- Замените в конфигурации адрес сервера Kafka:

	
	```
	"Kafka": {  
	    "BootstrapServer": "<KAFKAIP>:9092",  
	    "GroupId": "<instanceName>"  
	}  
	
	```
16. Если выполняется обновление с версии ниже 4.6.1140.0, откройте для редактирования файл конфигурации экземпляра ПО `/usr/share/comindware/configs/instance/<instanceName>.yml`.
	- Замените в конфигурации следующие директивы:

	
	```
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

	
	```
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
17. Перезапустите сервисы, настройки которых были изменены:


```
systemctl restart apigateway<instanceName> comindware<instanceName>
```

	- Проверьте конфигурацию NGINX:

	
	```
	nginx -t
	```
	- Если тест пройден, перезапустите NGINX:

	
	```
	nginx -s reload                
	```
18. 
19. Откройте сайт экземпляра ПО в браузере, дождитесь окончания загрузки, одновременно открыв выдачу журналов экземпляра в терминале:   

```
tail -f /var/log/comindware/<instanceName>/Log/sys*
```

## Связанные статьи

**[Резервное копирование. Настройка и запуск, просмотр журнала сеансов](https://kb.comindware.ru/article.php?id=2190)**



