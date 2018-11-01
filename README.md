# Smarty-Trash-Backend
A smart trash can connected to a mobile app that displays disposal statistics and trash levels, in order to encourage citizens to be more conscious of their actions and to promote sustainable living.  This is the backend code.

Guide to file structure:
-
* The first `Smarty_Trash` directory houses the contents of the Django project.
    * The second `Smarty_Trash` directory houses the Django configuration scripts.
        * The file `celery.py` within this directory houses the configuration script for Celery.
    * The `data` directory houses the Django app called "data" for this project.
        * The `templates/data` directory houses the JSON template files for the Data API.
        * The file `models.py` houses the interface for Django with the SQLite database.
        * The file `views.py` houses the renderer for bringing the SQLite db data into a JSON file.
        * The file `tasks.py` houses the Celery task for reading the sensor data from the Raspberry Pi.