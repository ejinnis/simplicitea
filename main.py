name = 'Mr. Potter'
email = 'apotter@wsd1.org'
teaID = [0,1,2,3,4,5,6,7]
teas = ["earlgrey","orangepekoe","peppermint","calmomile","englishbreakfast","chai","green","oolong"]
#make the tea names proper english for use in orderFinalizer
isInStock = [True,True,False,True,True,True,False,True]



def main():
    welcomeScreen(name)
    orderFinalizer(teaPicker())



def welcomeScreen(name):
    print("Welcome, "+str(name)+" to Simplicitea!")
    input("Press enter to begin.")

def teaPicker():
    print("What kind of tea would you like? (input the number)")
    getTea = int(input("0. Earl Grey \n1. Orange Pekoe \n2. Peppermint \n3.Calmomile \n4.English Breakfast \n5. Chai \n6. Green \n7. Oolong\n"))
    if getTea <= 7:
        if isInStock[getTea] == True:
            return getTea
        else:
            print("We're sorry, that tea is out of stock! Please check again later, or select a different tea.")
            teaPicker()
    else:
        print("Please input the number beside the tea.")
        teaPicker()

def orderFinalizer(tea):
    print("You selected: "+ teas[tea])

main()
