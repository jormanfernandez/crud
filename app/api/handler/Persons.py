import falcon
import json
from data.operators.PersonOperator import PersonOperator
from utils.logger import Log
from utils.form.validate import Validate

class PersonHandler(object):
    """
    It handles the request to no specific persons

    Args:
        object (object): No info
    """
    def on_get(self, req, resp):
        """
        Handles the GET for all the persons giving a list of all the people in the database

        Args:
            req (Falcon HTTP Request): Request received by the server
            resp (Falcon HTTP Response): Response constructed by the server

        Returns:
            None
        """
        Log(f"GET Request Received", req=req)
        resp.status = falcon.HTTP_200
        resp.content_type = "application/json"
        resp.body = json.dumps(PersonOperator.read(), ensure_ascii=False)
        resp.body += "\n"
    
    def on_post(self, req, resp):
        """
        Handles the POST request inserting an specific phone number.
        The req.body should contain all the parameters that the object allows

        Args:
            req (Falcon HTTP Request): Request received by the server
            resp (Falcon HTTP Response): Response constructed by the server

        Returns:
            None
        """
        Log(f"POST Request Received", req=req)
        resp.content_type = "application/json"
        resp.status = falcon.HTTP_400
        data = None

        try:
            data = json.loads(req.bounded_stream.read(), encoding='utf-8')
        except json.decoder.JSONDecodeError as err:
            Log(f"Error reading body: {err}", req=req, level=3)
            resp.body = json.dumps({
                "msg": f"Error reading body: {err}"
            }, ensure_ascii=False)
            resp.body += "\n"
            return

        validator = Validate()
        isValid = validator.fullValidation(data)
        if isValid["ok"] is not True:
            resp.body = json.dumps({
                "msg": isValid["msg"]
            }, ensure_ascii=False)
            resp.body += "\n"
            return
        
        create = PersonOperator.write(values=data)
        if create["ok"] is not True:
            resp.body = json.dumps({
                "msg": create["err"]
            }, ensure_ascii=False)
        else:
            resp.status = falcon.HTTP_200
            resp.body = json.dumps({
                "msg": f"{data['name']} was created successfully"
            }, ensure_ascii=False)
        resp.body += "\n"