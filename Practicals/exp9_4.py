SampleData = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
              {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
u = set(val for dict in SampleData for val in dict.values())
print(u)
