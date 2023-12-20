#Exercice 1 

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
     def sing(self, sounds):
        return f'{sounds}'

# Create instances of different cat breeds
bengal_cat = Bengal("Bengal Cat", 3)
Chartreux_cat = Chartreux("Chartreux Cat", 4)
siamese_cat = Siamese("Siamese Cat", 2)

all_cats = [bengal_cat, Chartreux_cat, siamese_cat]

sara_pets = Pets(all_cats)
sara_pets.walk()

#Exercice 2

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def bark(self):
        return f"{self.name} is barking"
    
    def run_speed(self):
        return self.weight / self.age * 10
    
    def fight(self, other_dog):

        self_run_speed = self.run_speed() * self.weight
        other_dog_run_speed = other_dog.run_speed() * other_dog.weight

        if self_run_speed > other_dog_run_speed:
            return f"{self.name} won the fight!"
        elif self_run_speed < other_dog_run_speed:
            return f"{other_dog.name} won the fight!"
        else:
            return "No winner in this fight."
        
dog1 = Dog("Caramel", 3, 15)
dog2 = Dog("Max", 4, 18)

# Testing the methods
print(dog1.bark()) 
print(f"Running speed of {dog1.name}: {dog1.run_speed()}") 
print(dog1.fight(dog2))        

#Exercice 3

