---
title: 'Comindware интеграция с ФНС'
kbId: 4924
tags: 
    - интеграция
    - ФНС
    - скрипт
hide: tags
---

# Получение данных из интеграция с ФНС {: #example_csharp_tax_service_integrate }

ФНС предоставляет данные компаний, которые, в частности, могут быть необходимы в процессе проверки контрагента. Интеграция с сервисом ФНС осуществляется через подключение к [API-ФНС](https://api-fns.ru/index). 

В данной статье представлен базовый вариант интеграций по следующему сценарию: получение ряда данных компании по указанному ИНН (метод *multinfo*). Интеграция запускается по нажатию кнопки в записи контрагента. Данные забираются из сведений баз данных ФНС, но не все данные могут присутствовать. Если ИНН является действительным, то полученные из базы ФНС данные запишутся в поля, если поля остались пустыми — это означает, что в ФНС таких данных нет. При повторном нажатии на кнопку данные будут перезаписаны.

Для юридического лица будут получены следующие данные:

- Наименование юридического лица;
- Количество сотрудников;
- Годовой доход;
- ФИО руководителя;
- ОГРН;
- КПП;
- Юридический адрес;
- ОКВЭД;
- Вид деятельности.

Для ИП будут получены следующие данные:

- Наименование;
- ФИО руководителя;
- ОГРН;
- Юридический адрес;
- ОКВЭД;
- Вид деятельности.

**Настройка**

**1.** Зарегистрируйтесь на сайте [API-ФНС](https://api-fns.ru/index) и получите API ключ для подключения. 

**2.** В шаблоне записи, где хранятся данные по контрагентам, добавьте кнопку с операцией C# скрипт.

**3.**Скачайте файл со скриптом из вложения к данной статье и модифицируйте его под свои данные:

- строка 23, 25, 30 — "INN" (вставьте в кавычках системное имя атрибута, хранящего данные по ИНН компании);
- строка 31 — "123" (вставьте в кавычках полученный API ключ);
- строка 42 — "NaimenovanieYuL" (вставьте в кавычках системное имя атрибута, хранящего данные по наименованию юридического лица);
- строка 43 — "Kolichestvosotrudnikov" (вставьте в кавычках системное имя атрибута, хранящего данные по количеству сотрудников компании);
- строка 45 — "Godovoydokhod" (вставьте в кавычках системное имя атрибута, хранящего данные по годовому доходу компании);
- строка 46, 57 — "FIOrukovoditelya" (вставьте в кавычках системное имя атрибута, хранящего данные по ФИО руководителя компании);
- строка 48, 58 — "OGRN" (вставьте в кавычках системное имя атрибута, хранящего данные по ОГРН компании);
- строка 49 — "KPP" (вставьте в кавычках системное имя атрибута, хранящего данные по КПП компании);
- строка 50, 59 — "Yuridicheskiyadres" (вставьте в кавычках системное имя атрибута, хранящего данные по юридическому адресу компании);
- строка 52, 61 — "OKVED" (вставьте в кавычках системное имя атрибута, хранящего данные по коду ОКВЭД компании);
- строка 53, 62 — "Viddeyatelnosti" (вставьте в кавычках системное имя атрибута, хранящего данные по виду деятельности компании);
- строка 56 — "Naimenovanie" (вставьте в кавычках системное имя атрибута, хранящего данные по наименованию ИП);
- строка 54, 64 — "Clients" (вставьте в кавычках системное имя шаблона записи, где хранятся все вышеуказанные атрибуты, т.е., текущий шаблон записи).

**4.** Во вкладке «***Скрипт***» вставьте получившийся скрипт.

**5.** Нажмите «***Сохранить***».

**6.** Расположите кнопку на формуе, или на области кнопок для формы.

При выполнении скрипта могут возникнуть следующие ошибки:

- Нет ИНН — атрибут для указания ИНН пустой.
- Проблема с ответом — произошла проблема на сервере ФНС или проблема с API.
- Нет компании по такому ИНН — в базе ФНС не найдена компания по такому ИНН;
- Пустые поля — ФНС не хранит данных по указанной компании.
- Ошибка — Возникла неизвестная ошибка.

``` cs
using System; 
using System.Collections.Generic;
using System.Linq;
using Comindware.Data.Entity;
using Comindware.TeamNetwork.Api.Data.UserCommands;
using Comindware.TeamNetwork.Api.Data;
using RestSharp;
using Newtonsoft.Json.Linq;

class Script{
    public static UserCommandResult Main(UserCommandContext userCommandContext, Comindware.Entities entities)    { 
var contextObjectId = userCommandContext.ObjectIds[0];
var sucssesFlag = true;
string text = "Выполнено";
IRestResponse response = new RestResponse();
string url_Source = "https://api-fns.ru/api/multinfo";
var client = new RestClient(url_Source);
var request = new RestSharp.RestRequest("", Method.GET);
request.AddHeader("RestRequest", "application/json");
request.AddHeader("Accept", "application/json");
long money = 0;
Dictionary<string,object> data = new Dictionary<string,object>();
var Properties = new[] {"INN"};//ИНН для поиска
try{
var data2 = Api.TeamNetwork.ObjectService.GetPropertyValues(new[]{userCommandContext.ObjectIds[0]}, new[] {"INN"});//берем ИНН для поиска
Dictionary<string, object> data_Dictionary = new Dictionary<string, object> {{"id", data2.FirstOrDefault().Key}};
foreach (string Property in Properties){
object _Value = null;
if (data2.FirstOrDefault().Value.TryGetValue(Property, out object obj) && obj != null){_Value = obj;}data_Dictionary.Add(Property, _Value);}
request.AddParameter("req", data_Dictionary["INN"].ToString());
request.AddParameter("key", "123");//Api key
try{
response = client.Execute(request);
if((int)response.StatusCode == 200 && response.Content.Length>15){
JObject jObject = JObject.Parse(response.Content);
var mass = jObject["items"][0].ToString().Split('{');
mass = mass[1].Split(':');
mass = mass[0].Split('"');
string gg= mass[1];
if (gg == "ЮЛ"){
try{money = (long)jObject["items"][0]["ЮЛ"]["Финансы"]["Выручка"] *1000;}catch{}
try{data.Add("NaimenovanieYuL", jObject["items"][0]["ЮЛ"]["НаимСокрЮЛ"].ToString());}catch{}
try{data.Add("Kolichestvosotrudnikov", (int)jObject["items"][0]["ЮЛ"]["ОткрСведения"]["КолРаб"] );
}catch{}
try{data.Add("Godovoydokhod", money);}catch{}
try{data.Add("FIOrukovoditelya", jObject["items"][0]["ЮЛ"]["Руководитель"]["ФИОПолн"].ToString());
}catch{}
try{data.Add("OGRN", jObject["items"][0]["ЮЛ"]["ОГРН"].ToString());}catch{}
try{data.Add("KPP", jObject["items"][0]["ЮЛ"]["КПП"].ToString());}catch{}
try {data.Add("Yuridicheskiyadres", jObject["items"][0]["ЮЛ"]["Адрес"]["АдресПолн"].ToString());
}catch{}
try{data.Add("OKVED", jObject["items"][0]["ЮЛ"]["ОснВидДеят"]["Код"].ToString());}catch{}
try{data.Add("Viddeyatelnosti", jObject["items"][0]["ЮЛ"]["ОснВидДеят"]["Текст"].ToString());}catch{}
Api.TeamNetwork.ObjectService.EditWithAlias("Clients", contextObjectId, data);}
else if(gg == "ИП"){
try{data.Add("Naimenovanie", jObject["items"][0]["ИП"]["НаимПолнЮЛ"].ToString());}catch{}
try{data.Add("FIOrukovoditelya", jObject["items"][0]["ИП"]["ФИОПолн"].ToString());}catch{}
try{data.Add("OGRN", jObject["items"][0]["ИП"]["ОГРНИП"].ToString());}catch{}
try{data.Add("Yuridicheskiyadres", jObject["items"][0]["ИП"]["Адрес"]["АдресПолн"].ToString());
}catch{}
try{data.Add("OKVED", jObject["items"][0]["ИП"]["ОснВидДеят"]["Код"].ToString());}catch{}
try{data.Add("Viddeyatelnosti", jObject["items"][0]["ИП"]["ОснВидДеят"]["Текст"].ToString());
}catch{}
Api.TeamNetwork.ObjectService.EditWithAlias("Clients", contextObjectId, data);}
}
else if( response.Content.Length<15){
text = "Нет компании по такому ИНН";
sucssesFlag = false;}
else{text = "Ошибка";}//ошибка
}
catch(Exception e){
text = "Проблема с ответом "+ e.Message;
sucssesFlag = false;}
}
catch{
text = "Нет Инн";
sucssesFlag = false;}
var result = new UserCommandResult{
Success = sucssesFlag,
Commited = true,
ResultType = UserCommandResultType.Notificate,
Messages = new[]{
new UserCommandMessage{
Severity = SeverityLevel.Normal,
Text = text}}
};
return result;
    }
}
```

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
