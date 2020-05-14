from utils.system import isSQL

if isSQL() is not True:
    from data.abstractor.NoSQLPerson import PersonHandler
else:
    from data.abstractor.SQLPerson import PersonHandler

"""
Here we define which Handler use to operate in the database
According to the parameters in the run command.
"""
PersonOperator = PersonHandler()