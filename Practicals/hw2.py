n = int(input("Enter no of rows : "))
print("(20461) Siddiqui Mamoon")
for i in range(1,n+1):
    for j in range(1, n+1-i):
        print(' ', end=' ')
    for j in range(1,i+1):
        print(j, end=' ')
    for j in range(i-1,0,-1):
        print(j, end=' ')
    print()