# This file contains the NON-SENSITIVE, source controlled configuration variables that your app needs.

DEBUG = False # Turn off debugging features in Flask

# Configuration for the Flask-Bcrypt extension
BCRYPT_LOG_ROUNDS = 12

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True
