## UI тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers


### Структура проекта
- `pages` - вспомогательные функции, разделенные по pages
- `tests` - пакет, содержащий тесты, разделенные по pages
- `helpers` - генерация данных дя юзера
- `data` - статичные данные для тестов


### Запуск автотестов
> `$ pytest tests`
> `$ pytest tests --alluredir=allure_results `

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Cоздание HTML-отчета о прохождении тестов**

>  `$ allure serve allure_results `
