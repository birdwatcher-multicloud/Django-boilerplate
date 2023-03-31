# Django-boilerplate

This project was created to help ELTE students to start a Django project taking into account most best practices. The code can be run as follows:

```
git clone https://github.com/birdwatcher-multicloud/Django-boilerplate.git
cd Django-boilerplate
docker-compose build
docker-compose up
```

If you want to create a new app in Django use this command:

docker-compose run --rm app sh -c "python manage.py startapp <app name>"

If you want to create a superuser for admin page use this command:

docker-compose run --rm app sh -c "python manage.py createsuperuser"
