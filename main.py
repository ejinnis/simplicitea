import random
import smtplib
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from keys import sender_address, sender_pass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

name = 'Elwood'
teaID = [0,1,2,3,4,5,6,7]
teas = ["Earl Grey","Orange Pekoe","Peppermint","Calmomile","English Breakfast","Chai","Green","Oolong"]
bagCountsID = [0,1,2]
bagCounts = [24,72,128]
shippingID = [0,1,2]
shippingOptions = ["Standard","Express","Overnight"]
total = 0
isInStock = [True,True,False,True,True,True,False,True]



def main():
    dbinit()
    emailinit()
    welcomeScreen(name)
    confirmOrder(orderFinalizer(teaPicker()))

def mainRetry():
    grandTotal = 0
    welcomeScreen(name)
    confirmOrder(orderFinalizer(teaPicker()))

def dbinit():
    global db
    cred = credentials.Certificate("firebase.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()

def emailinit():
    #i know you're not really supposed to use globals this much but I am lazy.
    global senderName
    global reciever
    global orderNum
    global session
    orderNum = random.randint(1000000,9999999)

    senderName = sender_address
    senderPass = sender_pass
    reciever = 'x1nni@x1nni.xyz'
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address,sender_pass)

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
    global grandTotal
    grandTotal = round(getTotal(taxAndService),2)
    print("Your grand total is $"+str(grandTotal))
    return [tea,getBags,getShip,grandTotal]


def confirmOrder(details):
    global readableTea
    global readableBags
    global readableShip
    for i in range(8):
        if details[0] == teaID[i]:
            readableTea = "Selected tea: "+teas[i]
            print(readableTea)
    for i in range(3):
        if details[1] == bagCountsID[i]:
            readableBags = str(bagCounts[i])+" bags"
            print(readableBags)
    for i in range(3):
        if details[2] == shippingID[i]:
            readableShip = "Selected shipping: "+shippingOptions[i]
            print(readableShip)

    isConfirmed = input("Place your order? (y/n) \n")
    while True:
        if isConfirmed in ("y","yes"):
            sendConfirm(details)
            doc_ref = db.collection(u'orders').document(str(orderNum))
            doc_ref.set({
                u'name': name,
                u'email': reciever,
                u'teaType': readableTea,
                u'bagCount': readableBags,
                u'shipTime': readableShip
                })
            print("Your order has been placed! Your order # is: "+str(orderNum)+"\nA confirmation email has been sent to you at "+reciever)
            exit()
        if isConfirmed in ("n","no"):
            print("Your order has been discarded. Please make your changes and try again.")
            mainRetry()
        else:
            print("Invalid option.")

def sendConfirm(details):
    message = MIMEMultipart()
    message['From'] = senderName
    message['To'] = reciever
    message['Subject'] = 'Order Confirmation: #'+str(orderNum)
    mailContent = 'Hello, '+name+'. This is a confirmation email for your order containing:\n'+readableTea+'\n'+readableBags+'\n'+readableShip+'\nGrand Total (+ tax / service fee): $'+str(grandTotal)+'\n\nIf you did not place this order, please contact Customer Support.\nThank you!'
    message.attach(MIMEText(mailContent, 'plain'))
    text = message.as_string()
    session.sendmail(senderName, reciever, text)
    session.quit()



main()
