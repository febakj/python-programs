class Animal:
    def speak(self):
        return "Some generic sound"

class Mammal(Animal):
    def has_fur(self):
        return True

class Dog(Mammal):
    def speak(self):
        return "Woof!"

# Usage
dog = Dog()
print(dog.speak())  # Woof!
print(dog.has_fur())  # True
