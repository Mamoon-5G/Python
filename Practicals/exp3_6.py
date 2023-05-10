r = int(input("Enter radius of Cylinder: "))
h = int(input("Enter height of Cylinder: "))
vol = 3.14 * r * r * h
sa = (2 * 3.14 * r * (r + h))
print(f"Volume of Cylinder with radius {r} and height {h} is {vol}")
print(f"Surface Area of Cylinder with radius {r} and height {h} is {sa}")