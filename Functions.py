#simple function

def welcome_1():
    print("Hello")

#or Return the string

def welcome_2():
    return "Hello"

#Now welcome_1 does print the value so calling that without print is advisable like following
welcome_1()
# welcome_2 doesnot print the value and returns something so calling that with print is advisable like following
print(welcome_2())


#Parameterised function

def add(a, b):
    return a + b

print(add(1,2))
print(add(1.34,2.22))

#In the above function we have only two parameters, if the parameter count is unknown and we want to add n number of values, then we can use *args

def dynamic_add(*args):
    list1 = args
    return sum(list1)

print(dynamic_add(1,2,3,4))
print(dynamic_add(1,2,3,4,5,6,7))
print(dynamic_add(1,2,3,4,5,6,7,8,9,10))


#Key word arguments:

def print_name(firstname, lastname):
    return firstname + " " + lastname

print(print_name(firstname="hari",lastname="haran"))
#The purpose of doing this is we can change the order we pass the arguments

print(print_name(lastname="haran", firstname="hari")) #The output will be same as before

#Now if we want to pass n number of key word arguments, then we can use **kwargs
def print_details(**kwargs):
    for key, values in kwargs.items():
        print(f"{key} - {values}")

print_details(firstname="hari", lastname="hari",age="25")

#Remember *args is a list structure and **kwargs is a dict structure. We can use different names other than args and kwargs. but * and ** are important

#Default parameters:

def welcome(name="Person"):
    print(f"Hello {name}")

welcome()
welcome("Hari Haran")




#Lambda function
#Lambda is a small anonymous function, it can take any number of arguments, but can have only one expression

add_lambda = lambda a,b : a + b
#The above statement is similar to def add(a, b): return a + b
print(add_lambda(1,2))
