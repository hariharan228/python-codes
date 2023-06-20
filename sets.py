'''
    Set is another iterable type. This is unordered unlike tuples and list, also doesnot allow duplicate values and unindexed. 
'''

sample_set = { 1, 2, 3 }
#or
sample_set = set([1,2,3])

print(sample_set)

#methods
sample_set.add(4) # adds new element to the set
print(sample_set)

sample_set_2 = { 4, 5, 6}
print(sample_set.difference(sample_set_2)) # Returns the elements of caller set which are not present in the argument set

sample_set.remove(2)
print(sample_set)

sample_set_3 = sample_set.union(sample_set_2) #Joins two sets
print(sample_set_3)

sample_set_2.pop() #=>Removes the first element
print(sample_set_2)


super_set = {1,2,3,4,5}
sub_set = {3,4}

print(super_set.issuperset(sub_set)) #Returns true if the argument is super of the caller set
print(sub_set.issubset(super_set)) #Returns true if the argument is subset of the caller set
