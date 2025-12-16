from employee import Employee
class EmployeeHour(Employee):

    def __init__(self,name,address,hours=0,perh=0):
        super().__init__(name,address)
        self.hours=hours
        self.perh=perh

    def getSalaire(self):
        return self.hours*self.perh