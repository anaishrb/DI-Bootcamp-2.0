def calculation(num1:int, num2:int)-> tuple:
    add = num1 + num2
    sub = num1 - num2

    return add,sub


a,b= calculation(8, 4)
print(a, b)