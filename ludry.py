import random
import os
import os.path


class User():
    ID = ""
    name = ""
    surname = ""
    phoneNumber = ""
    email = ""
    password = ""


class Driver(User):
    def __init__(self, email, password, name, surname, phoneNumber, ID):
        self.email = email
        self.password = password
        self.name = name
        self.surname = surname
        self.phoneNumber = phoneNumber
        self.ID = ID


class Administrator(User):
    def __init__(self, email, password, name, surname, phoneNumber, ID):
        self.email = email
        self.password = password
        self.name = name
        self.surname = surname
        self.phoneNumber = phoneNumber
        self.ID = ID


class Customer(User):
    DOB = ""
    homeAddress = ""

    monthlyBillValue = ""

    registrationConfirmed = False

    def __init__(self, email, password, name, surname, phoneNumber, address, DOB):
        self.email = email
        self.password = password
        self.name = name
        self.surname = surname
        self.phoneNumber = phoneNumber
        self.address = address
        self.DOB = DOB


class Reservation():
    reservationID = ""
    numberOfBags = 0
    specialLocker = False
    deliveryAddress = ""
    isCollected = False
    isOnCollectionRoute = False
    isReturned = False
    isOnReturnRoute = False
    collectionDate = ""
    collectionTime = ""

    def __init__(self, numberOfBags, specialLocker, deliveryAddress, collectionDate, reservationID):
        self.numberOfBags = numberOfBags
        self.specialLocker = specialLocker
        self.deliveryAddress = deliveryAddress
        self.collectionDate = collectionDate
        self.reservationID = reservationID
        self.isReturned = False
        self.isCollected = False
        self.isOnCollectionRoute = False
        self.isOnRetrunRoute = False
        ################################################


class Database():
    r = None
    c = None
    d = None

    def createUser(self, lst):
        lst.append("False")
        fileName = lst[0] + ".txt"
        f = open(fileName, "a+")
        for i in (lst):
            f.write(i + '$$')

        f.close()
        f = open("USERLIST.txt", "a+")
        f.write(lst[0] + "$$")
        f.close()

    def verify(self, lst):
        try:
            fileName = lst[0] + ".txt"
            nList = []
            f = open(fileName, "r")
            line = f.readline()
            nList = line.split('$$')
        except IOError:
            print("\n***NO ACCOUNT IS REGISTERED ON THIS EMAIL!***\n")

            login()
        if (nList[0] == lst[0] and nList[1] == lst[1]):
            print("\n***DETAILS CORRECT***\n")
            Database.c = Customer(nList[0], nList[1], nList[2], nList[3], nList[4], nList[5], nList[6])
            if nList[7] == "False":
                print(
                    "Your registration is not confirmed yet. \nIt usually takes 20 minutes to confirm your registration.\n")
                login()
            else:

                mainMenu()

        else:
            print("\n***WRONG PASSWORD***\n")
            f.close()
            login()


def greet():
    print("Welcome to the SkyLaundry!\n")
    n = input("Are you already a member?\n 1 - Yes, I am a member.\n 2 - No, I wolud like to become a member.\n")
    if n == "1":
        login()
    else:

        register()
        greet()


def login():
    print("\nProvide your login details below:")
    email = input("Email: ")
    password = input("Password: ")
    lst = [email, password]
    d.verify(lst)


def register():
    print("\nProvide your registration details below: ")
    name = input("Name: ")
    surname = input("Surname: ")
    email = input("Email: ")
    password = input("Password: ")
    phoneNumber = input("Phone number: ")
    address = input("Home address: ")
    DOB = input("Date of birth(dd/mm/yy): ")
    print("\n***YOUR ACCOUNT HAS BEEN CREATED!***\n")
    lst = [email, password, name, surname, phoneNumber, address, DOB]
    d.createUser(lst)


############################################################################
def mainMenu():
    print("\n***CUSTOMER MENU***")
    print("Select the action to take : ")
    print("1 - Schedule collection")
    print("2 - Finances")
    print("3 - Manage account")
    print("4 - Log out")
    n = input()
    if n == "1":
        scheduleCollection()
    elif n == "2":
        finances()
    elif n == "3":
        manageAccount()
    else:
        print("You have been logged out.")
        login()


