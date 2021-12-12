# financepeer_assesment


## Tech stack
- Flask
- SQLite

## Getting started
It is recommended to use the virtual environment feature. Here are steps to create virtual environment and install the requirements.
you have to delete orm.sqlite from "/instance" to run second time
#### Virtual environment
1. Create virtual environment: `python -m venv .wenv`
2. Activate virtaul environment:
   1. Windows: `.wenv/Scripts/activate.bat`
3. Install requirments: `pip install -r requirements.txt`

### How to start app?
Below are steps to start the application:

#### On windows
To run application on windows, you need to perform below steps.
1. Create environment variable to set application's start file: `set FLASK_APP=app.py`
2. Create environment variable to set application's environment: `set FLASK_ENV=development`
3. Start the application: `flask run`

#### App URL
http://localhost:5000/
