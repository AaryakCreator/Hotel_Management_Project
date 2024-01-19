import csv, math, os, datetime, tabulate, os

def printHeading(statement):
    # Using OS module to get width of screen    
    terminal_width = os.get_terminal_size().columns
    welcome_message = statement

    print("\n" + "~" * terminal_width)
    print(welcome_message.center(terminal_width))
    print("~" * terminal_width + "\n")

def showMenu():
    print("\n\t\t 1. ALL ROOM STATUS")
    print("\n\t\t 2. CHECK-IN")
    print("\n\t\t 3. CHECK-OUT")
    print("\n\t\t 4. OTHER EXPENSES")
    print("\n\t\t 5. ROOM ENQUIRY")
    print("\n\t\t 6. CREDITS")
    print("\n\t\t 0. LOG OUT")
    print("+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+")

def allRooms():
    rooms = [[1,101,'L','V',12000],
             [1,102,'L','V',12000],
             [1,103,'L','V',12000],
             [1,104,'S','V',12000],
             [2,201,'E','V',12000],
             [2,202,'L','V',12000],
             [2,203,'S','V',12000],
             [2,204,'L','V',12000],
             [3,301,'R','V',12000],
             [3,302,'L','V',12000],
             [3,303,'E','V',12000],
             [3,304,'E','V',12000],
             [3,305,'L','V',12000],
             ]
    
    with open("rooms.csv","w") as f:
        writer = csv.writer(f,delimiter=",",lineterminator="\n")
        for r in rooms:
            writer.writerow(r)

def roomStatus():
    with open("rooms.csv","r") as f:
        rm = [['FLOOR','ROOM NUMBER','ROOM TYPE','ROOM STATUS','RATE']]
        reader = csv.reader(f,delimiter=',')
        rtype= " "
        status = " "
        print("="*70)
        print("="*70)
        for row in reader:
            if row[2]=="L":
                rtype = "LAVISH"
            elif row[2]=="E":
                rtype ="EXTRAVAGANT"
            elif row[2]=="S":
                rtype ="SUMPTOUS"
            elif row[2]=="R":
                rtype="RECHERCE"
            if row[3]=='V':
                status = "VACANT"
            else:
                status = "OCCPIED"
            rm.append([row[0],row[1], rtype, status, row[4]])
        print(tabulate.tabulate(rm))
        print("="*70)
    input("Press Enter")

def reader_(roomType):
    with open("rooms.csv","r") as f:
        myreader = csv.reader(f, delimiter=',')
        for row in myreader:
            if row[2] == (roomType):
                if row[3] == 'V':
                    return row[1]
                else:
                    pass
    
    return "INVALID"
    
def checkIn():
    print("\n\n\t\t ^^^^^^^^^^^^^^^ WELCOME TO HOTEL TRANSELVANIA ^^^^^^^^^^^^^^^^^ ")
    
    visitorNum = 0
    if os.path.exists("Visitor.csv"):
        with open("Visitor.csv","r") as f:
            reader = csv.reader(f, delimiter=',')
            l = len(list(reader))
            visitorNum += 1
    else:
        visitorNum = 1
    
    dt = datetime.datetime.now()
    today = str(dt.day) + '/' + str(dt.month) + '/' + str(dt.year) + ' ' + str(dt.hour) + ':' + str(dt.minute) + ':' + str(dt.second)

    print("\n\t\t Today is: ",today)
    print("\n\t\t Visitor Numner: ", visitorNum)

    name = str(input("Enter your name: "))
    age = int(input("Enter your age: "))
    gender = str(input("Enter your gender: "))
    address = str(input("Enter address: \n\t"))
    phNo = int(input("Enter phone number: "))
    c = 0
    roomNo = ""
    rmstatus = []

    while c == 0:
        roomType = input("\t\t Enter Room Type (L/E/S/R): ")
        roomNo = reader_(roomType)
        
        if roomNo == "INVALID":
            print("\t\t No room under that suite is avaliable!!",roomType)
        else:
            status = checkRoomVacant(roomNo)
            rmstatus.append(status)
            if rmstatus =='INVALID':
                print("Enter valid room number: ")
            elif rmstatus[0] == 'V':
                c=1
            else:
                print("Room not vacant!")

    print("\t\t Room Number: ",roomNo)
    print("\t\t Check-In date and time: ",today)
    print("\t\t Room Rent: ", str(rmstatus[1])+'Day')
    
def checkRoomVacant(roomNo):
    with open("rooms.csv","r") as f:
        myreader = csv.reader(f,delimiter=',')
        found = False
        for row in myreader:
                if (row[1]) == (roomNo):
                    found = True
                    print(row[3],row[4])
                    return row[3], row[4]
                
                else:
                    return "INVALID"
    input("Press Enter...")

def ageCheck():
    l = int(input("Enter Age: "))
    if 18<= l <= 100:
        return l
    else:
        print("\t\t Invalid Age!! \n Age shoul be between 18 to 100")
        ageCheck()

def contact():
    printHeading("Developer")
    print("\n\t\t Project Name: HOTEL TRANSELVANIA (HOTEL MANAGEMENT SYSTEM)")
    print("\n\t\t Language: Python")

choice = 0
checkRoomVacant(roomNo=101)
while choice != 'NONE':
    printHeading("HOTEL TRANSALVANIA")
    showMenu()
    choice = int(input("\t\t\t ENTER YOUR CHOICE: "))
    if choice == 1:
        roomStatus()
    elif choice == 2:
        checkIn()
    elif choice == 3:
        checkOut()
    elif choice == 4:
        otherExpense()
    elif choice == 5:
        roomEnquiry()
    elif choice == 6:
        contact()
    elif choice == 0:
        choice = 'None'
        print("\n\t\t\t !! THANK YOU !!")
    else:
        print("\n\t\t\t == INVALID CHOICE == ")