def scheduleCollection():
    totalCost = 0
    print("\nEnter collection date(dd/mm/yyy): ")
    d = input("dd: ")
    m = input("mm: ")
    y = input("yyyy: ")
    collectionDate = d + "/" + m + "/" + y
    # ****************************
    print("\nEnter collection time(hh/mm): ")
    h = input("hh: ")
    m = input("mm: ")
    collectionTime = h + " : " + m
    # **************************************
    print("\nProvide number of bags to be collected(max 10 kilo each). ")
    numberOfBags = int(input("Number of bags: "))
    # ********************************************

    print("\nWolud you like to use the special locker?")
    l = input("yes/no: ")
    if l == "yes":
        specialLocker = True
        totalCost = (11 * numberOfBags)
    else:
        specialLocker = False
        totalCost = (8 * numberOfBags)
        # ********************

    print("\nProvide delivery address.")
    deliveryAddress = input("Delivery address: ")
    print("To confirm reservation press 1, to cancel press 2")
    o = input()
    if o == "1":
        reservationID = random.randrange(10000, 100000)
        r = Reservation(numberOfBags, specialLocker, deliveryAddress, collectionDate, reservationID)
        lst = [r.numberOfBags, r.specialLocker, r.deliveryAddress, r.collectionDate, r.reservationID, Database.c.name,
               Database.c.surname, Database.c.email, totalCost,
               r.isCollected, r.isReturned, r.isOnCollectionRoute, r.isOnReturnRoute]
        fileName = Database.c.email + "@Reservations.txt"
        f = open(fileName, "a+")
        for i in lst:
            f.write(str(i) + '$$')
        f.close()
        print("Thank you for making the reservation.")
        mainMenu()
    else:
        mainMenu()


def finances():
    toPay = 0
    fileName = Database.c.email + "@Reservations.txt"
    f = open(fileName, "r+")
    line = f.read()
    lst = line.split("$$")

    for i in range(8, len(lst), 13):
        toPay += float(lst[i])

    print("Total amount to pay: £%.2f" % toPay)
    n = input("To pay now press 1 to go back press 2: ")
    if n == "1":
        payNow()
    else:
        mainMenu()


def payNow():
    print("Provide your credit card details: ")
    cardHolderName = input("Card holder name: ")
    cardNumer = input("Card number: ")
    expDate = input("Expiry date(mm/yyyy): ")
    cvv = input("CVV: ")
    print("Payment suceessful, thank you!")
    fileName = Database.c.email + "@Reservations.txt"
    open(fileName, "w").close()
    mainMenu()


def manageAccount():
    print("\nSelect the action to take : ")
    print("1 - change home address")
    print("2 - change phone number")
    print("3 - change password")
    n = input()
    if n == "1":
        changeAddress()
    elif n == "2":
        changePhoneNumber()
    else:
        changePassword()


def changeAddress():
    a = input("Provide a new home address here: ")
    Database.c.address = a
    lst = [Database.c.email, Database.c.password, Database.c.name, Database.c.surname, Database.c.phoneNumber,
           Database.c.address, Database.c.DOB]
    fileName = Database.c.email + ".txt"
    f = open(fileName, "w")
    for i in lst:
        f.write(i + '$$')
    f.close()
    print("Home address changed to : " + a)
    mainMenu()


def changePhoneNumber():
    p = input("Provide a new phone number here: ")
    Database.c.phoneNumber = p
    lst = [Database.c.email, Database.c.password, Database.c.name, Database.c.surname, Database.c.phoneNumber,
           Database.c.address, Database.c.DOB]
    fileName = Database.c.email + ".txt"
    f = open(fileName, "w")
    for i in lst:
        f.write(i + '$$')
    f.close()
    print("Phone number changed to : " + p)
    mainMenu()


def changePassword():
    p = input("Provide a new password here: ")
    Database.c.password = p
    lst = [Database.c.email, Database.c.password, Database.c.name, Database.c.surname, Database.c.phoneNumber,
           Database.c.address, Database.c.DOB]
    fileName = Database.c.email + ".txt"
    f = open(fileName, "w")
    for i in lst:
        f.write(i + '$$')
    f.close()
    print("Phone password changed to : " + p)
    mainMenu()


#############################################################################


def driverGreet():
    print("***SkyLaundry delivery and collection service***\n")
    driverLogin()


