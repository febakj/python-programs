# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some generic sound"

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Usage
my_dog = Dog("Buddy")
print(my_dog.name)  # Buddy
print(my_dog.speak())  # Woof!
