import json
import os

class DB:
    """
    Handles the connection with the .json file that will be used as database
    """
    def __init__(self):
        self.path = os.path.join(os.getcwd(), "data/database/storage.json")

    def read(self, fromDoc = None):
        """
        It opens the .json file and reads its content transforming it in a JSON object.
        If a document is indicated it will send what that key contain in the json.

        Args:
            fromDoc (None, str): The document to read data from
        
        Returns:
            list: If the fromDoc parameter is send, it will return a list of all the rows stored
            dict: If the fromDOc is None, it will return a dict with the entire database object
        """
        f = open(self.path, "r")
        data = json.loads(f.read())
        f.close()

        if fromDoc is None:
            return data
        else:
            return data[fromDoc] if fromDoc in data else []

    def write(self, onDoc, value = []):
        """
        It opens the .json file reading the content and then applying the necessary updates on the fields.

        Args:
            onDoc (str): The document that will be written. This is the JSON key in the dict.
            value (list): The data that will be stored on the document or key of the JSON.
        
        Returns:
            None
        """
        data = self.read()
        
        if isinstance(value, list) is False:
            value = []

        data[onDoc] = value
        f = open(self.path, "w+")
        f.write(json.dumps(data))
        f.close()