def driverLogin():
    email = input("Enter here your email: ")
    password = input("Enter here your password: ")
    lst = [email, password]
    driverVerify(lst)


def driverVerify(lst):
    try:
        fileName = lst[0] + ".txt"
        nList = []
        f = open(fileName, "r")
        line = f.readline()
        nList = line.split('$$')
    except IOError:
        print("\n***NO ACCOUNT IS REGISTERED ON THIS EMAIL!***\n")
        driverLogin()
    if (nList[0] == lst[0] and nList[1] == lst[1]):
        print("\n***DETAILS CORRECT***\n")
        Database.d = Driver(nList[0], nList[1], nList[2], nList[3], nList[4], nList[5])
        deliveryList()

    else:
        print("\n***WRONG PASSWORD***\n")
        f.close()
        driverLogin()


def deliveryList():
    l = ''
    fileName = Database.d.email + 'xDELIVERYLIST.txt'
    f = open(fileName, "r+")
    line = f.readline()
    nList = line.split('$$')
    print("\n*** DELIVERY LIST ***")
    print(" ID, Name, Surname, Address: Email, Number of bags \n")
    for i in range(0, len(nList) - 1, 6):
        for n in range(i, i + 6):
            l += ("  " + str(nList[n]))
        print(l)
        l = ''

    f.close()
    print("\n")
    options(nList)


def options(nList):
    r = None
    l = ''
    cList = []
    lne = ''
    lst = ''
    print("\nTo change status of the laundry provide the reservation ID number: ")
    reservationID = input("Reservation ID: ")

    print("Selected reservation ID is : " + reservationID)

    for i in range(nList.index(reservationID), nList.index(reservationID) + 6):
        l += str(nList[i] + "  ")
    print(l + "\n")
    emailIndex = nList.index(reservationID) + 4
    custEmail = nList[emailIndex]
    fileName = custEmail + "@Reservations.txt"
    f = open(fileName, "r")
    lne = f.read()
    cList = lne.split("$$")
    f.close()
    IDindex = cList.index(reservationID)

    del cList[len(cList) - 1]

    changeStatus(cList, IDindex, custEmail)


def changeStatus(cList, IDindex, custEmail):
    print("\nChange status to: \n1 - On collectiom route\n2 - Collected\n3 - On return route\n4 - Returned")
    x = input()
    if x == "1":
        cList[IDindex + 5] = "True"
        cList[IDindex + 6] = "False"
        cList[IDindex + 7] = "False"
        cList[IDindex + 8] = "False"
        print("Status changed to : On collection route\n")


    elif x == '2':
        cList[IDindex + 5] = "False"
        cList[IDindex + 6] = "True"
        cList[IDindex + 7] = "False"
        cList[IDindex + 8] = "False"
        print("Status changed to : Collected\n")

    elif x == '3':
        cList[IDindex + 5] = "False"
        cList[IDindex + 6] = "False"
        cList[IDindex + 7] = "True"
        cList[IDindex + 8] = "False"
        print("Status changed to : On return route\n")

    else:
        cList[IDindex + 5] = "False"
        cList[IDindex + 6] = "False"
        cList[IDindex + 7] = "False"
        cList[IDindex + 8] = "True"

        print("Status changed to : Returned\n")

    fileName = custEmail + "@Reservations.txt"
    file = open(fileName, "w")
    for i in cList:
        file.write(str(i + '$$'))
    file.close()
    deliveryList()


########################################################################################################

def adminGreet():
    print("***SkyLaundry***\n")
    adminLogin()


def adminLogin():
    email = input("Enter here your email: ")
    password = input("Enter here your password: ")
    lst = [email, password]
    adminVerify(lst)


def adminVerify(lst):
    a = None
    try:
        fileName = lst[0] + ".txt"
        nList = []
        f = open(fileName, "r")
        line = f.readline()
        nList = line.split('$$')
    except IOError:
        print("\n***NO ACCOUNT IS REGISTERED ON THIS EMAIL!***\n")
        adminLogin()
    if (nList[0] == lst[0] and nList[1] == lst[1]):
        print("\n***DETAILS CORRECT***\n")
        Database.a = Administrator(nList[0], nList[1], nList[2], nList[3], nList[4], nList[5])
        adminPanel()

    else:
        print("\n***WRONG PASSWORD***\n")
        f.close()
        adminLogin()


