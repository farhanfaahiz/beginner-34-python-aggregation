class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
        
    def annual_salary(self):
        return (self.pay * 12) + self.bonus
    
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.obj_salary = salary
        
    def total_salary(self):
        return self.obj_salary.annual_salary()
    
salary = Salary(15000, 10000)
    
emp = Employee('max', 15, salary)
print(emp.total_salary())

# retry

class Salary:
    def __init__ (self, pay, bonus):
        self.__pay = pay
        self.__bonus = bonus
        
    def annual_salary(self):
        return (self.__pay * 12) 
    
class Employee:
    def __init__ (self, name, office, age, salary):
        self.__name = name
        self.__office = office
        self.__age = age
        self.obj_salary = salary
        
    def Total_salary (self):
        return self.obj_salary.annual_salary()
    
salary = Salary(500000, 200000)

emp = Employee('Farhan', 'HOD', 27, salary)
print(emp.Total_salary()) 