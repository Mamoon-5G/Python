a = {10, 20, 30, 40, 50}
b = {100, 20, 30, 70, 60}
print("Common Elements in A and B : ", a & b)
print("Union Elements in A and B : ", a | b)
print("Element present in a and not in b : ", a - b)
print("Element present in b and not in a : ", b - a)
print("Symmetric Difference : ", a ^ b)
a.clear()
print(a)