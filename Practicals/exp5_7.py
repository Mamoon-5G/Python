n = int(input("Enter a number: "))
sum = 0
temp = n
while (n>0):
    rem = n%10
    sum = sum + rem
    n//=10
print(f"Sum of {temp} is {sum}")
