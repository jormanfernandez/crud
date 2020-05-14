import sqlite3
import os
from sqlite3 import Error

def migration(tables={}, conn=None):
    if conn is None:
        print("Connection is unavailable")
        return False
    
    if len(tables.keys()) < 1:
        print("No tables where found")
        return False

    createTable = ""

    for tableName in tables.keys():
        table = tables[tableName]
        createTable += f"""
            CREATE TABLE IF NOT EXISTS {tableName} (
        """

        rowIndex = 0

        for rowName in table["rows"]:
            rowIndex += 1
            constraints = table["rows"][rowName]
            createTable += f"{rowName} {' '.join(constraints)}"
            if rowIndex < len(table["rows"]):
                createTable += ",\n"

        createTable += ");"
    cursor = conn.cursor()
    try:
        cursor.execute(createTable)
        conn.commit()
    except Error as e:
        return print(e)
    cursor.close()

filePath = os.path.dirname(os.path.realpath(__file__))
filePath = f"{filePath}/storage.db"

conn = sqlite3.connect(filePath)

tables = {
    "persons": {
        "rows": {
            "id": ["integer", "PRIMARY KEY", "AUTOINCREMENT"],
            "name": ["text", "NOT NULL"],
            "lastname": ["text", "NULL"],
            "email": ["text", "NULL"],
            "phone": ["text", "NOT NULL", "UNIQUE"]
        }
    }
}

migration(tables=tables, conn=conn)

conn.close()
