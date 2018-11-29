# Smarty-Trash-Backend
A smart trash can connected to a mobile app that displays disposal statistics and trash levels, in order to encourage citizens to be more conscious of their actions and to promote sustainable living.  This is the backend code.

Guide to Django file structure:
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

Installing and setting up this project:
-
#### Section 0: Raspberry Pi

Install the latest version of Raspbian on a Raspberry Pi (Preferably a Rasbperry Pi 3 Model B+ or later).
#### Section 1: Configuring the Source Code
1. Clone this project: `git clone https://github.com/ktraw2/Smarty-Trash-Backend`
2. Change directory into the downloaded repository: `cd Smarty-Trash-Backend`
3. Create the virtual environment: `python3 -m venv venv`
4. Activate the virtual environment: `source venv/bin/activate`
5. Install the required Python 3 packages: `pip3 install -r requirements.txt`
6. Install RabbitMQ: `sudo apt install rabbitmq-server`
7. Copy the `smbus` module into the venv environment (**Note**: you *must copy* and not move the directory): `cp -r smbus venv/lib/python3.x/site-packages` (**Note**: *python3.x* should be replaced with your Python version i.e. `python3.5`)
8. Change directory into the Django project directory: `cd Smarty_Trash/`
9. Make the database migrations: `python3 manage.py makemigrations`
#### Section 2: Configuring an Access Point (Optional)
##### Note: this section is optional, only do these steps if you want to connect the iPhone running the Smarty Trash app directly to the Raspberry Pi without going through some other network.

Follow the steps in [this guide](https://www.raspberrypi.org/documentation/configuration/wireless/access-point.md) through the section labelled "Add Routing and Masquerade".

Testing this project:
-
* If you wish to get raw data from the sensors, run the `test-sensors.py` script in the root directory.
* If you wish to test Django in a development server, set `DEBUG = True` in the file `Smarty_Trash/Smarty_Trash/settings.py`, then run `python3 manage.py runserver` while in the first `Smarty_Trash` directory.
