class Employee:
    count = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count = Employee.count + 1
    
    def displayCount(self):
        print("The number of employees in the organization are: ", self.count)
        
    @staticmethod
    def validateEmployId(employee_id):
        if(len(employee_id) > 5 and len(employee_id) <= 10) and employee_id[:3].isalpha():
            print("Valid Employee Id")
        else:
            print("Not a Valid Employee Id")
        
        
e1 = Employee("Ram",20000)   
e2 = Employee("Vijay", 25000)
e3 = Employee("Nandhana",25000)

e1.displayCount()
e1.validateEmployId("ABE12341")

