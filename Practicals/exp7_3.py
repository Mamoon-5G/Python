tup = ("zero","one","two","three","four","five","six","seven","eight","nine")
n = int(input("Enter a number: "))
temp = ' '
while n:
    rem = int(n%10)
    for i in range(0,len(tup)):
        if rem==i:
            temp = tup[i]+" "+temp
            break
    n = int(n/10)
print(temp)