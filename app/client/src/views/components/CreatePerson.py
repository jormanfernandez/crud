from src.models.person import Person
from src.services.PersonService import PersonService
from src.views.common.recreateScenary import recreate
from src.utils.form.userInput import get

def CreatePerson(arg=None):
    print("\n" * 2)
    print("Nice, we are going to ask you some easy question.")
    print("Please answer whenever you want")
    
    person = Person()
    person.setName(get("name"))
    person.setLastname(get("lastname"))
    person.setEmail(get("email"))
    person.setPhone(get("phone"))
    create = PersonService.write(values=person.dictify())

    if create["ok"] is not True:
        print("\n" * 2)
        print("There was an error adding the register: ", create["err"])
        recreate(text="Do you want to try again?", callback=CreatePerson)
        return
    
    print("*" * 5)
    print("Person registered successfully")
    print("*" * 5)

    recreate(text="Do you want to add someone else?", callback=CreatePerson)