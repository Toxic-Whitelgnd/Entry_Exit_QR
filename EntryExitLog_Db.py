#this is from other side for scanning purpose for entry andd exit
import time

import pyrebase,json,ast
import cv2
import pyzbar.pyzbar as pyzbars
from datetime import datetime
from PIL import Image
import numpy as np

#create seprate firebase console and add u r firebaseconfiguration
#i removed due to Privacy Reasons

firebaseConfig = {
    'apiKey': "",
    'authDomain': "",
    'projectId': "",
    'storageBucket': "",
    'messagingSenderId': "",
    'appId': "",
    'measurementId': "",
    'databaseURL':""
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
            stud_dict = ast.literal_eval(str1)
            print("the converted dict is :"+str(stud_dict))
            print(type(stud_dict))




            #extract the getting images
            print(stud_dict.get("USN"))
            stud_usn = stud_dict.get("USN")
            print("Y i cant pass")
            #extracting the key
            print(stud_dict.get("Key"))
            stud_key = stud_dict.get("Key")

            #need to enter the current time for outgoing time

            #inserting into db
            entry_qr_db( stud_usn,stud_key,stud_dict)

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

            # need to enter the current time for outgoing time

            # inserting into db
            exit_qr_db(stud_usn,stud_key, stud_dict)

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

