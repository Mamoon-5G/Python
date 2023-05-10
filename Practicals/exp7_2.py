tup = tuple()
n = int(input("Enter no. of elements: "))
for i in range(n):
    a = int(input(f"Enter element {i+1}: "))
    tup = tup + (a,)

print(f"Repeated Element(s): ", end="")
for i in range(0, len(tup)):
    for j in range(i+1, len(tup)):
            if tup[i]==tup[j]:
                print(f"{tup[j]}", end=" ")