# django_music

An introduction to django to the tune of git branches.

## Overview

This repo contains a very basic overview of django 1.11 and utilizes git's tagging to separate steps in basic app creation.

The `README.md`, when viewed on github, should guide through each chapter of the various apps created, in order of complexity. Git tags are used to separate the app into various steps of creation.

### Scope

#### What is covered (in order of complexity)

In the `apps` folder, I have separated the following apps:

1. Basic django html pages `web_pages`
2. Web Apps `web_app`
3. Django ORM `web_db`
4. Web / API Endpoints `web_endpoint`

`apps/django_music` is the project setting app. Base URLs are in `apps/django_music/urls.py`

#### What's not covered

* Deployment
* virtualenvs
* caching / rate-liming / scaling
* Databases (other than sqlite3) — we're just focused on ORM usage
* Static files
* JavaScript

The instructions were written for a linux development machine.

## 0. First Steps

1. Install Python & Git
2. Install virtualenv / pip
3. Clone the repo `git clone github.com/octaflop/django_music` (or `django-admin.py startproject django_music` for projects from scratch).
4. Spin up a virtual environment:

```bash
mkvirtualenv djmusic && pip install -r requirements.txt && add2virtualenv `pwd`/apps
```

* Ensure things are working by running `./manage.py runserver` and opening a browser to `localhost:8000`

## 1. `web_pages`

1. `git checkout -b web_page`
2. `./manage.py startapp web_pages && mv web_pages apps/web_pages`
3. Add the app to `INSTALLED_APPS`
4. Edit `apps/django_music/urls.py`
5. Edit `apps/web_pages/views.py`
6. Create a templates directory: `mkdir -p apps/web_pages/templates/web_pages/`
7. Create a template in that directory
8. Go to the local URL you set, in our case: `localhost:8000/pages/`


## 2. `web_app`

1. Same steps as 1-8 above, substituting `pages` for `app`
2. Let's edit the view this time. Note that template variables are just python dictionaries.
3. Also edit the template.
4. Create a new template and view function: `dynamic.html`.
5. Add a `<form>` to this template using [django forms](https://docs.djangoproject.com/en/1.11/topics/forms/)
6. Don't forget about `csrf`!

## 3. `web_db`

Now we're going to play with Django's ORM and admin: One of the main selling-points of Django vs other Web Libraries.

1. Repeat steps 1-8 in `web_pages`
2. Let's create a few DB models in `models.py`
3. Now we need migrations for them
  1. We create the migrations with `./manage.py makemigrations web_db`
  2. And migrate the db with `./manage.py migrate`. Note, this will migrate all apps if you haven't done so already.
  3. Note, if you're using the repo, that we added a `0002` migration to populate with initial data
4. We make things easier by using `include` for our URLS and adding our own urls.py definitions in the app, instead of the site.
5. We also use [Generic Views](https://docs.djangoproject.com/en/1.10/topics/class-based-views/generic-display/) for listing.
6. And we also add an `admin.py` file for easy management of the DB.
7. We can visit `localhost:8000/admin` and `localhost:8000/db/songs`; etc for more views.
8. Because our urls are named, we can use the `{% url %}` django template tag to directly link to a model's page (or the list page).
