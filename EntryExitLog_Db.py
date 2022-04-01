#this is from other side for scanning purpose for entry andd exit

import SendingMailAtExit
import pyrebase, ast
import cv2
import pyzbar.pyzbar as pyzbars
import SendingMailAtEntry

firebaseConfig = {
    'apiKey': "AIzaSyBFidAWIw-UggFx49xbXLunkXW5-_c1Ywo",
  'authDomain': "entryexittagglogdb.firebaseapp.com",
  'projectId': "entryexittagglogdb",
  'storageBucket': "entryexittagglogdb.appspot.com",
  'messagingSenderId': "898361353579",
  'appId': "1:898361353579:web:924cc29e68e3522c80d82e",
  'measurementId': "G-PWFZBQG312",
    'databaseURL':'https://entryexittagglogdb-default-rtdb.firebaseio.com'
}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

qr_values = ''

stud_usn = ''
stud_dict = ''

def entry_qr_db(stud_usn_passing,stud_key_db,stud_db_val):
    print("came to insert into db")
    #need to start codin from here
    print(stud_usn_passing,stud_key_db,stud_db_val)
    db.child(stud_usn_passing).child(stud_key_db).set(stud_db_val)
    print("successfully inserted into DAtabse After scanning at Entry Time")

def exit_qr_db(stud_usn_passing,stud_key_db,stud_db_val):
    print("came to insert into db")
    #need to start codin from here
    print(stud_usn_passing,stud_key_db,stud_db_val)
    db.child(stud_usn_passing).child(stud_key_db).set(stud_db_val)
    print("successfully inserted into DAtabse After scanning at Exit Time")



def scan_entry():
    cap = cv2.VideoCapture(0)

    while True:
        _,frame = cap.read()

        decodedObj = pyzbars.decode(frame)

        for obj in decodedObj:
            print(obj.data)
            qr_values = obj.data
            print(qr_values)
            print(type(qr_values))
            str1 = qr_values.decode('UTF-8')
            #it is in string dictionary we have to convert to pure from of dictionary
            print(str1)
            print(type(str1))



            #converting to dict
            stud_dict = ast.literal_eval(str1) #ast is a converter
            print("the converted dict is :"+str(stud_dict))
            print(type(stud_dict))

            print()




            #extract the getting images
            print(stud_dict.get("USN"))
            stud_usn = stud_dict.get("USN")
            print("Y i cant pass")
            #extracting the key
            print(stud_dict.get("Key"))
            stud_key = stud_dict.get("Key")


            #This is Seprate for Sending to the User about their report of Exiting!!
            #extracting the email
            print(stud_dict.get("emailid"))
            stud_email = stud_dict.get("emailid")

            #Extracting the Reason Time
            print(stud_dict.get("reason"))
            stud_reason = stud_dict.get("reason")
            #Extracting the Time
            stud_time = stud_dict.get("time*day")
            #Extracting when they went out time
            stud_Odate = stud_dict.get("Out*Date")
            #Extracting the out date
            stud_Otime = stud_dict.get("Out*Time")
            #Extract Name
            stud_name = stud_dict.get("Name")

            print("Extraction Succesfull")

             #inserting into db
            entry_qr_db( stud_usn,stud_key,stud_dict)
            print("Successful Now send to email")

            # Now i have email id,reason,time,outtime,outdate,name so total 5 parameters
            SendingMailAtEntry.sendmail(stud_name, stud_email, stud_time, stud_reason, stud_Otime, stud_Odate)
            print("Went Successfullyy!!")

        cv2.imshow("frames to scan QR Code",frame)

        key = cv2.waitKey(1)
        if(key == 10):
            break

def scan_exit():
    print("Came to  Exit")
    #need to start code from here
    cap = cv2.VideoCapture(0)

    while True:
        _, frame = cap.read()

        decodedObj = pyzbars.decode(frame)

        for obj in decodedObj:
            print(obj.data)
            qr_values = obj.data
            print(qr_values)
            print(type(qr_values))
            str1 = qr_values.decode('UTF-8')
            # it is in string dictionary we have to convert to pure from of dictionary
            print(str1)
            print(type(str1))

            # converting to dict
            stud_dict = ast.literal_eval(str1)
            print("the converted dict is :" + str(stud_dict))
            print(type(stud_dict))

            # extract the getting images
            print(stud_dict.get("USN"))
            stud_usn = stud_dict.get("USN")
            print("Y i cant pass")

            # extracting the key
            print(stud_dict.get("Key"))
            stud_key = stud_dict.get("Key")

            # This is Seprate for Sending to the User about their report of Exiting!!
            # extracting the email
            print(stud_dict.get("emailid"))
            stud_email = stud_dict.get("emailid")

            # Extracting the Reason Time
            print(stud_dict.get("reason"))
            stud_reason = stud_dict.get("reason")
            # Extracting the Time
            stud_time = stud_dict.get("time*day")
            # Extracting when they went out time
            stud_Odate = stud_dict.get("Out*Date")
            # Extracting the out date
            stud_Otime = stud_dict.get("Out*Time")
            # Extract Name
            stud_name = stud_dict.get("Name")
            #Extracting the in time
            stud_InTime1 = stud_dict.get("In*Time")
            #Extracting the in date
            stud_InDate = stud_dict.get("In*Date")

            print("Extraction Succesfull")

            # inserting into db
            exit_qr_db(stud_usn,stud_key, stud_dict)
            print("Successful Now Sending to mail!!")

            # Now i have email id,reason,time,outtime,outdate,name so total 5 parameters
            SendingMailAtExit.sendmail(stud_name, stud_email, stud_time, stud_reason, stud_Otime, stud_Odate,
                                       stud_InTime1, stud_InDate)
            print("Went Successfullyy!!")

        cv2.imshow("frames to scan QR code", frame)

        key = cv2.waitKey(1)
        if (key == 10):
            break



def selection():
    print("Select Your Operations:")
    print("1.SCAN FOR Entry(i.e is Going out!!)")
    print("2.SCAN FOR Exit(i.e is Coming in!!)")

    ch = int(input("1 or 2 :"))
    if(ch == 1 ):
        scan_entry()
    else:
        scan_exit()

selection()

