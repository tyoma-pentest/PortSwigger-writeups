# Reflected XSS into a JavaScript string with angle brackets HTML encoded

**Сложность:** Apprentice  
**Тема:** XSS  
**Ссылка:** [PortSwigger](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-string-angle-brackets-html-encoded)  

## 1. Описание уязвимости

Эта лаборатория содержит отраженную уязвимость кросс-сайтов в функции отслеживания поисковых запросов, где кодируются угловые скобки. Рефлексия происходит внутри струны JavaScript. Чтобы решить эту лабораторию, выполните атаку поперечного скрипта, которая вырывается из строки JavaScript и вызывает `alert` функцию.

---

## 2. Разведка

