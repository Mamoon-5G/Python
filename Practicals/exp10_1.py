s = input("Enter a string\n")
low = 0
up = 0
for i in range (0,len(s)):
    if s[i] > 'A' and s[i] < 'Z':
        up = up + 1
    elif s[i] > 'a' and s[i] < 'z':
        low = low + 1
print(f"\nUpper Case Characters {up}")
print(f"Lower Case Characters {low}")
