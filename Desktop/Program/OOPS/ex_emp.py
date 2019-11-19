class Employee():
    'Common base class for all employees'
    empCount = 0

    def __init__(self, eid, name, salary, did):
        self.eid = eid
        self.name = name
        self.salary = salary
        self.did = did
        Employee.empCount += 1
     
    def displayEmployee(self):
        print ("eid : ", self.eid,", Name : ", self.name,  ", Salary: ", self.salary,  ", did: ", self.did)
    

"This would create first object of Employee class"
emp1 = Employee(1,"Zara", 2000,10)

"This would create second object of Employee class"
emp2 = Employee(2,"Meera", 4000,20)

"This would create 3rd object of Employee class"
emp3 = Employee(3,"Gucci", 50000,30)

emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
print ("Total Employee %d" % Employee.empCount)


