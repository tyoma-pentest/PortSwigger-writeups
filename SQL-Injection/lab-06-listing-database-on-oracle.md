# SQL injection attack, listing the database contents on Oracle

**Сложность:** Practitioner  
**Тема:** SQL-Injection  
**Ссылка:** [PortSwigger](https://portswigger.net/web-security/sql-injection/examining-the-database/lab-listing-database-contents-oracle)  

## 1. Описание уязвимости

Эта лаборатория содержит уязвимость инъекций SQL в фильтре категории продукта. Результаты запроса возвращаются в ответе приложения. Необходимо определить название этой таблицы и содержащиеся в ней столбцы, а затем извлечь содержимое таблицы, чтобы получить имя пользователя и пароль всех пользователей.
