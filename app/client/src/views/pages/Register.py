from time import sleep
from src.utils.common.clear import clear
from src.views.components.CreatePerson import CreatePerson

def Register():
    clear()
    print("""
> Register a new person

    You are going to register a new person. 
    If the phone already exist, it won't be updated. We already have an option for that :)
    """)

    forward = str(input("Do you want to continue? y/n: ")).strip()
    forward = forward.lower()

    if forward not in ["y", "n"]:
        print("Option incorrect")
        sleep(1)
        Register()
    elif forward == "y":
        CreatePerson()
    else:
        from src.views.pages.Home import Home
        Home()