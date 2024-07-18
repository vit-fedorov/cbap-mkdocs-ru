---
kbId: 2329
---

# Аутентификация через OpenID Connect. Настройка подключения и служб

## Проверка адреса сервера {{ productName }}

1. Откройте раздел [«**Администрирование**» — «**Глобальная конфигурация**»][администрирование].
2. Удостоверьтесь, что **URL-адрес сервера** начинается с `https://`.  

    _![Проверка адреса сервера](openid_connection_check.png)_

## Настройка API и служб Google Cloud — этап 1

1. Откройте веб-сайт [https://console.developers.google.com/](https://console.developers.google.com/)
2. Если проекты отсутствуют, нажмите кнопку «**Create project**».
3. Если имеются проекты, нажмите кнопку «**Select a project**» и в отобразившемся окне нажмите кнопку «**New project**».

    _![Создание проекта](openid_connection_project_creation.png)_

4. Отобразится страница «**New project**».
5. Введите «**Project name**», например _Client ID_.
6. Нажмите кнопку «**Create**».

    _![Страница свойств нового проекта](openid_connection_project_properties.png)_

7. На отобразившейся странице нажмите кнопку «**Enable APIs and services**».

    _![Включение API и служб](openid_connection_api_switch_on.png)_
  
8. В поле «**Search for APIs & Services**» найдите **Site Verification API**.

    _![Поиск Site Verification API](openid_connection_api_search.png)_

9. Перейдите к разделу «**Site Verification API**».

    _![Переход к разделу Site Verification API](openid_connection_api_verification.png)_

10. Нажмите кнопку «**Enable**».

    _![Включение Site Verification API](openid_connection_api_verification_enabled.png)_

### Настройка страницы согласия OAuth

1. В меню слева выберите пункт «**OAuth consent screen**».
2. В разделе «**User type**» выберите «**External**» и нажмите кнопку «**Create**».  

    _![Настройка страницы согласия OAuth — тип пользователя](openid_connection_oath_user_type.png)_

#### Настройка сведений о приложении

1. Заполните обязательные поля разделе «**App information**»:

    - в поле «**App name**» укажите, например «_Сайт Mycompany.ru»;_
    - в поле «**User support email**» укажите, например, свой адрес эл. почты.

    _![Настройка страницы согласия OAuth — название приложения и адрес службы поддержки](openid_connection_oath_new_app.png)_

2. В разделе «**App domain**» в поле «**Application home page**» введите [адрес сервера](#проверка-адреса-сервера--productname-), указанный в глобальной конфигурации {{ productName }}, например [https://mycompany.ru](https://mycompany.ru/)
3. В разделе «**Authorized domains**» нажмите кнопку «**Add domain**» и введите в поле «**Authorized domain 1**» доменное имя сервера без префикса `https://`, например _mycompany.ru_
4. В разделе «**Developer contact information**» в поле «**Email addresses**» введите, например, свой адрес эл. почты.
5. Нажмите кнопку «**Save and continue**».  

    _![Настройка страницы согласия OAuth — главная страница приложения, домен, контактная информация разработчика](openid_connection_oath_agreement.png)_

#### Настройка запрашиваемых разрешений для приложения

1. На странице «**Scopes**» нажмите кнопку «**Add or remove scopes**».
2. В открывшейся форме установите три первых флажка и нажмите кнопку «**Update**».  

    _![Настройка страницы согласия OAuth — добавление разрешений для приложения](openid_connection_oath_permission.png)_

3. В нижней части страницы «**Scopes**» нажмите кнопку «**Save and continue**».  

    _![Настройка страницы согласия OAuth — сохранение настроенных разрешений](openid_connection_oath_permission_saving.png)_

4. На странице «**Test users**» кнопку «**Save and continue**».  

    _![Настройка страницы согласия OAuth — пропуск теста пользователей](openid_connection_oath_user_test.png)_

5. На странице «**Summary**» проверьте сведения и нажмите кнопку «**Back to dashboard**».  

    _![Настройка страницы согласия OAuth — проверка введенных сведений](openid_connection_oath_check.png)_

6. На открывшейся странице в разделе «**Publishing status**» нажмите кнопку «**Publish app**».
7. В окне подтверждения нажмите кнопку «**Confirm**».  

    _![Настройка страницы согласия OAuth — публикация приложения](openid_connection_oath_app_publication.png)_

8. Статус публикации изменится на «**In production**».  

    _![Настройка страницы согласия OAuth — статус опубликованного приложения](openid_connection_oath_app_status.png)_

### Настройка учётных данных клиента OAuth

1. В левой панели выберите пункт «**Credentials**».
2. На странице «**Credentials**» нажмите кнопку «**Create credentials**».
3. В раскрывающемся меню выберите пункт «**OAuth client ID**»  

    _![Переход к созданию клиента OAuth](openid_connection_oath_client_creation.png)_

4. В поле «**Application type**» выберите пункт «**Web application**».
5. В поле «Name» введите имя клиента, например «_OAuth client 1_».
6. В разделе «**Authorized JavaScript origins**» нажмите кнопку «**Add URI**».
7. Введите [адрес сервера](#проверка-адреса-сервера--productname-), указанный в глобальной конфигурации {{ productName }}, например [https://mycompany.ru](https://mycompany.ru/)
8. Нажмите кнопку «**Create**».  

    _![Настройка и сохранение учётных данных клиента OAuth](openid_connection_oath_client_settings.png)_

9. Отобразится окно с учётными данными созданного клиента OAuth.  

    _![Созданный клиент OAuth](openid_connection_oath_new_client.png)_

10. Не закрывайте эту вкладку в браузере, чтобы использовать данные с неё на последующих шагах.
11. Чтобы впоследствии посмотреть «**Client ID**» и «**Client Secret**», нажмите гиперссылку с названием клиента в таблице «**OAuth 2.0 Client IDs**» в разделе «**Credentials**».  

    _![Таблица учётных данных клиентов OAuth](openid_connection_oath_client_table.png)_

## Настройка подключения в {{ productName }}

1. Перейдите в раздел «**Администрирование**» — «**Подключения**».
2. Нажмите кнопку «**Cоздать**».
3. В раскрывающемся меню выберите пункт «**Аутентификация через OpenID Connect**».  
    
    ![Создание подключения для аутентификации через OpenID Connect](https://kb.comindware.ru/assets/Pasted%20image%2020230301152110.png)
    
    Создание подключения для аутентификации через OpenID Connect
    
4. Откроется окно «**Новое подключение**».
5. В поле «**Название**» введите название подключения, например «_Client ID_».
6. В поле «**Поставщик удостоверений**» выберите пункт «**Google**».
7. В поле «**ID клиента**» вставьте **Client ID**, скопированный из Google Cloud.
8. В поле «**Ключ клиента**» вставьте **Client secret**, скопированный из Google Cloud.
9. В поле «**Домены электронной почты**» оставьте домен _gmail.com_.
10. В поле «**Группа**» выбирать группу необязательно.
11. Поле «**Адрес перенаправления после входа**» будет заполнено автоматически после создания подключения.
12. Нажмите кнопку «**Создать**».  
    
    ![Настройка нового подключения для аутентификации через OpenID Connect](https://kb.comindware.ru/assets/Pasted%20image%2020230301153730.png)
    
    Настройка нового подключения для аутентификации через OpenID Connect
    
13. Откройте созданное подключение.
14. Скопируйте в буфер обмена **адрес перенаправления после входа**.
15. Нажмите кнопку «**Сохранить**».  
    
    ![Сформированный адрес перенаправления после входа](https://kb.comindware.ru/assets/Pasted%20image%2020230301160010.png)
    
    Сформированный адрес перенаправления после входа
    
16. Откройте страницу «**Администрирование**» – «**Регистрация и вход**».
17. Активируйте выключатель «**Разрешить вход**» на плитке «**Google OpenID Connect**».
    
    ![Рисунок 10.31. Включение входа через Google OpenID Connect](https://kb.comindware.ru/assets/img_6492fe8a50dba.png)
    
    Рисунок 10.31. Включение входа через Google OpenID Connect
    
18. Нажмите кнопку «**Сохранить**».

## Настройка API и служб Google Cloud — этап 2

1. Откройте веб-сайт Google Cloud [https://console.developers.google.com/](https://console.developers.google.com/)
2. В левой панели выберите пункт «**Credentials**».
3. Откройте параметры созданного ранее клиента _OAuth Client 1_, нажав гиперссылку с его названием в таблице «**OAuth 2.0 Client IDs**».
4. В разделе «**Authorized redirect URIs**» нажмите кнопку «**Add URI**».
5. В поле «**URIs 1**» введите ранее скопированный **адрес перенаправления после входа** включая префикс `https://`.
6. Нажмите кнопку «**Save**».  
    
    ![Добавление авторизованного адреса перенаправления после входа в клиент OAuth в Google Cloud](https://kb.comindware.ru/assets/Pasted%20image%2020230301160320.png)
    
    Добавление авторизованного адреса перенаправления после входа в клиент OAuth в Google Cloud
    

## Настройка реестра Windows для включения аутентификации через OpenID Connect в {{ productName }}

1. Запустите редактор реестра Windows: `regedit.exe`.
2. Откройте раздел реестра `Computer -> HKEY_LOCAL_MACHINE -> SOWTWARE->Сomindware -> Instances -> имя_экземпляра_Comindware_Business_Application_Platform`.
3. Дважды щёлкните параметр «**IsFederationAuthEnabled**».
4. Если значение этого параметра **0**, измените его на **1**.
5. Нажмите кнопку «**OK**».  
    
    ![Включение федеративной аутентификации для экземпляра {{ productName }} с помощью реестра Windows](https://kb.comindware.ru/assets/Pasted%20image%2020230301163726.png)
    
    Включение федеративной аутентификации для экземпляра {{ productName }} с помощью реестра Windows
    
6. В командной строке от администратора выполните команду: `iisreset /restart`
7. Дождитесь перезапуска служб IIS.  
    
    ![Перезапуск IIS с помощью командной строки](https://kb.comindware.ru/assets/Pasted%20image%2020230301171414.png)
    
    Перезапуск IIS с помощью командной строки
    

## Настройка ОС Linux для включения аутентификации через OpenID Connect в {{ productName }}

1. Перейдите в режим суперпользователя `root`:
    
    ```
    su -
    ```
    
    или
    
    ```
    sudo -i
    ```
    
2. Добавьте в файл `/etc/hosts` строку:
    
    ```
    "xxx.xxx.xxx.xxx" "mycompany.ru"
    ```
    
    Здесь `xxx.xxx.xxx.xxx` — IP-адрес, `mycompany.ru` адрес сервера **{{ productName }}**, указанный в [_глобальной конфигурации {{ productName }}_](https://kb.comindware.ru/article/517/%d0%90%d1%83%d1%82%d0%b5%d0%bd%d1%82%d0%b8%d1%84%d0%b8%d0%ba%d0%b0%d1%86%d0%b8%d1%8f-%d1%87%d0%b5%d1%80%d0%b5%d0%b7-openid-connect-%d0%9d%d0%b0%d1%81%d1%82%d1%80%d0%be%d0%b9%d0%ba%d0%b0-%d0%bf%d0%be%d0%b4%d0%ba%d0%bb%d1%8e%d1%87%d0%b5%d0%bd%d0%b8%d1%8f-%d0%b8-%d1%81%d0%bb%d1%83%d0%b6%d0%b1-2329.html#_%D0%9D%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0_%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B9_%D0%BA%D0%BE%D0%BD%D1%84%D0%B8%D0%B3%D1%83%D1%80%D0%B0%D1%86%D0%B8%D0%B8) (без указания протокола `HTTP` или `HTTPS`).
    
3. В файле `/usr/share/comindware/configs/instance/instanceName.yml` для параметра `isFederationAuthEnabled` установите значение `1`:
    
    ```
    isFederationAuthEnabled: 1
    ```
    
4. Сформируйте SSL-сертификат на сервере nginx. Например, согласно инструкциям в статье «[_Генерация SSL сертификата для NGINX (openssl)_](https://webguard.pro/web-services/nginx/generacziya-ssl-sertifikata-dlya-nginx-openssl.html)».
5. Откройте для редактирования файл конфигурации NGINX:
    
    ```
    vim /etc/nginx/sites-available/comindwareinstancename
    ```
    
6. Настройте конфигурацию SSL-сертификата согласно следующему примеру (добавьте выделенные жёлтым цветом директивы):
    
    ```
    server {
    ```
    
    Здесь _`**instanceName**`_ — имя экземпляра ПО.
    
7. Проверьте конфигурацию nginx: 
    
    ```
    nginx -t
    ```
    
8. Перезапустите **{{ productName }}**:
    
    ```
    systemctl restart elasticsearch nginx comindwareinstancename
    ```
    
    Здесь `instancename` — имя экземпляра ПО.
    

## Вход в {{ productName }}

1. Откройте веб-сайт экземпляра {{ productName }}, например [https://mycompany.ru](https://mycompany.ru/)
2. Нажмите кнопку «**Войти как администратор**».  
    
    ![Переход к странице входа администратора](https://kb.comindware.ru/assets/Pasted%20image%2020230301172309.png)
    
    Переход к странице входа администратора
    
3. Введите свои учётные данные и нажмите кнопку «**Войти**».  
    
    ![Вход с аккаунтом администратора](https://kb.comindware.ru/assets/Pasted%20image%2020230301172350.png)
    
    Вход с аккаунтом администратора
    
4. Выйдите из системы.
5. Отобразится страница входа с кнопкой «**Войти с помощью Google**».  
    
    ![Кнопка «Войти с помощью Google»](https://kb.comindware.ru/assets/Pasted%20image%2020230301173323.png)
    
    Кнопка «Войти с помощью Google»
    
6. На этом настройка входа через OpenID Connect завершена. Теперь пользователи смогут входить в **{{ productName }}** с помощью своих аккаунтов Google.