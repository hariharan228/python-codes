'''
    Tuple in python is an instance of Iterable.
    It is a collection of same or different type of objects which
    can be stored in contiguous block of memory.
    These are immutable data structure
'''

sample_tuple = (1,2,3,'4',True)

print(sample_tuple)
input_tuple = list(map(int, input().split()))
print(input_tuple)

#Accessing using index (Same priciple as the list)
print(sample_tuple[0])
print(sample_tuple[0:3])


#methods
print(input_tuple.count(1)) 
print(input_tuple.index(5))