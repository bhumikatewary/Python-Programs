import random

for i in range(3):
    print(random.random())  
    
# here random in line 1 is a module that we are importing 
# the second random is a function to generate random numbers


import random

for i in range(3):
    print(random.randint(10,20))
    
# for specific numbers



import random

members=["sam", "bob", "joe"]
for i in members:
    leader=random.choice(members)
    
print(leader)
