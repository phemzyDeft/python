# car game

# command = ""
#
# while command != "quit":
#     command = input("> ").lower()
#     if command == "start":
#         print('Car started....Ready to go!')
#         continue
#     elif command == "stop":
#         print("Car stop!")
#     elif command == "help":
#         print('''
# start - to start the car
# stop - to stop the car
# quit - to exit
#         ''')
#     elif command == "quit":
#         break
#     else:
#         print("i don't understand the statement!")


# incase you want to use conditional statement, that is using While True statement

# command = ""
#
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         print('Car started....Ready to go!')
#         continue
#     elif command == "stop":
#         print("Car stop!")
#     elif command == "help":
#         print('''
# start - to start the car
# stop - to stop the car
# quit - to exit
#         ''')
#     elif command == "quit":
#         break
#     else:
#         print("i don't understand the statement!")

# if the car is stop or started it should notify user.
command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car has already started!")
        else:
            started = True
            print('Car started....Ready to go!')
    elif command == "stop":
        if not started:
            print("the car has already stopped!")
        else:
            started = False
            print("Car stop!")
    elif command == "help":
        print('''
start - to start the car
stop - to stop the car
quit - to exit
        ''')
    elif command == "quit":
        break
    else:
        print("i don't understand the statement!")