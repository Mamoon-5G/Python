a = int(input("Enter marks of Advanced Java : "))
b = int(input("Enter marks of Operating System : "))
c = int(input("Enter marks of Environmental Studies : "))
d = int(input("Enter marks of Software Testing : "))
e = int(input("Enter marks of Client Side Scripting : "))
avg = (a + b + c + d + e)/5
print("Average Marks is ",avg)
if (avg >= 90):
    print("A Grade")
elif (avg >= 75):
    print("B Grade")
elif (avg >= 60):
    print("C Grade")
elif (avg >= 35):
    print("D Grade")
else:
    print("Fail")