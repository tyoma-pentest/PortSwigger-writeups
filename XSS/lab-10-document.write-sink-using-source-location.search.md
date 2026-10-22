# DOM XSS in document.write sink using source location.search inside a select element

**Сложность:** Practitioner  
**Тема:** XSS  
**Ссылка:** [PortSwigger](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-document-write-sink-inside-select-element)  

## 1. Описание уязвимости

Эта лаборатория содержит уязвимость кросс-сайтов на основе DOM в функциональности проверки запасов. Он использует JavaScript `document.write` функция, которая записывает данные на страницу. The `document.write` функция называется с данными из `location.search` который вы можете контролировать с помощью `URL-адреса` веб-сайта. Данные заключены в избранный элемент.

## 2. Разведка

