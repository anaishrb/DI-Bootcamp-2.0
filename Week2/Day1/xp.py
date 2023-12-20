#Exercice 1

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat("Caramel", 2)
cat2 = Cat("Filou", 3)
cat3 = Cat("Lila", 7)

def oldest_cat(*cats):
    oldest_cat = None
    max_age = float("-inf")

    for cat in cats:
        if cat.age > max_age:
            max_age = cat.age
            oldest_cat = cat

    return oldest_cat
oldest = oldest_cat(cat1, cat2, cat3)

if oldest:
   print(f"The oldest cat is {oldest.name} and is {oldest.age} years old.")
else:
    print("No cats found.")

#Exercice 2

class Dog:
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        jump_height = self.height * 2
        print(f"{self.name} jumps {jump_height} cm high")

          
davids_dog = Dog("Rex", 50)

print(f"Details of David's dog - Name: {davids_dog.name}, Height: {davids_dog.height} cm")
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)
print(f"\nDetails of Sarah's dog - Name: {sarahs_dog.name}, Height: {sarahs_dog.height} cm")
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"\n{davids_dog.name} is the bigger dog.")
elif sarahs_dog.height > davids_dog.height:
    print(f"\n{sarahs_dog.name} is the bigger dog.")
else:
    print("\nThe dogs are of the same height.")


#Exercice 3 
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
stairway = Song([
    "There’s a lady who's sure",
    "all that glitters is gold",
    "and she’s buying a stairway to heaven"
])
stairway.sing_me_a_song()


#Exercice 4

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animals(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"{new_animal} added to the zoo!")

    def get_animals(self):
        print("Animals in the zoo:")
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold.")

    def sort_animals(self):
        sorted_animals = {}
        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in sorted_animals:
                sorted_animals[first_letter] = [animal]
            else:
                sorted_animals[first_letter].append(animal)
                
        for key in sorted_animals:
            sorted_animals[key].sort()

        return sorted_animals

    def get_groups(self):
        sorted_animals = self.sort_animals()
        print("Groups of animals:")
        for key, value in sorted_animals.items():
            print(f"{key}: {value}")
my_zoo = Zoo("My Zoo")

# Add animals to the zoo
my_zoo.add_animals("Ape")
my_zoo.add_animals("Bear")
my_zoo.add_animals("Baboon")
my_zoo.add_animals("Cat")
my_zoo.add_animals("Cougar")
my_zoo.add_animals("Eel")
my_zoo.add_animals("Emu")

my_zoo.get_animals()

my_zoo.sell_animal("Ape")

my_zoo.get_groups()