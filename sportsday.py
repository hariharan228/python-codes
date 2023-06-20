cost_dict = { k:v for (k,v) in zip(['h','c','a'], list(map(int,input().split())))} 
max_area_dict = { k:v for (k,v) in zip(['h','c','a'], list(map(int,input().split())))} 

m_n = []
for i in range(3):
    m_n.append(list(map(int, input().split())))

m_n_dict = { k:v for (k,v) in zip(['h','c','a'], m_n)} 
total_area = int(input())
min_cost_category = sorted(cost_dict.items(), key=lambda x:x[1])[0][0]
max_cost_category = sorted(cost_dict.items(), key=lambda x:x[1])[2][0]
# print(max_cost_category)
thc = 0
tcc = 0
tac = 0
if min_cost_category == 'h':
    thc = cost_dict['h'] * max_area_dict['h']
    total_area -= max_area_dict['h']
elif min_cost_category == 'a':
    tac = cost_dict['a'] * max_area_dict['a']
    total_area -= max_area_dict['a']
elif min_cost_category == 'c':
    tcc = cost_dict['c'] * max_area_dict['c']
    total_area -= max_area_dict['c']
# print(f"{cost_dict['h']} * {m_n_dict['h'][0]} * {m_n_dict['h'][1]}")
# print(max_cost_category)
if max_cost_category == 'h':
    thc = cost_dict['h'] * m_n_dict['h'][0] * m_n_dict['h'][1]  
    total_area -= m_n_dict['h'][0] * m_n_dict['h'][1]  
    # print(total_area)
elif max_cost_category == 'a':
    tac = cost_dict['a'] * m_n_dict['a'][0] * m_n_dict['a'][1] 
    total_area -= m_n_dict['a'][0] * m_n_dict['a'][1]  
    # print(total_area)
elif max_cost_category == 'c':
    tcc = cost_dict['c'] * m_n_dict['c'][0] * m_n_dict['c'][1] 
    total_area -= m_n_dict['c'][0] * m_n_dict['c'][1]  
    # print(total_area)
if tac == 0 and tcc > 0 and thc > 0:
    tac = cost_dict['a'] * total_area
elif tcc == 0 and tac > 0 and thc > 0:
    tcc = cost_dict['c'] * total_area
elif thc == 0 and tac > 0 and tcc > 0:
    thc = cost_dict['h'] * total_area
   
print(thc + tcc + tac)
# print(thc , tcc , tac)
