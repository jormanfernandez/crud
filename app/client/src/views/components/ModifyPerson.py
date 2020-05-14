from src.models.person import Person
from src.services.PersonService import PersonService
from src.views.common.recreateScenary import recreate
from src.utils.form.userInput import get
from time import sleep

def ModifyPerson(person):

    updatePerson = Person()
    updatePerson.setName(get("name"))
    updatePerson.setLastname(get("lastname"))
    updatePerson.setEmail(get("email"))
    updatePerson.setPhone(get("phone"))
    
    chose = input("Do you agree? y/n: ")
    chose = str(chose).strip().lower()

    if chose not in ["y", "n"]:
        print("Wrong option")
        ModifyPerson(person)
        return
    if chose == "n":
        return
    
    updated = PersonService.write(values=updatePerson.dictify(), onPhone=person["phone"])

    if updated["ok"] is True:
        person.update(updatePerson.dictify())
        print(f"{person['name']} was updated successfully")
        sleep(2)
    else:
        print(f"There was an error updating the records: {updated['err']}")
        ModifyPerson(person)
