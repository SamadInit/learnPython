from abc import ABC,abstractmethod
class Employee(ABC):
    mat=1

    def __init__(self,name,address):
         self.name=name
         self.adress=address
         self.matriclue=Employee.mat
         Employee.mat+=1
    @abstractmethod
    def getSalaire():
         pass