
# formatted strings add a prefix to a strings and
# add a curlybrase to dynamically insert values to the strings


first = 'Femi'
last = 'David'
# not a formatted strings
message = first + ' [' + last + '] is a programmer'

# formatted strings
msg = f"{first} [{last}] is a programmer"
print(msg)