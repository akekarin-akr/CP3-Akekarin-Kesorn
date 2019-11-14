def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput.lower() == "ake" and passwordInput.lower() == "zaza":
        return True
    else:
        return False
def showMenu():
    print("-----ishop-----")
    print("1. Vatcalculator")
    print("2. Prince Calculator")
def menuSelect():
    userSelect = int(input("menuSelect >> "))
    if userSelect == 1:
        return True
    elif userSelect == 2:
        return False
    return userSelect
def vatCalculate(totalprice):
    vat = 7
    result = totalprice * vat / 100
    return result
def priceCalculate():
    price1 = int(input("First product price : "))
    price2 = int(input("Second product price : "))
    return vatCalculate(price1 + price2) + (price1 + price2)

if login() == True:
    showMenu()
    if  menuSelect() == True:
        print("Only vat is", vatCalculate(float(input("Price of all Product : "))))
    else:
        print("Price and Vat is :", priceCalculate())
else:
    print("Error you are not member")





