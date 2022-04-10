
# i = 1
#
# while i <= 5:
#     print(i)
#     i +=1
# print('done')
# print("\n")
# x = 1
# while x <= 5:
#     print('*' * x)
#     x +=1
# print('done')


# how to build a guessing game with while loop
secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("enter guess: "))
    guess_count +=1
    if guess == secret_number:
        print("you win!")
        break
else:
    print("you loose!")




