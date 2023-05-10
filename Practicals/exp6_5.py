l1=[]
n = int(input("Enter list elements: "))
for i in range (n):
    l1.append(int(input()))
print(l1)
l1.reverse()
print(f"The reverse is {l1}")