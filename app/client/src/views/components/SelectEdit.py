from time import sleep
from src.views.components.EditPerson import EditPerson
from src.views.components.PersonList import PersonList
from src.views.common.exitOrHome import exitOrHome

def SelectEdit(persons):
    PersonList(persons)
    amt = len(persons)
    if amt < 1:
        exitOrHome()
        return
    
    chose = input("Do you want to edit someone? If so, tell me the number. Else just say no: ")
    chose = str(chose).strip().lower()

    if chose == "no":
        exitOrHome()
        return
    
    try:
        chose = int(chose)
        chose = chose - 1
        if chose not in range(0, amt):
            raise Exception("Not in list")
    except:
        print("Wrong option")
        sleep(2)
        SelectEdit(persons)
        return
    
    EditPerson(persons[chose])
    exitOrHome()