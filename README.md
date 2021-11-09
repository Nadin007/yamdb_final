![yamdb_workflow](https://github.com/Nadin007/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

# О проекте YaMDbet

Проект YaMDbet собирает отзывы пользователей о различных произведениях искусства.
Произведения поделены на такие категории, как «Книги», «Фильмы», «Музыка».
Список категорий может быть расширен администратором.
Сами произведения не храняться в YaMDb, здесь нельзя смотреть фильмы или слушать музыку.
Произведение может иметь жанровый класс из списка предустановленных.
(например, «Сказка», «Скала» или «Артхаус»). Новые жанры могут быть созданы только администратором.

## Возможнности

- Создавать, удалять, рекагтировать пользователя (может как администратор так и владелец профиля пользователя);
- Выберать уникальный жанр для произведения искусства;
- Создавать и публиковать свои обзоры о разных произведениях;
- Оставить комментарий к обзору или прокоментировать комментарий;
- Просмотр других отзывов со всеми комментариями;

## Технология

использует ряд проектов с открытым исходным кодом для правильной работы:

- [Django 2.2.19] - веб-фреймворк Python высокого уровня.
- [Python 3.9]

И, конечно, сам API_YAMDB имеет открытый исходный код в [частном репозитории][Nadin007/yamdb_final]
на GitHub.

## Установка приложения

Клонировать и перейти в репозиторий с помощью терминала:

```sh
git clone git@github.com:Nadin007/yamdb_final.git
```

```sh
cd api_yamdb
```

Запуск API_YAMDB в режиме разработки:
- Создать и активировать виртуальную среду

```sh
python3 -m venv env

```
```sh
source venv/bin/activate

```
- Установить зависимости из файла requirements.txt

```sh
pip install -r requirements.txt
```
- В папке с файлом manage.py выполните команду:

```sh
cd api_yamdb
```

```sh
python3 manage.py runserver
````

Запуск API_YAMDB в [Docker]:
- Запустить docker-compose:

```sh
docker-compose up -d --build
```
- Выполнить миграции в базе данных:

```sh
docker-compose exec web python manage.py migrate --noinput
```
- Создать суперпользователя:

```sh
docker-compose exec web python manage.py createsuperuser
```
- Собрать статические файлы:

```sh
docker-compose exec web python manage.py collectstatic --no-input
```
- Проект доступен по адресу:

`http://127.0.0.1/api/v1/`

## Инструкция по заполнению .env

- Создайте файл .env с переменными окружения для работы с базой данных:

```sh
touch .env
```
- Вставте в файл данные переменного окружения:

```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

-  Для генерирования нового секретного ключа запустите следующую команду в терменале:

```sh
python3 manage.py shell
>>> from django.core.management.utils import get_random_secret_key
>>> print(get_random_secret_key())
```

- Скопируйте полученный ключ и вставьте в папку .env:

```sh
...

SECRET_KEY =полученный_ключ
```

## О программе закрузки CSV файлов

При загрузке CSV файлов в базу даннных приложения, убедитесь, что названия файлов
соответствуют названию моделей приложения. В качестве пробелов между словами, в
названиях файлов, используйте "_". Можете использовать в названиях как заглавные,
так и прописные буквы. Так же убедитесь, что имена колонок в CSV файлах, которые
явлются ForeignKey, названы по принципу <имя_поля_id> (пример genre_id).
Все CSV файлы желательно закружать в директорию: static/data.

## Работа с загрузчиком CSV файлов

В папке с файлом manage.py выполните команду:

```sh
python3 manage.py load-csv static/data

```

## Тип лицензии

MIT


   [Django 2.2.19]: <https://www.djangoproject.com/download/>
   [Python 3.7]: <https://www.python.org/downloads/release/python-390/>
   [Docker]: <https://docs.docker.com/get-docker/>
   [Nadin007/yamdb_final]: https://github.com/Nadin007/yamdb_final
   

Автор:
Тумарева Надежда