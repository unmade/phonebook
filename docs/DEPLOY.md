# Запуск в эксплуатацию


Что необходимо:
- чистая сборка серверной Ubuntu 14.04
- подключение к интернету
- умение следовать простым инструкциям

Все что необходимо, это выполнить по порядку ряд простых инструкций, после чего,
телефонный справочник будет готов для эксплуатации. Приложение будет запущено на uWSGI,
а Nginx будет выступать как инвертированный прокси.



## Настройка Базы данных

Для своей работы приложение использует СУБД PostgreSQL.

1. Установить `PostgreSQL`:
    ```shell
    sudo apt-get install postgresql postgresql-contrib
    ```

2. Задать пароль пользователя в консоли `PostgreSQL`:
    ```shell
    sudo -u postgres psql postgres
    ```

    В открывшейся консоли `PostgreSQL` ввести команду для установления пароля пользователя:
    ```sql
    \password postgres
    ```
    и ввести желаемый пароль желаемый пароль

3. Создать новую базу данных:
    ```sql
    CREATE DATABASE phonebook_db;
    ```

4. Покинуть консоль `PostgreSQL`:
    ```sql
    \q
    ```


## Подготовка проекта к эксплуатации

1. Установить "менеджер пакетов" `pip` для python3:
    ```shell
    sudo apt-get update
    sudo apt-get install python-pip3
    ```

2. Установить окружение `virtualenv`:
    ```shell
    sudo pip3 install virtualenv virtualenvwrapper
    ```

3. Установить переменные окружения:
    ```shell
    echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3" >> ~/.bashrc
    echo "export WORKON_HOME=~/Env" >> ~/.bashrc
    echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
    source ~/.bashrc
    ```

    После выполнения данных команд, в "домашней" директории появится папка `Env`.

    > Обычно "домашняя" директория это: /home/user.
    > Перейти в неё можно выполнив `cd ~/`

4. Создать виртуальную переменную:
    ```shell
    mkvirtualenv phonebook
    ```

5. Поместить в корень "домашней" директории проект
    > Здесь и далее подразумевается что папка с проектом называется `phonebook_project`

6. Перейти в директорию проекта и установить зависимости, выполнив команды:
    ```shell
    sudo apt-get install python3-dev python3-setuptools
    sudo apt-get install python3-dev python3-setuptools
    sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk
    cd backend
    sudo pip install -r requirements/production.txt
    ```

7. Создать файл `secrets.json` по адресу `backend/phonebook/phonebook/settings/`
    и внести данные:
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

8. Создать таблицы в базе данных:
    ```shell
    cd ~/phonebook_project/backend/phonebook
    python manage.py migrate --settings=phonebook.settings.production
    ```

9. Создать суперпользователя сайта:
    ```shell
    python manage.py createsuperuser --settings=phonebook.settings.production
    ```

    В появившемся диалоге установить желаемые имя и пароль.

10. Собрать все "статичные" (таблицы стилей, скрипты) элементы:
    ```shell
    python manage.py collectstatic --settings=phonebook.settings.production
    ```

11. Открыть файл `production.py`:
    ```shell
    sudo nano ~/phonebook_project/backend/phonebook/phonebook/settings/production.py
    ```

    найти строку `ALLOWED_HOSTS` и добавить туда IP-адрес сервера, например:

    ```python
    ALLOWED_HOSTS = ['192.168.18.70', '192.168.102.153']
    ```

12. Запустить тестовый сервер:
    ```shell
    python manage.py runserver 0.0.0.0:8000 --settings=phonebook.settings.production
    ```
    Перейти по адресу http://localhost:8000/admin. На экране должна появиться страница входа
    в административную часть сайта.
    > Стили и скрипты пока не будут доступны

    Если страница недоступна, то необходимо перепроверить правильность выполнения действий.


## Настройка uWSGI

1. Установить uWSGI:
    ```shell
    sudo apt-get install python3-dev
    sudo pip install uwsgi
    ```

