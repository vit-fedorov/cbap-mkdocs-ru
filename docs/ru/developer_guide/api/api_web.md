---
title: Методы Web API
kbId: 4861
---

# Методы Web API {: #api_web }

## Введение

Web API предоставляет общие RESTful-методы. Эти методы одинаковы для всех версий **{{ productName }}**.

В этом разделе представлен обзор методов Web API. Полную информацию см. в Swagger.

## Доступ к Web API

- Базовый URL-адрес для запросов Web API:
`https://your-host/webapi/`
- Web API поддерживает запросы `GET`, `PUT`, `POST`, `DELETE`.
- Методы Web API передают данные в форматах JSON и XML.

## Использование Swagger

Swagger предоставляет подробную справку по методам API, включая описания запросов и ответов, а также модели данных с примерами значений.

Swagger позволяет выполнять запросы и просматривать ответы.

Интерфейс Swagger для Web API доступен по адресу:

`https://your-host/docs/webapi`

Здесь `your-host` — доменное имя вашего сервера.

_![](https://kb.comindware.ru/assets/img_64d3708401e22.png)_Интерфейс Swagger для метода Web API, создающего шаблон аккаунта

### Определения

Методы Web API и документация Swagger используют следующие ***специфические имена*** для сущностей **{{ productName }}**:

- ***activity*** — элемент диаграммы процесса
- ***alias*** — системное имя
- ***behaviour*** — сценарий, элемент диаграммы процесса
- ***container*** — шаблон, приложение
- ***dataset*** — таблица в шаблоне
- ***global*** ***alias*** *(глобальный псевдоним)* — путь к объекту, состоящий из его типа, имени родительской системы и имени системы объекта
- ***id*** — идентификатор объекта
- ***inline*** — особый тип документа, который отображается на форме как текстовый блок и который можно редактировать в форме
- ***list*** — массив
- **object** (*объект*) — набор пар свойство/значение
- ***property***— атрибут
- ***record***— запись
- ***revision*** — версия файла, прикреплённого к атрибуту
- ***solution*** — приложение
- ***scheme*** — диаграмма процесса
- ***stream*** — файл, хранящийся в системе
- ***template*** — шаблон
- ***transfer*** — управление версиями приложения
- ***trigger*** — сценарий
- ***user*** ***command*** — кнопка
- ***worker*** — системный сервис

## Описание методов Web API

<table markdown="block" style="width: 98%;">
<tbody markdown="block">
<tr markdown="block">
<th markdown="block" colspan="5" style="overflow-wrap: break-word; width: 99.00%;">
<h3 id="mcetoc_1h7cte61o0">Аккаунт — отдельные аккаунты</h3>
</th>
</tr>
<tr markdown="block">
<th markdown="block" style="overflow-wrap: break-word; width: 6.0%; max-width: 80px; text-align: center; ">
<p><strong>Метод</strong></p>
</th>
<th markdown="block" style="overflow-wrap: break-word; width: 14.00%; max-width: 190px; min-width: 190px; ">
<p><strong>Запрос</strong></p>
</th>
<th markdown="block" style="overflow-wrap: break-word; min-width: 140px; max-width: 150px; width: 27.0%; ">
<p><strong>Описание</strong></p>
</th>
<th markdown="block" style="overflow-wrap: break-word; min-width: 190px; max-width: 190px; width: 29.0%; ">
<p><strong>Входные данные</strong></p>
</th>
<th markdown="block" style="overflow-wrap: break-word; min-width: 140px; max-width: 150px; width: 20.0%; ">
<p><strong>Выходные данные</strong></p>
</th>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
/webapi/<wbr/>Account</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Получает все аккаунты.
</td>
<td markdown="block" class="api-cell-input">
 
</td>
<td markdown="block" class="api-cell-output">
Массив объектов со свойствами аккаунтов.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method post">
POST
</td>
<td markdown="block" class="api-cell-endpoint">
/webapi/<wbr/>Account</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Создает аккаунт.
</td>
<td markdown="block" class="api-cell-input">
Объект свойств аккаунта.
</td>
<td markdown="block" class="api-cell-output">
Идентификатор аккаунта.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<span style="color: #c7254e;">/webapi/<wbr/>Accoun</span>t </span> </span>
</td>
<td markdown="block" class="api-cell-description">
Изменяет свойства аккаунта.
</td>
<td markdown="block" class="api-cell-input">
Объект свойств аккаунта.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method delete">
DELETE
</td>
<td markdown="block" class="api-cell-endpoint">
/webapi/<wbr/>Account/<wbr/>{accountId}
</td>
<td markdown="block" class="api-cell-description">
Удаляет аккаунт.
</td>
<td markdown="block" class="api-cell-input">
Идентификатор аккаунта.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>Account/<wbr/>{accountId}</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Получает свойства аккаунта.
</td>
<td markdown="block" class="api-cell-input">
Идентификатор аккаунта.
</td>
<td markdown="block" class="api-cell-output">
<p><span style="font-size: 10.0pt; font-family: 'Arial',sans-serif;">Объект свойств аккаунта.</span></p>
</td>
</tr>
<tr markdown="block">
<th markdown="block" colspan="5" style="overflow-wrap: break-word; width: 99.00%;">
<h3 id="mcetoc_1h7ctepcd2">AccountTemplate — шаблоны аккаунтов и связанные с ними аккаунты</h3>
</th>
</tr>
<tr markdown="block">
<th markdown="block" style="overflow-wrap: break-word; width: 6.0%;">
<p style="text-align: center;"><strong>Метод</strong></p>
</th>
<th markdown="block" style="overflow-wrap: break-word; width: 14.00%; max-width: 190px; min-width: 190px;">
<p><strong>Запрос</strong></p>
</th>
<th markdown="block" class="api-cell-description">
<p><strong>Описание</strong></p>
</th>
<th markdown="block" class="api-cell-input">
<p><strong>Входные данные</strong></p>
</th>
<th markdown="block" class="api-cell-output">
<p><strong>Выходные данные</strong></p>
</th>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method post">
POST
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>AccountTemplate/<wbr/>{solutionAlias}</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Создает шаблон аккаунта.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, объект свойств шаблона аккаунта.
</td>
<td markdown="block" class="api-cell-output">
Объект с системным именем шаблона аккаунта.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>AccountTemplate/<wbr/>{solutionAlias}</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Изменяет свойства шаблона аккаунта.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, объект свойств шаблона аккаунта.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method delete">
DELETE
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>AccountTemplate/<wbr/>{solutionAlias}/<wbr/>{accountTemplateAlias}</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Удаляет шаблон аккаунта.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, системное имя шаблона аккаунта.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>AccountTemplate/<wbr/>{solutionAlias}/<wbr/>{accountTemplateAlias}</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Получает свойства шаблона аккаунта.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, системное имя шаблона аккаунта.
</td>
<td markdown="block" class="api-cell-output">
Объект свойств шаблона аккаунта.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>AccountTemplate/<wbr/>{solutionAlias}/<wbr/>{accountTemplateAlias}/<wbr/>Disable</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Архивирует шаблон аккаунта.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, системное имя шаблона аккаунта.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>AccountTemplate/<wbr/>{solutionAlias}/<wbr/>{accountTemplateAlias}/<wbr/>Enable</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Разархивирует шаблон аккаунта.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, системное имя шаблона аккаунта.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>AccountTemplate/<wbr/>{solutionAlias}/<wbr/>{accountTemplateAlias}/<wbr/>Exclude</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Отвязывает аккаунты от указанного шаблона аккаунта.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, системное имя шаблона аккаунта, массив идентификаторов аккаунта.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>AccountTemplate/<wbr/>{solutionAlias}/<wbr/>{accountTemplateAlias}/<wbr/>Include</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Привязывает указанные аккаунты к указанному шаблону аккаунта.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, системное имя шаблона аккаунта, массив идентификаторов аккаунта.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>AccountTemplate/<wbr/>{solutionAlias}/<wbr/>{accountTemplateAlias}/<wbr/>ListIncluded</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Получает аккаунты, привязанные к указанному шаблону аккаунта.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, системное имя шаблона аккаунта.
</td>
<td markdown="block" class="api-cell-output">
Массив объектов со свойствами аккаунтов.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>AccountTemplate/<wbr/>List/<wbr/>{solutionAlias}</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Получает все шаблоны аккаунтов в указанном приложении.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения.
</td>
<td markdown="block" class="api-cell-output">
Массив объектов со свойствами шаблонов аккаунта.
</td>
</tr>
<tr markdown="block">
<th markdown="block" colspan="5" style="overflow-wrap: break-word; width: 99.00%;">
<h3 id="mcetoc_1h7ctfbpf3">Attribute — атрибуты шаблона.</h3>
</th>
</tr>
<tr markdown="block">
<th markdown="block" style="overflow-wrap: break-word; width: 6.0%;">
<p style="text-align: center;"><strong>Метод</strong></p>
</th>
<th markdown="block" style="overflow-wrap: break-word; width: 14.00%; max-width: 190px; min-width: 190px;">
<p><strong>Запрос</strong></p>
</th>
<th markdown="block" class="api-cell-description">
<p><strong>Описание</strong></p>
</th>
<th markdown="block" class="api-cell-input">
<p><strong>Входные данные</strong></p>
</th>
<th markdown="block" class="api-cell-output">
<p><strong>Выходные данные</strong></p>
</th>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method post">
POST
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>Attribute/<wbr/>{solutionAlias}</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Создает атрибут.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, объект свойств атрибута.
</td>
<td markdown="block" class="api-cell-output">
Объект с системным именем атрибута.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>Attribute/<wbr/>{solutionAlias}</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Изменяет свойства атрибута.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, объект свойств атрибута.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method delete">
DELETE
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>Attribute/<wbr/>{solutionAlias}/<wbr/>{attributeGlobalAlias}</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Удаляет атрибут.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, глобальный псевдоним атрибута: <code>Attribute@<wbr/>templateSystemName.<wbr/>attributeSystemName</code>
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>Attribute/<wbr/>{solutionAlias}/<wbr/>{attributeGlobalAlias}</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Получает свойства атрибута.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, глобальный псевдоним атрибута: Attribute@ <wbr/> templateSystemName. <wbr/> attributeSystemName
</td>
<td markdown="block" class="api-cell-output">
Объект свойств атрибута.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>Attribute/<wbr/>{solutionAlias}/<wbr/>{attributeGlobalAlias}/<wbr/>Disable</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Атрибут архива.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, глобальный псевдоним атрибута: <code>Attribute@<wbr/>templateSystemName.<wbr/>attributeSystemName</code>
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>Attribute/<wbr/>{solutionAlias}/<wbr/>{attributeGlobalAlias}/<wbr/>Enable</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Разархивирует атрибут.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, глобальный псевдоним атрибута: <code>Attribute@<wbr/>templateSystemName.<wbr/>attributeSystemName</code>
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>Attribute/<wbr/>List/<wbr/>{templateGlobalAlias}</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Получает все атрибуты указанного шаблона.
</td>
<td markdown="block" class="api-cell-input">
Глобальный псевдоним шаблона: <code>Template@<wbr/>applicationSystemName.<wbr/>templateSystemName</code>
</td>
<td markdown="block" class="api-cell-output">
Массив объектов с атрибутивными свойствами.
</td>
</tr>
<tr markdown="block">
<th markdown="block" colspan="5" style="overflow-wrap: break-word; width: 99.00%;">
<h3 id="mcetoc_1h7cth49q4">Backup — резервное копирование конфигураций и сессий</h3>
</th>
</tr>
<tr markdown="block">
<th markdown="block" style="overflow-wrap: break-word; width: 6.0%;">
<p style="text-align: center;"><strong>Метод</strong></p>
</th>
<th markdown="block" style="overflow-wrap: break-word; width: 14.00%; max-width: 190px; min-width: 190px;">
<p><strong>Запрос</strong></p>
</th>
<th markdown="block" class="api-cell-description">
<p><strong>Описание</strong></p>
</th>
<th markdown="block" class="api-cell-input">
<p><strong>Входные данные</strong></p>
</th>
<th markdown="block" class="api-cell-output">
<p><strong>Выходные данные</strong></p>
</th>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method delete">
DELETE
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Backup/<wbr/>Configuration</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Удаляет указанные конфигурации резервного копирования.
</td>
<td markdown="block" class="api-cell-input">
Массив идентификаторов конфигурации резервного копирования.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Backup/<wbr/>Configuration</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Получает все конфигурации резервного копирования.
</td>
<td markdown="block" class="api-cell-input">
 
</td>
<td markdown="block" class="api-cell-output">
Массив резервных объектов конфигурации.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method post">
POST
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Backup/<wbr/>Configuration</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Создает конфигурацию резервного копирования.
</td>
<td markdown="block" class="api-cell-input">
Резервный объект конфигурации.
</td>
<td markdown="block" class="api-cell-output">
Идентификатор конфигурации резервного копирования.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Backup/<wbr/>Configuration</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Изменяет конфигурацию резервного копирования.
</td>
<td markdown="block" class="api-cell-input">
Резервный объект конфигурации.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Backup/<wbr/>Configuration/<wbr/>{configurationId}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Получает конфигурацию резервного копирования.
</td>
<td markdown="block" class="api-cell-input">
Идентификатор конфигурации резервного копирования.
</td>
<td markdown="block" class="api-cell-output">
Резервный объект конфигурации.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method delete">
DELETE
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Backup/<wbr/>Session</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Удаляет указанные сеансы резервного копирования.
</td>
<td markdown="block" class="api-cell-input">
Массив идентификаторов сеансов резервного копирования.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method post">
POST
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Backup/<wbr/>Session</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Возвращает сеансы резервного копирования, соответствующие указанному фильтру.
</td>
<td markdown="block" class="api-cell-input">
Объект с фильтром сеанса резервного копирования.
</td>
<td markdown="block" class="api-cell-output">
Массив объектов со сведениями о сеансах резервного копирования.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method post">
POST
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Backup/<wbr/>Session/<wbr/>{configurationId} </span> </span>
</td>
<td markdown="block" class="api-cell-description">
Инициирует сеанс резервного копирования с использованием указанной конфигурации.
</td>
<td markdown="block" class="api-cell-input">
Идентификатор конфигурации резервного копирования.
</td>
<td markdown="block" class="api-cell-output">
Объект со сведениями о сеансе резервного копирования.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Backup/<wbr/>Session/<wbr/>{sessionId}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Получает сеанс резервного копирования.
</td>
<td markdown="block" class="api-cell-input">
Идентификатор сеанса резервного копирования.
</td>
<td markdown="block" class="api-cell-output">
Объект со сведениями о сеансе резервного копирования.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Backup/<wbr/>Session/<wbr/>{sessionId}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Прерывает сеанс резервного копирования.
</td>
<td markdown="block" class="api-cell-input">
Идентификатор сеанса резервного копирования.
</td>
<td markdown="block" class="api-cell-output">
Объект со сведениями о сеансе резервного копирования.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method post">
POST
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Backup/<wbr/>SetElasticsearchRepository/<wbr/>{name}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Задает репозиторий моментальных снимков Elasticsearch.
</td>
<td markdown="block" class="api-cell-input">
Имя существующего репозитория моментальных снимков Elasticsearch.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<th markdown="block" colspan="5" style="overflow-wrap: break-word; width: 99.00%;">
<h3 id="mcetoc_1h7cth8q45">BehaviourState — сценарии и элементы процессов</h3>
</th>
</tr>
<tr markdown="block">
<th markdown="block" style="overflow-wrap: break-word; width: 6.0%;">
<p style="text-align: center;"><strong>Метод</strong></p>
</th>
<th markdown="block" style="overflow-wrap: break-word; width: 14.00%; max-width: 190px; min-width: 190px;">
<p><strong>Запрос</strong></p>
</th>
<th markdown="block" class="api-cell-description">
<p><strong>Описание</strong></p>
</th>
<th markdown="block" class="api-cell-input">
<p><strong>Входные данные</strong></p>
</th>
<th markdown="block" class="api-cell-output">
<p><strong>Выходные данные</strong></p>
</th>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>BehaviourState/<wbr/>{solutionAlias}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Получает состояния сценариев и элементов процессов в указанном приложении.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения.
</td>
<td markdown="block" class="api-cell-output">
Объект с состояниями сценариев и элементов процессов.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>BehaviourState/<wbr/>{solutionAlias}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Обновляет состояния сценариев и элементов процессов в указанном приложении.
</td>
<td markdown="block" class="api-cell-input">
Объект с состояниями сценариев и элементов процессов.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<th markdown="block" colspan="5" style="overflow-wrap: break-word; width: 99.00%;">
<h3 id="mcetoc_1h7cthcp16">CaseTemplate — шаблоны кейсов (не используются)</h3>
</th>
</tr>
<tr markdown="block">
<th markdown="block" style="overflow-wrap: break-word; width: 6.0%;">
<p style="text-align: center;"><strong>Метод</strong></p>
</th>
<th markdown="block" style="overflow-wrap: break-word; width: 14.00%; max-width: 190px; min-width: 190px;">
<p><strong>Запрос</strong></p>
</th>
<th markdown="block" class="api-cell-description">
<p><strong>Описание</strong></p>
</th>
<th markdown="block" class="api-cell-input">
<p><strong>Входные данные</strong></p>
</th>
<th markdown="block" class="api-cell-output">
<p><strong>Выходные данные</strong></p>
</th>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method post">
POST
</td>
<td markdown="block" class="api-cell-endpoint">
<p><span style="font-family: SFMono-Regular, sans-serif, serif; color: #c7254e; font-size: 10pt;"><span >/webapi/<wbr/>CaseTemplate/<wbr/>{solutionAlias}</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Создает шаблон кейса  с/без связанного шаблона записи.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, объект свойств шаблона кейса.
</td>
<td markdown="block" class="api-cell-output">
Объект с системным именем шаблона кейса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<p><span style="font-family: SFMono-Regular, sans-serif, serif; color: #c7254e; font-size: 10pt;"><span >/webapi/<wbr/>CaseTemplate/<wbr/>{solutionAlias}</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Изменяет шаблон кейса.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, объект свойств шаблона кейса.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method delete">
DELETE
</td>
<td markdown="block" class="api-cell-endpoint">
<p><span style="font-family: SFMono-Regular, sans-serif, serif; color: #c7254e; font-size: 10pt;"><span >/webapi/<wbr/>CaseTemplate/<wbr/>{solutionAlias}/<wbr/>{caseTemplateAlias}</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Удаляет шаблон кейса.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, системное имя шаблона кейса.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<p><span style="font-family: SFMono-Regular, sans-serif, serif; color: #c7254e; font-size: 10pt;"><span >/webapi/<wbr/>CaseTemplate/<wbr/>{solutionAlias}/<wbr/>{caseTemplateAlias}</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Получает свойства шаблона кейса.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, системное имя шаблона кейса.
</td>
<td markdown="block" class="api-cell-output">
Объект свойств шаблона кейса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<p><span style="font-family: SFMono-Regular, sans-serif, serif; color: #c7254e; font-size: 10pt;"><span >/webapi/<wbr/>CaseTemplate/<wbr/>{solutionAlias}/<wbr/>{caseTemplateAlias}/<wbr/>Disable</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Образец архивного кейса.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, системное имя шаблона кейса.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<p><span style="font-family: SFMono-Regular, sans-serif, serif; color: #c7254e; font-size: 10pt;"><span >/webapi/<wbr/>CaseTemplate/<wbr/>{solutionAlias}/<wbr/>{caseTemplateAlias}/<wbr/>Enable</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Разархивирует шаблон кейса.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, системное имя шаблона кейса.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<p><span style="font-family: SFMono-Regular, sans-serif, serif; color: #c7254e; font-size: 10pt;"><span >/webapi/<wbr/>CaseTemplate/<wbr/>List/<wbr/>{solutionAlias}</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Получает все шаблоны кейсов в указанном приложении.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения.
</td>
<td markdown="block" class="api-cell-output">
Массив объектов со свойствами шаблонов кейсов.
</td>
</tr>
<tr markdown="block">
<th markdown="block" colspan="5" style="overflow-wrap: break-word; width: 99.00%;">
<h3 id="mcetoc_1h7cthglo7">Dataset — таблицы</h3>
</th>
</tr>
<tr markdown="block">
<th markdown="block" style="overflow-wrap: break-word; width: 6.0%;">
<p style="text-align: center;"><strong>Метод</strong></p>
</th>
<th markdown="block" style="overflow-wrap: break-word; width: 14.00%; max-width: 190px; min-width: 190px;">
<p><strong>Запрос</strong></p>
</th>
<th markdown="block" class="api-cell-description">
<p><strong>Описание</strong></p>
</th>
<th markdown="block" class="api-cell-input">
<p><strong>Входные данные</strong></p>
</th>
<th markdown="block" class="api-cell-output">
<p><strong>Выходные данные</strong></p>
</th>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method post">
POST
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>Dataset/<wbr/>{solutionAlias}</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Создает таблицу.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, объект конфигурации таблицы.
</td>
<td markdown="block" class="api-cell-output">
Объект конфигурации таблицы.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>Dataset/<wbr/>{solutionAlias}</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Изменяет конфигурацию таблицы.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, объект конфигурации таблицы.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method delete">
DELETE
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>Dataset/<wbr/>{solutionAlias}/<wbr/>{datasetGlobalAlias}</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Удаляет таблицу.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, глобальный псевдоним таблицы: <code>Dataset@<wbr/>templateSystemName.<wbr/>tablesystemName</code>
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>Dataset/<wbr/>{solutionAlias}/<wbr/>{datasetGlobalAlias}</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Получает конфигурацию таблицы.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, глобальный псевдоним таблицы: <code>Dataset@<wbr/>templateSystemName.<wbr/>tablesystemName</code>
</td>
<td markdown="block" class="api-cell-output">
Объект конфигурации таблицы.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>Dataset/<wbr/>List/<wbr/>{templateGlobalAlias}</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Получает все таблицы указанного шаблона.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, глобальный псевдоним шаблона: <code>Template@<wbr/>applicationSystemName.<wbr/>templateSystemName</code>
</td>
<td markdown="block" class="api-cell-output">
Массив объектов с конфигурациями таблиц.
</td>
</tr>
<tr markdown="block">
<th markdown="block" colspan="5" style="overflow-wrap: break-word; width: 99.00%;">
<h3 id="mcetoc_1h7cthk318">Document — файлы, прикрепленные к атрибутам типа «документ»</h3>
</th>
</tr>
<tr markdown="block">
<th markdown="block" style="overflow-wrap: break-word; width: 6.0%;">
<p style="text-align: center;"><strong>Метод</strong></p>
</th>
<th markdown="block" style="overflow-wrap: break-word; width: 14.00%; max-width: 190px; min-width: 190px;">
<p><strong>Запрос</strong></p>
</th>
<th markdown="block" class="api-cell-description">
<p><strong>Описание</strong></p>
</th>
<th markdown="block" class="api-cell-input">
<p><strong>Входные данные</strong></p>
</th>
<th markdown="block" class="api-cell-output">
<p><strong>Выходные данные</strong></p>
</th>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method post">
POST
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Document</span>
</td>
<td markdown="block" class="api-cell-description">
Создает документ.
</td>
<td markdown="block" class="api-cell-input">
Объект свойств документа.
</td>
<td markdown="block" class="api-cell-output">
Объект с идентификатором документа.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Document</span>
</td>
<td markdown="block" class="api-cell-description">
Изменяет свойства документа.
</td>
<td markdown="block" class="api-cell-input">
Объект свойств документа.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method delete">
DELETE
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Document/<wbr/>{documentId}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Удаляет документ.
</td>
<td markdown="block" class="api-cell-input">
Идентификатор документа.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Document/<wbr/>{documentId}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Получает свойства документа.
</td>
<td markdown="block" class="api-cell-input">
Идентификатор документа.
</td>
<td markdown="block" class="api-cell-output">
Объект свойств документа.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Document/<wbr/>{documentId}/<wbr/>Content</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Получает содержимое документа.
</td>
<td markdown="block" class="api-cell-input">
Идентификатор документа.
</td>
<td markdown="block" class="api-cell-output">
Содержимое документа (<code>application/octet-stream</code>).
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method post">
POST
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Document/Content</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Создает документ путем загрузки файла.
</td>
<td markdown="block" class="api-cell-input">
Объект с именем файла и его содержимым <code>(byte array</code>).
</td>
<td markdown="block" class="api-cell-output">
Объект с идентификатором документа.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method post">
POST
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Document/<wbr/>Revision/<wbr/>{documentId}/<wbr/>Content</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Создает версию путем загрузки файла.
</td>
<td markdown="block" class="api-cell-input">
Идентификатор документа, объект с именем файла и его содержимым (<code>byte array</code>).
</td>
<td markdown="block" class="api-cell-output">
Объект с идентификатором версии.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Document/<wbr/>Revision/<wbr/>{revisionId}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Получает свойства версии.
</td>
<td markdown="block" class="api-cell-input">
Идентификатор версии.
</td>
<td markdown="block" class="api-cell-output">
Объект свойств версии.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Document/<wbr/>Revision/<wbr/>{revisionId}/<wbr/>Content</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Получает содержимое версии.
</td>
<td markdown="block" class="api-cell-input">
Идентификатор версии.
</td>
<td markdown="block" class="api-cell-output">
Содержимое версии (<code>application/octet-stream</code>).
</td>
</tr>
<tr markdown="block">
<th markdown="block" colspan="5" style="overflow-wrap: break-word; width: 99.00%;">
<h3 id="mcetoc_1h7cthnpp9">DocumentExportTemplate — шаблоны экспорта</h3>
</th>
</tr>
<tr markdown="block">
<th markdown="block" style="overflow-wrap: break-word; width: 6.0%;">
<p style="text-align: center;"><strong>Метод</strong></p>
</th>
<th markdown="block" style="overflow-wrap: break-word; width: 14.00%; max-width: 190px; min-width: 190px;">
<p><strong>Запрос</strong></p>
</th>
<th markdown="block" class="api-cell-description">
<p><strong>Описание</strong></p>
</th>
<th markdown="block" class="api-cell-input">
<p><strong>Входные данные</strong></p>
</th>
<th markdown="block" class="api-cell-output">
<p><strong>Выходные данные</strong></p>
</th>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method post">
POST
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>DocumentExportTemplate/<wbr/>{solutionAlias}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Создает шаблон экспорта.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, объект свойств шаблона экспорта.
</td>
<td markdown="block" class="api-cell-output">
Системное имя шаблона экспорта.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>DocumentExportTemplate/<wbr/>{solutionAlias}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Изменяет шаблон экспорта.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, объект свойств шаблона экспорта.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method delete">
DELETE
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>DocumentExportTemplate/<wbr/>{solutionAlias}/<wbr/>{exportTemplateGlobalAlias}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Удаляет шаблон экспорта.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, глобальный псевдоним шаблона экспорта: <code>ExportTemplate@<wbr/>templateSystemName.<wbr/>exportTemplate<wbr/>SystemName</code>
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>DocumentExportTemplate/<wbr/>{solutionAlias}/<wbr/>{exportTemplateGlobalAlias}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Получает свойства шаблона экспорта.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, глобальный псевдоним шаблона экспорта: <code>ExportTemplate@<wbr/>templateSystemName.<wbr/>exportTemplate<wbr/>SystemName</code>
</td>
<td markdown="block" class="api-cell-output">
Объект свойств шаблона экспорта.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>DocumentExportTemplate/<wbr/>List/<wbr/>{templateGlobalAlias}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Получает все шаблоны экспорта для указанного шаблона.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, глобальный псевдоним шаблона: <code>Template@<wbr/>applicationSystemName.<wbr/>templateSystemName</code>
</td>
<td markdown="block" class="api-cell-output">
Массив объектов со свойствами шаблонов экспорта.
</td>
</tr>
<tr markdown="block">
<th markdown="block" colspan="5" style="overflow-wrap: break-word; width: 99.00%;">
<h3 id="mcetoc_1h7cthrjaa">Form — формы и правила для форм (кроме стартовых форм процессов и форм пользовательских задач)</h3>
</th>
</tr>
<tr markdown="block">
<th markdown="block" style="overflow-wrap: break-word; width: 6.0%;">
<p style="text-align: center;"><strong>Метод</strong></p>
</th>
<th markdown="block" style="overflow-wrap: break-word; width: 14.00%; max-width: 190px; min-width: 190px;">
<p><strong>Запрос</strong></p>
</th>
<th markdown="block" class="api-cell-description">
<p><strong>Описание</strong></p>
</th>
<th markdown="block" class="api-cell-input">
<p><strong>Входные данные</strong></p>
</th>
<th markdown="block" class="api-cell-output">
<p><strong>Выходные данные</strong></p>
</th>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method post">
POST
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Form/<wbr/>{solutionAlias}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Создает форму.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, объект конфигурации формы.
</td>
<td markdown="block" class="api-cell-output">
Системное имя форм.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Form/<wbr/>{solutionAlias}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Изменяет форму.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, объект конфигурации формы.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method delete">
DELETE
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Form/<wbr/>{solutionAlias}/<wbr/>{formGlobalAlias}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Удаляет форму.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, глобальный псевдоним формы: <code>Form@<wbr/>templateSystemName.<wbr/>formSystemName</code>. <wbr/>
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Form/<wbr/>{solutionAlias}/<wbr/>{formGlobalAlias}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Получает конфигурацию формы.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, глобальный псевдоним формы: <code>Form@<wbr/>templateSystemName.<wbr/>formSystemName</code> <wbr/>
</td>
<td markdown="block" class="api-cell-output">
Объект конфигурации формы.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Form/<wbr/>FormRules/<wbr/>{solutionAlias}/<wbr/>{formGlobalAlias}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Получает правила для формы.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, глобальный псевдоним формы: <code>Form@<wbr/>templateSystemName.<wbr/>formSystemName</code>
</td>
<td markdown="block" class="api-cell-output">
Объект правил для формы.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Form/<wbr/>FormRules/<wbr/>{solutionAlias}/<wbr/>{formGlobalAlias}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Устанавливает правила для формы.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, глобальный псевдоним формы (<code>Form@<wbr/>templateSystemName.<wbr/>formSystemName</code>) <wbr/> , объект правил для формы.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Form/<wbr/>List/<wbr/>{templateGlobalAlias}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Получает все формы указанного шаблона.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, глобальный псевдоним шаблона: <code>Template@<wbr/>solutionSystemName.<wbr/>templateSystemName</code>
</td>
<td markdown="block" class="api-cell-output">
Массив объектов с конфигурациями форм.
</td>
</tr>
<tr markdown="block">
<th markdown="block" colspan="5" style="overflow-wrap: break-word; width: 99.00%;">
<h3 id="mcetoc_1h7cthvsrb">SolutionGitIntegration — контроль версий приложений через Git </h3>
</th>
</tr>
<tr markdown="block">
<th markdown="block" style="overflow-wrap: break-word; width: 6.0%;">
<p style="text-align: center;"><strong>Метод</strong></p>
</th>
<th markdown="block" style="overflow-wrap: break-word; width: 14.00%; max-width: 190px; min-width: 190px;">
<p><strong>Запрос</strong></p>
</th>
<th markdown="block" class="api-cell-description">
<p><strong>Описание</strong></p>
</th>
<th markdown="block" class="api-cell-input">
<p><strong>Входные данные</strong></p>
</th>
<th markdown="block" class="api-cell-output">
<p><strong>Выходные данные</strong></p>
</th>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method post">
POST
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Git/<wbr/>AddRemoteBranch</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Создает ветвь в удаленном репозитории.
</td>
<td markdown="block" class="api-cell-input">
Объект конфигурации репозитория и ветви.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method post">
POST
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Git/<wbr/>Connect</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Инициализирует соединение с указанным репозиторием.
</td>
<td markdown="block" class="api-cell-input">
Объект конфигурации репозитория.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method post">
POST
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Git/<wbr/>GetRepositoryDetails</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Получает коммиты репозитория.
</td>
<td markdown="block" class="api-cell-input">
Объект конфигурации репозитория.
</td>
<td markdown="block" class="api-cell-output">
Массив объектов со свойствами коммитов.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Git/<wbr/>GetUserConfiguration</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Получает учетные данные пользователя репозитория.
</td>
<td markdown="block" class="api-cell-input">
 
</td>
<td markdown="block" class="api-cell-output">
Объект с учетными данными пользователя репозитория.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Git/<wbr/>GetUserSolutionConfig</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Получает конфигурацию репозитория и сведения о пользователе.
</td>
<td markdown="block" class="api-cell-input">
 
</td>
<td markdown="block" class="api-cell-output">
Объект с конфигурацией репозитория и учетными данными пользователя.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method post">
POST
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Git/<wbr/>ListBranches</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Получает все ветви репозитория.
</td>
<td markdown="block" class="api-cell-input">
Объект конфигурации репозитория.
</td>
<td markdown="block" class="api-cell-output">
<p><span style="font-size: 10.0pt; font-family: 'Arial',sans-serif;">Массив объектов со свойствами ветвей.</span></p>
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Git/<wbr/>ListRepositories</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Получает все репозитории подключений к Git.
</td>
<td markdown="block" class="api-cell-input">
 
</td>
<td markdown="block" class="api-cell-output">
Массив объектов с конфигурациями репозиториев.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method post">
POST
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Git/<wbr/>SaveUserCredentials</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Сохраняет учетные данные пользователя.
</td>
<td markdown="block" class="api-cell-input">
Объект с конфигурацией репозитория и учетными данными пользователя.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<th markdown="block" colspan="5" style="overflow-wrap: break-word; background: white; width: 99.00%;">
<h3 id="mcetoc_1h7cti49ic">Heartbeat — мониторинг состояния сервера, процессов, скриптов и служб.</h3>
</th>
</tr>
<tr markdown="block">
<th markdown="block" style="overflow-wrap: break-word; width: 6.0%;">
<p style="text-align: center;"><strong>Метод</strong></p>
</th>
<th markdown="block" style="overflow-wrap: break-word; width: 14.00%; max-width: 190px; min-width: 190px;">
<p><strong>Запрос</strong></p>
</th>
<th markdown="block" class="api-cell-description">
<p><strong>Описание</strong></p>
</th>
<th markdown="block" class="api-cell-input">
<p><strong>Входные данные</strong></p>
</th>
<th markdown="block" class="api-cell-output">
<p><strong>Выходные данные</strong></p>
</th>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>Heartbeat/<wbr/>Details</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Получает статистику использования служб.
</td>
<td markdown="block" class="api-cell-input">
 
</td>
<td markdown="block" class="api-cell-output">
Объект сведений об использовании служб.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>Heartbeat/<wbr/>IsAlive</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Получает статус доступности служб.
</td>
<td markdown="block" class="api-cell-input">
 
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>Heartbeat/<wbr/>ServerDetails</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Получает информацию о сервере.
</td>
<td markdown="block" class="api-cell-input">
 
</td>
<td markdown="block" class="api-cell-output">
Объект сведений о сервере.
</td>
</tr>
<tr markdown="block">
<th markdown="block" colspan="5" style="overflow-wrap: break-word; background: white; width: 99.00%;">
<h3 id="mcetoc_1h7ctiaqjd">ProcessObjects — миграция версии диаграммы процесса</h3>
</th>
</tr>
<tr markdown="block">
<th markdown="block" style="overflow-wrap: break-word; width: 6.0%;">
<p style="text-align: center; page-break-after: avoid;"><strong>Метод</strong></p>
</th>
<th markdown="block" class="api-cell-endpoint">
<p style="text-align: center; page-break-after: avoid;"><strong><span style="font-size: 10.0pt;">Запрос</span></strong></p>
</th>
<th markdown="block" class="api-cell-description">
<p style="text-align: center; page-break-after: avoid;"><strong>Описание</strong></p>
</th>
<th markdown="block" class="api-cell-input">
<p style="text-align: center; page-break-after: avoid;"><strong>Входные данные</strong></p>
</th>
<th markdown="block" class="api-cell-output">
<p style="text-align: center; page-break-after: avoid;"><strong>Выходные данные</strong></p>
</th>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method post">
POST
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>ProcessObjects/<wbr/>Migrate</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Изменяет версию диаграммы экземпляров процесса и перемещает токены.
</td>
<td markdown="block" class="api-cell-input">
Глобальный псевдоним шаблона процесса (<code>ProcessTemplate@<wbr/>applicationSystemName.<wbr/>templateSystemName</code>), идентификатор целевой диаграммы, идентификаторы экземпляров процесса.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<th markdown="block" colspan="5" style="overflow-wrap: break-word; width: 99.00%;">
<h3 id="mcetoc_1h7ctieu3e">ProcessTemplate — шаблоны процессов</h3>
</th>
</tr>
<tr markdown="block">
<th markdown="block" style="overflow-wrap: break-word; width: 6.0%;">
<p style="text-align: center;"><strong>Метод</strong></p>
</th>
<th markdown="block" style="overflow-wrap: break-word; width: 14.00%; max-width: 190px; min-width: 190px;">
<p><strong>Запрос</strong></p>
</th>
<th markdown="block" class="api-cell-description">
<p><strong>Описание</strong></p>
</th>
<th markdown="block" class="api-cell-input">
<p><strong>Входные данные</strong></p>
</th>
<th markdown="block" class="api-cell-output">
<p><strong>Выходные данные</strong></p>
</th>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method post">
POST
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>ProcessTemplate/<wbr/>{solutionAlias}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Создает шаблон процесса.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, объект свойств шаблона процесса.
</td>
<td markdown="block" class="api-cell-output">
Системное имя шаблона процесса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>ProcessTemplate/<wbr/>{solutionAlias}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Изменяет свойства шаблона процесса.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, объект свойств шаблона процесса.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method delete">
DELETE
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>ProcessTemplate/<wbr/>{solutionAlias}/<wbr/>{processTemplateAlias}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Удаляет шаблон процесса.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, системное имя шаблона процесса.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>ProcessTemplate/<wbr/>{solutionAlias}/<wbr/>{processTemplateAlias}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Получает свойства шаблона процесса.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, системное имя шаблона процесса.
</td>
<td markdown="block" class="api-cell-output">
Объект свойств шаблона процесса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>ProcessTemplate/<wbr/>{solutionAlias}/<wbr/>{processTemplateAlias}/<wbr/>Disable</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Шаблон процесса архивирования.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, системное имя шаблона процесса.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>ProcessTemplate/<wbr/>{solutionAlias}/<wbr/>{processTemplateAlias}/<wbr/>Enable</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Разархивирует шаблон процесса.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, системное имя шаблона процесса.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>ProcessTemplate/<wbr/>List/<wbr/>{solutionAlias}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Получает все шаблоны процессов в указанном приложении.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения.
</td>
<td markdown="block" class="api-cell-output">
Массив объектов со свойствами шаблона процесса.
</td>
</tr>
<tr markdown="block">
<th markdown="block" colspan="5" style="overflow-wrap: break-word; width: 99.00%;">
<h3 id="mcetoc_1h7ctjfagf">Record — одна запись (кроме шаблонов процессов)</h3>
</th>
</tr>
<tr markdown="block">
<th markdown="block" style="overflow-wrap: break-word; width: 6.0%;">
<p style="text-align: center;"><strong>Метод</strong></p>
</th>
<th markdown="block" style="overflow-wrap: break-word; width: 14.00%; max-width: 190px; min-width: 190px;">
<p><strong>Запрос</strong></p>
</th>
<th markdown="block" class="api-cell-description">
<p><strong>Описание</strong></p>
</th>
<th markdown="block" class="api-cell-input">
<p><strong>Входные данные</strong></p>
</th>
<th markdown="block" class="api-cell-output">
<p><strong>Выходные данные</strong></p>
</th>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method delete">
DELETE
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Record/<wbr/>{recordId}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Удаляет запись.
</td>
<td markdown="block" class="api-cell-input">
Идентификатор записи.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Record/<wbr/>{recordId}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Получает запись.
</td>
<td markdown="block" class="api-cell-input">
Идентификатор записи.
</td>
<td markdown="block" class="api-cell-output">
Объект со значениями атрибутов записи:  <br/><code>{"attribute<wbr/>SystemName": "value"}</code>
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Record/<wbr/>{recordId}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Изменяет запись.
</td>
<td markdown="block" class="api-cell-input">
Идентификатор записи, объект со значениями атрибутов записи: <code>[{"attribute<wbr/>SystemName": "value"}]</code>
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method post">
POST
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Record/<wbr/>{recordId}/<wbr/>{deepClone}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Запись клонов.
</td>
<td markdown="block" class="api-cell-input">
Идентификатор записи, флаг глубокого клонирования (true — клонировать связанные записи).
</td>
<td markdown="block" class="api-cell-output">
Клонированный идентификатор записи.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Record/<wbr/>{recordId}/<wbr/>Disable</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Запись архива.
</td>
<td markdown="block" class="api-cell-input">
Идентификатор записи.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Record/<wbr/>{recordId}/<wbr/>Enable</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Разархивирует запись.
</td>
<td markdown="block" class="api-cell-input">
Идентификатор записи.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method post">
POST
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Record/<wbr/>{templateGlobalAlias}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Создает запись.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, глобальный псевдоним шаблона (<code>Template@<wbr/>applicationSystemName.<wbr/>templateSystemName</code>) <wbr/> , объект со значениями атрибутов записи: <code>[{"attribute<wbr/>SystemName": "value"}]</code>
</td>
<td markdown="block" class="api-cell-output">
Идентификатор записи.
</td>
</tr>
<tr markdown="block">
<th markdown="block" colspan="5" style="overflow-wrap: break-word; width: 99.00%;">
<h3 id="mcetoc_1h7d30eor0">Record — несколько записей и экспорт/импорт записей (кроме шаблонов процессов)</h3>
</th>
</tr>
<tr markdown="block">
<th markdown="block" style="overflow-wrap: break-word; width: 6.0%;">
<p style="text-align: center;"><strong>Метод</strong></p>
</th>
<th markdown="block" style="overflow-wrap: break-word; width: 14.00%; max-width: 190px; min-width: 190px;">
<p><strong>Запрос</strong></p>
</th>
<th markdown="block" class="api-cell-description">
<p><strong>Описание</strong></p>
</th>
<th markdown="block" class="api-cell-input">
<p><strong>Входные данные</strong></p>
</th>
<th markdown="block" class="api-cell-output">
<p><strong>Выходные данные</strong></p>
</th>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method delete">
DELETE
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Records</span>
</td>
<td markdown="block" class="api-cell-description">
Удаляет указанные записи.
</td>
<td markdown="block" class="api-cell-input">
Массив идентификаторов записей.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Records</span>
</td>
<td markdown="block" class="api-cell-description">
Изменяет указанные записи.
</td>
<td markdown="block" class="api-cell-input">
Массив идентификаторов записей и объектов со значениями атрибутов записей: <code>[{"attribute<wbr/>SystemName": "value"}]</code>.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method delete">
DELETE
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Records/<wbr/>{templateGlobalAlias}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Удаляет все записи из указанного шаблона.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, глобальный псевдоним шаблона: Template@ <wbr/> applicationSystemName. <wbr/> templateSystemName
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Records/<wbr/>{templateGlobalAlias}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Получает все записи указанного шаблона.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, глобальный псевдоним шаблона: <code>Template@ <wbr/> applicationSystemName. <wbr/> templateSystemName</code>
</td>
<td markdown="block" class="api-cell-output">
<p><span style="font-size: 10.0pt; font-family: 'Arial',sans-serif;">Массив объектов со значениями атрибутов записей</span><span style="font-size: 10.0pt; font-family: 'Arial',sans-serif;">: </span><code>[{"attribute<wbr/>SystemName"<wbr/>: "value"}]</code></p>
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method post">
POST
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Records/<wbr/>{templateGlobalAlias}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Создает записи.
</td>
<td markdown="block" class="api-cell-input">
<p><span style="font-size: 10.0pt; font-family: 'Arial',sans-serif;">Глобальный псевдоним шаблона (</span><code>Template@ <wbr/> applicationSystemName. <wbr/> templateSystemName</code>), массив объектов со значениями атрибутов записи: <code>[{"attribute<wbr/>SystemName"<wbr/> : "value"}]</code></p>
</td>
<td markdown="block" class="api-cell-output">
Массив идентификаторов записей.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Records/<wbr/>{templateGlobalAlias}/<wbr/>Export</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Экспортирует все записи указанного шаблона.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, глобальный псевдоним шаблона: <code>Template@ <wbr/> applicationSystemName. <wbr/> templateSystemName</code>
</td>
<td markdown="block" class="api-cell-output">
Серийные записи данных.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Records/<wbr/>BulkEdit</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Обновляет указанные записи с теми же данными.
</td>
<td markdown="block" class="api-cell-input">
Запишите свойства и значения для обновления.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Records/<wbr/>Disable</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Архивирует указанные записи.
</td>
<td markdown="block" class="api-cell-input">
Массив идентификаторов записей.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Records/<wbr/>Enable</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Разархивирует указанные записи.
</td>
<td markdown="block" class="api-cell-input">
Массив идентификаторов записей.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method post">
POST
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Records/<wbr/>Export</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Экспортирует указанные записи.
</td>
<td markdown="block" class="api-cell-input">
Объект глобального псевдонима шаблона записи, массив идентификаторов записей.
</td>
<td markdown="block" class="api-cell-output">
Серийные записи данных.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method post">
POST
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Records/<wbr/>Import</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Импортирует записи из файла.
</td>
<td markdown="block" class="api-cell-input">
Идентификатор загруженного файла с сериализованными данными записей.
</td>
<td markdown="block" class="api-cell-output">
Количество импортированных записей.
</td>
</tr>
<tr markdown="block">
<th markdown="block" colspan="5" style="overflow-wrap: break-word; width: 99.00%;">
<h3 id="mcetoc_1h7ctl9rhh">RecordTemplate — шаблоны записей</h3>
</th>
</tr>
<tr markdown="block">
<th markdown="block" style="overflow-wrap: break-word; width: 6.0%;">
<p style="text-align: center;"><strong>Метод</strong></p>
</th>
<th markdown="block" style="overflow-wrap: break-word; width: 14.00%; max-width: 190px; min-width: 190px;">
<p><strong>Запрос</strong></p>
</th>
<th markdown="block" class="api-cell-description">
<p><strong>Описание</strong></p>
</th>
<th markdown="block" class="api-cell-input">
<p><strong>Входные данные</strong></p>
</th>
<th markdown="block" class="api-cell-output">
<p><strong>Выходные данные</strong></p>
</th>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method post">
POST
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>RecordTemplate/<wbr/>{solutionAlias}</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Создает шаблон записи.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, объект свойств шаблона записи.
</td>
<td markdown="block" class="api-cell-output">
Системное имя шаблона записи.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>RecordTemplate/<wbr/>{solutionAlias}</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Изменяет шаблон записи.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, объект свойств шаблона записи.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method delete">
DELETE
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>RecordTemplate/<wbr/>{solutionAlias}/<wbr/>{recordTemplateAlias}</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Удаляет шаблон записи.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, системное имя шаблона записи.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>RecordTemplate/<wbr/>{solutionAlias}/<wbr/>{recordTemplateAlias}</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Получает шаблон по имени системы.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, системное имя шаблона записи.
</td>
<td markdown="block" class="api-cell-output">
Объект свойств шаблона записи.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>RecordTemplate/<wbr/>{solutionAlias}/<wbr/>{recordTemplateAlias}/<wbr/>Disable</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Образец записи в архив.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, системное имя шаблона записи.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>RecordTemplate/<wbr/>{solutionAlias}/<wbr/>{recordTemplateAlias}/<wbr/>Enable</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Разархивирует шаблон записи.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, системное имя шаблона записи.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>RecordTemplate/<wbr/>List/<wbr/>{solutionAlias}</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Получает все шаблоны записей в указанном приложении.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения.
</td>
<td markdown="block" class="api-cell-output">
Массив объектов со свойствами шаблона записи.
</td>
</tr>
<tr markdown="block">
<th markdown="block" colspan="5" style="overflow-wrap: break-word; width: 99.00%;">
<h3 id="mcetoc_1h7ctleo2i">ReferenceData — записи с указанными значениями атрибутов</h3>
</th>
</tr>
<tr markdown="block">
<th markdown="block" style="overflow-wrap: break-word; width: 6.0%;">
<p style="text-align: center;"><strong>Метод</strong></p>
</th>
<th markdown="block" style="overflow-wrap: break-word; width: 14.00%; max-width: 190px; min-width: 190px;">
<p><strong>Запрос</strong></p>
</th>
<th markdown="block" class="api-cell-description">
<p><strong>Описание</strong></p>
</th>
<th markdown="block" class="api-cell-input">
<p><strong>Входные данные</strong></p>
</th>
<th markdown="block" class="api-cell-output">
<p><strong>Выходные данные</strong></p>
</th>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method delete">
DELETE
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>ReferenceData/<wbr/>Delete</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Удаляет запись с указанными значениями ключевых атрибутов. 
</td>
<td markdown="block" class="api-cell-input">
Объект глобального псевдонима шаблона, объект с системными именами и значениями ключевых атрибутов.
</td>
<td markdown="block" class="api-cell-output">
Идентификатор удалённой записи. Если несколько записей совпадают, возвращает null, и никакие записи не удаляются.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method post">
POST
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>ReferenceData/<wbr/>Get</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Получает значения атрибутов записи с указанными значениями ключевых атрибутов.
</td>
<td markdown="block" class="api-cell-input">
Объект глобального псевдонима шаблона, объект с ключевыми системными именами атрибутов и значениями, массив системных имён атрибутов, которые необходимо получить.
</td>
<td markdown="block" class="api-cell-output">
Объект со значениями атрибутов записи. Если несколько записей совпадают, возвращает null.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>ReferenceData/<wbr/>Put</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Изменяет запись с указанными значениями ключевых атрибутов. 
</td>
<td markdown="block" class="api-cell-input">
Объект глобального псевдонима шаблона, массив системных имён ключевых атрибутов, объект с системными именами и значениями ключевых атрибутов, объект с системными именами атрибутов и их новыми значениями.
</td>
<td markdown="block" class="api-cell-output">
Идентификатор отредактированной записи. Если несколько записей совпадают, возвращает null и никакие записи не редактируются.
</td>
</tr>
<tr markdown="block">
<th markdown="block" colspan="5" style="overflow-wrap: break-word; width: 99.00%;">
<h3 id="mcetoc_1h7ctli71j">Solution — приложения</h3>
</th>
</tr>
<tr markdown="block">
<th markdown="block" style="overflow-wrap: break-word; width: 6.0%;">
<p style="text-align: center;"><strong>Метод</strong></p>
</th>
<th markdown="block" style="overflow-wrap: break-word; width: 14.00%; max-width: 190px; min-width: 190px;">
<p><strong>Запрос</strong></p>
</th>
<th markdown="block" class="api-cell-description">
<p><strong>Описание</strong></p>
</th>
<th markdown="block" class="api-cell-input">
<p><strong>Входные данные</strong></p>
</th>
<th markdown="block" class="api-cell-output">
<p><strong>Выходные данные</strong></p>
</th>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Solution</span>
</td>
<td markdown="block" class="api-cell-description">
Получает все приложения.
</td>
<td markdown="block" class="api-cell-input">
 
</td>
<td markdown="block" class="api-cell-output">
Массив объектов со свойствами приложения.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method post">
POST
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Solution</span>
</td>
<td markdown="block" class="api-cell-description">
Создает приложение.
</td>
<td markdown="block" class="api-cell-input">
Объект со свойствами приложения.
</td>
<td markdown="block" class="api-cell-output">
Системное имя приложения.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Solution </span>
</td>
<td markdown="block" class="api-cell-description">
Изменяет свойства приложения.
</td>
<td markdown="block" class="api-cell-input">
Объект со свойствами приложения.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method delete">
DELETE
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Solution/<wbr/>{solutionAlias}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Удаляет приложение.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Solution/<wbr/>{solutionAlias}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Получает свойства приложения.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения.
</td>
<td markdown="block" class="api-cell-output">
Объект со свойствами приложения.
</td>
</tr>
<tr markdown="block">
<th markdown="block" colspan="5" style="overflow-wrap: break-word; width: 99.00%;">
<h3 id="mcetoc_1h7ctlmo9k">Toolbar — области кнопок и кнопки на них</h3>
</th>
</tr>
<tr markdown="block">
<th markdown="block" style="overflow-wrap: break-word; width: 6.0%;">
<p style="text-align: center;"><strong>Метод</strong></p>
</th>
<th markdown="block" style="overflow-wrap: break-word; width: 14.00%; max-width: 190px; min-width: 190px;">
<p><strong>Запрос</strong></p>
</th>
<th markdown="block" class="api-cell-description">
<p><strong>Описание</strong></p>
</th>
<th markdown="block" class="api-cell-input">
<p><strong>Входные данные</strong></p>
</th>
<th markdown="block" class="api-cell-output">
<p><strong>Выходные данные</strong></p>
</th>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method post">
POST
</td>
<td markdown="block" class="api-cell-endpoint">
<p><span style="font-size: 10pt; color: #c7254e; font-family: SFMono-Regular, sans-serif, serif;"><span >/webapi/<wbr/>Toolbar/<wbr/>{solutionAlias}</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Создает область кнопок.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, объект конфигурации области кнопок.
</td>
<td markdown="block" class="api-cell-output">
Системное имя области кнопок.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<p><span style="font-size: 10pt; color: #c7254e; font-family: SFMono-Regular, sans-serif, serif;"><span >/webapi/<wbr/>Toolbar/<wbr/>{solutionAlias}</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Панель инструментов редактирования.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, объект конфигурации области кнопок.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method delete">
DELETE
</td>
<td markdown="block" class="api-cell-endpoint">
<p><span style="font-size: 10pt; color: #c7254e; font-family: SFMono-Regular, sans-serif, serif;"><span >/webapi/<wbr/>Toolbar/<wbr/>{solutionAlias}/<wbr/>{toolbarGlobalAlias}</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Удаляет область кнопок.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, глобальный псевдоним области кнопок: <code>Toolbar@<wbr/>templateSystemName.<wbr/>toolbarAlias</code>
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<p><span style="font-size: 10pt; color: #c7254e; font-family: SFMono-Regular, sans-serif, serif;"><span >/webapi/<wbr/>Toolbar/<wbr/>{solutionAlias}/<wbr/>{toolbarGlobalAlias}</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Получает область кнопок по имени системы.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, глобальный псевдоним области кнопок: <code>Toolbar@<wbr/>templateSystemName.<wbr/>toolbarAlias</code>
</td>
<td markdown="block" class="api-cell-output">
Объект конфигурации области кнопок.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<p><span style="font-size: 10pt; color: #c7254e; font-family: SFMono-Regular, sans-serif, serif;"><span >/webapi/<wbr/>Toolbar/<wbr/>List/<wbr/>{templateGlobalAlias}</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Получает все области кнопок для указанного шаблона.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, глобальный псевдоним шаблона: <code>Template@<wbr/>applicationSystemName.<wbr/>templateSystemName</code>
</td>
<td markdown="block" class="api-cell-output">
Массив объектов конфигурации области кнопок.
</td>
</tr>
<tr markdown="block">
<th markdown="block" colspan="5" style="overflow-wrap: break-word; width: 99.00%;">
<h3 id="mcetoc_1h7ctlqqql">Transfer — экспорт/импорт модели приложения</h3>
</th>
</tr>
<tr markdown="block">
<th markdown="block" style="overflow-wrap: break-word; width: 6.0%;">
<p style="text-align: center;"><strong>Метод</strong></p>
</th>
<th markdown="block" style="overflow-wrap: break-word; width: 14.00%; max-width: 190px; min-width: 190px;">
<p><strong>Запрос</strong></p>
</th>
<th markdown="block" class="api-cell-description">
<p><strong>Описание</strong></p>
</th>
<th markdown="block" class="api-cell-input">
<p><strong>Входные данные</strong></p>
</th>
<th markdown="block" class="api-cell-output">
<p><strong>Выходные данные</strong></p>
</th>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Transfer/<wbr/>{fileId}/<wbr/>Validate</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Проверяет модель приложения.
</td>
<td markdown="block" class="api-cell-input">
Идентификатор файла модели приложения.
</td>
<td markdown="block" class="api-cell-output">
Объект с итогом проверки.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Transfer/<wbr/>{solutionAlias}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Экспорт модели приложения.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения.
</td>
<td markdown="block" class="api-cell-output">
Объект с ZIP-файлом модели приложения в формате Base64 и сводкой экспорта.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method post">
POST
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Transfer/<wbr/>{solutionAlias}/<wbr/>{fileId}/<wbr/>{publishAfterImport}/<wbr/>{policy}</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Импортирует модель приложения.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, идентификатор файла ZIP/CTF модели приложения, флаг публикации импортированных диаграмм процессов (<code>true</code> — публикация), политика состояния поведения (<code>ApplyNew</code>, <code>ApplyOld</code>, <code>DisableAll</code> или <code>EnableAll</code>).
</td>
<td markdown="block" class="api-cell-output">
Объект со сводкой по импорту приложений.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method post">
POST
</td>
<td markdown="block" class="api-cell-endpoint">
<span >/webapi/<wbr/>Transfer/<wbr/>Upload</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Загружает файл модели приложения.
</td>
<td markdown="block" class="api-cell-input">
ZIP-файл модели приложения в формате Base64.
</td>
<td markdown="block" class="api-cell-output">
Объект с идентификатором загруженного файла.
</td>
</tr>
<tr markdown="block">
<th markdown="block" colspan="5" style="overflow-wrap: break-word; width: 99.00%;">
<h3 id="mcetoc_1h7ctlulam">UserCommand — кнопки</h3>
</th>
</tr>
<tr markdown="block">
<th markdown="block" style="overflow-wrap: break-word; width: 6.0%;">
<p style="text-align: center;"><strong>Метод</strong></p>
</th>
<th markdown="block" style="overflow-wrap: break-word; width: 14.00%; max-width: 190px; min-width: 190px;">
<p><strong>Запрос</strong></p>
</th>
<th markdown="block" class="api-cell-description">
<p><strong>Описание</strong></p>
</th>
<th markdown="block" class="api-cell-input">
<p><strong>Входные данные</strong></p>
</th>
<th markdown="block" class="api-cell-output">
<p><strong>Выходные данные</strong></p>
</th>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method post">
POST
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>UserCommand/<wbr/>{solutionAlias}</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Создает кнопку.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, объект конфигурации кнопки.
</td>
<td markdown="block" class="api-cell-output">
<p><span style="font-size: 10.0pt; font-family: 'Arial',sans-serif;">Системное имя кнопки.</span></p>
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>UserCommand/<wbr/>{solutionAlias}</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Изменяет кнопку.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, объект конфигурации кнопки.
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method delete">
DELETE
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>UserCommand/<wbr/>{solutionAlias}/<wbr/>{userCommandGlobalAlias}</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Удаляет кнопку.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, глобальный псевдоним кнопки: <code>UserCommand@<wbr/>templateSystemName.<wbr/>userCommandAlias</code>
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>UserCommand/<wbr/>{solutionAlias}/<wbr/>{userCommandGlobalAlias}</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Получает конфигурацию кнопки.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, глобальный псевдоним кнопки: <code>UserCommand@<wbr/>templateSystemName.<wbr/>userCommandAlias</code>
</td>
<td markdown="block" class="api-cell-output">
Объект конфигурации кнопки.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>UserCommand/<wbr/>{solutionAlias}/<wbr/>{userCommandGlobalAlias}/<wbr/>Disable</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Архивирует кнопку.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, глобальный псевдоним кнопки: <code>UserCommand@<wbr/>templateSystemName.<wbr/>userCommandAlias</code>
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>UserCommand/<wbr/>{solutionAlias}/<wbr/>{userCommandGlobalAlias}/<wbr/>Enable</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Разархивирует кнопку.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, глобальный псевдоним кнопки: <code>UserCommand@<wbr/>templateSystemName.<wbr/>userCommandAlias</code>
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method get">
GET
</td>
<td markdown="block" class="api-cell-endpoint">
<p>/webapi/<wbr/>UserCommand/<wbr/>List/<wbr/>{templateGlobalAlias}</span> </span></p>
</td>
<td markdown="block" class="api-cell-description">
Получает все кнопки указанного шаблона.
</td>
<td markdown="block" class="api-cell-input">
Системное имя приложения, глобальный псевдоним шаблона: <code>Template@<wbr/>applicationSystemName.<wbr/>templateSystemName</code>
</td>
<td markdown="block" class="api-cell-output">
Массив объектов конфигурации кнопок.
</td>
</tr>
<tr markdown="block">
<th markdown="block" colspan="5" style="overflow-wrap: break-word; width: 99.00%;">
<h3 id="mcetoc_1h7ctm2ppn" style="margin-bottom: 7.2pt;">WorkerEngine — системные службы</h3>
</th>
</tr>
<tr markdown="block">
<th markdown="block" style="overflow-wrap: break-word; width: 6.0%;">
<p style="text-align: center;"><strong>Метод</strong></p>
</th>
<th markdown="block" style="overflow-wrap: break-word; width: 14.00%; max-width: 190px; min-width: 190px;">
<p><strong>Запрос</strong></p>
</th>
<th markdown="block" class="api-cell-description">
<p><strong>Описание</strong></p>
</th>
<th markdown="block" class="api-cell-input">
<p><strong>Входные данные</strong></p>
</th>
<th markdown="block" class="api-cell-output">
<p><strong>Выходные данные</strong></p>
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="overflow-wrap: break-word; background: #0f6ab4; width: 6.0%; vertical-align: middle;">
<p style="text-align: center; page-break-after: avoid;"><span style="color: white;">GET</span></p>
</td>
<td markdown="block" class="api-cell-endpoint">
<p style="page-break-after: avoid;"><span >/webapi/<wbr/>WorkerEngine/<wbr/>GetConfiguration</span> </p>
</td>
<td markdown="block" class="api-cell-description">
<p style="text-indent: 0cm; page-break-after: avoid;">Получает статусы системных служб (<code>true</code> — включена).</p>
</td>
<td markdown="block" class="api-cell-input">
<p style="text-indent: 0cm; page-break-after: avoid;"> </p>
</td>
<td markdown="block" class="api-cell-output">
<p style="text-indent: 0cm; page-break-after: avoid;">Объект со статусами системных служб.</p>
</td>
</tr>
<tr markdown="block">
<td markdown="block" class="api-cell-method put">
PUT
</td>
<td markdown="block" style="overflow-wrap: break-word; background: white; width: 14.00%;">
<span >/webapi/<wbr/>WorkerEngine/<wbr/>SetConfiguration</span> </span>
</td>
<td markdown="block" class="api-cell-description">
Устанавливает статусы системных служб.
</td>
<td markdown="block" class="api-cell-input">
Объект со статусами системных служб (<code>true</code> — включена).
</td>
<td markdown="block" class="api-cell-output">
Объект статуса.
</td>
</tr>
</tbody>
</table>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
