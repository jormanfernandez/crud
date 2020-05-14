from time import sleep
from src.utils.common.clear import clear

from src.views.common.PersonDetail import printPerson
from src.views.common.exitOrHome import exitOrHome

from src.views.components.SearchBy import searchByEmail
from src.views.components.SearchBy import searchByLastname
from src.views.components.SearchBy import searchByName
from src.views.components.SearchBy import searchByPhone

from src.views.components.SelectEdit import SelectEdit

switch = {
    "n": searchByName,
    "l": searchByLastname,
    "e": searchByEmail,
    "p": searchByPhone,
    "b": exitOrHome
}

def PersonSearch():
    clear()
    print("""
> Searching a person

    So we are going to help you look for someone in detail
    and maybe edit some of their data (or delete them if you want to)
    
    Here is how you can search them:
        N .- Name
        L .- Last Name
        E .- Email (if it has one)
        P .- Phone
        B .- Back
    """)

    how = str(input("What's your move?: ")).strip().lower()
    if how not in switch:
        print("Wrong option")
        sleep(1)
        PersonSearch()
    
    if how == "b":
        switch[how]()
        return

    persons = switch[how](PersonSearch)
    SelectEdit(persons)