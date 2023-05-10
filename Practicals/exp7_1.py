tup = tuple()
n = int(input("Enter no. of elements: "))
for i in range(n):
    a = int(input(f"Enter element {i+1}: "))
    tup = tup + (a,)
min = tup[0]
max = tup[0]
for i in range(n):
    if min > tup[i]:
        min = tup[i]
for i in range(n):
    if max < tup[i]:
        max = tup[i]
print(f"Tuple {tup}")
print(f"Minimum: {min}")
print(f"Maximum: {max}")