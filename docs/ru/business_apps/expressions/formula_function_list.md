---
title: Список функций языка формул
kbId: 4993
tags:
    - язык выражений
    - язык формул
    - выражения
    - формулы
    - enum
    - enumvalue
    - справочник функций
hide:
    - tags
---

# Список функций языка формул {{ companyName }} {: #formula_function_reference }

В данном разделе приведен синтаксис и использование функций в языке формул **{{ companyName }}**.

литералы, атрибуты, переменные, функции, возвращающие значения нужного типа.

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ADD()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Суммирует два значения. Конкатенация строк не поддерживается.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ADD(argument1, argument2)
```

</td>
</tr>

<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `argument1`: число, `argument2`: число.
- `argument1`: длительность, `argument2`: длительность.
- `argument1`: **дата и время**, `argument2`: длительность.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">

- Число
- Длительность
- Дата и время

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ADD(DATE('2024-01-01T01:01:01'), DURATION('P3Y6M4DT12H30M5S'))
```

Результат: `03.07.2027 13:31:06`

Здесь:

- `DATE()` — литерал, который преобразует строку в дату в формате ISO 8601.
- `DURATION()`  — литерал, который преобразует строку в длительность в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ADDDAYS()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">

Добавляет к значению типа «**Дата и время**» в местном часовом поясе указанное число дней.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ADDDAYS(DateTime, Number)
```
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `DateTime`: **дата и время**.
- `Number`: количество дней, которое требуется добавить к первому аргументу.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ADDDAYS(DATE('2024-01-01T01:01:01'), 3)
```

Результат: `04.01.2024 1:01:01`

Здесь:

- `DATE()` — литерал, который преобразует строку в дату в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ADDDAYSUTC()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">

Добавляет указанное количество дней к значению типа «**Дата и время**» в формате UTC.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ADDDAYSUTC(DateTime, Number)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `DateTime`: **дата и время**.
- `Number`: количество дней, которое требуется добавить к первому аргументу.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ADDDAYSUTC(DATE('2024-01-01T01:01:01'), 3)
```

Результат: `04.01.2024 1:01:01`

Здесь:

- `DATE()` — литерал, который преобразует строку в дату в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ADDDUR()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">

Суммирует два значения типа «**Длительность**».
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ADDDUR(argument1, argument2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`, `argument2`: длительность.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Длительность
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ADDDUR(DURATION('P1DT12H30M5S'), DURATION('P1DT12H30M5S'))
```

Результат: `3 д 1 ч 10 с`

Здесь:

- `DURATION()`  — литерал, который преобразует строку в длительность в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ADDHOURS()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">

Добавляет указанное количество часов к значению типа «**Дата и время**».
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ADDHOURS(DateTime, Number)
```
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `DateTime`: **дата и время**.
- `Number`: количество часов, которое требуется добавить к первому аргументу.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ADDHOURS(DATE('2024-01-01T01:01:01'), 3)
```

Результат: `01.01.2024 4:01:01`

Здесь:

- `DATE()` — литерал, который преобразует строку в дату в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ADDHOURSUTC()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">

Добавляет указанное количество часов к значению типа «**Дата и время**» в формате UTC.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ADDHOURSUTC(DateTime, Number)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `DateTime`: **дата и время**.
- `Number`: количество часов, которое требуется добавить к первому аргументу.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ADDHOURSUTC(DATE('2024-01-01T01:01:01'), 3)
```

Результат: `01.01.2024 4:01:01`

Здесь:

- `DATE()` — литерал, который преобразует строку в дату в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ADDLOC()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">

Добавляет значение типа «**Длительность**» к значению типа «**Дата и время**» в местном часовом поясе.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ADDLOC(DateTime, Duration)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `DateTime`: **дата и время**.
- `Duration`: длительность, которую требуется добавить к первому аргументу.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ADDLOC(DATE('2024-01-01T01:01:01'), DURATION('P1DT12H30M5S'))
```

Результат: `02.01.2024 13:31:06`

Здесь:

- `DATE()` — литерал, который преобразует строку в дату в формате ISO 8601.
- `DURATION()`  — литерал, который преобразует строку в длительность в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ADDMINUTES()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">

Добавляет указанное количество минут к значению типа «**Дата и время**» в местном часовом поясе.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ADDMINUTES(DateTime, Number)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `DateTime`: **дата и время**.
- `Number`: количество минут, которое требуется добавить к первому аргументу.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
**дата и время**
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ADDMINUTES(DATE('2024-01-01T01:01:01'), 3)
```

Результат: `01.01.2024 1:04:01`

Здесь:

- `DATE()` — литерал, который преобразует строку в дату в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ADDMINUTESUTC()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">

Добавляет указанное количество минут к значению типа «**Дата и время**» в формате UTC.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ADDMINUTESUTC(DateTime, Number)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `DateTime`: **дата и время**.
- `Number`: количество минут, которое требуется добавить к первому аргументу.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ADDMINUTESUTC(DATE('2024-01-01T01:01:01'), 3)
```

Результат: `01.01.2024 1:04:01`

Здесь:

- `DATE()` — литерал, который преобразует строку в дату в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ADDMONTHS()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">

Добавляет указанное количество месяцев к значению типа «**Дата и время**» в местном часовом поясе.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ADDMONTHS(DateTime, Number)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `DateTime`: **дата и время**.
- `Number`: количество месяцев, которое требуется добавить к первому аргументу.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ADDMONTHS(DATE('2024-01-01T01:01:01'), 3)
```

Результат: `01.04.2024 1:01:01`

Здесь:

- `DATE()` — литерал, который преобразует строку в дату в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ADDMONTHSUTC()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">

