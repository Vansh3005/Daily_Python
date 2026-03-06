# Print the total of the list
list = [1,2,2,3,4,5,5,6,7]
print("sum of the list is:",sum(list))

# Remove duplicacy in list
result = []
for i in list:
    if i not in result:
        result.append(i)
print("List without duplicacy",result) 