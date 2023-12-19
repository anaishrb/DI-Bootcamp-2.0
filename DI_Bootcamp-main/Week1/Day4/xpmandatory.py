#Exercice 1

def display_message():
    """We are learning data science"""
    print("We are learning data science")
display_message()

#Exercice 2

def favorite_book(book):
    print("My favourite book is " + book)

favorite_book("Harry Poter")

#Exercice 3

def describe_city(city, country="Israel"):
    if country == "Israel":
        print(city + " is in Israel")


describe_city("Tel Aviv")

#Exercice 5

def make_shirt(size="Large", text="I love python"):
        print(f"The size of the shirt is {size} and the text is '{text}'.")

make_shirt("medium")
make_shirt("medium", "I love Tel Aviv")

#Exercice 6

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magician_names):
     print(magician_names)

show_magicians(magician_names)

def make_great(show_magicians):
     for i in range(len(show_magicians)):
        show_magicians[i] += " The Great" 
        print(show_magicians)
        
print("n\After modification:")
make_great(magician_names)

#Exercice 7 

import random
def get_random_temp():
    return random.randint(-10, 40)
for _ in range(2):  # Generating 2 random temperatures for testing
    random_temperature = get_random_temp()
    print(f"Random temperature: {random_temperature} degrees Celsius")

def main(get_random_temp)