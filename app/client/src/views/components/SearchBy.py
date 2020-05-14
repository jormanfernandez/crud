from src.services.PersonService import PersonService

def searchByPhone(callback):
    print("Ok.. now you are searching by the phone number (Type \"r\" to return).")
    phone = input("What are we looking for?: ")
    phone = str(phone).strip()

    if phone == "r":
        callback()
        return

    return PersonService.searchBy(key="phone", value=phone)

def searchByName(callback):
    print("Ok.. now you are searching by the first name (Type \"<cancel>\" to return).")
    name = input("Who are we looking for?: ")
    name = str(name).strip()

    if name == "<cancel>":
        callback()
        return
    return PersonService.searchBy(key="name", value=name)

def searchByLastname(callback):
    print("Ok.. now you are searching by the last name (Type \"<cancel>\" to return).")
    name = input("Who are we looking for?: ")
    name = str(name).strip()

    if name == "<cancel>":
        callback()
        return
    return PersonService.searchBy(key="lastname", value=name)

def searchByEmail(callback):
    print("Ok.. now you are searching by the email (Type \"<cancel>\" to return).")
    email = input("What email are we looking for?: ")
    email = str(email).strip()

    if email == "<cancel>":
        callback()
        return
    return PersonService.searchBy(key="email", value=email)