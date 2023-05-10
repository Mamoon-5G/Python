import math
l1=[]
n = int(input("Enter list elements: "))
for i in range (n):
    l1.append(int(input()))
sm = l1[0]
for i in range(0,n):
    if (sm > l1[i]):
        sm = l1[i]
print(f"Smallest is {sm}")
print(f"Smallest is {min(l1)}")
