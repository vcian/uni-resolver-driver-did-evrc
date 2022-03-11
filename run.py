# This is the file that is invoked to start up a development server.
# It gets a copy of the app from your package and runs it.
# This is not for use in production, but it will see a lot of mileage in development.

# Run a test server.
import os
import sys
sys.path.append(os.path.join(os.getcwd(), './evrc_method'))
from evrc_method import app


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)