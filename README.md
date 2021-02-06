# DRF With Knox Boilerplate

##

### Pre Requisite

- Add a new SECRET_KEY
- Add new Postgres credentials

##

## Instructions

1. Run `pip install -r requirements.txt`
2. Next `python manage.py makemigrations`
3. Then `python manage.py migrate`
4. After that `python manage.py createsuperuser` and fill up the credentials.
5. Finally `python manage.py runserver`

- **POST:** http://127.0.0.1:8000/api/v1/register
- **POST:** http://127.0.0.1:8000/api/v1/login
- **POST:** http://127.0.0.1:8000/api/v1/logout
- **POST:** http://127.0.0.1:8000/api/v1/logoutall
- **PUT:** http://127.0.0.1:8000/api/v1/change-password

##
