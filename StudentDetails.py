#this is for student purpose for crwating qr code while going out and coming in.

import os
import random
import re
import shutil
import string
from pathlib import Path
import qrcode,image


from Exit_Qr_Making import *

regex = '^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$'


firebaseConfig = {
'apiKey': "AIzaSyBXHtKztH7seF8qciW-G8CfpC013pBir48",
  'authDomain': "entryexittag.firebaseapp.com",
  'databaseURL': "https://entryexittag-default-rtdb.firebaseio.com",
  'projectId': "entryexittag",
  'storageBucket': "entryexittag.appspot.com",
  'messagingSenderId': "34693254962",
  'appId': "1:34693254962:web:a13cc27de7304a8fc1912b",
  'measurementId': "G-RWTCEVDJWR"
}
firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

stud_usn_temp = ''

#need to edit this path
file_source = r'D:\\PyCharm\\PycharmProjects\\EntryExit_QR\\'
file_destination_txt = r'D:\\PyCharm\\PycharmProjects\\EntryExit_QR\\Student_profiles'
file_destination_qr = r'D:\PyCharm\PycharmProjects\ExitEntry_QR\Students_generated_qrcodes'
qr_imge = r'D:\\PyCharm\\PycharmProjects\\EntryExit_QR\\Students_generated_qrcodes\\entry.jpg'

file_txt = r" Student_profiles\ "

def valid_email(email):
    if (re.search(regex, email)):
        print("Valid Email")
    else:
        print("Invalid Email")

def home_page():
    print("1.Create Student Profile Data")
    print("2.Go to Profile")
    ch = int(input("Enter u r choice:"))
    if(ch == 1):
        student_details()
    else:
        student_profile()


def student_profile():
    print("Entered into student profile")
    #need to start code from here

    # this part will be in reteriving from db or it will store in mobile memory like login or something
    #need to do like a pro ,import os and extract the txt file
    for root, dirs, files in os.walk(r'D:\\PyCharm\\PycharmProjects\\EntryExit_QR\\Student_profiles'):
        print("Available profiles!")
        for file in files:

            if file.endswith('.txt'):
                print(os.path.join(file))
                transfer_file = os.path.join(file)

        print("<--------------------------->")

    ch = input("Enter the file name:")

    with open(file_destination_txt+r'\\'+ch,'r')  as f:
        a = f.read()

    print("values inside the file:"+str(a))
    print(type(a))
    b = []
    b.append(a)
    print(b)

    #splitting the values from the file
    c = b[0].split()

    print(c)
    print(c[0])
    print(c[1])

    #assigning the values of key(id) and usn
    stud_id = c[0]
    stud_id_usn = c[1]

    #creating a empty dict
    stud_db_acc_dict = {}

    stud_db = db.child(stud_id).child(stud_id_usn).get()
    for stud_db_acc in stud_db.each():
        print(stud_db_acc.key(),stud_db_acc.val())
        if(stud_db_acc.key() == "Name"):
            stud_name_db = stud_db_acc.val()
            stud_db_acc_dict["Name"] = stud_name_db
        elif(stud_db_acc.key() == "USN"):
            stud_USN_db = stud_db_acc.val()
            stud_db_acc_dict["USN"]=stud_USN_db
        elif (stud_db_acc.key() == "sem"):
            stud_sem_db = stud_db_acc.val()
            stud_db_acc_dict["sem"] = stud_sem_db
        elif (stud_db_acc.key() == "Branch"):
            stud_branch_db = stud_db_acc.val()
            stud_db_acc_dict["Branch"] = stud_branch_db
        elif (stud_db_acc.key() == "Mobileno"):
            stud_mobilno_db = stud_db_acc.val()
            stud_db_acc_dict["Mobileno"] = stud_mobilno_db
        elif(stud_db_acc.key() == "emailid"):
            stud_emailid_db = stud_db_acc.val()
            stud_db_acc_dict["emailid"] = stud_emailid_db

    print(stud_db_acc_dict)

    print("Make a QR for Entry//")
    print("Make a QR for Exit//")
    ch = int(input("1 or 2:"))
    if(ch == 1):
        # name usn branch sem

        print("Reason for Going out//")
        stud_reason = input("Reason:")
        stud_reason_time = input("time/day:")
        print("Came to QR code making")
        #creating another one database for storing the reason date/time wiht student details.
        #now i making simple

        # getting date and time when they logged in
        stud_time = datetime.today().strftime("%H:%M:%S %p")
        print(stud_time)
        now = datetime.now()
        stud_date = now.strftime("%y-%m-%d")
        print(stud_date)

        stud_db_acc_dict["reason"] = stud_reason
        stud_db_acc_dict["time*day"] = stud_reason_time

        # adding the date and time to dictionary
        stud_db_acc_dict["Out*Date"] = stud_date
        stud_db_acc_dict["Out*Time"] = stud_time

        # after inserting date and time


        S = 12  # number of characters in the string.
        # call random.choices() string module to find the string in Uppercase + numeric data.
        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=S))
        print("The randomly generated string is : " + str(ran))



        stud_db_acc_dict["Key"] = ran

        print(stud_db_acc_dict)

        print(stud_db_acc_dict["USN"])

        stud_usn_passing = stud_db_acc_dict["USN"]

        #passing into the db
        #entrylog_db(student_usn=stud_usn_passing,student_details_entry=stud_db_acc_dict)
        # print("went succcesfully")

        stud_qr_random = qrcode.QRCode(version=3,error_correction=qrcode.ERROR_CORRECT_M
                                       ,box_size=10,border=4)
        stud_qr_random.add_data(stud_db_acc_dict)
        stud_qr_random.make(fit=True)
        stud_qrrr=stud_qr_random.make_image(fill_color='black',back_color='blue')
        stud_QR=stud_qrrr.save(qr_imge)
        print("Random QR had made successfully")

        # for file in Path(file_source).glob(stud_QR):
        #     print("y i cant move")
        #     shutil.move(os.path.join(file_source, file), file_destination_qr)
        #     print("QR Moved to student generated qr")




    else:
        print("Entered in Exit_Qr")
        print(stud_id_usn)
        intial_usn_check(stud_id_usn)
        #Exitqr(stud_id_usn)

