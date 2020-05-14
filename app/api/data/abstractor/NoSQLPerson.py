from data.database.NoSQL import DB
from utils.commons.search import search

database = DB()

class PersonHandler:
    """
    Data handler for persons. 
    This handler uses the NoSQL Database to store and read data.
    """
    def __init__(self):
        self.doc = "persons"

    def searchBy(self, key="", value=""):
        """
        Search a person or a group of persons that has aproximatly the same value.

        Args:
            key (str): The key in the person object that will be compared
            value (str): The value to be compared
        
        Returns:
            list: A list of persons that match the search 
        """
        data = self.read()
        persons=[]

        for i in range(0, len(data)):
            person = search(data[i], params={key: value})
            if person is False:
                continue
            else:
                persons.append(person)

        return persons

    def exists(self, data=[], phone="", excludeIndex=None):
        """
        It check from a list of persons, if a phone number exists.
        If a index is passed, it will exclude it from the search

        Args:
            data (list): The list of persons where the search will be done
            phone (str): The phone to be checked
            excludeIndex (None, int): The index to be excluded from the data list in case its needed.
        
        Returns:
            boolean: True if the phone number exists in the conditions. False if it doesn't
        """
        itExists = False
        
        for i in range(0, len(data)):
            if isinstance(excludeIndex, int) and i == excludeIndex:
                continue
            person = data[i]
            if person["phone"] == phone:
                itExists = True
                break

        return itExists

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
        data = self.read()
        toUpdate = {
            "ok": False,
            "err": "Nothing to update"
        }

        if len(values.keys()) < 1:
            return toUpdate

        if onPhone is not None:
            for i in range(0, len(data)):
                person = data[i]
                if person["phone"] == onPhone:
                    if "phone" in values and self.exists(data=data, phone=values["phone"], excludeIndex=i):
                        toUpdate["err"] = "Someone already has this phone"
                    else:
                        person.update(values)
                        toUpdate["ok"] = True
                        toUpdate["err"] = ""
                    break
                data[i] = person
        else:
            if self.exists(data=data, phone=values["phone"]):
                toUpdate["err"] = "Someone already has this phone"
            else:
                data.append(values)
                toUpdate["ok"] = True
                toUpdate["err"] = ""
        
        if toUpdate["ok"] is True:
            database.write(onDoc=self.doc, value=data)
        return toUpdate

    def delete(self, onPhone=None):
        """
        Deletes a person or the entire list of person

        Args:
            onPhone (None, str): The phone that should be deleted
        
        Returns:
            boolean: True if it deletes, False it an error occurs
        """
        data = self.read()
        deleted = False

        if onPhone is None:
            deleted = True
            database.write(onDoc=self.doc)
            return deleted
        
        for i in range(0, len(data)):
            person = search(data[i], params={
                "phone": onPhone
            }, ratio=1.0)

            if person is False:
                continue
            
            del data[i]
            database.write(onDoc=self.doc, value=data)
            deleted = True
            break

        return deleted

    def read(self):
        """
        Get the list of persons stored in the database

        Args:
            None
            
        Returns:
            list: List of people stored
        """
        data = database.read(fromDoc=self.doc)
        return data
