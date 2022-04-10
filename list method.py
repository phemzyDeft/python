#
# numbers = [2, 5, 2, 7, 9, 10, 33, 3, 1]
#
# # to add a number at the end of the list
# # numbers.append(100)
# #
# # # to add a number at anywhere in the list irrespective of the index no.
# # numbers.insert(0, 3)
# #
# # # to remove an item in the list
# # numbers.remove(5)
#
# # to clear all items or number in the list
# # numbers.clear()
#
# # to delete the last item or number in a list
# numbers.pop()
#
# # to get the index of a number
# print(numbers.index(5))
#
# # this will check if 50 is in the list, but if it doesn't
# # it will surely return a boolean value
# print(50 in numbers)
#
# # To sort an items in an ascending order
# numbers.sort()
#
# # TO sort an item in a descending order or reverse the item
# numbers.reverse()
# print(numbers)
#
# num = [2, 4, 1, 5, 3, 2, 2, 1, 10]
#
# # To count the amount of item in a list
# print(num.count(2))
#
# # to copy all the items in the list
# num2 = num.copy()
# num3 = num.append(34)
# print(num2)


# write a program to remove a duplicate in a list
numbers = [2, 2, 3, 11, 5, 0, 11, 4, 5, 9, 10]
number2 = []

for number in numbers:
    if number not in number2:
        number2.append(number)
print(number2)