# Django Test

Testing how to setup and run a simple Django project.

## Getting Started

### Virtual Env

* Enter: `django-env\Scripts\activate.bat`
* Exit: `deactivate`

### Server

* Run: `python manage.py runserver`
* Exit: `Ctrl + C`

### Database Migrations

* Make: `python manage.py makemigrations`
* Show waiting: `python manage.py showmigrations`
* Show SQL: `python manage.py sqlmigrate <appname> <migrationnamer>`
* Run: `python manage.py migrate`

### Apps

* Create: `python manage.py startapp <NAME>`

### Admin Site

* Create superuser: `python manage.py createsuperuser`

### Shell

* Open: `python manage.py shell`

### Model API

* Manager: `<CLASS>.objects`
* Get all: `<CLASS>.objects.all()`
* Get single instance: `<CLASS>.objects.get(<FIELD>=<VALUE>)`
* Get certain objects that include field value: `<CLASS>.filter(<FIELD>=<VALUE>)`
* Get certain objects that exclude field value: `<CLASS>.exclude(<FIELD>=<VALUE>)`
* Save: `<OBJECT>.save()`
* Delete: `<OBJECT>.delete()`

**Note:** If the `<FIELD>` is a foreign key the format will be `<FIELD>__<CLASS>`
