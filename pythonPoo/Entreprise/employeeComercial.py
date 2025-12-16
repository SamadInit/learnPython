from employee import Employee
class EmployeeWeek(Employee):

    def __init__(self,name,address,weeks=0,perW=0):
        super().__init__(name,address)
        self.weeks=weeks
        self.perW=perW
    def getSalaire(self):
        return self.weeks*self.perW
