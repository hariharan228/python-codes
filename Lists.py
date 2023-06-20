# # '''List in python is an instance of Iterable.
# #     It is a collection of same or different type of objects which
# #     can be stored in contiguous block of memory.
# #     These are mutable data structure
# # '''


# sample_list = [1,2,3,4,'5',[6,7,8],True,9.0]

# print(sample_list)
# print(len(sample_list))

# input_list = list(map(int, input().split()))
# print(input_list)
# # 1. Reads the input string using input()
# # 2. Splits that using comma as separator with split()
# # 3. maps each string value to int type 
# # 4. Finally converting the map object to list to get the list as output

# # Eg:
# '''
#  inputs: 10 11 12 13
#  input_list will be [10,11,12,13]
# '''

# #Accessing and slicing using the indexes

# print(sample_list[1]) #=> Prints the second element
# print(sample_list[0:4]) #=> Prints the elements at 0,1,2,3 indices only not upto 4
# print(sample_list[-1]) #=> Prints last element (-1 means last index. From the beginning index starts at 0 and last starts at -1)
# print(sample_list[-4:-1]) #=> Prints the last 3 elements excluding last element (-1)
# print(sample_list[-1:-4]) #=> Empty list is printed. Because by default the increment happens. To do the decrement we have to pass it explicitly
# print(sample_list[-1:-4:-1]) #=> Now we are decrementing so it works. The application of this method is really helpful in reversing the list
# print(sample_list[4:]) #=>Prints the entire list from the index 4
# print(sample_list[-3::-1]) #=> Prints the entire list from 3 element in the last to the beginning
# print(sample_list[:4]) #=> Same as [0:4]


# #Methods

# print(sample_list.append(10)) #=>Appends the value in the end. It does this in-place so it wont return the list. 
# print(sample_list) #=>Now you can see the modified list here

# sample_list.insert(0,'0')#=>Inserts '0' at the index 0 and shifts the other elements one place ahead
# print(sample_list)

# #If we use append method to add a new list to the existing list, it will be added as a single element.

# sample_list_2 = [11,12,13] #To add a the elements of this list to sample_list, use extend
# sample_list.extend(sample_list_2)
# print(sample_list)

# sample_list.remove('0') #=>Remove the value from the list
# print(sample_list)

# print(sample_list.pop()) #=> Returns the removed value. Typically the last value
# print(sample_list)

# sample_list.reverse() #=> In place reverse method
# print(sample_list)

# print(sample_list.index(12)) #=> Returns the index of the value

# print(sample_list.count(2)) #=> Returns the count of the value in the list

# copied_sample_list = sample_list.copy()
# print(copied_sample_list)


# nums = [3,4,2,5,1]
# nums.sort() #=> In place sort method
# print(nums)

# nums.sort(reverse=True) #=> Descending order sort
# print(nums)

# print(sorted(nums)) #=> Returns the sorted list

# print(min(nums)) #=> Returns the minimum value
# print(max(nums)) #=> Returns the maximum value
# print(sum(nums)) #=> Returns the Sum of all the values


# #Looping the list

# for num in nums:
#     print(num) #Prints the value in separate lines. Because by default the end key word argument has '\n'. We can change it explicitly

# for num in nums:
#     print(num,end=" ") #Prints the value in one single line with space in between every num.


# List is reference type

# list1 = [1,2,3]
# list2 = list1
# print(list1) 
# print(list2)

# list2[0] = 10
# print(list1)
# print(list2)

# print(list1 == list2)
# print(list1 is list2)

# l = [1,2,3]
# li = l

import time as t
print(dir(t))
print(t.localtime())

for i in range(10):
    t.sleep(1)
    print(t.localtime()[5])
