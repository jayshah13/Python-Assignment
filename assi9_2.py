import numpy as np

list = []

n = int(input("Enter number of elements in the list : "))

for i in range(0, n):
   elm = int(input())
   list.append(elm) 
print("The entered list is: \n",list)

print(np.min(list))
print(np.max(list))
print(np.average(list))
print(np.var(list))
print(np.std(list))
