!!! tip "Включение буфера обмена в Google Chrome"

    В зависимости от конфигурации сервера **{{ productName }}** для использования буфера обмена в конструкторе диаграмм может потребоваться настроить браузер Google Chrome, как указано ниже.

    1. Введите в адресную строку: 
        
        ``` html
        chrome://flags/#unsafely-treat-insecure-origin-as-secure
        ```
    
    2. Включите функцию «**Insecure origins treated as secure**» (Разрешить небезопасные источники).
    3. Добавьте в список источников адрес сервера **{{ productName }}**, например:

        ``` html
        http://your-host/
        ```

    4. Нажмите кнопку «**Перезапустить**».

    _![Включение буфера обмена в Google Chrome](img/diagram_designer_chrome_clipboard_enable.png)_