d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

merged_dict = {**d1, **d2}
for key in d1.keys() & d2.keys():
    merged_dict[key] = d1[key] + d2[key]
print(merged_dict)
