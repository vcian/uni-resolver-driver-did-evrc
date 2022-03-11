# This file initializes your application and brings together all of the various components.

import connexion
from flask_cors import CORS

connex = connexion.App(
    __name__.split('.')[0],
    server_args={"instance_relative_config": True},  # Use the "instance" directory for any config overrides
    specification_dir='./' # where the openapi specs are
)

# Read the swagger.yml file to configure the endpoints.
connex.add_api(
    '../evrc_method.yaml',
    strict_validation=True
)

# Pull out the flask instance to continue with.
app = connex.app

# Add CORS support
CORS(app)

# Config file in instance to override parameters
app.config.from_object('config')     
app.config.from_pyfile('config.py')     