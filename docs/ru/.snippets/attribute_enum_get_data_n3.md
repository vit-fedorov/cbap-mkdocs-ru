С помощью **N3** для атрибута типа «**Список значений**» можно получить:

- объект с атрибутом:

    ``` turtle
    ("TemplateSystemName" "EnumAttributeSystemName") object:findProperty ?enumAttribute.
    ```

- из объекта с атрибутом — массив возможных значений атрибута в текущей записи:

    ``` turtle
    ?item ?enumAttribute ?enumAttributeValues.
    ```

    **Из этого массива можно получить:**

    - ID текущего значения атрибута:

        ``` turtle
        ?enumAttributeValues cmw:variantName ?enumValueId
        ```

    - системное имя значения атрибута:

        ``` turtle
        ?enumAttributeValues cmw:variantAlias ?enumValueSystemName
        ```

    - код значка значения атрибута:

        ``` turtle
        ?enumAttributeValues cmw:variantIcon ?enumValueIcon
        ```

    - цвет значения атрибута в десятичном формате:

        ``` turtle
        ?enumAttributeValues cmw:color ?enumValueColor
        ```

    - массив объектов с заполненными названиями значения атрибута на английском, русском и немецком языках:

        ``` turtle
        ?enumValueId l10n:text ?enumValueLanguageVersions
        ```

        **Из каждого элемента этого массива можно получить:**

        - код языка:

            ``` turtle
            ?enumValueLanguageVersions l10n:lang ?langCode
            ```

        - название значения атрибута на соответствующем языке:

            ``` turtle
            ?enumValueLanguageVersions l10n:data ?enumValueLocalizedName
            ```
