

print("---Welcome to Mark Coffee---")
print(" ")
num1 = int(input("Plrase type 1 to show menu : "))
print(" ")

if num1 == 1 :
    menu = ["Espresso", "Cappuccio", "Latte"]
    print("""---Choose the menu---
1. Espresso
2. Cappuccino
3. Latte""")
    print(" ")

    num2 = int(input("Select coffee : "))
    print(" ")
    if num2 in [1, 2, 3]:
        print(""" ---Choose the type of the coffee---
1. Hot 55 baht
2. Cold 60 baht """)
        print(" ")
        print(" ")
        type = int(input("Select type: "))
        if type == 1:
            print("---You chose Hot %s 55 baht---"% menu[num2-1])
            print(" ")
            money = int(input("Input your money: "))
            if money >= 55:
                Tangthon = money - 55
                print("You recieved a change of %d baht" %Tangthon)
                print("---Thanks you---")   
            else:
                print("Not enough money")
                print("---Please try again---")
        elif type == 2:
            print("---You chose Cold %s 60 baht---"% menu[num2-1])
            print(" ")
            money = int(input("Input your money: "))
            if money >= 60:
                Tangthon = money - 60
                print("You recieved a change of %d baht" %Tangthon)
                print("---Thanks you---")
            else:
                print("Not enough money")
                print("---Please try again---")
else:
    print("Sorry, something went wrong")

