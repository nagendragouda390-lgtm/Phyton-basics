nums =[1,4,2,4,6,4,5]
unique = []
low_k = []
k = 5
for n in nums:
    if n not in unique:
        unique.append(n)
print (unique )
for u in unique:
    inserted = False
    for i in range(len(low_k)):
        if u < low_k[i]:
            low_k.insert(i,u)
            inserted = True
            break 
    if not inserted:
        low_k.append(u)
    
    if len(low_k)> k:
        low_k.pop()
print (low_k)
if len(low_k) < k:
       print (f' No {k}th lowest')
else:
       print(f' {k}th lowest is',low_k[k-1])
       
        