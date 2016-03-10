# Установка телефонного справочника

Настоящий документ содержит краткое руководство по запуску приложения на локальном сервере.

Что необходимо:
- наличие python3 и pip3,
- наличие npm, bower и gulp,
- наличие `PostgreSQL`

После выполнения процесса по настройке и запуску приложение телефонного справочника будет запущенно
с использованием сервера разработчика, который идет в комплекте с Django.


## Подготовка и запуск

1. Создать базу данных с именем `phonebook_db` в `PostgreSQL`.

2. Создайте файл `secrets.json` по адресу `backend/phonebook/phonebook/settings/`
и внесите данные:
```json
{
    "SECRET_KEY": "*",
    "DB_USER": "*",
    "DB_PASSWORD": "*",
    "DB_HOST": "*",
    "DB_PORT": "*"
}
```
где `SECRET_KEY` - это секретный ключ, который должен быть большим случайным значением
и хранится в секрете от окружающих,
а `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT` - это имя пользователя, пароль, адрес и порт БД соответственно.
    > Вместо звездочки вставьте соответствующие значения
    
3. Перейти в папку `backend` и выполнить:
```shell
pip3 install -r requirements/local.txt
```

4. Перейти в папку `frontend` и выполнить:
```shell
cd frontend
npm install
bower install
```

5. Создать таблицы. Для этого перейти в папку `backend/phonebook` и выполнить:
```shell
python3 manage.py migrate --settings=phonebook.settings.local
```

6. Создать суперпользователя сайта:
```shell
python manage.py createsuperuser --settings=phonebook.settings.production
```

    В появившемся диалоге установить желаемые имя и пароль.

7. Запустить сервер:
```shell
python3 manage.py runserver --settings=phonebook.settings.local
```

8. Проверить, что сайт доступен по адресу http://localhost:8000

9. Администраторская часть будет доступна по адресу http://localhost:8000/admin

    > В качестве логина и пароля использовать данные суперпользователя из п. 6.
