class Employee():
    mat=1

    def __init__(self,name,address):
         self.name=name
         self.adress=address
         self.matriclue=Employee.mat
         Employee.mat+=1
    
