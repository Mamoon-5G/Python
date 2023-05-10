#import math
l1=[]
#lar = 0
n = int(input("Enter list elements: "))
for i in range (n):
    l1.append(int(input()))
lar = l1[0]
for i in range(0,n):
    if (lar < l1[i]):
        lar = l1[i]
print(f"Largest is {lar}")
