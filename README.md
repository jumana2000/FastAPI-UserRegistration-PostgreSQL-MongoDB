# FastAPI-UserRegistration-PostgreSQL-MongoDB

#How to run
1. .\venv\Scripts\activate
2. cd .\app\
3. uvicorn main:app --reload

#config.py 
config.py file sets up the configuration for connecting to PostgreSQL and MongoDB.

#models.py
This is a Python module defining two classes using the SQLAlchemy library to create database tables. The User class represents a user and has columns for their id, fullname, email, password, phone, and a relationship with the Profile class. The Profile class represents a user's profile and has columns for its id, user_id, profile_picture, and a relationship with the User class.

#schemas.py
The UserSchema and ProfileSchema define the data structure of the User and Profile models respectively. The RequestUser and RequestProfile are used as input data to create a user and profile respectively. The Response model is used as output data for all endpoints, to return a status code, a status message and the result data (in case of successful response).

#crud.py
This module contain a set of following functions:

get_user - This function gets all the users from the database.

create_user - This function creates a new user in the database.

get_user_by_id - This function retrieves a single user from the database by their id.

#routes.py 
This file includes 3 endpoints:
1. '/create' endpoint - accepts a POST request to create a user
2. '/' endpoint - accepts a GET request to display all users
3. '/{id}' endpoint - accepts GET request to display a user with specific id.
