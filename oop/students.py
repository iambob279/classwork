class students:
    id = ""
    name = ""
    age = ""
    subject = ""

    def __init__(self, studentid, studentname, studentage, studentsubject):
        self.id = studentid
        self.name = studentname
        self.age = studentage
        self.subject = studentsubject

    def get_student_information(self):
        return self.id, self.name, self.age, self.subject

person = students("AD1893", "David", "19", "Computer science")

print(person.get_student_information())