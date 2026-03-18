name = "jack"
age = 188
format_string = "my name is {}, age is {}"
print(format_string.format(name, age))
print(format_string.format("mike", 19))


number = 1.33
print("{:.3f}".format(number))
print("{:-^20}".format(name))

print(r"Newlines are indicated by \n")