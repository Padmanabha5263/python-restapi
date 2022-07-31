class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grades = grade
    
    def average(self):
        return sum(self.grades)/len(self.grades)

    @staticmethod
    def static_method():
        print("called static method")

Student.static_method()
st1 = Student("padmanabha", (60, 70, 60))
print(st1.name)
print(st1.grades)
print(st1) #   <__main__.Student object at 0x000001667FB17D60>



# __str__ method and __repr__ method

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name={self.name} and age= {self.age}"

    def __repr__(self):
        return f"name={self.name} and age= {self.age}"

pr2 = Person("padmanabha", 60)
print(pr2)