
# nested loops basically means adding one loop inside another loop
for X in range(4):
    for Y in range(3):
        print(f"({X}, {Y})")

numbers = [5, 2, 5, 2, 2]
for X in numbers:
    # print('X' * X)
    for count in X:
        print(X)


