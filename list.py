

peoples = ['oluwafemi', 'david', 'isreal', 'yolu']
print(peoples[2])
print(peoples[2:4])
print(peoples[:])


# to replace a nmae in the list item
names = ['zacchaeus', 'david', 'lekan', 'yolu']
names[0] = 'phemzy'
print(names)

# write a program to find a largest number in the list
lists = [2, 4, 6, 7, 9, 10, 20]
max = lists[0]

for list in lists:
    if list > max:
        max = list
print(max)

# for name in names:
#     print(name)