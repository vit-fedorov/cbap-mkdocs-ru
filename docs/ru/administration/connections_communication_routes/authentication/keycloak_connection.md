---
title: Аутентификация через OpenID Connect
kbId: 4685
---

# Аутентификация через OpenID Connect. Настройка подключения и служб {: #openid_connection}

## Проверка адреса сервера {{ productName }}

1. Откройте раздел [«**Администрирование**» — «**Глобальная конфигурация**»][administration].
2. Удостоверьтесь, что **URL-адрес сервера** начинается с `https://`.

    _![Проверка адреса сервера](openid_connection_check.png)_

## Настройка API на примере Keycloak — этап 1 {: .pageBreakBefore }

1. Откройте админскую консоль Keycloak
2. В левом меню выбирете **master** область(realm) или, если нужная область(realm) существует, выбирете её

_![Переход к управлению областями(realms)](openid_manage_realms.png)_

3. Если нужная область(realm) отсутствуют, нажмите кнопку **Create realm** и введите наименование, например _myRealm_ и нажмите кнопку **Create**.

_![создание новой области(realm)](openid_create_new_realm.png)_

4. В левом меню нажмите кнопку **Clients**
5. Нажмите кнопку **Create client**
6. Введите «**Client ID**», например _myClient_.

_![создание нового клиента](openid_create_new_client.png)_

7. Во вкладке **Capability config** включите **Client authentication** и **Direct access grants**

_![создание нового клиента](openid_create_new_client_2.png)_

8. Во вкладке **Login settings** укажите **Root URL**, **Home URL**, **Valid redirect URIs**, **Web origins**
(например: https://mycompany.ru/, https://mycompany.ru/, https://mycompany.ru/*, https://mycompany.ru/, соответственно, где mycompany.ru URL-адрес сервера из глобальной конфигурации)

_![создание нового клиента](openid_create_new_client_3.png)_

9. Нажмите кнопку «**Save**».
10. На отобразившейся странице нажмите отключите **Logout settings Front channel logout** и введите **Backchannel logout URL**.
(например: https://mycompany.ru/OpenIdLogoutChallenge где mycompany.ru URL-адрес сервера из глобальной конфигурации)

_![создание нового клиента](openid_logout_settings.png)_

11. Скопируйте **Client Secret** с вкладки **Credentials**_

_![создание нового клиента](openid_copy_client_secret.png)_


## Настройка API на примере Keycloak — этап 2 {: .pageBreakBefore }

1. В левом меню нажмите кнопку ***Users**
2. Для того чтобы создать нового пользователя нажмите кнопку **Create new user** или **Add user**, если пользователи уже есть
3. Заполните поля Username, Email, First name, Last name
4. Включите **Email verified**
4. Нажмите кнопку **Create**

_![создание нового клиента](openid_create_new_user.png)_

5. Во вкладке Credentials нажимте кнопку **Set password**
6. Установите временный пароль для пользователя

_![создание нового клиента](openid_create_new_user_set_password.png)_


### Настройка конфигурации пратформы {: .pageBreakBefore }

1. В файле конфигурации платформы заполните поля:

#################### Настройки OpenId-аутентификации ####################
# Имя OpenId сервиса использующегося для входа
auth.openId.displayName: MyKeycloak

# Вкл./выкл. функции
auth.openId.enabled: true

# Адрес сервера OpenId Connect
auth.openId.server: https://my.Keycloak.ru

# Пространство имен или контекст, в котором происходит аутентификация пользователей. Используется для управления идентификацией и доступом в системе OpenID Connect
auth.openId.realm: myRealm

# Уникальный идентификатор клиентского приложения, используемый для аутентификации и авторизации запросов в рамках протокола OpenID Connect
auth.openId.clientId: myClient

# Секретный ключ OpenId Connect
auth.openId.clientSecret: _скопированный Сlient Secret_

# Список идентификаторов целевой аудитории, для которой предназначены токены, используемые в процессе аутентификации и авторизации в OpenID Connect.
auth.openId.audience: myAudience

## Настройка ОС Linux для включения аутентификации через OpenID Connect в {{ productName }} {: .pageBreakBefore }

1. Перейдите в режим суперпользователя `root`:

    --8<-- "linux_sudo.md"

2. Добавьте в файл `/etc/hosts` строку:

    ```
    "xxx.xxx.xxx.xxx" "mycompany.ru"
    ```

    Здесь `xxx.xxx.xxx.xxx` — IP-адрес, `mycompany.ru` адрес сервера **{{ productName }}**, указанный в [_глобальной конфигурации {{ productName }}_](#проверка-адреса-сервера-comindware-platform) (без указания протокола `HTTP` или `HTTPS`).

3. Сформируйте SSL-сертификат на сервере NGINX. Например, согласно инструкциям в статье «[_Генерация SSL сертификата для NGINX (openssl)_](https://webguard.pro/web-services/nginx/generacziya-ssl-sertifikata-dlya-nginx-openssl.html)».
4. Откройте для редактирования файл конфигурации NGINX:

    ```
    vim /etc/nginx/sites-available/comindware<instanceName>
    ```

    {% include-markdown ".snippets/pdfPageBreakHard.md" %}

5. Настройте конфигурацию SSL-сертификата аналогично следующему примеру:

    ``` cs
    server {
        listen 80 default;
        listen 443 ssl;

        root /var/www/<instanceName>;
        server_name mycompany.ru;

        ssl_certificate /etc/nginx/ssl/nginx.crt;
        ssl_certificate_key /etc/nginx/ssl/nginx.key;

        client_max_body_size 300m;
        fastcgi_read_timeout 10000;
        location / {
            proxy_read_timeout 10000;
                        proxy_connect_timeout 10000;
                        proxy_send_timeout 10000;
                        root          /var/www/<instanceName>/;
                        fastcgi_pass  unix:/var/www/<instanceName>/App_Data/comindware.socket;
                        include       /etc/nginx/fastcgi.conf
                        }
    }
    ```
    {% include-markdown ".snippets/pdfEndOfBlockHack.md" %}

7. Проверьте конфигурацию NGINX:

    ```
    nginx -t
    ```

8. Перезапустите **{{ productName }}**:

    ```
    systemctl restart elasticsearch nginx comindware<instanceName>
    ```

{% endif %}

## Вход в {{ productName }} {: .pageBreakBefore }

1. Откройте веб-сайт экземпляра {{ productName }}, например [https://mycompany.ru](https://mycompany.ru/)
2. Нажмите кнопку «**Войти как администратор**».

    _![Переход к странице входа администратора](openid_connection_administrator_entry.png)_

3. Введите свои учётные данные и нажмите кнопку «**Войти**».

    _![Вход с аккаунтом администратора](openid_connection_administrator.png)_

    {% include-markdown ".snippets/pdfPageBreakHard.md" %}

4. Выйдите из системы.
5. Отобразится страница входа с кнопкой «**Войти с помощью MyKeycloak**».

    _![Кнопка «Войти с помощью MyKeycloak](openid_connection_Keycloak_entry.png)_

6. На этом настройка входа через OpenID Connect завершена. Теперь пользователи смогут входить в **{{ productName }}** с помощью своих аккаунтов Keycloak.

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