Добавляет указанное количество месяцев к значению типа «**Дата и время**» в формате UTC.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ADDMONTHSUTC(DateTime, Number)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `DateTime`: **дата и время**.
- `Number`: количество месяцев, которое требуется добавить к первому аргументу.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ADDMONTHSUTC(DATE('2024-01-01T01:01:01'), 3)
```

Результат: `01.04.2024 1:01:01`

Здесь:

- `DATE()` — литерал, который преобразует строку в дату в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ADDSECONDS()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">

Добавляет указанное количество секунд к значению типа «**Дата и время**» в местном часовом поясе.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ADDSECONDS(DateTime, Number)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `DateTime`: **дата и время**.
- `Number`: количество секунд, которое требуется добавить к первому аргументу.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ADDSECONDS(DATE('2024-01-01T01:01:01'), 3)
```

Результат: `01.01.2024 1:01:04`

Здесь:

- `DATE()` — литерал, который преобразует строку в дату в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ADDSECONDSUTC()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">

Добавляет указанное количество секунд к значению типа «**Дата и время**» в формате UTC.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ADDSECONDSUTC(DateTime, Number)
```
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `DateTime`: **дата и время**.
- `Number`: количество секунд, которое требуется добавить к первому аргументу.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ADDSECONDSUTC(DATE('2024-01-01T01:01:01'), 3)
```

Результат: `01.01.2024 1:01:04`

Здесь:

- `DATE()` — литерал, который преобразует строку в дату в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ADDUTC()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">

Добавляет значение типа «**Длительность**» к значению типа «**Дата и время**» в формате UTC.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ADDUTC(DateTime, Duration)
```
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `DateTime`: **дата и время**.
- `Duration`: длительность, которую требуется добавить к первому аргументу.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Дата и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ADDUTC(DATE('2024-01-01T01:01:01'), DURATION('P1DT12H30M5S'))
```

Результат: `02.01.2024 13:31:06`

Здесь:

- `DATE()` — литерал, который преобразует строку в дату в формате ISO 8601.
- `DURATION()`  — литерал, который преобразует строку в длительность в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ADDYEARS()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">

Добавляет указанное количество лет к значению типа «**Дата и время**» в местном часовом поясе.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ADDYEARS(DateTime, Number)
```
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `DateTime`: **дата и время**.
- `Number`: количество лет, которое требуется добавить к первому аргументу.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
**дата и время**
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ADDYEARS(DATE('2024-01-01T01:01:01'), 3)
```

Результат: `01.01.2027 1:01:01`

Здесь:

- `DATE()` — литерал, который преобразует строку в дату в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ADDYEARSUTC()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Добавляет указанное количество лет к значению типа «**Дата и время**» в формате UTC.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
ADDYEARSUTC(DateTime, Number)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `DateTime`: **дата и время**.
- `Number`: количество лет, которое требуется добавить к первому аргументу.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
**дата и время**
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ADDYEARSUTC(DATE('2024-01-01T01:01:01'), 3)
```

Результат: `01.01.2027 1:01:01`

Здесь:

- `DATE()` — литерал, который преобразует строку в дату в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ALL()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Берет список логических переменных и возвращает значение **Истина**, если все логические переменные принимают значение **Истина**.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>

<td markdown="block">
ALL(list)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`list`: список логических переменных, или список выражений, результатом которых являются значения логического типа.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
значение логического типа
</td>

</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `AND()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Берет два значения логического типа или два выражения, результатом которых являются значения логического типа, и возвращает результат логического умножения этих значений.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
``` cs
AND(bool1, bool2)
```
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
bool1, bool2: значение логического типа или выражение, результатом которого является значение логического типа.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
значение логического типа
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ANY()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Проверка на непустую последовательность.
Проверяет список на не пустоту.
По условию выборки формирует последовательность значений любого типа и проверяет её на не пустоту.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
```
ANY(list), ANY((sequence))
```
Для задания последовательности используйте стандартный запрос `from where select`.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">
```
ANY( from I in db->Tickets where i->product = ‘Data Monsoon’ select i->name)
```
Данное выражение вернет значение Истина, если хотя бы один элемент имеет значение предиката product равным «Data Monsoon».
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `list`: список значений любого типа
- `sequence`: условие выборки

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
значение логического типа
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ANY()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Проверка предиката. Формирует выборку элементов и проверяет, что в ней есть хотя бы один элемент с истинным значением заданного предиката.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

`ANY([(argument1), argument2, argument3])`
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
ANY([(
        from I in db->Tickets where i->product==’Data Monsoon’ select i),
        i,
        i->NeedsQAHelp
    ])
```

Данное выражение вернет значение Истина, если поступил хотя бы один запрос по продукту Data Monsoon, при обработке которого потребуется участие отдела QA.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
- `argument1`: запрос типа from where select, который возвращает последовательность элементов.
- `argument2`: локальная переменная, используемая в запросе.
- `argument3`: логическое утверждение об элементе последовательности, результатом которого является значение логического типа.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
значение логического типа
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ASCENDING()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Сортирует элементы последовательности в порядке возрастания.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
```
ASCENDING(list)
```
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`list`: список значений типа «Число» или строка
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
сортированный список значений
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">
```
ASCENDING('л', 'а', 'и')
```
Возвращает `(String:а String:и String:л)`
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `AVERAGE()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Возвращает среднее арифметическое аргументов.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
AVERAGE(argument1, argument2)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
argument1, `argument2`: число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
число
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `BETWEEN()`

</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">

