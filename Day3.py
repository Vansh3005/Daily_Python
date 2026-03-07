# Find all pairs whose sum = target
list = [1,2,3,4,5,6]
target = 5
for i in range(len(list)):
    for j in range(i+1,len(list)): # (i+1) avoid the duplicacy and comparison with itself
        if list[i] + list[j] == target:
            print(list[i], list[j])


