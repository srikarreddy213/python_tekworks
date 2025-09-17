
class Empoly:
    def __init__(self, name, eid, salary):
        self.name = name 
        self.eid = eid
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Employ id:", self.eid)
        print("Salary:", self.salary)



class Manager(Empoly):  
    def __init__(self, name, eid, salary, dep):
        super().__init__(name, eid, salary)  
        self.dep = dep

    def display(self):
        super().display()  
        print("Department:", self.dep)



emp = Empoly("Srikar", "23b81a67b3", 280000)
emp.display()

print("\nManager Info:")
mgr = Manager("Ravi", "23b81a67m1", 500000, "IT")
mgr.display()
