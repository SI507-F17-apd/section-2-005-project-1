class Student:
    def __init__(self, first_name, last_name):
        self.name = first_name + ' ' + last_name

    def __str__(self):
        return "Student's name is {0}".format(self.name)

a = Student('Anand', 'Doshi')
print(a.name)
print(a)
print(str(a)=="Student's name is Anand Doshi")
# Anand Doshi
