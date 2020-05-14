def recreate(text="", callback=None, param=None):
    again = str(input(f"{text} y/n: ")).strip().lower()
    if again == "y":
        if callable(callback) is True:
            callback(param)
    elif again == "n":
        from src.views.pages.Home import Home
        Home()
    else:
        print("Wrong input.")
        print("\n" * 2)
        recreate(text=text, callback=callback, param=param)