2. Проверить работу uWSGI, выполнив следующую команду:
    ```shell
    uwsgi --http :8080 --home /home/user/Env/phonebook --chdir /home/user/phonebook_project/backend/phonebook -w phonebook.wsgi
    ```
    Перейти по адресу http://localhost:8000/admin. На экране должна появиться страница входа
    в административную часть сайта.
    > Стили и скрипты пока не будут доступны

3. Создать конфигурационный файл для uWSGI:
    ```shell
    sudo mkdir -p /etc/uwsgi/sites
    cd /etc/uwsgi/sites
    sudo nano phonebook.ini
    ```

    В открывшемся текстовом редакторе поместить следующие строки:
    ```ini
    [uwsgi]
    project = phonebook_project/backend/phonebook
    project_name = phonebook
    base = /home/user
    chdir = %(base)/%(project)
    home = %(base)/Env/%(project_name)
    module = %(project_name).wsgi:application
    master = true
    processes = 5
    socket = %(base)/%(project)/%(project_name).sock
    chmod-socket = 664
    vacuum = true
    ```

4. Добавить uWSGI в автозагрузку:
    ```shell
    sudo nano /etc/init/uwsgi.conf
    ```

    В открывшемся текстовом редакторе поместить следующие строки:
    ```conf
    description "uWSGI application server in Emperor mode"
    start on runlevel [2345]
    stop on runlevel [!2345]
    setuid user
    setgid www-data
    exec /usr/local/bin/uwsgi --emperor /etc/uwsgi/sites
    ```

## Настройка Nginx

1. Установить Nginx:
    ```shell
    sudo apt-get install nginx
    ```

2. Создать конфигурационный файл приложения для Nginx:
    ```shell
    sudo nano /etc/nginx/sites-available/phonebook
    ```

    В открывшемся текстовом редакторе поместить следующие строки:
    ```
    server {
        listen 80;
        server_name SERVER_IP_ADDRESS;

        location = /favicon.ico { access_log off; log_not_found off; }
        location /static/ {
            root /home/user/phonebook_project/backend/phonebook;
        }
        location /media/ {
            root /home/user/phonebook_project/backend/phonebook;
        }

        location / {
            include         uwsgi_params;
            uwsgi_pass      unix:/home/user/phonebook_project/backend/phonebook/phonebook.sock;
        }
    }
    ```
    > Вместо SERVER_IP_ADDRESS указать IP-адрес сервера

3. Добавить ссылку в директорию `sites-enabled`:
    ```shell
    sudo ln -s /etc/nginx/sites-available/phonebook /etc/nginx/sites-enabled
    ```

4. Проверить правильность настройки конфигурации Nginx:
    ```shell
    sudo service nginx configtest
    ```

    В ответ должно появиться сообщение:
    ```shell
    * Testing nginx configuration                         [OK]
    ```

    Если сообщение не появилось, значит настройки некорректны.

5. Запустите uWSGI и Nginx:
    ```shell
    sudo service nginx restart
    sudo serivce uwsgi restart
    ```


## Эксплуатация

1. Для остановки сервера выполнить следующие команды:
    ```shell
    sudo service nginx stop
    sudo service uwsgi stop
    ```

2. Для запуска сервера выполнить следующие команды:
    ```shell
    sudo service nginx start
    sudo service uwsgi start
    ```

3. Для перезапуска сервера использовать следующие команды:
    ```shell
    sudo service nginx restart
    sudo serivce uwsgi restart
    ```

4. Сайт будет доступен по адресу http://SERVER_IP_ADDRESS/:

    > Вместо SERVER_IP_ADDRESS указать IP-адрес сервера

5. Административная часть сайта будет доступна по адресу http://SERVER_IP_ADDRESS/admin

    > В качестве логина и пароля использовать данные созданного суперпользователя.
    > Вместо SERVER_IP_ADDRESS указать IP-адрес сервера
