from time import sleep
from src.utils.common.clear import clear
from src.services.PersonService import PersonService
from src.views.common.exitOrHome import exitOrHome
from src.views.components.EditPerson import EditPerson
from src.views.components.PersonList import PersonList

def AllPersons():
    clear()

    print("""
> Persons full list
    You are viewing all the records stored in the database
    """)

    persons = PersonService.read()

    if len(persons) < 1:
        exitOrHome("There are no results, do you want to go home?")
        return
    
    PersonList(persons)
    
    chose = input("Do you want to edit someone? If so, tell me the number. Else just say no: ")
    chose = str(chose).strip().lower()

    if chose == "no":
        exitOrHome("Nice, do you want to go home?")
        return
    
    try:
        chose = int(chose)
        chose = chose - 1
        if chose not in range(0, len(persons)):
            raise Exception("Not in list")
    except:
        print("Wrong option")
        sleep(2)
        AllPersons()
        return
    
    EditPerson(persons[chose])
    exitOrHome("Do you want to go home?")
