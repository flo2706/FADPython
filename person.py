class Person :
    def __init__(self, lastname, firstname, address) -> None:
        self.lastname = lastname
        self.firstname = firstname
        self.address = address
    
    clean_name = lambda name: ''.join([char for char in name if char.isalpha()]).strip().title()


    @property
    def lastname(self):
        return self.__lastname
    
    @lastname.setter
    def lastname(self, lastname):
        clean_lastname = Person.clean_name(lastname)
        self.__lastname = clean_lastname
    
    @property
    def firstname(self):
        return self.__firstname
    
    @firstname.setter
    def firstname(self, firstname):
        clean_firstname = Person.clean_name(firstname)
        self.__firstname = clean_firstname.strip().title()

    @property
    def address(self):
        return self.__address
    
    @address.setter
    def address(self, address):
        self.__address = address.strip()
    
    def __str__(self) -> str:
        return f"Lastname: {self.lastname}, Firstname: {self.firstname}, Address: {self.address}"
    
