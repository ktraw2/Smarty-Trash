# Smarty-Trash-Backend
A smart trash can connected to a mobile app that displays disposal statistics and trash levels, in order to encourage citizens to be more conscious of their actions and to promote sustainable living.  This is the backend code.

Guide to file structure:
-
* The first `Smarty_Trash` directory houses the contents of the Django project.
    * The second `Smarty_Trash` directory houses the Django configuration scripts.
        * The file `celery.py` houses the configuration script for Celery.
        * The file `urls.py` houses the definitions of the various URL endpoints of the project.
    * The `data` directory houses the Django app called "data" for this project.
        * The `templates/data` directory houses the JSON template files for the Data API.
        * The file `models.py` houses the interface for Django with the SQLite database.
        * The file `views.py` houses the renderer for bringing the SQLite db data into a JSON file.
        * The file `tasks.py` houses the Celery task for reading the sensor data from the Raspberry Pi.
        * The file `sensors.py` houses the classes which provide access to the various sensors used in this project.
        * The file `urls.py` houses the definitions of the various URL endpoints for this app.

Installing this project:
-
* Clone this project: `git clone https://github.com/ktraw2/Smarty-Trash-Backend`
* Change directory into the downloaded repository: `cd Smarty-Trash-Backend`
* Create the virtual environment: `python3 -m venv venv`
* Activate the virtual environment: `source venv/bin/activate`
* Install the required Python packages: `pip3 install -r requirements.txt`        