import os
import sqlite3
from utils.logger import Log

class DB:
    """
    Handles the database connection and data updates using SQLite3
    """
    def __init__(self):
        self.path = os.path.join(os.getcwd(), "data/database/storage.db")
        self.conn = None
        self.error = None
        self.stmt = ""
        self.whereStmt = ""
        self.orderStmt = ""
        self.rows = []
    
    def connect(self):
        """
        It realizes the connection between the app and the database

        Args:
            None
        
        Returns:
            DB: It returns the same instance for concatenation of methods
        """
        if self.conn is None:
            self.conn = sqlite3.connect(self.path)

        return self

    def hasError(self):
        """
        Indicate if there's an error stored in the object

        Args:
            None
        
        Returns:
            boolean: If some data is stored in error
        """
        return self.error is not None and len(self.error) > 0

    def cleanError(self):
        """
        Removes the data stored in the error attribute

        Args:
            None
        
        Returns:
            DB: It returns the same instance for concatenation of methods
        """
        self.error = None
        return self
    
    def countRows(self):
        """
        It counts how many rows are stored in the instance
        
        Args:
            None
        
        Returns:
            int: Number of rows stored in the instance
        """
        return len(self.rows)
    
    def fetchRows(self):
        """
        It returns the rows stored on the instance

        Args:
            None
        
        Returns:
            list[None, tuple]: Returns the list of the elements in the instance. 
                               Mostly is a tuple returned from the database
        """
        return list(self.rows)

    def insert(self, table="", fields=[]):
        """
        Create the structured query for an insert

        Args:
            table (str): The name of the table where the operation should be performed
            fields (list): The list of fields that will be inserted
        
        Returns:
            DB: It returns the same instance for concatenation of methods
        """
        self.stmt = f"INSERT INTO {table}({', '.join(fields)}) VALUES("

        for i in range(0, len(fields)):
            self.stmt += "?"
            if i < len(fields) - 1:
                self.stmt += ", "
        
        self.stmt += ")"

        return self
    
    def select(self, fields=["*"], table=""):
        """
        Create the structured query for a select

        Args:
            table (str): The name of the table where the operation should be performed
            fields (list): The list of fields that will be selected
        
        Returns:
            DB: It returns the same instance for concatenation of methods
        """
        self.stmt = f"SELECT {', '.join(fields)} FROM {table}"
        return self
    
    def update(self, table="", fields=[]):
        """
        Create the structured query for an update

        Args:
            table (str): The name of the table where the operation should be performed
            fields (list): The list of fields that will be updated
        
        Returns:
            DB: It returns the same instance for concatenation of methods
        """
        self.stmt = f"UPDATE {table} SET {', '.join(f'{field}=?' for field in fields)}"
        return self
    
    def delete(self, table=""):
        """
        Create the structured query for a delete

        Args:
            table (str): The name of the table where the operation should be performed
            
        Returns:
            DB: It returns the same instance for concatenation of methods
        """
        self.stmt = f"DELETE FROM {table}"
        return self
    
    def where(self, prefix = None, field="", condition="", value="?"):
        """
        Indicate a Where condition to be appended in the query

        Args:
            prefix (None, str): It indicates something before the actual condition. Mostly and "AND" or and "OR"
            field (str): The field that will be checked
            condition (str): The condition that will be perfomed
            value (str): The value that will be checked in the field. 
                         To prevent database injection, all values should be appended at the end with a bin in the execute method.
        
        Returns:
            DB: It returns the same instance for concatenation of methods
        """
        if len(self.whereStmt) < 1:
            self.whereStmt = " WHERE "
        
        if prefix is not None:
            self.whereStmt += f" {prefix} "
        
        self.whereStmt += f" {field} {condition} {value}"
        return self
    
    def orderBy(self, orderBy=[]):
        """
        Indicate the order in how the rows should be returned from the database

        Args:
            orderBy (list): a list of the orders that should be done before returning the rows

        Returns:
            DB: It returns the same instance for concatenation of methods
        """
        if len(self.orderStmt) < 1:
            self.orderStmt = " ORDER BY "
        
        if len(orderBy) < 1:
            return self
        
        self.orderStmt += ", ".join(order for order in orderBy)
        return self
    
    def cleanQuery(self):
        """
        Clean the statements that are going to be sent to the database

        Args:
            None
        
        Returns:
            DB: It returns the same instance for concatenation of methods
        """
        self.stmt = ""
        self.whereStmt = ""
        self.orderStmt = ""
        return self
    
    def execute(self, bind=[], commit=False, clean = True):
        """
        It executes the stored statement

        Args:
            bind (list): It send on a safe way the parameters to the query.
            commit (boolean): If an update, delete or insert is done. This parameter should be true so it updates the records in the database.
            clean (boolean): This value clean the query after the execution is done.

        Returns:
            DB: It returns the same instance for concatenation of methods
        """
        self.rows = []
        self.connect()

        cursor = self.conn.cursor()
        query = self.stmt

        if len(self.whereStmt) > 0:
            query += self.whereStmt
        
        if len(self.orderStmt) > 0:
            query += self.orderStmt

        try:
            if len(bind) > 0:
                cursor.execute(query, tuple(bind))
            else:
                cursor.execute(query)

            if commit is True:
                self.conn.commit()

            self.rows = cursor.fetchall()
            
        except sqlite3.Error as e:
            self.error = e.args[0]
            Log(f"Error on: {query} - {self.error}", level=3, file="db")
            
        finally:
            cursor.close()
            self.close()
        
        if clean is True:
            self.cleanQuery()
        return self
    
    def close(self):
        self.conn.close()
        self.conn = None
