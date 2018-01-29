# Django Rest Framework Project Seed

A(nother) seed project for the django rest framework.

# Features

  -  [x] Built in Oauth2 Toolkit
  -  [x] Custom user model (That actually works with the default groups model)
  -  [x] Public User registration endpoint 
  -  [x] CORS enabled
  -  [x] Built in Swagger docs (Visit `/docs/`)
  
# How to use
Just create a virtualenv with Python 3.6.4 (That's the version I've used), install the requirements and migrate the database.


# Endpoints

 - POST /account/create/ -> Endpoint to create new users.
 - GET /account/me/ -> Get logged in user data
 - PATCH / PUT /account/me/ -> Update logged in user
 - DELETE /account/me/ -> Delete logged in user
 
This seed also exposes the default Django OAuth Toolkit endpoints for authentication.
Never used the Django OAuth Toolkit before? Read the [great tutorial](https://django-oauth-toolkit.readthedocs.io/en/latest/tutorial/tutorial.html) (There you'll find all the endpoints you need)!


# Random stuff

 - Localization: Right now the API returns all the "django default messages" in german. I don't like that either but our customers do.. You can change this in the settings.py file in `/rest/rest/`.
 - Is there an endpoint to see other users? No. Feel free to create your own :)