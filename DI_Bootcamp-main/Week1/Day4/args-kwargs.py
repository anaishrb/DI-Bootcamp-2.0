def print_names(*sababa):
    for i in sababa:
        print(i)


# args = *
print_names('David')

#kwargs = **

def print_info(**kwargs):
    print(kwargs)


print_info(address = (5,7), score = [25, 47, 899])


def gamer_info(*args, **kwargs):
    print(max(args))
    print(kwargs)

gamer_info(150, 123, 544, 534, name = 'John', l_name = "Doe", age = 23)