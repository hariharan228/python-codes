#If, If .. else, elif
a = 2

if a % 2 == 0:
    print(f"{a} is even number")

if a % 2 == 0:
    print(f"{a} is even number")
else:
    print(f"{a} is odd number")

val = 0
if a > 0:
    print(f"{val} is positive number")
elif a < 0: 
    print(f"{val} is negative number")
else:
    print(f"{val} is zero")

#### If in iterables

l1 = [1,2,3,4]

if 1 in l1:
    print('1 is in the list')
else:
    print('1 is not in the list')




### Loops

#For loop

n = 10

for i in range(n):
    print(i+1)

#While loop

while i > 0:
    print(i)
    i -= 1