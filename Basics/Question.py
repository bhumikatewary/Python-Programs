# Finding Largest Number in a List

numbers=[5,2,1,6,4]
max = numbers[0]
for i in numbers:
    if(i>max):
        max = i

print (max)

# Remove Duplicates from the List

numbers=[2,2,4,5,7,8,4,3]
unique=[]
for i in numbers:
    if i not in unique:
        unique.append(i)
        
print(unique)
