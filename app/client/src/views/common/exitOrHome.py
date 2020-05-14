from src.utils.system import closeApp
def exitOrHome(text="Do you want to go home?"):
    chose = input(f"\n\n{text} y/n: ")
    chose = str(chose).strip().lower()

    if chose not in ["y", "n"]:
        print("Wrong option")
        exitOrHome(text)
        return
    
    if chose == "y":
        from src.views.pages.Home import Home
        Home()
    else:
        closeApp()