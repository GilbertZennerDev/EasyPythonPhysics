#Objects: INHERITANCE

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Unknown sound"

    def sleep(self):
        return f"{self.name} is sleeping."

class Dog(Animal): # Dog inherits from Animal
    def __init__(self, name, breed):
        super().__init__(name) # Calls the constructor of the parent class
        self.breed = breed

    def make_sound(self): # Overrides the parent class's method
        return "Woof! Woof!"

    def fetch(self):
        return f"{self.name} fetches the ball!"

class Cat(Animal): # Cat also inherits from Animal
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color

    def make_sound(self): # Overrides the parent class's method
        return "Meow!"

# Create objects
my_animal = Animal("Lissy")
my_dog = Dog("Bello", "Golden Retriever")
my_cat = Cat("Minka", "Black")
print("Animal class")
print("************")
print(my_animal.make_sound())
print(my_animal.sleep())
print()
print("Dog Class")
print("*********")
print(my_dog.make_sound())
print(my_dog.sleep())
print(my_dog.fetch()) # Specific method for Dog
print()
print("Cat class")
print("*********")
print(my_cat.make_sound())
print(my_cat.sleep())
