#Strings are sequence of characters. String is immutable type

input_str = input("Enter the string:\n ")
print(type(input_str))
print(dir(input_str)) #=> Returns the available methods of the type
print(len(input_str))


# methods in string

print(input_str.capitalize()) #=>Capitalizes the first letter of the string
print(input_str.count('haran')) #=> Returns the count of the substring in the calling string
print(input_str.find('haran')) #=> Returns the starting index of the substring in the calling string (With 0 as the base index) else returns -1
print(input_str.lower()) #=> Returns the lower case version of the string
print(input_str.upper()) #=>Returns the upper case version of the string
print(input_str.index('r')) #=> Returns the first occuring index of the substring in the calling string, else throws ValueError 
print(input_str.strip()) #=> Returns the string without leading and trailing spaces
print(input_str.rstrip()) #=> Returns the string without trailing spaces
print(input_str.lstrip()) #=> Returns the string without leading spaces
print(input_str.swapcase()) #=> Returns the case swappedstring 
print(input_str.title()) #=> Returns the space separated string with each word's first character capitalized
print(input_str.replace('hari','haran')) #=> Replaces the first mentioned string in the calling string using the target string which is mentioned second => hariharan.replace('hari','haran') => haranharan 
print(input_str.split()) #=> Splits the calling string with the mentioned separator and returns a list as the result
print(','.join(input_str.split())) #=> Called upon a joiner, this method takes an iterable and joins them using that connector and returns the string=> ','.join(['hari','haran']) => hari,haran

# Boolean methods
print(input_str.endswith('an')) #=> Returns True if the calling string endswith the mentioned substring else False
print('a'.isalnum())    #=> Returns true if the character is alphanumeric (a-z,A-Z,0-9) else false
print('1'.isalnum())    #=> Returns true if the character is alphanumeric (a-z,A-Z,0-9) else false
print('@'.isalnum())    #=> Returns true if the character is alphanumeric (a-z,A-Z,0-9) else false
print('HARI'.isupper()) #=> Returns True if the string is uppercase
print('hari'.islower()) #=> Returns True if the string is lowercase
print('1'.isdigit()) #=> Returns true if the given string is digit
print('1'.isdecimal()) #=> Returns true if the given string is decimal

# #dunder methods

print('hari'.__add__(' haran')) #=> Returns the concatenated string same as str1+str2 => here str1 is the caller so it is self 
print('hari'.__contains__('zari')) #=> Returns True if the self contains the substring else false
print('hari'.__eq__('Hari')) #=> Returns True if the self string is equal to the parameter. It does the ascii value comparison
print('hari'.__lt__('Hari')) #=> Returns True if the self string is lesser than the parameter. It does the ascii value comparison
print('hari'.__gt__('Hari')) #=> Returns True if the self string is greater than the parameter. It does the ascii value comparison
print('hari'.__ge__('Hari')) #=> Returns True if the self string is greater than or equal to the parameter. It does the ascii value comparison
print('hari'.__le__('Hari')) #=> Returns True if the self string is lesser than or equal to the parameter. It does the ascii value comparison
print('hari'.__ne__('hari')) #=>Returns True if the self is not equal to the parameter


#String formatting

name = 'Hari Haran'
age = 25
style_1 = 'Hi I am {}. I\'m {}'.format(name, age)
style_2 = 'I\'m {1} and my name is {0}'.format(name, age)
style_3 = f'Hi I am {name} and I\'m {age}'

print(style_1)
print(style_2)
print(style_3)

# Multi line string

sample_multi_line = '''
    Hi I am Hari Haran.
    I am 25 years old
'''

print(sample_multi_line)


# To concatenate any other type to a string remember to convert that first

age = 25
name = 'Hari haran'

# print('Hi I am '+ name +'. I\'m ' + age) #=> Throws type error
print('Hi I am '+ name +'. I\'m ' + str(age)) #After converting it works
