
# try except keep our code out of errors
try:
    age = int(input('age: '))
    income = 2000
    risk = income / age
    print(age)

except ValueError:
    print("not an int, number only!")

except ZeroDivisionError:
    print("age cannot be zero (0)")