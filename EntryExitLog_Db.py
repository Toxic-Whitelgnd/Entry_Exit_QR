#this is from other side for scanning purpose for entry andd exit
import time

import pyrebase,json,ast
import cv2
import pyzbar.pyzbar as pyzbars
from datetime import datetime
from PIL import Image
import numpy as np


firebaseConfig = {
    'apiKey': "AIzaSyBmy71aLIDAN87gm3JAMIqRWq57dRPfceE",
    'authDomain': "entryexitlog.firebaseapp.com",
    'projectId': "entryexitlog",
    'storageBucket': "entryexitlog.appspot.com",
    'messagingSenderId': "573883830371",
    'appId': "1:573883830371:web:1b3f0dba7a23945b7c6856",
    'measurementId': "G-2VM7YZ0BPE",
    'databaseURL':"https://entryexitlog-default-rtdb.firebaseio.com"
}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

qr_values = ''

stud_usn = ''
stud_dict = ''

def inserting_db(stud_usn_passing,stud_db_val):
    print("came to insert into db")
    #need to start codin from here
    print(stud_usn_passing,stud_db_val)
    db.child(stud_usn_passing).set(stud_db_val)
    print("successfully inserted into DAtabse After scanning")



def scan():
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

            #need to enter the current time for outgoing time

            #inserting into db
            inserting_db( stud_usn,stud_dict)

        cv2.imshow("frames",frame)

        key = cv2.waitKey(1)
        if(key == 10):
            break


scan()