def student_details():
    stud_name = input("Enter a name:")
    stud_usn = input("Enter a USN:")
    stud_branch = input("Enter a Branch:")
    stud_sem = input("Enter a Sem:")
    stud_year = input("Enter a Year:")
    stud_emailid = input("Enter a Emailid:")
    #check for valid email
   # valid_email(stud_emailid)
    stud_mobilno = input("Enter a Mobile no:")

    stud_usn_temp = stud_usn
    stud_usn={
        "Name":stud_name,
        "USN":stud_usn,
        "Branch":stud_branch,
        "sem":stud_sem,
        "Year":stud_year,
        "emailid":stud_emailid,
        "Mobileno":stud_mobilno
    }
    #need to generate a key and store it in a file with that key we can fetch from the database
    S = 10  # number of characters in the string.
    # call random.choices() string module to find the string in Uppercase + numeric data.
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=S))
    print("The randomly generated string is : " + str(ran))


    db.child(ran).child(stud_usn_temp).set(stud_usn)
    print("successfully inserted to db")

    '''stud_qr = qrcode.make(stud_usn)
    stud_qr.save(stud_name+".jpg")
    print("qr code successfully generated!")'''

    #this will be key to access the databse content,while creating a app this will be in shared preference memory.
    f = open(stud_usn_temp+'.txt','a')
    f.write(ran)
    f.write('\n')
    f.write(stud_usn_temp)
    f.close()

    #this is for listing the files
    for root,dirs,files in os.walk(file_source):
        for file in files:
            if file.endswith('.txt'):
                print(os.path.join(file))
                transfer_file = os.path.join(file)
                print("File successfully founded")

                #this is for moving the file
                try:
                    for file_to_transfer in Path(file_source).glob(transfer_file):
                        shutil.move(os.path.join(file_source,file_to_transfer),file_destination_txt)
                        print("file moved successfully")
                except:
                    print("File already Existed in the folder")





    print("Successfully Created the profile!!")

home_page()

''''apiKey': "AIzaSyBXHtKztH7seF8qciW-G8CfpC013pBir48",
  'authDomain': "entryexittag.firebaseapp.com",
  'databaseURL': "https://entryexittag-default-rtdb.firebaseio.com",
  'projectId': "entryexittag",
  'storageBucket': "entryexittag.appspot.com",
  'messagingSenderId': "34693254962",
  'appId': "1:34693254962:web:a13cc27de7304a8fc1912b",
  'measurementId': "G-RWTCEVDJWR"'''