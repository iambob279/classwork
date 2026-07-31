class Person:
    #attributes
    first_name=""
    last_name=""

    def __init__(self, given_first_name, given_last_name):
        self.first_name = given_first_name
        self.last_name = given_last_name

    def set_first_name(self, given_first_name):
        self.first_name = given_first_name

    def get_first_name (self):
        return self.first_name
        
    def set_last_name(self, given_last_name):
        self.last_name = given_last_name

    def get_last_name (self):
        return self.last_name

class Student(Person):
    #attributes
    subject_studied=""

    def __init__(self, first_name, given_last_name, given_subject_studied):
        super().__init__(first_name, given_last_name)
        self.subject_studied = given_subject_studied

    def set_subject_studied(self, given_subject_studied):
        self.subject_studied = given_subject_studied

    def get_subject_studied (self):
        return self.subject_studied

class Teacher(Person):
    subject_taught = ""

    def __init__(self, firstname, lastname, taughtsubject):
        super().__init__(firstname, lastname)
        self.subject_taught = taughtsubject
    
    def setsubjecttaught(self, taughtsubject):
        self.subject_taught = taughtsubject
    
    def getsubjecttaught(self):
        return self.subject_taught


    
        

s1 = Student("Rishi", "Sunak", "Maths")
s2 = Student("Keir", "Starmer", "English")
s3 = Teacher("Bradley", "something", "comp sci")


print (s1.get_first_name(), s1.get_last_name(), 'is currently studying', s1.get_subject_studied())
print (s2.get_first_name(), s2.get_last_name(), 'is currently studying', s2.get_subject_studied())
print(s3.get_first_name(), s3.get_last_name(), "Is current teaching", s3.getsubjecttaught())
