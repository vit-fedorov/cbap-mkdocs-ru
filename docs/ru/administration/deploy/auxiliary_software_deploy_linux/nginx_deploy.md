---
title: NGINX. Установка и настройка. Краткое руководство
kbId: 2096
---

# NGINX. Установка и настройка. Краткое руководство

## Введение

В настоящем документе представлена краткая инструкция по установке и настройке конфигурации HTTP-сервера NGINX в ОС Ubuntu 20.04 для использования NGINX в сочетании с {{ productName }}.

Подробные сведения по установке и настройке NGINX представлены на следующих сайтах:

- [http://NGINX.org/ru/docs/beginners\_guide.html](http://nginx.org/ru/docs/beginners_guide.html)
- [https://ruvds.com/ru/helpcenter/kak-nastroit-NGINX-na-ubuntu-20-04/](https://ruvds.com/ru/helpcenter/kak-nastroit-nginx-na-ubuntu-20-04/)
- [https://webdevblog.ru/bezopasnost-NGINX-kak-uluchshit-konfiguraciju-vashego-servera/](https://webdevblog.ru/bezopasnost-nginx-kak-uluchshit-konfiguraciju-vashego-servera/)

## 1. Установка NGINX

Войдите в систему под учётной записью, имеющей разрешение на запуск команды `sudo`, и выполните следующие команды:

- `$ sudo apt update`
- `$ sudo apt install NGINX`

Первая команда обновляет базу данных пакетов, доступных для установки. Вторая — устанавливает компоненты NGINX.

После установки NGINX настройте его конфигурацию.

## 2. Настройка сервера NGINX

Конфигурация NGINX хранится в файле `NGINX.conf`. По умолчанию файл `NGINX.conf` находится в следующей папке:

- `/etc/NGINX` или `/usr/local/etc/NGINX` — в системах Linux;
- `[папка установки NGINX]/conf` — в системах Windows.

### 2.1. Пример конфигурации прокси-сервера

| server {     server\_name  domain.com;     reset\_timedout\_connection  on;     listen 80;       location /robots.txt { root /var/www/html; }     return 301 https://$host$request\_uri; }   server {     server\_name  domain.com;     reset\_timedout\_connection  on;        listen 443 ssl;       location / {     proxy\_pass http://backend-server:8081/;     proxy\_next\_upstream error timeout invalid\_header http\_500 http\_503;       # do not set HOST header     proxy\_set\_header  Host                $host;     proxy\_set\_header  X-Forwarded-For     $proxy\_add\_x\_forwarded\_for;     proxy\_set\_header  X-Forwarded-Proto   $scheme;     proxy\_set\_header  X-Real-IP           $remote\_addr;       proxy\_connect\_timeout     90;     proxy\_send\_timeout        1000;     proxy\_read\_timeout        1000;       # enable WebSockets     proxy\_http\_version 1.1;     proxy\_set\_header Upgrade $http\_upgrade;     proxy\_set\_header Connection "upgrade";       client\_max\_body\_size 100m;       error\_log /var/log/NGINX/domain-error.log error;     access\_log /var/log/NGINX/domain-access.log;   } } |
| --- |

### 2.2. Настройка UFW

Для защиты подключений рекомендуется настроить межсетевой экран с помощью утилиты Uncomplicated Firewall (UFW).

Просмотреть профили приложений можно с помощью команды: `$ sudo ufw app list`

Для просмотра и изменения параметров используйте соответствующие команды. Например, команда для подключения к NGINX посредством HTTP: `$ sudo ufw allow 'NGINX HTTP'`

Команда для проверки статуса: `$ sudo ufw status`

### 2.3. Отключение команды server\_tokens

По умолчанию команда `server_tokens`возвращает номер версии NGINX.

Чтобы скрыть версию NGINX, отключите команду `server_tokens`, добавив в файле конфигурации NGINX следующую директиву: `server_tokens off`

### 2.4. Контроль ресурсов и ограничения

Для предотвращения DoS-атак на NGINX можно установить ограничения на размер буфера для всех клиентов. Для это в разделе `server` файла конфигурации NGINX используйте следующие директивы:

- `client_body_buffer_size` — размер буфера тела запроса клиента. Типовое значение — 8 или 16 КБ, но рекомендуется установить его равным 1 КБ с помощью следующей директивы: `client_body_buffer_size 1k`.
- `client_header_buffer_size` — размер буфера заголовка запроса клиента. Размер буфера 1 КБ подходит для большинства запросов, например: `client_header_buffer_size 1k`
- `client_max_body_size` — максимально допустимый размер тела клиентского запроса, например: `client_max_body_size`. Размера 1 КБ должно быть достаточно, но его следует увеличить, если загрузка файлов осуществляется методом POST.
- `large_client_header_buffers` —максимальное количество и размер буферов, которые будут использоваться для чтения больших заголовков клиентских запросов. Например, чтобы установить максимальное количество буферов равным 2, каждый с максимальным размером 1 КБ, и разрешить прием URI-данных размером 2 КБ, используйте следующую директиву: `large_client_header_buffers 2 1k`

### 2.5. Настройка NGINX для включения заголовков безопасности

Чтобы дополнительно защитить веб-сервер NGINX, можно добавить определенные заголовки HTTP. Ниже приведены рекомендованные варианты таких заголовков.

**X-Frame-Options**

Заголовок HTTP-ответа `X-Frame-Options` используется чтобы указать, разрешено ли браузеру отображать страницу в фреймах `<frame>`, `<iframe>`, `<embed>` и `<object>`. Чтобы разрешить отображение страниц во фреймах только с того же домена, на котором размещен веб-сайт, добавьте следующую директиву в раздел server файла конфигурации NGINX: `add_header X-Frame-Options "SAMEORIGIN";`

**Strict-Transport-Security**

[HTTP Strict Transport Security (HSTS)](https://www.acunetix.com/blog/articles/what-is-hsts-why-use-it/) — это механизм, позволяющий веб-сайту сообщать браузеру, что доступ к нему разрешен только через безопасное соединение (HTTPS). Если веб-сайт объявил политику HSTS, браузер должен отклонять все HTTP-соединения и запретить пользователям принимать незащищенные SSL-сертификаты. Чтобы сервер NGINX возвращал заголовок HSTS, добавьте следующую директиву в раздел `server`: `add_ header Strict-Transport-Security "max-age=31536000; includeSubdomains; preload";`

**Политика CSP**

Политика безопасности контента (CSP) защищает веб-сервер от определенных типов атак, включая атаки с использованием [Cross-site Scripting](https://www.acunetix.com/websitesecurity/cross-site-scripting/) (XSS) и атаки с использованием data injection. Чтобы реализовать CSP, добавьте заголовок Content-Security-Policy, как показано в следующем примере (фактический заголовок должен быть настроен в соответствии с вашими уникальными требованиями) в раздел `server`: `add_header Content-Security-Policy "default-src 'self' http: https: data: blob: 'unsafe-inline'" always;` 

**Заголовок X-XSS-Protection**

Заголовок HTTP X-XSS-Protection поддерживают браузеры IE и Safari. Он не требуется для современных браузеров, если используется строгая политика безопасности содержимого. Однако, чтобы предотвратить атаки типа XSS при использовании старых браузеров (которые не поддерживают CSP), добавьте заголовок X-XSS Protection в раздел `server`: `add_header X-XSS-Protection "1; mode=block”;`

### 2.6. Настройка SSL и наборов шифров Cipher Suite

Конфигурация NGINX по умолчанию позволяет использовать небезопасные старые версии протокола TLS, которые н рекомендуется применять. Следует изменить конфигурацию для поддержки только новых, безопасных версий TLS. Для этого добавьте следующую директиву в раздел `server` файла конфигурации NGINX: `ssl_protocols TLSv1.2 TLSv1.3;`

Укажите конкретные наборы шифров (криптографических алгоритмов), чтобы предотвратить использование уязвимых наборов не поддерживаются. Либо для автоматического выбора шифра на стороне сервера добавьте следующую директиву в раздел `server`: `ssl_prefer_server_ciphers on;`

### 2.7. Регулярное обновление сервера

Следует регулярно устанавливать последние обновления NGINX с официального сайта: [http://NGINX.org/en/security\_advisories.html](http://nginx.org/en/security_advisories.html)

### 2.8. Проверка состояния сервера

Команда проверки статуса веб-сервера NGINX: `$ systemctl status NGINX`

![Статус веб-сервера NGINX](https://kb.comindware.ru/assets/Picture_10.png)

Статус веб-сервера NGINX



