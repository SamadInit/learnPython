from employee import Employee
from employeeComercial import EmployeeWeek
from employeeDay import EmployeeDay
from employeeHour import EmployeeHour

if  __name__=="__main__":
    
    emp1=EmployeeHour("abdessamad","rue 13 el fath",50,12)
    emp2=EmployeeDay("mohammed","majidi rue 14",14,100)
    emp3=EmployeeWeek("mahmoud","agadir tadaart rue 1",20,20)
    emps=[]
    emps.append(emp1)
    emps.append(emp2)
    emps.append(emp3)

    for i in emps:
        print(i.getSalaire())
        if isinstance(i,EmployeeHour):
            var=i.getSalaire()
            var=(var/24)/7
            print(f"the total earned in a week is : {var}")
        elif isinstance(i,EmployeeDay):
            var=i.getSalaire()
            var=var/7
            print(f"the total earned in a week is : {var}")
        elif isinstance(i,EmployeeWeek):
            print("the totale earned this week is also {}".format(i.getSalaire()/7))
        
        print("___________________________________")
