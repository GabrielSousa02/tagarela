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
***If you want to connect to a different database, edit the `path/to/tagarela/settings.py` file***

## Tagarela's Entity-Relationship Diagram

![](./tagarela-erd.png)

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
  
# Example of usage
***It can be found running on [Heroku](https://www.heroku.com/)***

- Base URL: `https://tagarela-test.herokuapp.com`
- Endpoints for user/account usage:
  - Register a user: `/api/account/signup`
    ```json
       POST https://tagarela-test.herokuapp.com/api/account/signup
       Content-Type: application/json
       {
         "username": "Gabe",
         "first_name": "Gabe",
         "last_name": "Sousa",
         "password": "MySuperSafePassword",
         "email": "gabe@email.com.br"
       }
    ```
  - Login: `/api/account/login`
      ```json
       POST https://tagarela-test.herokuapp.com/api/account/login
       Content-Type: application/json
       {
         "username": "Gabe",
         "password": "MySuperSafePassword",
       }
      ```
  - Logout from current device: `/api/account/logout`
      ```json
       POST https://tagarela-test.herokuapp.com/api/account/logout
       Authorization: Token MySuperSafeToken-79e160a07bb5b976e7a87d60b4
      ```
  - Logout from all devices: `/api/account/logoutall`
      ```json
       POST https://tagarela-test.herokuapp.com/api/account/logoutall
       Authorization: Token MySuperSafeToken-79e160a07bb5b976e7a87d60b4
      ```
  - See current user detail: `/api/account/detail`
      ```json
       POST https://tagarela-test.herokuapp.com/api/account/detail
       Authorization: Token MySuperSafeToken-79e160a07bb5b976e7a87d60b4
      ```
  - List all users: `/api/account/`
      ```json
       GET https://tagarela-test.herokuapp.com/api/account/logout
       Authorization: Token MySuperSafeToken-79e160a07bb5b976e7a87d60b4
      ```
  - Follow user by username: `/api/account/follow`
      ```json
       PATCH http://localhost:8000/api/account/follow
       Authorization: Token MySuperSafeToken-79e160a07bb5b976e7a87d60b4
       Content-Type: application/json

       {
           "username": "john"
       }
       ```
  - Unfollow user by username: `/api/account/unfollow`
       ```json
       PATCH http://localhost:8000/api/account/unfollow
       Authorization: Token MySuperSafeToken-79e160a07bb5b976e7a87d60b4
       Content-Type: application/json

       {
           "username": "john"
       }
       ```
- Endpoints for posts:
  - See general feed: `/api/post/general`
      ```json
       GET https://tagarela-test.herokuapp.com/api/post/general
       Authorization: Token MySuperSafeToken-79e160a07bb5b976e7a87d60b4
      ```
  - See personalized feed (Only users being followed): `/api/post/`
      ```json
       GET https://tagarela-test.herokuapp.com/api/post/
       Authorization: Token MySuperSafeToken-79e160a07bb5b976e7a87d60b4
      ```
  - Create a post: `/api/post`
      ```json
      POST https://tagarela-test.herokuapp.com/api/post/
      Authorization: Token MySuperSafeToken-79e160a07bb5b976e7a87d60b4
      Content-Type: application/json
      {
         "content": "Tweet 213214!"
      }
      ```
