nums = [1,0,0,1,1,0,1,1]
#1

unique= []
highest= float('-inf')
second_highest = float('-inf')
for n in nums :
    if n == 0:
        nums.remove(0) 
        nums.insert(len(nums),n)                     
    if n not in unique:
        unique.append(n)
        for u in unique:
            if u > highest:
                second_highest = highest
                highest = u
            elif u > second_highest:
                second_highest = u
if second_highest == float('-inf'):
    second_highest = 'No second highest'
if highest == float('-inf'):
    highest = 'No highest'
               

print (highest) 
print (second_highest) 
print(nums)            
                