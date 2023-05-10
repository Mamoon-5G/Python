a = int(input("Enter first Number : "))
b = int(input("Enter second Number : "))
c = int(input("Enter third Number : "))
if (a > b and a > c):
    print("Greatest Number is ",a)
elif (b > a and b > c):
    print("Greatest Number is ",b)
else:
    print("Greatest Number is ",c)