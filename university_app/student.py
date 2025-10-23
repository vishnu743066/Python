import logging as lg
lg.basicConfig(
    filename="University.log",
    level=lg.DEBUG,
    format = "[%(asctime)s - %(levelname)s] - %(message)s"
)
from person import Person    
class Student(Person):
    # student take name,student id,branch,email id
    def __init__(self, name, student_id, branch, email_id):
        # by using super() method automatically call person class constructor
        super().__init__(name)
        self.student_id = student_id
        self.branch = branch
        self.email_id = email_id

    def display(self):
        lg.info("Student details displayed")
        # display name,student id,branch,email id by super() method automatically call person class method
        print(super().display())
        print(f"Student ID: {self.student_id}, Branch: {self.branch}, Email ID: {self.email_id}")
