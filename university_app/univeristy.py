class Person:
    # person take name
    def __init__(self, name):
        self.name = name

    def display(self):
        # display name
        print(f"Name: {self.name}")
        
        
class Student(Person):
    # student take name,student id,branch,email id
    def __init__(self, name, student_id, branch, email_id):
        # by using super() method automatically call person class constructor
        super().__init__(name)
        self.student_id = student_id
        self.branch = branch
        self.email_id = email_id

    def display(self):
        # display name,student id,branch,email id by super() method automatically call person class method
        print(super().display())
        print(f"Student ID: {self.student_id}, Branch: {self.branch}, Email ID: {self.email_id}")

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
        # display name, department, employee id, subject, branch, salary by super() method automatically call person class method
        print(super().display())
        print(f"Department: {self.department}, Employee ID: {self.employee_id}, Subject: {self.subject}, Branch: {self.branch}, Salary: {self.salary}")

class University:
    def __init__(self, university_name, course=list[str]):
        self.university_name = university_name
        self.course = course
        self.students_table = {}
        self.emp_table = {}
    
    # add student method  that takes employee onject on parameter
    def addStudent(self, std_obj):
        if std_obj.student_id not in self.students_table:
            self.students_table[std_obj.student_id] = [std_obj.name, std_obj.branch, std_obj.email_id]
            return f"Successfully {std_obj.name} added to university"
        else:
            return "Student already exists"
    
    # add professor method that takes professor object on parameter
    def addProfessor(self, prof_obj):
        if prof_obj.employee_id not in self.emp_table:
            self.emp_table[prof_obj.employee_id] = [prof_obj.name, prof_obj.department, prof_obj.subject, prof_obj.branch, prof_obj.salary]
            return f"Successfully {prof_obj.name} added to university"
        else:
            return "Professor already exists"

    # add course method that takes current course list:
    def addCourse(self, new_course):
        self.course.append(new_course)
        
            
    #total student list,(based on requirement it returns)
    def totalStudents(self,search_branch:str=None):
        if search_branch:
            for item in self.students_table.items():
                if item[1][1] == search_branch:
                    print(item)
        else:
            for item in self.students_table.items():
                print(item)
    
    # total employee lsit,(based on requirement it retuns)
    def totalEmployees(self,search_dept:str=None):
        if search_dept:
            for item in self.emp_table.items():
                if item[1][1] == search_dept:
                    print(item)
        else:
            for item in self.emp_table.items():
                print(item)