Проверяет факт вхождения даты или длительности в заданный диапазон. Значения типа «**Дата и время**» должны быть в местном часовом поясе.
</td>
</tr>
<tr markdown="block">
<td markdown="block" >
**Синтаксис**
</td>
<td markdown="block">

``` cs
BETWEEN(Value, Min, Max)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `Value` — дата или длительность для проверки.
- `Min` — начальное значение диапазона.
- `Max` — конечное значение диапазона.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
BETWEEN(DURATION("PT3H15M"), DURATION("PT3H1M"), DURATION("PT3H25M"))
```

Результат: `true`

Здесь:

- `DURATION()` — литерал, который объявляет длительность в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `BETWEENUTC()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">

Проверяет факт вхождения даты или длительности в заданный диапазон. Значения типа «**Дата и время**» должны быть в формате UTC.
</td>
</tr>
<tr markdown="block">
<td markdown="block" >
**Синтаксис**
</td>
<td markdown="block">

``` cs
BETWEENUTC(Date, StartDate, EndDate)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `Date` — дата для проверки.
- `StartDate` — начальное значение диапазона.
- `EndDate` — конечное значение диапазона.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
BETWEENUTC(DATE("2023-01-15"), DATE("2024-08-15"), DATE("2024-08-15"))
```

Результат: `false`

Здесь:

- `DATE()` — литерал, который объявляет дату в формате ISO 8601.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `BOOL()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Преобразует строку в логический тип. Для правильной конвертации, значение строки должно быть равно `true` или `false` без учёта регистра.
</td>
</tr>
<tr markdown="block">
<td markdown="block" >
**Синтаксис**
</td>
<td markdown="block">

``` cs
BOOL(String)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`String` — строка, которая преобразуется в логическое значение,  со значением `true` или `false` (без учёта регистра). При неподходящих значениях атрибута (0, 1, истина, ложь и т. п.) функция возвращает пустое значение.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
BOOL('TrUE')
```

Возвращает `True`
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `CEILING()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Округляет до ближайшего большего целого.
</td>
</tr>
<tr markdown="block">
<td markdown="block" >
**Синтаксис**
</td>
<td markdown="block">

``` cs
CEILING(Number)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">


`Number` — число, которое будет округлено.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
CEILING(4.1)
```

Возвращает `5`
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `CENTURY()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">

Принимает аргумент типа «**Дата и время**» и возвращает числовое значение, соответствующее веку указанной даты в местном часовом поясе.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
CENTURY(DateTime)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">


`DateTime` — дата, для которой требуется определить век.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
CENTURY(DATE("2024-08-15T13:45:15"))
```

Возвращает `21`

Здесь:

`DATE()` — литерал, который объявляет дату в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `COMPARE()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Сравнивает два экземпляра объекта длительность и возвращает целое число:

- `1`, если первая длительности больше второй;
- `0`, если длительности равны;
- `-1`, если первая длительность короче второй.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
COMPARE(argument1, argument2)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">


`argument1`, `argument2`: длительность.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
COMPARE(DURATION("PT3H15M"), DURATION("PT3H16M"))
```

Возвращает `-1`

Здесь:

`DURATION()` — литерал, который объявляет длительность в формате ISO 8601.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `CONCAT()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Преобразует список строк в одну объединённую.
</td>
</tr>
<tr markdown="block">
<td markdown="block" >
**Синтаксис**
</td>
<td markdown="block">

``` cs
CONCAT(list)
```

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`list` — список строк, которые требуется объединить.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
строку
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
CONCAT(LIST("Сумма доходов равна: ", "100000"))
```

Возвращает `Сумма доходов равна: 100000`

Здесь:

`LIST()` — функция, которая использует в качестве аргумента перечень значений одного типа, разделённых запятыми, и возвращает список.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `CONTAINS()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">

Сравнивает две строки между собой. Если первая строка содержит вторую, то возвращает логическое значение **Истина**.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
CONTAINS(String, Substring)
```
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `String` — строка, в которой происходит поиск подстроки.
- `Substring` — подстрока, которая ищется в строке.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
CONTAINS("Это срочная заявка.", "срочн")
```

