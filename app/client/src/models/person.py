class Person:
    """
    Structure the parameters that a person should have
    """
    def __init__(self, name="", lastname="", phone="", email=""):
        """
        Creates the person
        
        Args:
            name (str): The first name of a person
            lastname (str, None): Lastname of a person
            phone (str, int): Phone number of a person
            email (str, None): Email of a person
        
        Returns:
            None
        """
        self.name = name
        self.lastname = lastname
        self.phone = phone
        self.email = email
    
    def dictify(self):
        """
        It returns the attributes of the person in form of a dictionary

        Args:
            None
        
        Returns:
            dict: {name: (str), lastname: (str, None), phone: (str, int), email: (str, None)}
        """
        return {
            "name" : self.name,
            "lastname" : self.lastname,
            "phone" : self.phone,
            "email" : self.email
        }
    
    def getName(self):
        """
        Returns the name of the person

        Args:
            None
        
        Returns:
            str
        """
        return self.name
    
    def getLastname(self):
        """
        Returns the lastname of the person

        Args:
            None
        
        Returns:
            str
            None
        """
        return self.lastname
    
    def getPhone(self):
        """
        Returns the phone of the person

        Args:
            None
        
        Returns:
            str
            int
        """
        return self.phone
    
    def getEmail(self):
        """
        Returns the email of the person

        Args:
            None
        
        Returns:
            str
            None
        """
        return self.email

    def setName(self, name):
        """
        Sets the name of the person

        Args:
            name (str)
        
        Returns:
            Person: Instance of itself
        """
        self.name = name
        return self

    def setLastname(self, lastname):
        """
        Sets the lastname of the person

        Args:
            lastname (str, None)
        
        Returns:
            Person: Instance of itself
        """
        self.lastname = lastname
        return self

    def setPhone(self, phone):
        """
        Sets the phone of the person

        Args:
            phone (str, int)
        
        Returns:
            Person: Instance of itself
        """
        self.phone = phone
        return self

    def setEmail(self, email):
        """
        Sets the email of the person

        Args:
            email (str, None)
        
        Returns:
            Person: Instance of itself
        """
        self.email = email
        return self
