import logging as lg
lg.basicConfig(
    filename="University.log",
    level=lg.DEBUG,
    format = "[%(asctime)s - %(levelname)s] - %(message)s"
)

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
            lg.info(f"Student {std_obj.name} added to university")
            return f"Successfully {std_obj.name} added to university"
        else:
            lg.warning("Student already exists")
            return "Student already exists"
    
    # add professor method that takes professor object on parameter
    def addProfessor(self, prof_obj):
        if prof_obj.employee_id not in self.emp_table:
            self.emp_table[prof_obj.employee_id] = [prof_obj.name, prof_obj.department, prof_obj.subject, prof_obj.branch, prof_obj.salary]
            lg.info(f"Professor {prof_obj.name} added to university")
            return f"Successfully {prof_obj.name} added to university"
        else:
            lg.warning("Professor already exists")
            return "Professor already exists"

    # add course method that takes current course list:
    def addCourse(self, new_course):
        self.course.append(new_course)
        lg.info(f"Course {new_course} added to university")
        return f"Successfully {new_course} added to university"
        
            
    #total student list,(based on requirement it returns)
    def totalStudents(self,search_branch:str=None):
        if search_branch:
            for item in self.students_table.items():
                if item[1][1] == search_branch:
                    lg.info(f"Student found in branch {search_branch}: {item[1][0]}")
                    print(item)
        else:
            for item in self.students_table.items():
                lg.info(f"Student details: {item[1][0]}")
                print(item)
    
    # total employee lsit,(based on requirement it retuns)
    def totalEmployees(self,search_dept:str=None):
        if search_dept:
            for item in self.emp_table.items():
                if item[1][1] == search_dept:
                    lg.info(f"Employee found in department {search_dept}: {item[1][0]}")
                    print(item)
        else:
            for item in self.emp_table.items():
                lg.info(f"Employee details: {item[1][0]}")
                print(item)