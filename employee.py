class Employee:
    def __init__(self, firstname, lastname) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = f"{firstname} {lastname}"
        self.email = f"{firstname}.{lastname}@company.com"

#emp_1 = Employee("John", "Smith")               
#emp_2 = Employee("Mary",  "Sue")             
#emp_3 = Employee("Antony", "Walker")
                  
#print(emp_1.fullname)
#print(emp_2.email)
#print(emp_3.firstname)