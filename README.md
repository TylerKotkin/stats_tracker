# <div align="center">Stats Tracker</div>

Stats Tracker is an API created as the back-end to a web application that allows a user to set personal goals and track their progress towards those goals.

The live site can be found [here](https://stats-tracker.herokuapp.com).

### <div align="center">API Endpoints</div>

##### Activities

Method   | URL                                       | Action
------ | ---                                        | -------
GET    | api/activities/                               | Shows a list of all activities a user is tracking
POST   | api/activities/                               | Allows a user to create a new activity to be tracked
GET    | api/activities/{activity_id}/                          | Gives a user information on a single activity being tracked
PUT  | api/activities/{activity_id}/                          | Allows a user to update a single activity
DELETE | api/activities/{activity_id}/                          | Allows a user to delete a single activity
POST   | api/activities/{activity_id}/stats/           | Allows a user to add one day of tracked data for an activity
PUT    | api/activities/{activity_id}/stats/{stat_id}/ | Allows a user to update one day of tracked data for an activity
DELETE | api/activities/{activity_id}/stats/{stat_id}/ | Allows a user to delete one day of tracked data for an activity

##### Users

Method   | URL                                       | Action
------ | ---                                        | -------
GET    | api/users/                               | Returns all registered users
POST   | api/users/                               | Allows for the creation of a user
GET    | api/users/{username}                          | Returns information on one user
PUT  | api/users/{username}                          | Allows a single user's information to be updated
DELETE | api/users/{username}                          | Allows a user to be deleted

##### WhoAmI

Method   | URL                                       | Action
------ | ---                                        | -------
GET    | api/whoami/                               | Returns information on a currently logged in user


## <div align="center">Instructions</div>

* Before the user can run the Stats Tracker application, the user must first clone the `stats_tracker` repo onto their computer. The user will need to create a virtual environment running Python 3 in the `stats_tracker` repo folder.
* To properly run the application, the contents of requirements.txt must be installed.
  * After navigating to the folder containing `requirements.txt`, enter `pip install -r requirements.txt` on the command-line to download the contents of requirements.txt.
* This application is set up to run on PostgreSQL. The local database is named `stats_tracker` with a user of `stats_tracker` and a password of `stats_tracker`. This configuration can be changed in the `settings.py` file. Instructions for setting up PostgreSQL can be found [here](https://github.com/tiyd-python-2015-08/course-resources/blob/master/week7/PostgreSQL-and-Django.md).
* To create the tables for the database, the user must navigate to the `stats_tracker` folder that contains `manage.py` and enter `python manage.py migrate` on the command-line.
* The user must run a local server in order to use the application. After navigating to the `stats_tracker` folder which contains `manage.py`, enter `python manage.py runserver` on the command-line to start the local sever. The application can now be accessed via the user's web browser at `http://localhost:8000/`.