def adminPanel():
    print("\n***Administration Panel***")
    print('Select:\n1 - Manage users\n2 - View bookings\n3 - Log out')
    n = input()
    if n == '1':
        manageUsers()
    elif n == "2":
        viewBookings()
    else:
        print("You have been logged out.")
        adminGreet()


def manageUsers():
    lst = []
    line = ''
    f = open("USERLIST.txt", "r")
    line = f.read()
    f.close()
    lst = line.split("$$")
    for i in lst:
        print(i)
    selectUser(lst)


def selectUser(lst):
    aList = lst
    email = ""
    print("\nWhich user would you like to select?")
    email = input("Enter your choice here or press ENTER to go further: ")
    print("You have selected: " + email)
    print("\nWhat action would you like to perform?")
    print(
        "1 - delete user\n2 - confirm registration\n3 - change user de-tails\n4 - create new user\n5 - preview finances")
    n = input()
    if n == "1":
        deleteUser(email, aList)
    elif n == "2":
        confirmRegistration(email, aList)
    elif n == "3":
        changeUserDetails(email)
    elif n == "4":
        createNewUser()
    else:
        previewFinances(email)


def deleteUser(email, aList):
    fileName = email + ".txt"
    os.remove(fileName)
    index = aList.index(email)
    del (aList[index])

    f = open("USERLIST.txt", "w")
    for i in aList:
        f.write(str(i + "$$"))
    f.close()
    print("\n***USER HAS BEEN DELETED***\n")
    adminPanel()


def confirmRegistration(email, aList):
    n = input("\nTo confirm registration press 1, to reject press 2: ")
    if n == "1":
        l = ''
        f = open(email + ".txt", "r")
        l = f.read()
        f.close()
        lst = l.split('$$')

        lst[7] = "True"
        f = open(email + ".txt", "w")
        for i in lst:
            f.write(str(i + "$$"))
        print("\n***REGISTRATION CONFIRMED***\n")
        f.close()
        adminPanel()


    else:
        deleteUser(email, aList)
        print("\n***REGISTRATION REJECTED***\n")
        adminPanel()


def changeUserDetails(email):
    uList = []
    l = ''
    f = open(email + ".txt")
    l = f.read()
    f.close()
    uList = l.split('$$')
    print("\nCurrent details are: ")
    print("Email: " + uList[0])
    print("Password: " + uList[1])
    print("Name: " + uList[2])
    print("Surname: " + uList[3])
    print("Phone number: " + uList[4])

    print("\nProvide new details: ")
    uList[0] = input("Email: ")
    uList[1] = input("Password: ")
    uList[2] = input("Name: ")
    uList[3] = input("Surname: ")
    uList[4] = input("Phone number: ")

    f = open(email + ".txt", "w")
    for i in uList:
        f.write(str(i + "$$"))
    f.close()
    print("\n***DETAILS CHANGED***\n")
    adminPanel()


def createNewUser():
    n = input("Is a new user Administrator(1) or Driver(2)?")
    if n == "1":
        print("\nTo create new Administrator account provide the following details: ")

        email = input("Email: ")
        password = input("Password: ")
        name = input("Name: ")
        surname = input("Surname: ")
        phoneNumber = input("Phone number: ")
        ID = input("Employee ID: ")
        lst = [email, password, name, surname, phoneNumber, ID]
        f = open(email + ".txt", "a+")
        for i in lst:
            f.write(str(i + "$$"))
        f.close()
        f = open("USERLIST.txt", "a+")
        f.write(email + "$$")
        f.close()
        print("\n***NEW ADMINISTRATOR ACCOUNT HAS BEEN CREATED***\n")
        adminPanel()

    else:
        print("\nTo create new Driver account provide the following de-tails: ")

        email = input("Email: ")
        password = input("Password: ")
        name = input("Name: ")
        surname = input("Surname: ")
        phoneNumber = input("Phone number: ")
        ID = input("ID: ")
        lst = [email, password, name, surname, phoneNumber, ID]
        f = open(email + ".txt", "a+")
        for i in lst:
            f.write(str(i + "$$"))
        f.close()
        f = open("USERLIST.txt", "a+")
        f.write(email + "$$")
        f.close()
        f = open("DRIVERSLIST.txt", "a+")
        f.write(email + "$$")
        f.close()
        fileName = email + 'xDELIVERYLIST.txt'
        f = open(fileName, "a+")
        f.close()
        print("\n***NEW DRIVER ACCOUNT HAS BEEN CREATED***\n")
        adminPanel()


