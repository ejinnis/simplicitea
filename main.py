name = 'Mr. Potter'
email = 'apotter@wsd1.org'
teaID = [0,1,2,3,4,5,6,7]
teas = ["Earl Grey","Orange Pekoe","Peppermint","Calmomile","English Breakfast","Chai","Green","Oolong"]
total = 0
#make the tea names proper english for use in orderFinalizer
isInStock = [True,True,False,True,True,True,False,True]



def main():
    welcomeScreen(name)
    confirmOrder(orderFinalizer(teaPicker()))

def getTotal(item):
    global total
    total = total + item
    return total




def welcomeScreen(name):
    print("Welcome, "+str(name)+" to Simplicitea!")
    input("Press enter to begin.")

def teaPicker():
    while True:
        print("What kind of tea would you like? (input the number)")
        getTea = int(input("0. Earl Grey \n1. Orange Pekoe \n2. Peppermint \n3.Calmomile \n4.English Breakfast \n5. Chai \n6. Green \n7. Oolong\n"))
        if getTea <= 7:
            if isInStock[getTea] == True:
                return getTea
            else:
                print("We're sorry, that tea is out of stock! Please check again later, or select a different tea.")
        else:
            print("Please input the number beside the tea.")

def orderFinalizer(tea):
    while True:
        print("You selected: "+ teas[tea])
        getBags = int(input("How many bags would you like? \n0. 24 bags ($16) \n1. 72 bags ($25) \n2. 120 bags ($32)"))
        if getBags == 0:
            bagCost = 16
            break
        elif getBags == 1:
            bagCost = 25
            break
        elif getBags == 2:
            bagCost = 32
            break
        else:
            print("Invalid option.")
    print("Your new total is $"+str(getTotal(bagCost)))
    while True:
        getShip = int(input("When would you like it? \n0. Standard (4-10 days) Free \n1. Express (2-4 days) +$10 \n2. Overnight (next day) +$20 \n"))
        if getShip == 0:
            shipCost = 0
            break
        elif getShip == 1:
            shipCost = 10
            break
        elif getShip == 2:
            shipCost = 20
            break
        else:
            print("Invalid option.")
    print("Your new total is $"+str(getTotal(shipCost)))
    taxAndService = total * 0.14
    print("+12% GST and PST, +2% Service fee")
    grandTotal = round(getTotal(taxAndService),2)
    print("Your grand total is $"+str(grandTotal))
    return [getTea,getBags,getShip,grandTotal]

def confirmOrder(details):
    #print details of order using return of orderFinalizer
    isConfirmed = input("Place your order? (y/n) \n")
    if isConfirmed == 'y':



main()
