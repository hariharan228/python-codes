l = list(map(int, input().split()))
s1 = 0
s2 = 0

for i in range(len(l)):
    if i % 2 == 0:
        s1 += l[i]
    else:
        s2 += l[i]

if s1 > s2:
    print(s1 - s2)
else:
    print(s2 - s1)

