import logging as lg
lg.basicConfig(
    filename="University.log",
    level=lg.DEBUG,
    format = "[%(asctime)s - %(levelname)s] - %(message)s"
)
from person import Person

class Professor(Person):
    # professor take name, department, employee id, subject, branch, salary
    def __init__(self, name, department, employee_id, subject, branch, salary):
        # by using super() method automatically call person class constructor
        super().__init__(name)
        self.department = department
        self.employee_id = employee_id
        self.subject = subject
        self.branch = branch
        self.salary = salary

    def display(self):
        lg.info("Professor details displayed")
        # display name, department, employee id, subject, branch, salary by super() method automatically call person class method
        print(super().display())
        print(f"Department: {self.department}, Employee ID: {self.employee_id}, Subject: {self.subject}, Branch: {self.branch}, Salary: {self.salary}")
