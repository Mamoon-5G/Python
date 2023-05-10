n = int(input("Enter a number: "))
rev=0
sum=0
temp=n
while (n>0):
    rem = n%10
    rev = (rev*10) + rem
    n//=10
print(f"Reverse of {temp} is {rev}")
