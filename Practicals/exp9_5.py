from collections import Counter
d1 = {'a': 100, 'b': 20, 'c': 400, 'd': 10, 'e': 21}
k = Counter(d1)
n = k.most_common(3)
for i in n:
    print(i[0], " : ", i[1])