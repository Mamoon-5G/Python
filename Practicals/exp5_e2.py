n = int(input("Enter a number: "))
sum = 0
temp = n
while (temp>0):
    digit = temp%10
    sum = sum +(digit**3)
    temp = temp//10
if(n==sum):
    print(f"{n} is an armstrong number")
else:
    print(f"{n} is not an armstrong number")
