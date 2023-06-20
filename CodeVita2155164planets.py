mn = list(map(int, input().split()))
m = mn[0]
n = mn[1]

paths = []

di = {}

for _ in range(m):
    path = list(map(int, input().split()))
    if path[0] in di.keys():
        di[path[0]].append(path[1])
    else:
       di[path[0]] = [path[1]]

print(di)  
res = []
for i in di.keys():
  if len(di[i]) == 1 and i not in res and di[i][0] not in res:
    res.append(i)
    res.append(di[i][0])
    
if len(res) == 0:
  print(-1)
else:
  for i in res:
    print(i)
    
  
  
