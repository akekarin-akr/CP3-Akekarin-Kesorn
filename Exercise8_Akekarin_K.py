username = input("Username : ") #ake
password = input("Password : ") #zaza
water = 10
candy = 5
showerCream = 38
if username.lower() == "ake" and password.lower() == "zaza":
    print("----------Welcome-to-AKE-shop----------")
    print("----------List-of-products-------------")
    print("1.water               ", water, " THB")
    print("2.candy                ", candy, " THB")
    print("3.Shower Cream        ", showerCream, " THB")
    user_input = int(input("select order : "))
    if user_input == 1:
        Enter_the_amount_of_the_product = int(input("How much : "))
        print("Total water price is :", Enter_the_amount_of_the_product * water, "THB")
    elif user_input == 2:
        Enter_the_amount_of_the_product = int(input("How much : "))
        print("Total candy price is :", Enter_the_amount_of_the_product * candy, "THB")
    elif user_input == 3:
        Enter_the_amount_of_the_product = int(input("How much : "))
        print("Total shower cream price is :", Enter_the_amount_of_the_product * showerCream, "THB")
    else:
        print("Error")
else:
    print("You are not member of AKE shop!!!")






