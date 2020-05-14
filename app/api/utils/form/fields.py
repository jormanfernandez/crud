class Fields:
    """
    Contains the fields that would be validated in the forms when a user is created or updated
    It also contains if the field can be empty and the functions to be run in order to validate it
    In case an error occurs, it also contains the error message to be displayed
    """
    field = {
        "name": {
            "label": "Contact Name: ",
            "empty": False,
            "checker": {
                "regex": "^[a-zA-Z]{2,35}$"
            },
            "error": "The name should be between 2 and 35 characters long"
        },
        "lastname": {
            "label": "Contact Lastname: ",
            "empty": True,
            "checker": {
                "regex": "^[a-zA-Z]{2,35}$"
            },
            "error": "The lastname should be between 2 and 35 characters long"
        },
        "phone": {
            "label": "Contact Phone: ",
            "empty": False,
            "checker": {
                "regex": "^[0-9]{3,9}"
            },
            "error": "The phone should be between 2 and 9 digits long"
        },
        "email": {
            "label": "Contact Email: ",
            "empty": True,
            "checker": {
                "regex": r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
            },
            "error": "The email is invalid"
        }
    }
