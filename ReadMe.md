![Students' Gymkhana 2017](https://img.shields.io/badge/Students'%20Gymkhana-2017-red.svg)
![Status active](https://img.shields.io/badge/Status-active%20development-2eb3c1.svg)
![Django 1.11.3](https://img.shields.io/badge/Django-1.11.3-green.svg)
![Build beta-0.1](https://img.shields.io/badge/Build-beta--0.1-orange.svg)
# Dynamic web portal and forum for Students' Gymkhana of IIT Jodhpur
## Summer project for Students' Gymkhana, IIT Jodhpur
### Purpose
Simplify the workflow of updating the gymkhana website without much knowledge on how to code. And also provide certain utility features.

This project includes:
- A main `web portal` which can be updated dynamically through an admin interface.
- A `forum/discussion` app for general purpose discussions.
- An app called `Konnekt` to find/search people with a certain required skill set.
### Installation:
Requirements:
- Python 3 runtime
- Django 1.11.3
- Other dependencies in `requirements.txt`

Procedure:
- Install [python](https://www.python.org/downloads/) in your environment
- Use pip to install other dependencies from `requirements.txt`
- Setup the database in `src/gymkhana/settings.py` (more details at [djangoproject.com](https://docs.djangoproject.com/) )
- Change to `src` directory
- Make database migrations with `python manage.py makemigrations` followed by `python manage.py migrate`
- Create a superuser with `python manage.py createsuperuser`
- Run development server on localhost with `python manage.py runserver`
