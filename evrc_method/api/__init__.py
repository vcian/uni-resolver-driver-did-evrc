# See documentation here: https://connexion.readthedocs.io/en/latest/request.html
import json
import requests
from instance import config
from flask import make_response, abort

# Following fucntions are API handlers

def get_did(identifier: str):
    """
    This function responds to a request for /identifiers/{identifier}
    to get the information of identifier

    Args:
        identifier (str): DID
    
    Returns:
        Return identifier metadata
    """ 
    # API route
    CRED_API_ROUTE = f'{config.EVERYCRED_API_ROUTE}/v1/identifier/did/{identifier}'
    response = requests.get(CRED_API_ROUTE)
    json_string = response.content.decode()
    identifier = json.loads(json_string)

    status_code = response.__dict__['status_code']

    # Check status code of api response and return response
    if status_code==400:
        return abort(404, "Invalid Input")
    
    if status_code!=200:
        return abort(500, "Error")
    
    return identifier['data'], 200