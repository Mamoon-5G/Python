import collections
dic = {100: 1, 90: 4, 80: 6, 101: 5, 99: 3}
sort = collections.OrderedDict(sorted(dic.items()))
print(sort)
