import random

for i in range(3):
    print(random.random())

for i in range(3):
    print(random.randint(10, 20))

members = ['femi', 'isreal', 'segun', 'yolu']
leader = random.choice(members)
print(leader)