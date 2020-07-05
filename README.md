# Flask-NChooseK

A project I created to learn the basics of [Flask](https://flask.palletsprojects.com/en/1.1.x/) and [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/) in Python 3.

## Installation

There are a few installations required to run a Flask application.

First make sure you have Python3 installed (https://www.python.org/downloads/)

Next you will have to download a virtual enviroment to run the code on. Follow the installation instructions from [this](https://dev.to/sahilrajput/install-flask-and-create-your-first-web-application-2dba) page if you dont already have venv installed. 

Then run the following commands while in the main directory, to set the code running.

```bash
. venv/bin/activate
export FLASK_APP=run.py
flask run
```

(Please note: these instructions are for MacOS, if you google 'How to setup flask', there are plenty of resources for how to set it up on other resources)

## Usage

To use the website, enter a 'N' and 'K' value into the input boxes, and click submit to calculate the N Choose K combinations.