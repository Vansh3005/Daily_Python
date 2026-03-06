# Print the total of the list
list = [1,2,2,3,4,5,5,6,7]
print("sum of the list is:",sum(list))

# Remove duplicacy in list
result = []
for i in list:
    if i not in result:
        result.append(i)
print("List without duplicacy",result) 

# Count frequency of each element
for i in list:
   count = 0
   for j in list:
        if i==j:
            count += 1
   print(i," : ",count)

# Merge Two Lists
list1 = ['A','B','C','D']
list2 = [1,2,3,4]
merged = list1 + list2
print("Merged List:",merged)
        
# Rotate List Left by 1
list2 = [1,2,3,4]
start = list2[0]
for i in range(len(list2)-1):
    list2[i] = list2[i+1]
list2[-1]=start
print("Left Rotate list:",list2)
  