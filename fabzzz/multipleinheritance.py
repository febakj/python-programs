class Flyer:
    def fly(self):
        return "Flying"

class Swimmer:
    def swim(self):
        return "Swimming"

class Duck(Flyer, Swimmer):
    pass

# Usage
duck = Duck()
print(duck.fly())  # Flying
print(duck.swim())  # Swimming
