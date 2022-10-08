# Make attributes Private
# Make Getters / Setters
# oStud.Course.append()

#Person Class
class Person():
    def __init__ (self, fName, lName) :
        self.__first_name = fName
        self.__last_name = lName

# Student/Instructors Getters & Setters
    def set_name (self, fname, lname) :
        self.__first_name = fname
        self.__last_name = lname

    def get_name(self) :
        return(self.__first_name + " " + self.__last_name)

#Student Class
class Student(Person):
    
    def __init__ (self, fName, lName, GPA) :
        super().__init__(fName, lName)
        self.__gpa = GPA
        self.__course = []

    def scholarship_status(self):
            if self.__gpa >= 3.95:
                return(self.get_name + " has a Full Scholarship")
            elif self.__gpa >= 3.9:
                return(self.get_name+ " has a Part Scholarship")
            else:
                return(self.get_name + " has No Scholarship")

    def set_gpa(self, GPA):
        self.__gpa = GPA

    def get_gpa(self):
        return(self.__gpa)


#Faculty Class
class Faculty(Person):
    
    def __init__ (self, fName, lName, tenure) :
        super().__init__(fName, lName)
        self.__tenure = tenure

    def get_tenure_status(self):
        if self.__tenure == "Y":
            return(self.get_name + ' has tenure.')
        elif self.__tenure == "N":
            return(self.get_name + ' does not have tenure.')

    def set_tenure(self, tenure) : 
        self.__tenure = tenure
    
    def get_tenure(self) :
        return(self.__tenure)

#Course Class
class Course(): 
    def __init__(self, cName):
        self.__course_name = cName

    # Course Getters & Setters
    def set_name(self, course) :
        self.__course_name = course

    def get_name(self) :
        return(self.__course_name)


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
oStudent.__course = oCourse

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
print(oFaculty.get_tenure_status())