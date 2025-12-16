from employee import Employee
class EmployeeDay(Employee):

    def __init__(self,name,address,days=0,perD=0):
        super().__init__(name,address)
        self.days=days
        self.perD=perD

    def getSalaire(self):
        return self.days*self.days