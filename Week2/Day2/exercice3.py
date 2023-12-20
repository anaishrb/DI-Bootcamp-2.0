#Exercice 3

from exercice import Dog
import random

class PetDog(Dog):  # Inheriting from the Dog class
    def __init__(self, name, age, weight, breed):
        super().__init__(name, age, weight)
        self.breed = breed
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dog_names = ', '.join(args)
        print(f"{dog_names} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(random.choice(tricks))
        else:
            print("The dog is not trained yet.")

# Example usage
if __name__ == "__main__":
    pet_dog = PetDog("Buddy", 3, 15, "Labrador")

    pet_dog.train()  

    pet_dog.play("Max", "Rocky", "Charlie")  

    # Performing a trick
    pet_dog.do_a_trick()  

#Exercice 4

class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulations! A new child named {kwargs['name']} was born to the {self.last_name} family.")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False  # Return False if the member's name is not found

    def family_presentation(self):
        print(f"Family Name: {self.last_name}")
        print("Family Members:")
        for member in self.members:
            print(f"Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']}, Child: {member['is_child']}")

members_list = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
]

family = Family("Smith", members_list)

family.born(name='John', age=0, gender='Male', is_child=True)  
print(f"Is Michael over 18? {family.is_18('Michael')}")  
family.family_presentation()  

#Exercice 5

my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]
