inputNumber = int(input("Number : "))
countSpace = int((inputNumber - 1) / 2)
for i in range(1, inputNumber+2, 2):
    print(" " * countSpace, ("*" * i))
    countSpace -= 1
