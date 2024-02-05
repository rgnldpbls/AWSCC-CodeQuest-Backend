class Student:
    def __init__(self, name, age, is_enrolled, classes, offenses):
        self.name = name
        self.age = age
        self.is_enrolled = is_enrolled
        self.classes = classes
        self.offenses = offenses
    
    def addClass(self, newClass):
        self.classes.append(newClass)

    def addOffense(self, newOffense):
        self.offenses.append(newOffense)

student1 = Student("Juan Dela Cruz", 20, True, [], [])
student1.addClass('English')
student1.addClass('Mathematics')
student1.addOffense('Late')

print(f"Name: {student1.name}")
print(f"Age: {student1.age}")
print(f"Status: {'Enrolled' if student1.is_enrolled else 'Not Enrolled Yet'}")
print(f"Classes: {student1.classes}")
print(f"Offenses: {student1.offenses}")

