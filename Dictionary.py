'''
    Dictionary in python has key-value structure. This is ordered mutable type of iterable
'''

my_dict = {"name" : "Hari Haran", "age": 25}

#or

my_dict = dict(name = "Hari Haran", age=25)

print(my_dict)
print(len(my_dict))

#accessing using keys
print(my_dict["name"])

#methods
print(my_dict.get("name", "No name is there")) #Gets the value of specified key, if the key is not in dictionary returns the default fallback value
print(my_dict.get("country", "No country is there")) #Gets the value of specified key, if the key is not in dictionary returns the default fallback value

print(my_dict.keys()) #Returns the list of keys
print(my_dict.values()) #Returns the list of values
print(my_dict.items()) #Returns the list of items 

my_dict.update({"name": "Hari Haran Elangovan"})
print(my_dict)

my_dict.pop("age") # Remove the specified key 
print(my_dict)

my_dict['role'] = 'Engineer' #Adds new key value
print(my_dict)

my_dict.popitem() #remove the last entered item
print(my_dict)

#looping 

emp_details = {
    "Name" : "Hari Haran",
    "DOJ" : "07/07/2022",
    "BusinessUnit": "MBU",
    "BaseLocation": "Chennai",
    "Office":"Chennai One SEZ"
}

for key in emp_details: #It will only get keys. Because if we use the dict directly in for loop, it takes only the keys list
    print(key)


for value in emp_details.values(): #As we know values() method will give the list of values so we can use this method to get the values
    print(value)


for key, value in emp_details.items(): #As we know items() method will give the list of keys and values so we can use this method to get both the keys and values and unpack them to assign key to key variable and value to value variable
    print(f"{key} - {value}")