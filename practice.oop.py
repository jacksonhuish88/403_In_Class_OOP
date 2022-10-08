#Testing Testing
# Hey Dallas we are doing everything


# Make attributes Private
# Make Getters / Setters
# oStud.Course.append()

#Person Class
class Person():
    def __init__ (self, fName, lName) :
        self.first_name = fName
        self.last_name = lName

#Student Class
class Student(Person):
    
    def __init__ (self, fName, lName, GPA) :
        super().__init__(fName, lName)
        self.gpa = GPA
        self.course = []

    def scholarship_status(self):
            if self.gpa >= 3.95:
                return(self.first_name + ' ' + self.last_name + " has a Full Scholarship")
            elif self.gpa >= 3.9:
                return(self.first_name + ' ' + self.last_name + " has a Part Scholarship")
            else:
                return(self.first_name + ' ' + self.last_name + " has No Scholarship")

#Falcuty Class
class Faculty(Person):
    
    def __init__ (self, fName, lName, tenure) :
        super().__init__(fName, lName)
        self.tenure = tenure

    def tenure_status(self):
        if self.tenure == "Y":
            return(self.first_name + ' ' + self.last_name + ' has tenure.')
        elif self.tenure == "N":
            return(self.first_name + ' ' + self.last_name + ' does not have tenure.')

#Course Class
class Course(): 
    def __init__(self, cName):
        self.course_name = cName


#---------------------------------------------------
#---------------- C O U R S E ----------------------
#---------------------------------------------------

#Course Input
oCName = input("Enter the course name: ")

# Creating Course Object
oCourse = Course("oCName")


#---------------------------------------------------
#----------------- S T U D E N T -------------------
#---------------------------------------------------

# Student Inputs
oSfName = input("\nEnter the student's first name: ")
oSlName = input("Enter the student's last name: ")
oSGPA = float(input("Enter the student's GPA: "))

# Creating Student Object
oStudent = Student(oSfName, oSlName, oSGPA)
oStudent.course = oCourse

# Return Student Scholarship Info
print(oStudent.scholarship_status())


#---------------------------------------------------
#---------------F A C U L T Y ----------------------
#---------------------------------------------------


# Falcuty Inputs
oFfName = input("\nEnter the faculty members's first name: ")
oFlName = input("Enter the faculty member's last name: ")
oFTenure = input("Enter the faculty member's tenure status (Y/N): ").upper()

# Creating Faculty Object
oFaculty = Faculty(oFfName, oFlName, oFTenure)

# Return Faculty Tenure Status
print(oFaculty.tenure_status())
