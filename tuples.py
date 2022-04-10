
# Tuples is like a list, it's used to store multiple items
# but it cannot be immutable or reassign

numbers = (1, 2, 3, 4, 5)

# it cannot be reassign
# Tuples[0] = 10

print(numbers[0])
print(numbers)

# Unpacking
# it works for both in a list and tuples

coordinate = (1, 3, 5)
x, y, z = coordinate
print(y)

coordinate_list = [1, 3, 5]
x, y, z = coordinate_list
print(z)