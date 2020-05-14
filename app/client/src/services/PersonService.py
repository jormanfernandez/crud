from src.services.http import HTTP

class Service:
    """
    Data handler for persons. 
    This handler uses the NoSQL Database to store and read data.
    """
    def __init__(self, endpoint="localhost:8000"):
        self.request = HTTP(endpoint)

    def searchBy(self, key="", value=""):
        """
        Search a person or a group of persons that has aproximatly the same value.

        Args:
            key (str): The key in the person object that will be compared
            value (str): The value to be compared
        
        Returns:
            list: A list of persons that match the search 
        """
        response = self.request.get(f"/person/search/{key}/{value}")

        if response["status"]["code"] != 200:
            return []
        else:
            return response["data"]

    def write(self, values = {}, onPhone = None):
        """
        It writes on the database an update or a new person according to the arguments.
        If the {onPhone} parameter is send, the function will run as an update for the 
        person that has that number

        Args:
            values (dict): It receives the parameters that you want to be written on the object.
            onPhone (None, str): Indicate the phone where the update should be done
        
        Returns:
            dict: {"ok": boolean, "err": str} It says if the update was successfull and a error message in case it wasn't
        """
        # onPhone to update
        if onPhone is not None:
            response = self.request.put(f"/person/{onPhone}", params=values)
        else:
            response = self.request.post("/person", params=values)
        
        if response["status"]["code"] != 200:
            return {
                "ok": False,
                "err": response["data"]["msg"] if "msg" in response["data"] else response["status"]["desc"]
            }
        else:
            return {
                "ok": True
            }

    def delete(self, onPhone=None):
        """
        Deletes a person or the entire list of person

        Args:
            onPhone (None, str): The phone that should be deleted
        
        Returns:
            boolean: True if it deletes, False it an error occurs
        """
        response = self.request.delete(f"/person/{onPhone}")
        return response["status"]["code"] == 200

    def read(self):
        """
        Get the list of persons stored in the database

        Args:
            None
            
        Returns:
            list: List of people stored
        """
        response = self.request.get("/person")
        return response["data"] if response["status"]["code"] == 200 else []

PersonService = Service()