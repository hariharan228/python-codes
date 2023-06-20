import math
l = list(map(int, input().split()))
n = int(input())
res = abs(l[n-1] - l[n-2]) + abs(l[n] - l[n-1])
print(res)