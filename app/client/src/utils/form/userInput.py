from src.utils.form.validate import Validate
validator = Validate()
def get(field, message=""):
    """
    Search through the fields that can be validated and it applies the respecting one.
    If it does not match the validations, then it executes itself again until all validations are True

    Args:
        field (str): The field to be validated in the form
        message (str): The message that will be displayed in the prompt to the user
    
    Returns:
        str: The input of the user already validated
    """
    fieldProps = validator.getConfig(field)
    text = fieldProps["label"] if message == "" else message
    data = str(input(text)).strip()
    validation = validator.runValidations(data, fieldProps)

    if validation["ok"] is False:
        print(validation["msg"])
        return get(field, text)

    return data