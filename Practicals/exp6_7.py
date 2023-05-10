l1 = []
n = int(input("Enter number of elements\n"))
for i in range (n):
    l1.append(int(input()))
for i in l1:
    if i%2==0:
        print("Even Elements: ",i,end=' ')