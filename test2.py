import random

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

def create_random_animal():
    animals = [Dog, Cat]
    names = ["Buddy", "Mittens", "Rex", "Whiskers"]
    name = random.choice(names)
    age = random.randint(1, 15)
    animal_class = random.choice(animals)
    return animal_class(name, age)

if __name__ == "__main__":
    random_animal = create_random_animal()
    print(f"Created a {random_animal.__class__.__name__} named {random_animal.name} who is {random_animal.age} years old.")
    print(random_animal.speak())