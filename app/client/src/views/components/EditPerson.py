from time import sleep
from src.utils.common.clear import clear
from src.views.common.PersonDetail import printPerson
from src.views.components.ModifyPerson import ModifyPerson
from src.views.components.DeletePerson import DeletePerson

def EditPerson(person):
    clear()
    print("> Modify and delete person")
    printPerson(person, 0)
    print("""
        Options:
            M .- Modify
            D .- Delete
            B .- Back
    """)
    chose = str(input("What do you want to do?: ")).strip()

    if chose.lower() not in ["m", "d", "b"]:
        print("Wrong option")
        sleep(2)
        EditPerson(person)
        return
    
    if chose == "m":
        ModifyPerson(person)
        EditPerson(person)
    elif chose == "d":
        DeletePerson(person, EditPerson)
