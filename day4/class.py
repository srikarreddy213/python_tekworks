class Student:
    def __init__(self, name, roll, marks):
        self.name = name #private
        self.roll = roll#public
        self.marks = marks#protected

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll)
        print("Marks:", self.marks)


s = Student("Srikar", "23b81a67b3", 28)
s.display()
