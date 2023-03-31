# Django-boilerplate

## Install Docker

The first step is to download Docker Engine or Docker Desktop to your PC or laptop. (https://docs.docker.com/get-docker/)

## Running the project

This project was created to help ELTE students to start a Django project taking into account most best practices. The code can be run as follows:

```
git clone https://github.com/birdwatcher-multicloud/Django-boilerplate.git
cd Django-boilerplate
docker-compose build
docker-compose up
```

If you want to break up your code more, you may want to create several different Django applications. This can be done as follows:

```
docker-compose run --rm app sh -c "python manage.py startapp <app name>"
```

To use the admin platform you need to create a superuser, which you can do with the following code:

```
docker-compose run --rm app sh -c "python manage.py createsuperuser"
```

## Important links for local use

- The swagger documentation is available via the following link: http://127.0.0.1/api/schema/swagger-ui/
- The admin interface is available at this link: http://127.0.0.1/admin/
- The redoc documentation is available at this link: https://127.0.0.1/api/schema/redoc/