Возвращает `True`
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `CONVERTTIMEZONE()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Переводит значение типа «**Дата и время**» из локального часового пояса в заданный часовой пояс в формате IANA.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
CONVERTTIMEZONE(Date, TimeZone)
```
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `Date` — дата в местном часовом поясе.
- `TimeZone` — подстрока, которая ищется в строке.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
логическое значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
CONTAINS("Это срочная заявка.", "срочн")
```
Возвращает `True`
</td>
</tr>




</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `COUNT()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Возвращает количество элементов в списке.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
COUNT(argument1)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: список строк
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
число
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `DATETIMEFROMSECONDS()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Преобразует заданное количество секунд в дату.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
DATETIMEFROMSECONDS(argument1)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
**дата и время**
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `DATETIMEINSECONDS()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Преобразует заданную в качестве аргумента дату в количество секунд, прошедшее с 00:00:00 1 января 1970 года (Unix-время).
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
DATETIMEINSECONDS(argument1)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: **дата и время**
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
число
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `DAY()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» и возвращает числовое значение, соответствующее дню месяца указанной даты в местном часовом поясе.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
`DAY(argument1)`
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: **дата и время**
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
число
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `DAYTZ()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» и возвращает числовое значение, соответствующее дню месяца указанной даты в заданном часовом поясе. Идентификатор часового пояса должен быть задан в формате базы данных часовых поясов IANA.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
`DAYTZ(argument1, argument2)`
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: **дата и время**
`argument2`: строка
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
число
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `DECIMAL()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">

Преобразует строку в число.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
DECIMAL(String)
```
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`String` — строка с числовым значением (например, 10, 10,5, 10 000 для русского языка или 10, 10.5, 10,000 — для английского, т. е. значение интерпретируется в соответствии с языком текущего пользователя). При неподходящих значениях атрибута (1 р., $50 и т. п.) функция возвращает пустое значение.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
DECIMAL("10,5")
```

Возвращает `10,5`
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `DIVIDE()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Берет в качестве аргументов два значения числового типа и возвращает результат деления одного на другое.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
`DIVIDE(argument1, argument2)`
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
argument1 (делимое): число
argument2 (делитель): число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
число
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `DURATIONFROMSECONDS()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Преобразует заданное количество секунд в длительность.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
`DURATIONFROMSECONDS(argument1)`
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
длительность
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `DURATIONINSECONDS()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Преобразует заданную длительность в количество секунд.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
`DURATIONINSECONDS(argument1)`
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: длительность
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
число
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `EMPTY()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Берет в качестве аргумента выражение, результатом которого является некоторое значение, и проверяет данное значение на пустоту.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
`EMPTY(argument1)`
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

`argument1`: значение, являющееся результатом выражения, заданного в качестве аргумента, и имеющее один с ним тип.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
значение логического типа
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ENDOFDAY()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» и возвращает дату и время окончания дня, в пределах которого находится значение аргумента.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
`ENDOFDAY(argument1)`
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: **дата и время**
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
**дата и время**
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ENDOFMONTH()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» и возвращает дату и время окончания месяца, в пределах которого находится значение аргумента.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
`ENDOFMONTH(argument1)`
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: **дата и время**
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
**дата и время**
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ENDOFQUARTER()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» и возвращает дату и время окончания квартала, в пределах которого находится значение аргумента.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
`ENDOFQUARTER(argument1)`
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: **дата и время**
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
**дата и время**
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ENDOFWEEK()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» и возвращает дату и время окончания недели, в пределах которого находится значение аргумента.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
`ENDOFWEEK(argument1)`
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: **дата и время**
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
**дата и время**
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ENDOFYEAR()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» и возвращает дату и время окончания года, в пределах которого находится значение аргумента.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
ENDOFYEAR(argument1)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: **дата и время**
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
**дата и время**
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ENDSWITH()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Сравнивает два аргумента и возвращает значение Истина, если значение аргумента1 оканчивается на значение аргумента2, в противном случае возвращает Ложь.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
ENDSWITH(argument1, argument2)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
argument1, `argument2`: строка
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
значение логического типа
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ENUMVALUE()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">

Находит ID значения атрибута типа «<a href="https://kb.{{ companyName }}.ru/article.php?id=2244"><strong>Список значений</strong></a>» по системным именам атрибута и значения.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
<code>ENUMVALUE("AttributeSystemName", "ValueSystemName")</code>
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

<code>AttributeSystemName</code>: строка, системное имя атрибута типа «<strong>Список значений</strong>».
<code>ValueSystemName</code>: строка, системное имя одного из значенийатрибута типа «<strong>Список значений</strong>».

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Строку с ID искомого значения атрибута.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

<code>EQUALS($Status, ID(ENUMVALUE("Status", "Resolved")))</code> — возвращает <code>true</code>, если атрибут<code>Status</code>имеет значение<code>Resolved</code>.
Атрибут типа «<strong>Список значений</strong>» хранит ID своего текущего значения. Поэтому в формуле функция<code>ID()</code>приводит тип <code>string</code> к типу <code>id</code>, чтобы функция <code>EQUALS()</code> сравнивала значения одного типа.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `EQUALS()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Сравнивает два аргумента и возвращает значение Истина, если аргумент1 равен аргументу2, в противном случае возвращает результат Ложь.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
EQUALS()
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
argument1, `argument2`: значение любого типа
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
значение логического типа
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `FIRST()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">

Возвращает первый элемент из списка. При отсутствии элементов в списке FIRST() возвращает пустое значение.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
FIRST(List)
```
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `List` — список значений.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
тип возвращаемого значения совпадает с типом элементов последовательности
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
FIRST((from i in db->music where i>album == ‘Whale Meditation’ select i->song))
```

Возвращает первую песню из альбома "Whale Meditation".
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `FLOOR()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Округляет число в меньшую сторону.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
FLOOR(argument1)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
число
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `FORMAT()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Выполняет форматирование аргументов в соответствии с заданным шаблоном и возвращает отформатированную строку.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
FORMAT(строка задания формата, LIST(argument0, argument1, ..., argument N))
Формат для argument0 задается частью строки, обозначенной как {0}. Формат для argument1 определяется частью строки {1} и так далее.
Аргументы должны быть записаны в следующем виде: LIST(argument0, argument1, ..., argument N).
Также возможно использование функции FORMAT() для конкатенации строк. Например, FORMAT("{0}, {1}", LIST($title,$assignee)).
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
строка задания формата: строка
argument0, argument1, ..., argument N: значения любого типа.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
строка
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `GREATER()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Возвращает логическое значение Истина, если аргумент1 больше аргумента2, в противном случае возвращает результат Ложь.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
GREATER(argument1, argument2)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
argument1, `argument2`: значение логического типа, типа «Число», строка или **дата и время**.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
значение логического типа
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `GREATEREQ()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Возвращает логическое значение Истина, если аргумент1 больше либо равен аргументу2, в противном случае возвращает результат Ложь.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
GREATEREQ(argument1, argument2)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
argument1, `argument2`: значение логического типа, типа «Число», строка или **дата и время**.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
значение логического типа
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `HOUR()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» и возвращает числовое значение, соответствующее часу указанной даты в местном часовом поясе.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
`HOUR(argument1)`
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: **дата и время**
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
число
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `HOURTZ()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» и возвращает числовое значение, соответствующее часу указанной даты в заданном часовом поясе. Идентификатор часового пояса должен быть задан в формате базы данных часовых поясов IANA.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
`HOURTZ(argument1, argument2)`
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
- `argument1`: **дата и время**
` `argument2`: строка
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
число
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ID()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Преобразует строку с ID объекта в его идентификатор.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
<code>ID("ObjectID")</code>
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
<code>ObjectID</code>: строка, системное имя объекта.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
ID объекта
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

