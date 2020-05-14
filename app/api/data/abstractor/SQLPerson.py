from data.database.SQL import DB
from utils.logger import Log

database = DB()

class PersonHandler:
    """
    Data handler for persons.
    This handler use the SQLite Database to store and read data
    """
    def __init__(self):
        self.table = "persons"
    
    def searchBy(self, key="", value=""):
        """
        Search a person or a group of persons that has aproximatly the same value.

        Args:
            key (str): The key in the person object that will be compared
            value (str): The value to be compared
        
        Returns:
            list: A list of persons that match the search 
        """
        database.select(table=self.table).where(field=key, condition="LIKE").execute(bind=[f"%{value}%"])

        if database.hasError() is True:
            database.cleanError()
            return []
        
        return self._structureRow(database.fetchRows())
    
    def _structureRow(self, fetchedRows):
        """
        A function that structure a tuple in the row object that every person row has

        Args:
            fetchedRows (tuple, list[list]): Rows that came from the database to transform them as objects
        
        Returns:
            list[dict]: The rows, now in dict, with the id of every field
        """
        rows = [{
            "id": row[0],
            "name": row[1],
            "lastname": row[2],
            "email": row[3],
            "phone": row[4]
        } for row in fetchedRows]

        return rows

    def read(self):
        """
        It gets all the persons from the database

        Args:
            None

        Returns:
            list: List of all persons in the database
        """
        database.select(table=self.table).execute()

        if database.hasError() is True:
            database.cleanError()
            return []

        return self._structureRow(database.fetchRows())
    
    def exists(self, phone="", exclude=None):
        """
        It check in the database if a phone number exists. Excluding the {exclude} in case is send

        Args:
            phone (str): The phone to be checked
            phone (None, str): The phone to be excluded in the search.
        
        Returns:
            boolean: True if there are more than 0 rows in the database that match the search. False if it don't
        """
        database.select(table=self.table, fields=["id"]).where(field="phone", condition="=", value="?")
        bind=[phone]
        if exclude is not None:
            bind.append(exclude)
            database.where(prefix="AND", field="phone", condition="!=", value="?")
            
        database.execute(bind=bind)

        if database.hasError() is True:
            database.cleanError()
            return False

        return database.countRows() > 0
    
    def write(self, values={}, onPhone=None):
        """
        It writes on the database an update or a new person according to the arguments.
        If the {onPhone} parameter is send, the function will run as an update for the 
        person that has that number

        Args:
            values (dict): It receives the parameters that you want to be written on the object.
            onPhone (None, str): Indicate the phone where the update should be done
        
        Returns:
            dict: {"ok": boolean, "err": str, "insert": boolean} It says if the update was successfull and a error message in case it wasn't
        """
        toUpdate = {
            "ok": False,
            "err": "Nothing to update",
            "insert": True
        }

        if onPhone is not None:
            toUpdate["insert"] = False
        if len(values.keys()) < 1:
            return toUpdate

        if "phone" in values and self.exists(phone=values["phone"], exclude=onPhone):
            toUpdate["err"] = "Someone already has this phone"
        else:
            toUpdate["ok"] = True
            toUpdate["err"] = ""

        if toUpdate["ok"] is not True:
            return toUpdate

        if toUpdate["insert"] is True:
            database.insert(table=self.table, fields=list(values.keys()))
        else:
            if self.exists(phone=onPhone) is not True:
                toUpdate["ok"] = False
                toUpdate["err"] = f"We couldn't find someone with the phone {onPhone}"
                return toUpdate

            database.update(table=self.table, fields=list(values.keys())).where(field="phone", condition="=")
            values["phoneUpdate"] = onPhone
        
        database.execute(bind=list(values.values()), commit=True)

        if database.hasError() is True:
            toUpdate["ok"] = False
            toUpdate["err"] = database.error
            database.cleanError()
        else:
            toUpdate["ok"] = True
            toUpdate["err"] = ""
        
        return toUpdate
    
    def delete(self, onPhone=None):
        """
        Deletes a person or the entire list of person

        Args:
            onPhone (None, str): The phone that should be deleted
        
        Returns:
            boolean: True if it deletes, False it an error occurs
        """
        if onPhone is None:
            return False
        
        if self.exists(phone=onPhone) is False:
            return False
        
        database.delete(table=self.table).where(field="phone", condition="=").execute(bind=[onPhone], commit=True)

        if database.hasError() is not True:
            return True
        else:
            database.cleanError()
            return False