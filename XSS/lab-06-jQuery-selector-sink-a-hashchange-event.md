# DOM XSS in jQuery selector sink using a hashchange event

**Сложность:** Apprentice  
**Тема:** XSS  
**Ссылка:** [PortSwigger](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-jquery-selector-hash-change-event)  

## 1. Описание уязвимости

Эта лаборатория содержит уязвимость кросс-сайтов на основе DOM на домашней странице. Он использует `jQuery's $()` функция селектора для автоматической прокрутки на заданную должность, заголовок которого передается через `location.hash` собственность.

---

## 2. Разведка

Открыл лабораторную - блог с комментариями. В исходном коде (Ctrl+U) уязвимый jQuery-скрипт скрыт, но из названия лабы известно: используется селектор jQuery с `location.hash` и событие `hashchange`. Это DOM-based XSS: значение из хеша подставляется в `$(...).find()` без проверки.

---

## 3. Ход решения

Уязвимость в jQuery-селекторе: `$(window).on('hashchange', function() { $('section.blog-posts').find(location.hash); })`. Значение из хеша подставляется в `.find()` без проверки. Так как `hashchange` срабатывает только при изменении хеша, открыть URL с payload напрямую не получится. Использовал exploit server с iframe: iframe загружает страницу с `#`, а через `onload` меняет хеш на `<img src=x onerror=print()>`. Срабатывает `hashchange`, jQuery парсит payload и выполняет `print()`. Лаба решена.

<iframe src="https://victim.com/#" onload="this.src+='<img src=x onerror=print()>'"></iframe>
