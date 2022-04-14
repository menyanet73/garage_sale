# garage_sale
Тренировочный проект доски объявлений. 
#### Стек:
Python 3, Django 4.0

## Возможности:
* Регистрация, авторизация
* Размещение, удаление объявлений
* Добавление фотографий товаров(Вывод фотографий на страницу товара реализован не до конца)
* Создание категорий товаров (Через админку)

Стек: Python 3, Django 4.0
## How start project:

Clone a repository and go to command line:

```sh
git clone git@github.com:menyanet73/garage_sale.git
```

```sh
cd garage_sale
```

Create and activate virtual environment:

```sh
python3 -m venv env
```
For Windows:
```sh
source env/Scripts/activate  
```
For Linux:
```sh
source env/bin/activate  
```

Install dependencies from a file requirements.txt:

```sh
python3 -m pip install --upgrade pip
```

```sh
pip install -r requirements.txt
```

Apply migrations:

```sh
python3 manage.py migrate
```
Create superuser:
```sh
python3 manage.py createsuperuser
```


Start project:

```sh
python3 manage.py runserver
```

## Быстрый старт:

Создайте категорию в админке:
```sh
https://127.0.0.1:8000/admin/
```

Теперь можно попробовать функционал по основному адресу:
```sh
https://127.0.0.1/
```
