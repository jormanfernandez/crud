def printPerson(person, index):
    print(f"""
* * * * * * * * * *
    [{index + 1}] - Details
        Name: {person["name"]} {person["lastname"]}
        Phone: {person["phone"]}
        Email: {person["email"]}
* * * * * * * * * *    
""")