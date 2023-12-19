#functions

def say_hello(username, language):
    if language == "EN":
        print("Hello "+ username)
    elif language == "FR":
        print("Bonjour "+username)
    else:
        print("This language is not supported: " + language)


username = "Rick"
language = "FR"

say_hello(username, language) #variable arguments
say_hello('Rick', 'FR') # positional arguments
say_hello(username="Rick", language="FR") #keyword arguments
say_hello("Rick", language="EN") #mixed arguments: 1st has to be positional


#DEFAULT VALUE IN ARGUMENTS
def say_hello(username, language = 'EN'):
    if language == "EN":
        print("Hello "+ username)
    elif language == "FR":
        print("Bonjour "+username)
    else:
        print("This language is not supported: " + language)

say_hello('Juliana')


# 6. Local And Global Scope
# Local Scope

def number_by_three(name, day):
    #local scope
    sentence = f'Hello {name}! Today is {day}.'
    print(sentence)

# print(name) #impossible to use the variables from the local
#in the global scope



# Global Scope
# name = 'Avner'

# def say_hi():
#   name = name.lower()
#   print(name)

# say_hi()

def square(number:int)-> int:
    num_squared = number**2
    return num_squared

print(square(2))

def country_info(country:str)-> tuple:
    '''checks the population and capital of a country'''
    if country == 'Israel':
        population = 9364000
        capital = 'Jerusalem'
        squared_pop = square(population)
    if country == 'Russia':
        population = 143400000
        capital = 'Moscow'
        squared_pop = square(population)
    if country == 'Brazil':
        population = 214300000
        capital = 'Brasilia'
        squared_pop = square(population)
    
    return population, squared_pop, capital

print(country_info('Russia'))

pop, sq, cap = country_info('Brazil')
print(sq)

a = country_info('Israel')

print(f'The population is {a[0]}')


