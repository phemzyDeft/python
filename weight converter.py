

weight = int(input("weight: "))
unit = input("(L)bs or (K)g: ")

if unit.upper() == "L": #using the .upper will convert what the user input to upercase
    converter = weight * 0.45
    print(f"you are {converter} kilos")
elif unit.upper() == "K":
    converter = weight / 0.45
    print(f"you are {converter} kilos")
else:
    print("there's an error in what you inputed")