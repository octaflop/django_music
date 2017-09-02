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
4. Spin up a virtual environment ```mkvirtualenv djmusic && pip install -r requirements.txt && add2virtualenv `pwd`/apps
```
5. Ensure things are working by running `./manage.py runserver` and opening a browser to `localhost:8000`

## 1. `web_pages`

1. `git checkout -b web_page`
2. `./manage.py startapp web_pages && mv web_pages apps/web_pages`
3. Edit `apps/django_music/urls.py`
4. Edit `apps/web_pages/views.py`
5. Create a templates directory: `mkdir -p apps/web_pages/templates/web_pages/`
6. Create a template in that directory
7. Go to the local URL you set, in our case: `localhost:8000/pages/`
