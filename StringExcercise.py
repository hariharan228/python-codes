string = "James"

print(string[0], string[len(string)//2], string[len(string)-1], sep="")


s1 = "Ault"
s2 = "Kelly"

s3 = s1[0: len(s1)//2] + s2 + s1[len(s1)//2:]
print(s3)

s1 ='/*Jon is @developer & musician!!'
s2 = ''

for i in s1:
    if not(i.isalnum()) and i != " ":
        s2+='#'
    else:
        s2+=i

print(s2)