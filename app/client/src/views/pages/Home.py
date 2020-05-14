from src.utils.common.clear import clear
from src.utils.system import closeApp
from src.utils.form.userInput import get
from time import sleep
from datetime import date

def Home():
    clear()
    today = date.today().strftime("%d/%m/%Y")
    print(f"Today is: {today}")
    print("""
Hello, welcome to your main agenda... 
To navigate in the basic system, the menu would be:

    A .- Add new register to your agenda
    S .- Search for a specific person
    V .- View the entire list
    C .- Close 
""")

    option = str(input("Please, tell me where do you want to go: "))
    option = option.strip().lower()
    goTo(option)

def goTo(place):
    if place == "a":
        from src.views.pages.Register import Register
        Register()
    elif place == "s":
        from src.views.pages.Search import PersonSearch
        PersonSearch()
    elif place == "v":
        from src.views.pages.AllPersons import AllPersons
        AllPersons()
    elif place == "c":
        closeApp()
    else:
        print("Wrong option....")
        sleep(2)
        Home()
        