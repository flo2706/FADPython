from person import Person

class Employee(Person):
    def __init__(self, lastname, firstname, address, job_title) -> None:
        super().__init__(lastname, firstname, address)
        self.job_title = job_title
    
    @property
    def job_title(self):
        return self.__job_title 
    
    @job_title.setter
    def job_title(self, job_title):
        self.__job_title = job_title.strip()
        
    def __str__(self) -> str:
        return super().__str__() + f", JobTitle: {self.job_title}"