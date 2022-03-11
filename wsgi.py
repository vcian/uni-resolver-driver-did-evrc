# Entry point for server to run application
# Run a test server.
import os
import sys
sys.path.append(os.path.join(os.getcwd(), './evrc_method'))
from evrc_method import app


if __name__ == "__main__":
    app.run(port=8080, debug=False)