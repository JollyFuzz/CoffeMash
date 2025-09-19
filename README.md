# CoffeMash
Сервис CoffeMash по книге Микросервисы и API

## Установка и настройка
```
pipenv --three 
pipenv shell
pipenv sync 
```

## Запуск
Для запуска сервиса заказов orders
```
uvicorn orders.app:app  --reload
```