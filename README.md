# Django-boilerplate

If you want to create a new app in Django use this command:

docker-compose run --rm app sh -c "python manage.py startapp <app name>"

If you want to create a superuser for admin page use this command:

docker-compose run --rm app sh -c "python manage.py createsuperuser"
