a = 0
b = 1
n = int(input("Enter a number: "))
print(a, end=' ')
print(b, end=' ')
for i in range (0,n):
    temp = a
    a = b
    b = temp + a
    print(b, end=' ')