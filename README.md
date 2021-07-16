# meTube
----------

MeTube is a video straming web app built using the Python web development library, Django. It enables to user to register, sign in and upload videos of their choice. Other functionalities include the ability to like and comment videos.

# Quickstart
----------

You need Python 3.8 or later to run meTube.
To check the currently installed version of Python, open your terminal and type:
```
python --version
```

To install Python, you can find the installer packages for your operating system on the official [Python downloads page](https://www.python.org/downloads/).
In Ubuntu, Mint and Debian you can install Python 3 like this:
```
$ sudo apt-get update
$ sudo apt-get install python3.6
```

### Requirements
----------
After you have cloned the repo, you will need to install the requirements to run it.
Open a terminal window inside the project folder and type:
```
pip install -r requirements.txt
```

### Run
----------
To run the project open a terminal window inside the project folder and type:
```
python manage.py runserver
```

## Working with virtualenv
If you are using virtualenv, make sure you are running a python3 environment. Installing via pip3 in a v2 environment will not configure the environment to run installed modules from the command line.
```
$ python3 -m pip install -U virtualenv
$ python3 -m virtualenv env
```
