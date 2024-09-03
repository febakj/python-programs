class Animal:
    def make_sound(self):
        return "Some sound"

class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

def print_animal_sound(animal):
    print(animal.make_sound())

dog = Dog()
cat = Cat()

print_animal_sound(dog)  # Output: Bark
print_animal_sound(cat)  # Output: Meow
