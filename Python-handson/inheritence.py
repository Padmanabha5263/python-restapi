
class Animal:
    def __init__(self, name,  color):
        self.name=name
        self.color=color
    
    def __str__(self):
        return f"name = {self.name} and color = {self.color}"

class Dog(Animal):
    def __init__(self,name, color, age):
        super().__init__(name, color)
        self.age=age
    
    def __str__(self):
        return f"{super().__str__()} and age = {self.age}"

Dog1 = Dog("dashands", "brown", 12)
print(Dog1)