<code>ID("oa.21")</code>— возвращает идентификатор шаблона <code>oa.21</code>.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `IF()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Использует в качестве аргументов значения или выражения, результатом которых является некоторое значение. Возвращает аргумент2, если аргумент1 является Истиной, в противном случае возвращает аргумент3.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
IF(argument1, argumen2, argument3)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: значение логического типа или выражение, результатом которого является значение логического типа.
argument2, `argument3`: значение любого типа или выражение, результатом которого является значение любого типа.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Тип возвращаемого значения тот же, что у аргументов argument2 и argument3
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `INDEXOF()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Возвращает номер (отсчитываемый от нуля) позиции, на которой располагается искомая строка в исходной строке. Номер позиции может отсчитываться от произвольного положения (опционально).
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
``` cs
INDEXOF(argument1, argument2, [опциональный argument3])
```
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: исходная строка,
`argument2`: искомая строка,
argument3 (опционально): номер позиции, от которой производится отсчет
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
число
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `INSECONDS()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Преобразует значение длительности в секунды и наоборот.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
INSECONDS(argument1)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: длительность
argument 1: число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
число, если в качестве аргумента используется значение длительности
длительность, если в качестве аргумента используется число
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ISOFORMAT()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Преобразует значение типа «**Дата и время**» в формат ISO.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
`ISOFORMAT(argument1)`
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: **дата и время**
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
строка
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ISTODAY()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Возвращает значение Истина, если задана сегодняшняя дата. В противном случае возвращает результат Ложь.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
`ISTODAY(аргумент1)`
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
аргумент1: **дата и время**
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
значение логического типа
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `JOIN()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Объединяет строки с использованием заданного разделителя.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
`JOIN(argument1, list(argument2, argument3,.. argument N))`
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: разделитель объединяемых строк,
argument2, argument3, ..., argument N (в функции list): объединяемые строки
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
строка
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `LENGTH()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Возвращает количество символов в строке.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
`LENGTH(argument1)`
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: строка
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
число
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `LESS()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Возвращает логическое значение Истина, если аргумент1 меньше аргумента2, в противном случае возвращает результат Ложь.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
`LESS(argument1, argument2)`
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
argument1, `argument2`: значение логического типа, число, строка или **дата и время**.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
значение логического типа
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `LESSEQ()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Возвращает логическое значение Истина, если аргумент1 меньше либо равен аргументу2, в противном случае возвращает результат Ложь.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
`LESSEQ(argument1, argument2)`
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
argument1, `argument2`: значение логического типа, число, строка или **дата и время**..
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
значение логического типа
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `LIST()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Определяет список. Берет перечисление значений одного типа, разделяет их запятыми и возвращает список.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
``` cs
LIST(argument1, …, argument N)
```
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
argument1, …, argument N: значения одного типа
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
список
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `MAKEDATETIME()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Возвращает дату и время в местном часовом поясе, соответствующие указанным значениям года, месяца, дня, часа, минут и секунд.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
MAKEDATETIME(argument1, argument2, argument3, argument4, argument5, argument6)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: числовое значение, соответствующее году.
`argument2`: числовое значение, соответствующее месяцу.
`argument3`: числовое значение, соответствующее дню.
argument4: числовое значение, соответствующее часу.
argument5: числовое значение, соответствующее минутам.
argument6: числовое значение, соответствующее секундам.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
**дата и время**
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `MAKEDATETIMETZ()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Возвращает дату и время в заданном часовом поясе, соответствующие указанным значениям года, месяца, дня, часа, минут и секунд. Идентификатор часового пояса должен быть задан в формате базы данных часовых поясов IANA
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
MAKEDATETIMETZ(argument1, argument2, argument3, argument4, argument5, argument6, argument7)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
аргумент1: числовое значение, соответствующее году.
аргумент1: числовое значение, соответствующее месяцу.
аргумент3: числовое значение, соответствующее дню.
аргумент4: числовое значение, соответствующее часу.
аргумент5: числовое значение, соответствующее минутам.
аргумент6: числовое значение, соответствующее секундам.
аргумент7: строка, соответствующая идентификатору часового пояса
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
**дата и время**
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `MATCHES()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Использует в качестве аргументов строку и регулярное выражение. Возвращает логическое значение Истина, если какая-либо часть строки или строка полностью соответствуетусловию, заданному регулярным выражением. В противном случае возвращает результат Ложь.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
MATCHES(argument1, argument2)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: строка
`argument2`: строка (регулярное выражение)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
значение логического типа
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `MAX()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Определяет максимальное значение при помощи функции GREATER среди всех элементов списка, заданного в качестве аргумента. Элементы списка могут быть значениями или выражениями, результатом которых является значение. Все элементы списка должны быть одного типа.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
MAX(argument1)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: список, состоящий из значений типа «Число», длительность или **дата и время**.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Тип возвращаемого значения тот же, что и у элементов списка. Являющегося аргументом.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `MIN()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Определяет минимальное значение при помощи функции LESS среди всех элементов списка, заданного в качестве аргумента. Элементы списка могут быть значениями или выражениями, результатом которых является значение. Все элементы списка должны быть одного типа.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
MIN(argument1)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: список, состоящий из значений типа «Число», длительность или **дата и время**.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
Тип возвращаемого значения тот же, что и у элементов списка, являющегося аргументом.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `MINUTE()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» и возвращает числовое значение, соответствующее минуте указанной даты в местном часовом поясе.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
MINUTE(argument1)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: **дата и время**
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
число
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `MINUTETZ()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» и возвращает числовое значение, соответствующее минуте указанной даты в заданном часовом поясе. Идентификатор часового пояса должен быть задан в формате базы данных часовых поясов IANA.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
MINUTETZ(argument1, argument2)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: **дата и время**
`argument2`: строка
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
число
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `MONTH()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» и возвращает числовое значение, соответствующее месяцу указанной даты в местном часовом поясе.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
MONTH(argument1)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: **дата и время**
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
число
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `MONTHTZ()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» и возвращает числовое значение, соответствующее месяцу указанной даты в заданном часовом поясе. Идентификатор часового пояса должен быть задан в формате базы данных часовых поясов IANA.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
MONTHTZ(argument1, argument2)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: **дата и время**
`argument2`: строка
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
число
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `NOT()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Использует в качестве аргумента значение логического типа или выражение, результатом которого является значение логического типа. Выполняет операцию логического отрицания над аргументом.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
NOT(argument1)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: логический
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
значение логического типа
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `NOTEQUALS()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Сравнивает два аргумента и возвращает логическое значение Истина, если аргумент1 не равен аргументу2, в противном случае возвращает результат Ложь.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
NOTEQUALS(argument1, argument2)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
argument1, `argument2`: значение любого типа
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
значение логического типа
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `NOTMATCHES()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Использует в качестве аргументов строку и регулярное выражение. Возвращает логическое значение Истина, если часть строки или строка полностью не соответствуют условию, заданному регулярным выражением. В противном случае возвращает результат Ложь.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
NOTMATCHES(argument1, argument2)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: строка
`argument2`: строка (регулярное выражение)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
значение логического типа
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `NOW()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Возвращает текущую дату и время
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
NOW()
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
аргументы не требуются
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
текущую дату и время
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `OBJECT()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Поиск записи шаблона, в которой атрибут имеет указанное значение
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
OBJECT(<code>argument1</code>, <code>argument2</code>, <code>argument3</code>, <code>argument4</code>)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

