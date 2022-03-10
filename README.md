# uni-resolver-driver-did-evrc
> Short blurb about what your product does.

<!-- [![PyPI][pypi-image]][pypi-url]
[![Build Status][travis-image]][travis-url]
[![Downloads Stats][pypi-downloads]][pypi-url] -->

One to two paragraph statement about your product and what it does.

<!-- ![](header.png) -->

## Install + configure the project

### 1. Linux
```
# Create python virtual environment
python3 -m venv venv

# Activate the python virtual environment
source venv/bin/activate

# Install the requirements for the project into the virtual environment
pip install -r requirements.txt
```
### 2. Windows
```
# Create python virtual environment
conda create --name venv python=3.8

# Activate the python virtual environment
conda activate venv

# Install the requirements for the project into the virtual environment
pip install -r requirements.txt
```

## Run the server in development mode
Add environment variables (given in .env) by running following command in cmd/terminal:
```
set PYTHONPATH=./evrc_method
```

Run the server
```
python run.py
```
Then browse the API at: http://localhost:8080/v1/ui/

## Testing

Few examples for testing APIs

* To load fixtures into database
```
python load_fixture.py users.yaml
```

* To test API endpoints
```
pytest -s
```
## Running Docker image (Optional)

Below are the few commands used to build and run docker image (containerized flask app):

 - Build the docker image
 ```
 docker image build -t flask-backend-boilerplate .
 ```

 - Verify that your image shows in your image list
 ```
 docker image ls
 ```

 - Run the docker container which is exposed to 5001 port
 ```
 docker run -p 5001:8080 -d flask-backend-boilerplate
 ```

 - Check the log output of the container
 ```
 docker container ls
 docker container logs [container id]
 ```

 - Stop a docker container
 ```
 docker container stop [container id]
 ```

 - Remove the stopped containers
 ```
 docker system prune
 ```
## Usage example

A few motivating and useful examples of how your product can be used. Spice this up with code blocks and potentially more screenshots.

_For more examples and usage, please refer to the [Wiki][wiki]._

## Release History
* 0.0.1
    * Work in progress