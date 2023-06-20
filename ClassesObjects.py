'''
    Class is a blue print for a real world entity. Object is an instance of that blueprint with own properties
'''

class Employee:
    def __init__(self): #Constructor. The self keyword(can be anyting other than self also) is important while creating a method inside a class
        print("Employee created")

e1 = Employee()


#Parameterized constructor and instance variables

class Employee:
    def __init__(self,id, name): #Constructor. The self keyword(can be anyting other than self also) is important while creating a method inside a class
        self.id = id #instance variable -> Varies for each object
        self.name = name #instance variable -> Varies for each object
        print(f"Hello {self.name} - EmpId : {self.id}") #Access the instance variables using self.


e1 = Employee(1, "Hari") #Prints Hello Hari - EmpId : 1
e2 = Employee(2, "John") #Prints Hello John - EmpId : 2


#Static variables

class Employee:
    salary = 15_000 #Static variable. Available as a common one to all objects
    def __init__(self,id, name): #Constructor. The self keyword(can be anyting other than self also) is important while creating a method inside a class
        self.id = id #instance variable -> Varies for each object
        self.name = name #instance variable -> Varies for each object
        print(f"Hello {self.name} - EmpId : {self.id}") #Access the instance variables using self.


e1 = Employee(1, "Hari") #Prints Hello Hari - EmpId : 1
e2 = Employee(2, "John") #Prints Hello John - EmpId : 2

print(e1.salary) #Though this is possible accessing this with object names is not good way, use Employee.salary instead
print(e2.salary)



#Instance methods
class Employee:
    salary = 15_000 #Static variable. Available as a common one to all objects
    def __init__(self,id, name): #Constructor. The self keyword(can be anyting other than self also) is important while creating a method inside a class
        self.id = id #instance variable -> Varies for each object
        self.name = name #instance variable -> Varies for each object

    def print_emp_information(self):  #This is an instance method 
        return(f"Hello {self.name} - EmpId : {self.id}") #Access the instance variables using self.
        


e1 = Employee(1, "Hari") #Prints Hello Hari - EmpId : 1
e2 = Employee(2, "John") #Prints Hello John - EmpId : 2

print(e1.print_emp_information()) 
print(e2.print_emp_information())


#ClassMethod
class Employee:
    salary = 15_000 #Static variable. Available as a common one to all objects
    def __init__(self,id, name): #Constructor. The self keyword(can be anyting other than self also) is important while creating a method inside a class
        self.id = id #instance variable -> Varies for each object
        self.name = name #instance variable -> Varies for each object

    def print_emp_information(self):  #This is an instance method 
        return(f"Hello {self.name} - EmpId : {self.id}") #Access the instance variables using self.
        
    @classmethod
    def print_salary_information(cls): #Class method has @classmethod decorator and cls as the first parameter, not self
        return cls.salary


e1 = Employee(1, "Hari") #Prints Hello Hari - EmpId : 1
e2 = Employee(2, "John") #Prints Hello John - EmpId : 2

print(e1.print_emp_information()) 
print(e2.print_emp_information())

print(e1.print_salary_information()) 
print(e2.print_salary_information())




#Inheritance


#Single inheritance

class A:
    a = 1
    def print_a_info(self):
        print("This is from A class")

class B(A): #Inherits A class
    b = 2
    def print_b_info(self):
        print("This is from B Class")

obj = B()
obj.print_a_info() #has access to the instance method of A class 
print(obj.a) #has access to the static variable of A class 
obj.print_b_info() #has access to the instance method of Bclass 
print(obj.b) #has access to the static variable of B class 

#Multilevel inheritance

class A:
    a = 1
    def print_a_info(self):
        print("This is from A class")

class B(A): #Inherits A class
    b = 2
    def print_b_info(self):
        print("This is from B Class")

class C(B): #Inherits B class, since B has access to A, C conventionally gets access to A
    c = 3
    def print_c_info(self):
        print("This is from C Class")

obj = C()
obj.print_a_info() #has access to the instance method of A class 
print(obj.a) #has access to the static variable of A class 
obj.print_b_info() #has access to the instance method of Bclass 
print(obj.b) #has access to the static variable of B class 
obj.print_c_info() #has access to the instance method of C class 
print(obj.c) #has access to the static variable of c class 



#Multiple inheritance -> Typically problematic in other languages, but not in python



class A: #This is standalone class
    def print_info(self): #Method name is common in all the classes.
        print("Hello this is from A class")
class B: # This is also standalone class

    def print_info(self):
        print("This is from B Class")

class C(A, B): #Inherits A class
    def print_info(self):
        print("This is from C Class")

obj = C()
obj.print_info() #What will be printed? => Prints C class's method

#what if, the following scenario?

class A: #This is standalone class
    def print_parent_info(self): #Method name is common in all the classes.
        print("Hello this is from A class")
class B: # This is also standalone class

    def print_parent_info(self):
        print("This is from B Class")

class C(A, B): #Inherits A class
    def print_c_info(self):
        print("This is from C Class")

obj = C()
obj.print_parent_info() #What will be printed? => Whichever class is inherited first gets printed. In our case C(A, B) , it is A's method.If we change that to C(B, A), then it will be B's



