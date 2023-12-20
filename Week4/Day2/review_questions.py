# # 5: Exercise: Create a dictionary containing the following information about you: your name, 
# # your age, your gender, your favorite food. Be sure to use appropriate keys.
# myinfo = {"Name": "Jeremy", "Age": 30, "Gender": "Male", "Favorite Food": "Steak"}
# print(myinfo.values())

# # 11: Exercise: Write a loop that takes numbers from the user until it receives the number
# # 0 and prints the sum of the numbers received.

# sum = 0
# while True:

#     number = int(input("Enter a number: \n"))

#     sum = sum + number # sum += number

#     if number == 0:
#         break

# print(sum)

# Exercise: Define a function that takes three numbers and prints their average (mean).
# (4 + 9) / 2 = 6.5

def avg3(num1: float, num2: float, num3: float):
    print((num1 + num2 + num3) / 3)

avg3(4, 6, 20)