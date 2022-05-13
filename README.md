# Project3_COMP380 Database Portion

## Overview

Project running in Django and sqlite3 for the database backend

## Requirements
Python 3 or higher<br>
Pip 3

## How to
On windows m

## What does this do?
### Download Python 3 and Install
#### Windows
https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe

#### MacOS
`brew install python3`

#### Linux/Ubuntu
`sudo apt install python3`

### Download and install pip3
#### Windows/MacOS
Installed with previous commands

#### Linux/Ubuntu
`sudo apt isntall python3-pip`

### Install Django
`pip3 install django`

### Migrate and Load Data
Migraions files are included already

In the root of the project directory run the following commands
`python3 manage.py migrate`
`python3 manage.py loaddata data.json`

### Run Django Web Server
`python3 manage.py runserver`

If no errors happen

Open up 127.0.0.1:5000 in your browser
