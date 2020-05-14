import falcon
import json
from data.operators.PersonOperator import PersonOperator
from utils.logger import Log
from utils.form.validate import Validate

class PersonDetailHandler(object):
    """
    It handles the request to a single phone person

    Args:
        object (object): No info
    """
    def on_get(self, req, resp, phone):
        """
        Handles the GET request searching an specific phone number

        Args:
            req (Falcon HTTP Request): Request received by the server
            resp (Falcon HTTP Response): Response constructed by the server
            phone (str): Phone number to be search in the database

        Returns:
            None
        """
        Log(f"GET Request Received: Searching {phone}", req=req)
        resp.status = falcon.HTTP_204
        resp.content_type = "application/json"
        person = PersonOperator.searchBy(key="phone", value=str(phone))
        if len(person) < 1:
            resp.body = json.dumps({
                "msg": f"The person with the phone {phone} wasn't found"
            })
        else:
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(person, ensure_ascii=False)
        resp.body += "\n"
    
    def on_put(self, req, resp, phone):
        """
        Handles the PUT request updating an specific phone number.
        The req.body should contain all the parameters that the object allows
        because it will validate them as if it was an insert

        Args:
            req (Falcon HTTP Request): Request received by the server
            resp (Falcon HTTP Response): Response constructed by the server
            phone (str): Phone number to be updated in the database

        Returns:
            None
        """
        Log(f"PUT Request Received: Searching {phone}", req=req)
        resp.status = falcon.HTTP_400
        resp.content_type = "application/json"
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

        person = PersonOperator.searchBy(key="phone", value=str(phone))
        if len(person) != 1:
            resp.body = json.dumps({
                "msg": f"The person with the phone {phone} wasn't found"
            })
            resp.body += "\n"
            return
        person = None
        validator = Validate()
        isValid = validator.fullValidation(data)

        if isValid["ok"] is not True:
            resp.body = json.dumps({
                "msg": isValid["msg"]
            }, ensure_ascii=False)
            resp.body += "\n"
            return
        
        update = PersonOperator.write(values=data, onPhone=str(phone))

        if update["ok"] is not True:
            resp.body = json.dumps({
                "msg": f"There was an error updating the records: {update['err']}"
            })
        else:
            resp.status = falcon.HTTP_200
            resp.body = json.dumps({
                "msg": f"{data['name']} was updated successfully"
            })
        
        resp.body += "\n"

    
    def on_delete(self, req, resp, phone):
        """
        Handles the DELETE request. It deletes an specific phone number

        Args:
            req (Falcon HTTP Request): Request received by the server
            resp (Falcon HTTP Response): Response constructed by the server
            phone (str): Phone number to be deleted in the database

        Returns:
            None
        """
        Log(f"DELETE Request Received: Searching {phone}", req=req)
        resp.status = falcon.HTTP_400
        resp.content_type = "application/json"

        person = PersonOperator.searchBy(key="phone", value=str(phone))
        if len(person) != 1:
            resp.body = json.dumps({
                "msg": f"The person with the phone {phone} wasn't found"
            })
            resp.body += "\n"
            return
        person = person[0]
        delete = PersonOperator.delete(onPhone=str(phone))

        if delete is True:
            resp.status = falcon.HTTP_200
            resp.body = json.dumps({
                "msg": f"{person['name']} was deleted successfully"
            })
        else:
            resp.body = json.dumps({
                "msg": f"{person['name']} couldn't be deleted"
            })
        
        resp.body += "\n"
