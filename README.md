## Home Manager is a home inventory management system developed in Python using OOP practices and architected using RESTful API standards. It is a multi-tiered application which includes a database, server and GUI.

# How to run this Python application

## Setup
* Make sure python3 is installed: `sudo apt update -y && sudo apt install python3 python3-venv` (Note: This application will not run properly using Python 2.x)
* Create a folder for this project and use it for the rest of the commands below
* Create a Python virtual environment: `python3 -m venv venv`
* This will create a Python environment in the folder venv, using the Python module venv (-m).
* Activate the virtual environment: `source venv/bin/activate`
* Install the following Python packages: sqlalchemy, flask, requests `pip3 install sqlalchemy flask requests`

## Running the application
* To run this application first run the 'create_tables.py' file to initialize our database: `python3 create_tables.py`
* Then run the 'home_api.py' file to run our server at localhost:5000 `python3 home_api.py`
* Finally run the 'home_gui.py' file to run our graphical interface where you can interact with the application `python3 home_gui.py`