def previewFinances(email):
    try:
        toPay = 0
        fileName = email + "@Reservations.txt"
        f = open(fileName, "r+")
        line = f.read()
        lst = line.split("$$")
        f.close()

        for i in range(8, len(lst), 13):
            toPay += float(lst[i])

        print("Total amount to pay: £%.2f" % toPay)
    except:
        try:
            l = ''
            count = 0
            fileName = email + 'xDELIVERYLIST.txt'
            f = open(fileName, "r+")
            line = f.readline()
            nList = line.split('$$')
            for i in range(0, len(nList) - 1, 6):
                for n in range(i, i + 6):
                    l += ("  " + str(nList[n]))
                print(l)
                l = ''
                count += 1
            f.close()
            count = count * 10
            print("This week salary is: £%.2f" % count)
        except:
            print("The selected user is an administratior.")

    adminPanel()


def viewBookings():
    line = ''
    l = ''
    aLine = ''
    lst = []
    f = open("USERLIST.txt", "r")
    line = f.read()
    lst = line.split("$$")
    del (lst[len(lst) - 1])

    f.close()

    for i in lst:
        if os.path.isfile(i + "@Reservations.txt"):
            f = open(i + "@Reservations.txt")
            l = f.read()
            aList = l.split("$$")
            del (aList[(len(aList) - 1)])

            for a in range(4, len(aList) - 1, 13):
                print(str(aList[a] + "  " + i))
            f.close()
    selectBooking()


def selectBooking():
    print("\nEnter here the ID of booking and email you wolud like to select: ")
    ID = input("ID: ")
    email = input("email: ")
    print("You have selected: \nemail: " + email + "\nID: " + ID)

    print("To assign a driver press 1, to cancel booking press 2")
    i = input()
    if i == "1":

        assignDriver(email, ID)
    else:
        cancelBooking(email, ID)


def cancelBooking(email, ID):
    line = ''
    lst = []
    f = open(email + "@Reservations.txt", "r")
    line = f.read()
    lst = line.split("$$")
    f.close()

    del lst[len(lst) - 1]
    indexID = lst.index(ID)
    beforeID = indexID - 4
    for i in range(9):
        del lst[indexID]
    for i in range(4):
        del lst[beforeID]
    f = open(email + "@Reservations.txt", "w")
    for i in lst:
        f.write(str(i + "$$"))
    f.close()
    print("\n***THE RESERVATION HAS BEEN CANCELED***\n")
    adminPanel()


def assignDriver(email, ID):
    line = ''
    lst = []
    l = ''
    aList = []
    dEmail = ''

    f = open("DRIVERSLIST.txt", "r")
    line = f.read()
    lst = line.split("$$")
    f.close()
    for i in lst:
        print(i)

    print("\nWhich drivier wolud you like to assign? ")
    dEmail = input("Provide selected email here: ")
    print("You have selected: " + dEmail)
    #################################################
    file = open(email + "@Reservations.txt", "r")
    l = file.read()
    file.close()
    aList = l.split('$$')

    indexID = aList.index(ID)

    bList = [aList[indexID], aList[indexID + 1], aList[indexID + 2], aList[indexID - 2], aList[indexID + 3],
             aList[indexID - 4]]

    filename = dEmail + "xDELIVERYLIST.txt"
    files = open(filename, "a+")
    for i in bList:
        files.write(str(i + "$$"))
    files.close()
    print('\n*** DRIVER ' + dEmail + ' HAS BEEN ASSIGNED TO RESERVATION ID: ' + ID + ' ***')
    adminPanel()


# *******************************************************#
#                        main                           #
# *******************************************************#
d = Database()
print("1 - Login Driver\n2 - Login Customer\n3 - Login Administrator\n4 - Exit")
n = input()
if n == "1":
    driverGreet()
elif n == "2":
    greet()
elif n == "3":
    adminGreet()
else:
    exit()


############################################################
