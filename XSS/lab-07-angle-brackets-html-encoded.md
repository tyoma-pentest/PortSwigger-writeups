# Reflected XSS into attribute with angle brackets HTML-encoded

**Сложность:** Apprentice  
**Тема:** XSS  
**Ссылка:** [PortSwigger](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-attribute-angle-brackets-html-encoded)  

## 1. Описание уязвимости

Эта лаборатория содержит отраженную уязвимость кросс-сайтов в функциональности поискового блога, где угловые скобки кодируются `HTML-кодом`. Чтобы решить эту лабораторию, выполните атаку по сценарию, которая вводит атрибут и называет `alert` функция.

---

## 2. Разведка

Открыл лабораторную - это сайт с блогами, присутсвует параметр `search the blog`, так же под блогами можно оставлять коментарии.

![Решения](images/Screenshot_2026-10-11_20_05_22.png)

---

## 3. Ход решения