<code>argument1</code>: системное имя бизнес-приложения
<code>argument2</code>: системное имя шаблона записи
<code>argument3</code>: системное имя атрибута
<code>argument4</code>: значение атрибута
Строковые литералы в аргументах следует заключать в кавычки.

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
ID записи
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `OR()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Берет два значения логического типа или два выражения, результатом которых являются значения логического типа, и возвращает результат логического сложения этих значений.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
OR(argument1, argument2)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
argument1, `argument2`: значение логического типа или выражение, результатом которого является значение логического типа.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
значение логического типа
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `PRODUCT()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Берет в качестве аргументов два значения числового типа и возвращает результат умножения одного на другое.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
PRODUCT(argument1, argument2)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: число
`argument2`: число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
число
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `QUOTIENT()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Использует в качестве аргументов два значения числового типа и возвращает целочисленный результат деления одного на другое.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
QUOTIENT(argument1, argument2)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
argument1(делимое): число
argument2(делитель): число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
целое число
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `REGEXREPLACE()`
</th>
</tr>
<tr markdown="block">
<td markdown="block">
<span >Описание</span>
</td>
<td markdown="block">
<span >Принимает исходную строку</span><code >sourceString</code><span >, находит в ней подстроки по регулярному выражению (шаблону)</span><code >regEx</code><span >, заменяет найденные подстроки замещающей строкой</span><code >replacementString</code><span >и возвращает результирующую строку. Инструмент отладки регулярных выражений со справкой:<a href="https://regex101.com/">https://regex101.com/</a></span>
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
<span >REGEXREPLACE(sourceString, regEx, replacementString)</span>
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

<code>sourceString</code>: исходная строка
<code>regEx</code>: строка с регулярным выражением
<code>replacementString</code>: замещающая строка

</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
строку
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

<code>REGEXREPLACE($FIO,"(.+) (.+) (.+)","$2")</code>— принимает строку вида «Фамилия Имя Отчество» и возвращает Имя (второе слово из трёх).
<code>REGEXREPLACE($Subject,".*\[#([0-9]+)\].*","$1")</code>— принимает строку вида «Рассмотрите заявку [#12345]» и возвращает заявки (12345).
<code>REGEXREPLACE($HTML,"&lt;p class=""title"">(.+)&lt;\/p>","&lt;h1>$1&lt;h1>")</code>— принимает HTML-код, заменяет параграфы класса<code>title</code>на заголовки уровня 1 и возвращает результирующий HTML-код.

</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `REMAINDER()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Использует в качестве аргументов два значения числового типа и возвращает остаток от деления одного значения на другое.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
`REMAINDER(argument1, argument2)`
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
argument1(делимое): число
argument2(делитель): число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
число
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `REPLACE()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Заменяет все экземпляры заданной строки в исходной строке на новое значение.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
`REPLACE(argument1, argument2, argument3)`
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: исходная строка
`argument2`: заменяемая строка
`argument3`: новая строка
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
строка
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `ROUND()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Округляет число к ближайшему целому числу.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
`ROUND(argument1)`
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: число
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
число
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `SECOND()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» и возвращает числовое значение, соответствующее секундам указанной даты в местном часовом поясе.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
`SECOND(argument1)`
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: **дата и время**
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
число
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `SECONDTZ()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» и возвращает числовое значение, соответствующее секундам указанной даты в заданном часовом поясе. Идентификатор часового пояса должен быть задан в формате базы данных часовых поясов IANA.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
`SECONDTZ(argument1, argument2)`
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: **дата и время**
`argument2`: строка
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
число
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `STARTOFDAY()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» и возвращает дату и время начала дня, в пределах которого находится значение аргумента.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
`STARTOF`DAY(argument1)``
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: **дата и время**
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
**дата и время**
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `STARTOFMONTH()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» и возвращает дату и время начала месяца, в пределах которого находится значение аргумента.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
STARTOFMONTH(argument1)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: **дата и время**
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
**дата и время**
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `STARTOFQUARTER()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» и возвращает дату и время начала квартала, в пределах которого находится значение аргумента.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
STARTOFQUARTER(argument1)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: **дата и время**
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
**дата и время**
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `STARTOFWEEK()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» и возвращает дату и время начала недели, в пределах которой находится значение аргумента.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
`STARTOFWEEK(argument1)`
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: **дата и время**
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
**дата и время**
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `STARTOFYEAR()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» и возвращает дату и время начала года, в пределах которой находится значение аргумента.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
`STARTOFYEAR(argument1)`
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: **дата и время**
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
**дата и время**
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `STARTSWITH()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Сравнивает два аргумента и возвращает значение Истина, если значение аргумента1 начинается с значения аргумента2, в противном случае возвращает Ложь.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
`STARTSWITH(argument1, argument2)`
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
argument1, `argument2`: строка
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
значение логического типа
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `SUBSTRING()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Извлекает из строки подстроку определенной длины начиная с заданной позиции (задание длины опционально).
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
`SUBSTRING(argument1, argument2, [опциональный argument3])`
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: строка
`argument2`: номер позиции подстроки (отсчитываемый от нуля)
argument 3(опционально): количество символов в подстроке
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
строка
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `SUBTRACT()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Вычитает значение аргумента2 из значения аргумента1.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
`SUBTRACT(argument1, argument2)`
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: число; `argument2`: число
`argument1`: длительность; `argument2`: длительность
`argument1`: **дата и время**; `argument2`: длительность.
`argument1`: **дата и время**; `argument2`: **дата и время**
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
число
длительность
**дата и время**
длительность
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `SUM()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Суммирует все значения списка, используемого в качестве аргумента. Конкатенация строк не поддерживается.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
`SUM(argument1)`
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: список, состоящий из значений типа «Число» или длительность
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
тип возвращаемого значения тот же, что и у элементов списка, являющегося аргументом
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `TOLOWER()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Переводит строку в нижний регистр (к прописным буквам).
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
`TOLOWER(argument1)`
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: строка
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
строка
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `TOUPPER()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Переводит строку в верхний регистр (к заглавным буквам).
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
`TOUPPER(argument1)`
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: строка
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
строка
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `USER()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Возвращает текущего пользователя или идентификатор текущего пользователя, в зависимости от того, к какому типу данных относится поле. Если вычисляемый атрибут принадлежит типу данных Пользователь, функция возвращает текущего пользователя. Если вычисляемый атрибут текстового типа, функция возвращает идентификатор текущего пользователя.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
`USER()`
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
аргументы не требуются
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
пользователь или строка
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `VALUE()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">

Принимает два аргумента: проверяемое выражение и значение по умолчанию. Возвращает значение первого аргумента, если оно не пустое и не равно NULL, в противном случае возвращает значение второго аргумента, если он есть.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">

``` cs
VALUE(argument, [defaultValue])
```
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">

- `argument` — проверяемое выражение.
- `defaultValue` — значение по умолчанию. Является необязательным аргументом.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
тип возвращаемого значения совпадает с типом проверяемого выражения
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Пример**
</td>
<td markdown="block">

``` cs
VALUE($Amount, "Не заполнено поле Amount")
```

Возвращает значение атрибута _Amount_. В противном случае вернёт текст _«Не заполнено поле Amount»_.
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `WORKDAYS()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Возвращает дату на основании количества рабочих дней с определенной даты, с поправкой на праздники и фактические выходные дни.
Если временная зона рабочего офиса отличается от зоны сервера {{ companyName }}, используйте функцию WORKDAYSTZ().
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
WORKDAYS(argument1, argument2, [опционально list (argument3, argument4, ..., argument M)])
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: **дата и время** начала работы,
`argument2`: количество рабочих дней,
argument3, argument4, …, argument M (в опциональной функции list): праздники и исключения из выходных дней, т. е. если в списке указан рабочий день, он считается праздником, и наоборот, если в списке выходной день, он считается рабочим.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
**дата и время**
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `WORKDAYSTZ()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Возвращает дату на основании количества рабочих дней с определенной даты, с поправкой на праздники и фактические выходные дни, а также на временную зону рабочего офиса.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
WORKDAYSTZ(argument1, argument2, list (argument3, argument4, .., argument M), argument N)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: **дата и время** начала работы
`argument2`: количество рабочих дней
argument3, argument4, …, argument M (в функции list): праздники и исключения из выходных дней, т. е. если в списке указан рабочий день, он считается праздником, и наоборот, если в списке выходной день, он считается рабочим
argument N: временная зона рабочего офиса в формате olson db
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
**дата и время**
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `WORKDAYSDURATION()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Возвращает продолжительность работы между двумя датами, на основании предположения, что рабочий день начинается в 00:00 и длится 24 часа.
Если временная зона рабочего офиса отличается от зоны сервера {{ companyName }}, используйте функцию WORKDAYSDURATIONTZ ().
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
WORKDAYSDURATION(argument1, argument 2, [опционально list
(argument3, argument4, …, argument M)])
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: **дата и время** начала работы,
`argument2`: **дата и время** окончания работы,
argument3, argument4, …, argument M (в опциональной функции list): праздники и исключения из выходных дней, т. е. если в списке указан рабочий день, он считается праздником, и наоборот, если в списке выходной день, он считается рабочим.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
длительность
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `WORKDAYSDURATIONTZ()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Возвращает продолжительность работы между двумя датами с поправкой на временную зону рабочего офиса, на основании предположения, что рабочий день начинается в 00:00 и длится 24 часа.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
WORKDAYSDURATIONTZ(argument1, argument2, list (argument3,
Argument4, .., argument M), argument N)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: **дата и время** начала работы,
`argument2`: **дата и время** окончания работы,
argument3, argument4, …, argument M (в функции list): праздники и исключения из выходных дней, т. е. если в списке указан рабочий день, он считается праздником, и наоборот, если в списке выходной день, он считается рабочим,
argument N: временная зона рабочего офиса в формате olson db.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
длительность
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `WORKHOURS()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Возвращает дату и время на основании количества рабочих часов с определенного момента времени, с поправкой на праздники и фактические выходные дни.
Если временная зона рабочего офиса отличается от зоны сервера {{ companyName }}, используйте функцию WORKHOURSTZ ().
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
WORKHOURS(argument1, argument2, argument3, argument 4, [опционально list (argument5, argument6, .., argument M)])
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: **дата и время** начала работы,
`argument2`: количество рабочих часов,
`argument3`: время начала рабочего дня,
argument4: длительность рабочего дня (должна быть меньше разницы между 24 ч и временем начала рабочего дня),
argument5, argument6, … argument M (в опциональной функции list): праздники и исключения из выходных дней, т. е. если в списке указан рабочий день, он считается праздником, и наоборот, если в списке выходной день, он считается рабочим.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
**дата и время**
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `WORKHOURSDURATION()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Возвращает продолжительность работы между двумя датами при условии, что рабочий день начинается в заданное время и имеет определенную длительность.
Если временная зона рабочего офиса отличается от зоны сервера {{ companyName }}, используйте функцию WORKHOURSDURATIONTZ ().
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
WORKHOURSDURATION(argument1, argument2, argument3, argument 4, [опционально list (argument5, argument6, .., argument M)])
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: **дата и время** начала работы
`argument2`: **дата и время** окончания работы
`argument3`: время начала рабочего дня
argument4: длительность рабочего дня (должна быть меньше разницы между 24 ч и временем начала рабочего дня)
argument5, argument6, .., argument M (в опциональной функции list): праздники и исключения из выходных дней, т. е. если в списке указан рабочий день, он считается праздником, и наоборот, если в списке выходной день, он считается рабочим.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
длительность
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `WORKHOURSDURATIONTZ()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Возвращает продолжительность работы между двумя датами с поправкой на временную зону рабочего офиса, при условии, что рабочий день начинается в заданное время и имеет определенную длительность.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
WORKHOURSDURATIONTZ(argument1, argument2, argument3, argument4, list (argument5, argument6, .., argument M), argument N)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: **дата и время** начала работы
`argument2`: **дата и время** окончания работы
`argument3`: время начала рабочего дня
argument4: длительность рабочего дня (должна быть меньше разницы между 24 ч и временем начала рабочего дня)
argument5, argument6, .., argument M(в функции list): праздники и исключения из выходных дней, т. е. если в списке указан рабочий день, он считается праздником, и наоборот, если в списке выходной день, он считается рабочим
argument N: временная зона рабочего офиса в формате olson db.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
длительность
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `WORKHOURSTZ()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Возвращает дату и время на основании количества рабочих часов с определенного момента времени, с поправкой на праздники и фактические выходные дни, а также на временную зону рабочего офиса.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
WORKHOURSTZ(argument1, argument2, argument3, argument4, list(argument5, argument6, .., argument M), argument N)
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: **дата и время** начала работы,
`argument2`: количество рабочих часов,
`argument3`: время начала рабочего дня,
argument4: длительность рабочего дня (должна быть меньше разницы между 24 ч и временем начала рабочего дня),
argument5, argument6, argument M (в функции list): праздники и исключения из выходных дней, т. е. если всписке указан рабочий день, он считается праздником, и наоборот, если в списке выходной день, он считается рабочим,
argument N: временная зона рабочего офиса в формате olson db.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
**дата и время**
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `YEAR()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» и возвращает числовое значение, соответствующее году указанной даты в местном часовом поясе.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
`YEAR(argument1)`
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
`argument1`: **дата и время**
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
число
</td>
</tr>
</tbody>
</table>

<table markdown="block">
<tbody markdown="block">
<tr markdown="block">
<th colspan="2" markdown="block">

## `YEARTZ()`
</th>
</tr>
<tr markdown="block">
<td markdown="block" style="width:100px">
**Описание**
</td>
<td markdown="block">
Принимает аргумент типа «**Дата и время**» и возвращает числовое значение, соответствующее году указанной даты в заданном часовом поясе.
Идентификатор часового пояса должен быть задан в формате базы данных часовых поясов IANA.
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Синтаксис**
</td>
<td markdown="block">
`YEARTZ(argument1, argument2)`
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Аргументы**
</td>
<td markdown="block">
argument: **дата и время**
argument: строка
</td>
</tr>
<tr markdown="block">
<td markdown="block">
**Результат**
</td>
<td markdown="block">
число
</td>
</tr>
</tbody>
</table>

{% include-markdown ".snippets/hyperlinks_mkdocs_to_kb_map.md" %}
