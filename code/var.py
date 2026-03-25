i = 5
print(i)
i = i + 1
print(i)

s = '''This is a multi-line string.
This is the second line.'''
print(s)

print("=====================")

attributes = ['name', 'dob', 'gender']
values = [['jason', '2000-01-01', 'male'],
          ['mike', '1999-01-01', 'male'],
          ['nancy', '2001-02-01', 'female']
          ]

# 实现了功能了，可能不够 pythonic
data_list = []
for valueList in values:
    data = {}
    for i in range(0, len(attributes)):
        data[attributes[i]] = valueList[i]
    data_list.append(data)
print(data_list)

# expected output:
# [{'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'},
#  {'name': 'mike', 'dob': '1999-01-01', 'gender': 'male'},
#  {'name': 'nancy', 'dob': '2001-02-01', 'gender': 'female'}]

d = {'mike': 10, 'lucy': 2, 'ben': 30}

# 按值来升序排序，返回的是二元元组列表
sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
print(sorted_d)

sorted_d = sorted(d.items(), key=lambda x: x[1])
print(sorted_d)