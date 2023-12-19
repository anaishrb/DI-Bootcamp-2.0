## Variables and data types ##
# x = 7
# y = 13
# print(x+y)

# greeting = 'hello world'

# print(greeting[2:5])

## Conditions ##

# mypassword = input("Please input your password")

# if len(mypassword) < 8:
#     print("Password is not long enough.")

# elif len(mypassword) > 24:
#     print("Password is too long.")

# else:
#     print("Great password.")

# income = int(input("Please input your income"))

# if income < 10000:
#     print("Tax is 0")
# elif income > 10000 and income < 15000:
#     tax = 0.05 * (income - 10000)
#     print("Your tax is " + str(tax))
#     # print(f"Your tax is {tax}")
# else:
#     tax = (income - 15000) * 0.1 + 5000 * 0.05 + 10000 * 0
#     print("Your tax is " + str(tax))

#     # 17542 2542 * 0.1  (17542 - 15000) (income - 15000) * 0.1 + 5000 * 0.05

## Loops ##

# mylist = [2,3,4,56,45,7]

# for number in mylist:
#     print(number + 2)
#     print(number * 2)

# # 4, 4, 5, 6, 6, 8, ....

# print("done")

# counter = 0
# while counter < 10:
#     print(f"the count is {counter}")
#     counter += 1

# for counter in range(20):
#     if counter % 2 == 0:
#         print(f"The counter is {counter} and it is even.")


# counter = 0
# while counter < 20:
#     if counter % 2 == 0:
#         print(f"The counter is {counter} and it is even.")
#     counter += 1

## Functions ##

# "going to the park."
# string = input("Enter your string: \n")
# counter = 0
# while string[counter] != '.':
#     counter += 1

# print(counter)

# def stringcounter(string: str):
#     counter = 0
#     while string[counter] != '.':
#         counter += 1

#     print(counter)

# st = input("Enter your string: \n")
# stringcounter(st)

## Functions without input ##

# def printimage():
#     t = """***     ***
#     ** ** **
#     """
#     print(t)

# printimage()
# printimage()
# printimage()

## Functions with return values/output ##

def sum(number1: int, number2: int):
    result = number1 + number2
    print(result)
    # return result

res = sum(45, 68)
print(res)

result2 = res + 9
result2 = sum(res,9)
print(result2)
