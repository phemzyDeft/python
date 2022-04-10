
# A dictionary is a structure that allows us to map a key to a value
customers = {
    'name': 'oluwafemi david',
    'age': 20,
    'is_verified': True
}

print(customers['name'])

# To reassign another item to the key in the dictionary
customers['name'] = 'segun isreal'
print(customers['name'])

# To add another item that is not in the dictionary
customers['DOB'] = 'sep 4 2002'
print(customers["DOB"])

# using a get method
# None is an object that represent the absent of a value
print(customers.get('family_name', 'Adesanya'))


phone = input('Phone: ')
out_put = ''
phone_dictionary ={
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four'
}

for char in phone:
    out_put+= phone_dictionary.get(char, '!') + ' '
print(out_put)