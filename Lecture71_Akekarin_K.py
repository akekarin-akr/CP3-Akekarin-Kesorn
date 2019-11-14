menuList = []
PriceList = []
def showBill():
    print("----My-Food----")
    for number in range(len(menuList)):
        print(menuList[number], ":", PriceList[number], "THB")
def totalPrice():
    total = 0
    for num in range(len(menuList)):
        total += PriceList[num]
    print("Total Price is %.1f THB" % (total))

while True:
    menuName = input("Please Enter Menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = float(input("Price : "))
        menuList.append(menuName)
        PriceList.append(menuPrice)
showBill()
totalPrice()




