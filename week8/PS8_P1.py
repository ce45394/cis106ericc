class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def bonus(self):
        return self.salary * 0.10

    def display(self):
        print("Employee:", self.first_name, self.last_name)
        print("Salary: $", self.salary)
        print("Bonus: $", self.bonus())
        print()


# Derived Manager class
class Manager(Employee):
    def bonus(self):
        return self.salary * 0.20

    def long_term_bonus(self):
        return self.salary * 0.50


# Test the classes
emp1 = Employee("Ali", "Baba", 60000)
emp1.display()

mgr1 = Manager("The", "Cook", 90000)
mgr1.display()
print("Long Term Bonus: $", mgr1.long_term_bonus())
