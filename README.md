# Investing-Site

Проблема: С одной стороны в Кыргызстане малый и средний бизнес, часто не могут найти инвесторов для расширения своего бизнеса или поддержание его на плаву, из-за этого берут кредиты в банках и занимают деньги у родственников, довольно часто закрываются. 

С другой стороны у нас есть потенциальные инвесторы на рынке, которые неделями ищут инвестиционные проекты, и в большинстве случаев уходят на международный рынок в поисках возможностей для инвестиций. 

Но что самое смешное каждый год, Кыргызстан старается привлечь инвесторов из-за рубежа. 

Острое осознание всей боли владельцев малого и среднего бизнеса, подтолкнуло нас на создание этого проекта 

Решение: После тщательного анализа рынка, мы поняли что наш проект, сможет помочь удовлетворить потребности как и владельцев малого и среднего бизнеса, так и инвесторов.

                                                            Настройка проекта
                                                            
Склоньте проект

Установите и активируйте виртуальное окружение

sudo apt install python3-venv python3 -m venv venv source venv/bin/activate

Установите все библиотеки

pip install -r requirements.txt

Этот проект работает на Postgresql, поэтому установите его:

sudo apt-get update sudo apt-get install python3-pip python3-dev libpq-dev postgres postgres-contrib (MacOS) / sudo apt-get install postgresql postgresql-contrib (Ubuntu) sudo -u postgres psql

Введите свой postgresql и создайте базу данных:

sudo -u postgres psql CREATE DATABASE ; CREATE USER WITH PASSWORD 'your_super_secret_password'; ALTER ROLE SET client_encoding TO 'utf8'; ALTER ROLE SET default_transaction_isolation TO 'read committed'; ALTER ROLE SET timezone TO 'UTC'; GRANT ALL PRIVILEGES ON DATABASE TO '';

Синхронизируйте базу данных с Django:

    python manage.py makemigrations
    python manage.py migrate

Создать суперпользователя

    python manage.py createsuperuser

И, наконец, запустите проект:

    python manage.py runserver
