l1=[]
n = int(input("Enter list elements: "))
mul = 1
for i in range (n):
    l1.append(int(input()))
    mul = mul*l1[i]
print(f"Multiplication of items in the list {mul}")