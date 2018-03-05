class Student(object):
    def __init__(self,name="",school="",grade=""):
 
        if not name:
            name=raw_input("name?")
        if not school:
            school=raw_input("school?")
        if grade not in grade1:
            grade=self.get_grade()
        self.name=name
        self.school=school
        self.grade=grade
        

    def get_grade(self):
        grade=raw_input("grade?")
        while True:
 
            if grade not in grade1:
                grade=raw_input("grade?")
            else:
                break
        return grade
                

    def print_student(self):
        print self.name,
        print self.school,
        print self.grade
        
def print_roster(students):
    for a in students:
        a.print_student()
    
def main():
        global grade1
        grade1=["a","b"]
        student1=Student()
        student2=Student()
        students=[student1,student2]
        print_roster(students)
 
        
        
if __name__=="__main__":
        main()
        
        

    
            
    
