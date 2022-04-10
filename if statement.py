
# if statement allows to build program that can make decision based on some coditions

is_cold = True
is_hot = False

if is_cold:
    print("it's a cold day")
    print("wear warm cloth")
elif is_hot:
    print("it's hot day drink")
    print("drink plenty of water")
else:
    print("it's a lovely day")
print("enjoy your day")



# '''
# Price of a house is $1M
# if buyer has good credit,
#     they need to put down 10%
# otherwise
#     they need to put down 20%
# print the down payment
# '''

house_price = 1000000
buyer_credit = True

if buyer_credit:
    down_payment = 0.1 * house_price #or 10/100 * house_price
else:
    down_payment = 0.2 * house_price #or 20/100 * house_price
print(f"the downpayment is ${down_payment}")

