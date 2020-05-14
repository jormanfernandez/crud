import falcon
import json
from data.operators.PersonOperator import PersonOperator
from utils.logger import Log
from utils.form.fields import Fields

fields = Fields()

class PersonSearchHandler(object):
    """
    It handles the request to no specific persons

    Args:
        object (object): No info
    """
    def on_get(self, req, resp, mode, value):
        """
        Handles the GET for search of persons and gives a list of people that match the search

        Args:
            req (Falcon HTTP Request): Request received by the server
            resp (Falcon HTTP Response): Response constructed by the server
            mode (str): The search method to be used (name, lastname, phone, email)
            value (str, int): The value to be search

        Returns:
            None
        """
        Log(f"GET Request Received", req=req)
        resp.content_type = "application/json"

        if mode not in getattr(fields, "field"):
            resp.status = falcon.HTTP_400
            resp.body = json.dumps({
                "msg": "Search method not allowed"
            })
        else:
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(PersonOperator.searchBy(key=mode, value=value), ensure_ascii=False)
        
        resp.body += "\n"
    