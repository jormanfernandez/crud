from src.services.PersonService import PersonService

def DeletePerson(person, callback):
    chose = input("Are you sure you want to delete this person? y/n: ")
    chose = str(chose).strip().lower()

    if chose not in ["y", "n"]:
        print("Wrong option")
        DeletePerson(person, callback)
        return
    if chose == "y":
        deleted = PersonService.delete(onPhone=person["phone"])
        if deleted:
            print(f"{person['name']} was deleted successfully")
        else:
            print(f"{person['name']} coudln't be deleted")
    else:
        callback(person)
