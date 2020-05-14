from src.views.common.PersonDetail import printPerson

def PersonList(persons):
    print("*" * 5)
    print(f"There are {len(persons)} person(s)")
    
    if len(persons) < 1:
        return
    
    for i in range(0, len(persons)):
        printPerson(persons[i], i)

