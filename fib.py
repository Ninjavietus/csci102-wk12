#John Robert
#CSCI 102 - Section E
#Workshop Week 2

num_1 = 0
num_2 = 1
print(num_2)
for i in range(2, 100):
    num_3 = num_1 + num_2
    num_1 = num_2
    num_2 = num_3
    print(num_3)
    
