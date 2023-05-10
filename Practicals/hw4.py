print("(20461) Siddiqui Mamoon")
k=4
count=1
for i in range(0,4):
    for j in range(0,k):
        print(end=" ")
    k = k - 1
    for j in range(0, i+1):
        print(count, end=" ")
        count=count+1
    print("\r")