# create main function        
if __name__ == "__main__":
    uni = University("University", ["DS", "DA", "PFS", "JFS"])
    # creating student objects 
    S1=Student("VISHNU VARDHAN","S101","DS","PABO.CS@RMKEC.AC.IN")
    S2=Student("RAHUL","S102","DA","abc4.CS@RMKEC.AC.IN")
    S3=Student("KARTHIK","S103","PFS","xyz123.@gmail.com")
    S4=Student("NAVEEN","S104","JFS","naveen12.@gmail.com")
    S5=Student("MANOJ","S105","DS","manoj34.@gmail.com")
    S6=Student("RISHIKESH","S106","DA","rishi56.@gmail.com")
    S7=Student("SUSHANTH","S107","PFS","sushanth78.@gmail.com")
    S8=Student("PRASANTH","S108","JFS","prasanth90.@gmail.com")
    S9=Student("KIRAN","S109","DS","kiran11.@gmail.com")
    S10=Student("ABHILASH","S110","DA","abhilash22.@gmail.com")
    S11=Student("NAGA SAI","S111","PFS","nagasai33.@gmail.com")
    S12=Student("RAVI","S112","JFS","ravi44.@gmail.com")
    S13=Student("AKASH","S113","DS","akash55.@gmail.com")
    S14=Student("SAI","S114","DA","sai66.@gmail.com")
    S15=Student("RAM CHARAN","S115","PFS","ramcharan77.@gmail.com")
    S16=Student("CHARAN","S116","JFS","kurucharana88.@gmail.com")
    S17=Student("KRISHNA","S117","DS","abhinav99.@gmail.com")
    S18=Student("RUTHIK","S118","DA","ruthikreddy00.@gmail.com")
    S19=Student("BHUVAN","S119","PFS","bhuvan21.@gmail.com")
    S20=Student("VAMSI","S120","JFS","vamsikrishna32.@gmail.com")
    # adding student data into the student table by using addStudent method
    uni.addStudent(S1)
    uni.addStudent(S2)
    uni.addStudent(S3)
    uni.addStudent(S4)
    uni.addStudent(S5)
    uni.addStudent(S6)
    uni.addStudent(S7)
    uni.addStudent(S8)
    uni.addStudent(S9)
    uni.addStudent(S10)
    uni.addStudent(S11)
    uni.addStudent(S12)
    uni.addStudent(S13)
    uni.addStudent(S14)
    uni.addStudent(S15)
    uni.addStudent(S16)
    uni.addStudent(S17)
    uni.addStudent(S18)
    uni.addStudent(S19)
    uni.addStudent(S20)
    # creating professor objects
    E1=Professor("Dr.Abhilash","CSE","E101","DS","DS","50000")
    E2=Professor("Dr.Shivakrishna","CSE","E102","DA","DA","60000")
    E3=Professor("Dr.Bhanu","CSE","E103","PFS","PFS","70000")
    E4=Professor("Dr.Manoj","CSE","E104","JFS","JFS","80000")
    E5=Professor("Dr.Prasanth","CSE","E105","DS","DS","90000")
    E6=Professor("Dr.Kiran","CSE","E106","DA","DA","100000")
    E7=Professor("Dr.Rishi","CSE","E107","PFS","PFS","110000")
    E8=Professor("Dr.Sushanth","CSE","E108","JFS","JFS","120000")
    E9=Professor("Dr.Naveen","CSE","E109","DS","DS","130000")
    E10=Professor("Dr.Naga sai","CSE","E110","DA","DA","140000")
    E11=Professor("Dr.Abhinav","ECE","E111","DA","DA","140000")
    E12=Professor("Dr.Ruthik reddy","MECH","E112","DA","DA","140000")
    E13=Professor("Dr.Bhuvun","CIVIL","E113","DA","DA","140000")
    E14=Professor("Dr.Vamsi krishna","MBA","E114","DA","DA","140000")
    E15=Professor("Dr.Rishivanth","MCA","E115","DA","DA","140000")
    E16=Professor("Dr.Ram charan","CSE","E116","DA","DA","140000")
    E17=Professor("Dr.Kuru charan","CSE","E117","DA","DA","140000")
    E18=Professor("Dr.Ravi","CSE","E118","DA","DA","140000")
    E19=Professor("Dr.Sai","CSE","E119","DA","DA","140000")
    E20=Professor("Dr.Akash","CSE","E120","DA","DA","140000")
    # adding professor data into the employee table by using addProfessor method
    uni.addProfessor(E1)
    uni.addProfessor(E2)
    uni.addProfessor(E3)
    uni.addProfessor(E4)
    uni.addProfessor(E5)
    uni.addProfessor(E6)
    uni.addProfessor(E7)
    uni.addProfessor(E8)
    uni.addProfessor(E9)
    uni.addProfessor(E10)
    uni.addProfessor(E11)
    uni.addProfessor(E12)
    uni.addProfessor(E13)
    uni.addProfessor(E14)
    uni.addProfessor(E15)
    uni.addProfessor(E16)
    uni.addProfessor(E17)
    uni.addProfessor(E18)
    uni.addProfessor(E19)
    uni.addProfessor(E20)
    # print total student and employee list
    print(uni.totalStudents())
    print(uni.totalEmployees())
    # print total student and employee list based on branch and department
    print(uni.totalStudents("DS"))
    print(uni.totalEmployees("CSE"))