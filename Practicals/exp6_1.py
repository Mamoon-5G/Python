l1=[]
n = int(input("Enter list elements: "))
sum = 0
for i in range (n):
    l1.append(int(input()))
    sum = sum+l1[i]
print(f"Sum of items in the list {sum}")
