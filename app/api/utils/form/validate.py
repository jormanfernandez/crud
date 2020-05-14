import re
from utils.form.fields import Fields

fields = Fields()

class Validate:
    """
    Validator of the user input
    """

    def fullValidation(self, data):
        """
        It runs a full validation of all the keys in the data parameter. 
        It validates that matchs exactly the requested fields for an insert.

        Args:
            data (dict): The key<value> pair to be validated
        
        Returns:
            dict: {ok: boolean, msg: str} 
        """
        for key in getattr(fields, "field"):
            if key not in data:
                return {
                    "ok": False,
                    "msg": f"Parameter {key} missing"
                }

        for key in data:
            config = self.getConfig(key)
            if config is False:
                return {
                    "ok": False,
                    "msg": f"Field {key} is invalid"
                }

            isValid = self.runValidations(data[key], config)

            if isValid["ok"] is not True:
                return isValid
        
        return {"ok": True}

    def getConfig(self, field):
        """
        Returns the configuration that should be applied to the exact field

        Args:
            field (str): The name of the field to get the config
        
        Returns:
            dict: The configuration of the field
        """
        f = getattr(fields, "field")
        return f[field] if field in f else False
    
    def runValidations(self, data, config):
        """
        It runs every validation of the user input.

        Args:
            data (str): The user input
            config (dict): The configuration for the required input
        
        Returns:
            dict: {ok: boolean, msg: str} If ok is False, some of the validations where not valid.
        """
        if config["empty"] is False:
            if len(data) < 1:
                return {"ok": False, "msg": config["error"]}
        else:
            if len(data) < 1:
                return {"ok": True, "msg": ""}
        
        for check in config["checker"]:
            if getattr(self, check)(data, config["checker"][check]) is not True:
                return {"ok": False, "msg": config["error"]}
        return {"ok": True, "msg": ""}


    def regex(self, field, regex):
        """
        It executes a regular expression in a string to check if it pass it

        Args:
            field (str): The field to be checked
            regex (str): The regular expression
        
        Returns:
            boolean: If True, the regular expression match
        """
        return re.search(regex, field) is not None
