# This file contains configuration variables that shouldn’t be in version control.
# This includes things like API keys and database URIs containing passwords.
# A template version is included here to adapt as needed.

# PLEASE IGNORE IN YOUR LOCAL INDEX:
# git update-index --skip-worktree instance/config.py

# This also contains variables that are specific to this particular instance of your application.
# For example, you might have DEBUG = False in config.py, but set DEBUG = True in instance/config.py on your local machine for development.
# Since this file will be read in after config.py, it will override it and set DEBUG = True.

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Turns on debugging features in Flask
DEBUG = True

# EVERYCRED API ROUTE
EVERYCRED_API_ROUTE = "https://api.everycred.com"