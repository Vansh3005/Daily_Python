# Take 5 numbers as input and store in list
values = []
for i in range(5):
    num = int(input("Enter the number"))
    values.append(num)
print("List is:", values)

# Find sum and average of list
print("Total of the list is:",sum(values))
avg = sum(values)/2
print("Avg of list is:",avg)

# Find maximum and minimum element
print("Max value in list:",max(values))
print("Min value in list:",min(values))

# Reverse list without using reverse()
print("The reverse of list is:",values[::-1])
     
# Check if Number Exists in List
check = int(input("Check no. is present in list or not:"))
if check in values:
    print("Number is exists")
else:
    print("Number is not exists")