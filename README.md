# @gvadellupa_birthdate_bot
### `@gvadellupa_birthdate_bot` - телеграм бот, который напоминает про дни рождения. По каждой дате происходит 3 напоминания: за 7 дней, за 1 день и непосредственно в день рождения. Алгоритм поиска подходящих дат запускается каждый день в 9 утра. База дней рождения хранится в Google таблице. 

## Для запуска нужен Docker:
## Установка `Docker`
https://docs.docker.com/install/linux/docker-ce/ubuntu/

## Установка `docker-compose`
https://docs.docker.com/compose/install/


## Запустить бот можно командами ниже:
```bash
docker-compose build
docker-compose up
```

При отсутствии `Docker`, команда для запуска будет выглядеть так:
```bash
python bot.py
```