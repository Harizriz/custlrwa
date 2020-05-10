# custlrwa
## Custlr Web Application, by SEGP Group 10a


# Description of project
The basic idea is to create something similar to Booking.com, where a web/mobile app will search other websites for clothes specific to the user's specification. Users should able able to find a listing of clothing  which cater to their specific request. 

# Frontend
**Done by Hariz, Hanis, and Nooh**

To use the website, just start from src boighor/index.html! The files are all there and linked to each other without any external packages required. Other pages can be opened too, but the general flow for the website should always start from index.html, as everything links from that point!

# Backend
**Done By Gerald and Brandon**

The server is hosted on Gerald's PC, and HTTP requests will be made by the frontend to get a JSON file for information.

## Getting Started With Backend

*Make sure you have these installed:*
- python (3.7+, currently 3.7.6 64-bit)
- pip
- pipenv
- PSQL
- PGAdmin 4


Run "pipenv install", and all dependencies for the project itself will be added in 

To check what packages are installed right now, run "pipenv run pip freeze"

*Currently, the project should have some of these installed when you run the above command(everything to run the Django server is in the pipfile):-*
- astroid==2.4.1
- beautifulsoup4==4.9.0
- certifi==2019.11.28
- chardet==3.0.4
- colorama==0.4.3
- Django==2.2.9
- django-cors-headers==3.2.1
- djangorestframework==3.11.0
- get==2019.4.13
- html5lib==1.0.1
- idna==2.9
- isort==4.3.21
- Js2Py==0.70
- lazy-object-proxy==1.4.3
- mccabe==0.6.1
- mysqlclient==1.4.6
- psycopg2==2.8.5
- public==2019.4.13
- pyjsparser==2.7.1
- pylint==2.5.2
- PyMySQL==0.9.3
- pytz==2020.1
- query-string==2019.4.13
- requests==2.23.0
- six==1.14.0
- soupsieve==2.0
- sqlparse==0.3.1
- toml==0.10.0
- typed-ast==1.4.1
- tzlocal==2.0.0
- urllib3==1.25.8
- webencodings==0.5.1
- wrapt==1.12.1

### Once all the packages are installed, and there aren't any errors, run "pipenv shell" to enter the shell for the environment with all the packages installed

Inside the shell is where all the important packages will be installed. The reason why we use a virtual environment to keep all our packages, is so that we know exactly what packages we'll need in our project, and not anything from other projects, etc. To add a new package, install with "pipenv install packagename" i.e to install django I ran "pipenv install django". More information on pipenv can be found here: https://pipenv-fork.readthedocs.io/en/latest/basics.html

## Django, Django REST, on PostGreSQL

**NOTE - A PostGreSQL 4 server should be running, with the database 'custlrwa' setup with an account of the same name before the Django server runs! Password can be changed in the settings.py file**

To run the server and type in 'py manage.py runserver 0.0.0.0:8000' into the CLI in the cwabackend file. The server is hosted on a PC as mentioned before, and NoIP is utilized to redirect the frontend from the link 'custlrwa.ddns.net:8000' to the PC's IP. Migrations made for db - i.e new tables, changes to columns in tables, etc. will require you to run 'py manage.py makemigrations', then 'py manage.py migrate'.


# Git Bash
1. Make sure you are in your directory

```
<!-- git bash ui --!>
/custlrwa (your name)
$
```

2. Committing and Pushing

```
git add .
git commit -m "insert description of changes made"
git push
```
3. Check branch is up to date

```
git status
```
4. To update the latest code from staging
```
git checkout staging
git pull
git checkout *your branch name*
git merge staging
```
