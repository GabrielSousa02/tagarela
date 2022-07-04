# Tagarela
This is a sample project, demonstrating the usage of [Django](https://www.djangoproject.com/), 
[Django REST Framework](https://www.django-rest-framework.org/), 
[Django-rest-knox](https://james1345.github.io/django-rest-knox/).

## What is `Tagarela`?

- It's only a sample project with a funny name.
  - `Tagarela` in `Portuguese` means `Chatterbox` (FYI - That's the funny part)
- It's a minified backed-RESTFul API, of a twitter-like application.

## Installation:

- Python version: `3.9.11`

- **REQUIRED** packages:
  - `django>=4.0`
  - `django-rest-framework>=3.13.1`
  - `knox>=4.2.0`
  - `gunicorn>=20.1.0`
  - `psycopg2>=2.9.3`

- **OPTIONAL** packages:
  - `django-filter>=22.1`
  - `Markdown>=3.3.7`
  - `black>=22.6.0`
  - `pylint>=2.14.4`

***It's highly recommended that you use a python virtual environment.***

- `Tagarela` is set to connect to a Postgresql database using these parameters:
```python
"default": {
    "ENGINE": "django.db.backends.postgresql_psycopg2",
    "NAME": "tagarela",
    "USER": "postgres",
    "PASSWORD": "",
    "HOST": "127.0.0.1",
    "PORT": "5432",
        }
```
***If you want to connect to a different database, edit the `tagarela/settings.py` file***

## Tagarela's Entity-Relationship Diagram

![](./tagarela-erd.png)





### It can be found running on Heroku

## It can be run locally by following these steps:

- Activate your local environment:

**mac-OS and linux:**
```
source ./.venv/bin/activate
```

**Windows:**
```
/.venv/Script/activate
```
- Update `pip` and install `all dependencies`:

`make install` 

**or**

`make install-required`

**to install only the required packages.**

***Please note that some make features such as `format` and `lint` require the optional packages.***

- Run migrations to the database:

`make migrations`

- Run locally:

`make run`

- Optional features:
  - `make format`
    - This option will format your code using the `black` package.
  - `make lint`
    - This option will perform a static code analysis using the `pylint` package.
  