#Exit QR making
import pyrebase
from datetime import datetime

import qrcode

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


print("Checking for any ActiveStatus in Database!!")
#create a function to check the active status available or not
#retrive all usn and check witht he usn by usnig some functions
#and pass to Exitqe
def check_usn(stud_usn_check):
    users = db.child(stud_usn_check).get()
    print(users.val())

    #creating a list
    stud_key_list = []

    #establishing a flag to know it is active or not,active na 1.or 0
    active  = 0
    active_db_key = ''

    # creating a dict
    stud_dict = {}

    for user in users.each():
        print("Came to For loop ")
        print(user.key())
        stud_key_identification = user.key()
        print(stud_key_identification)
        stud_key_list.append(stud_key_identification)
        print(stud_key_list)

        stud_outtime_check = db.child(stud_usn_check).child(stud_key_identification).get()
        print(stud_outtime_check)

        print("Retreived the available keys")


        for stud_in_time in stud_outtime_check.each():
            print(stud_in_time.key(),stud_in_time.val())
            stud_dict[stud_in_time.key()] = stud_in_time.val()

        print(stud_dict)
        b = 'In*Time'
        if b in stud_dict.keys():
            print("Present")

        else:
            print("Not present")
            active = 1
            active_db_key = stud_dict.get("Key")
            active_db(stud_usn_check, active_db_key)
            




    print(len(stud_key_list))
    for i in range(len(stud_key_list)):
        print(stud_key_list[i])

        print("keys in list of loop")


    if(users.val() != None):
        print("Came here in the if loop")
        #Exitqr(stud_usn_check)

    else:
        print(" OOPS Sorry U didn't make any Entry!!")


def active_db(stud_fk_usn,stud_fk_key):
    print("Fked up here")
    print(stud_fk_key,stud_fk_usn)
    #need to  satrt code from here
    Exitqr(stud_fk_usn,stud_fk_key)



def Exitqr(stud_usn,stud_key):
    print("Entered here")
    print(stud_usn)
    stud_details = db.child(stud_usn).child(stud_key).get()

    stud_db_acc_dict = {}

    try:
        for stud_db_acc in stud_details.each():
            print(stud_db_acc.key(),stud_db_acc.val())
            if (stud_db_acc.key() == "Name"):
                stud_name_db = stud_db_acc.val()
                stud_db_acc_dict["Name"] = stud_name_db
            elif (stud_db_acc.key() == "USN"):
                stud_USN_db = stud_db_acc.val()
                stud_db_acc_dict["USN"] = stud_USN_db
            elif (stud_db_acc.key() == "sem"):
                stud_sem_db = stud_db_acc.val()
                stud_db_acc_dict["sem"] = stud_sem_db
            elif (stud_db_acc.key() == "Branch"):
                stud_branch_db = stud_db_acc.val()
                stud_db_acc_dict["Branch"] = stud_branch_db
            elif (stud_db_acc.key() == "Mobileno"):
                stud_mobilno_db = stud_db_acc.val()
                stud_db_acc_dict["Mobileno"] = stud_mobilno_db
            elif (stud_db_acc.key() == "Out*Time"):
                stud_Time_db = stud_db_acc.val()
                stud_db_acc_dict["Out*Time"] = stud_Time_db
            elif (stud_db_acc.key() == "reason"):
                stud_reason_db = stud_db_acc.val()
                stud_db_acc_dict["reason"] = stud_reason_db
            elif (stud_db_acc.key() == "time*day"):
                stud_td_db = stud_db_acc.val()
                stud_db_acc_dict["time*day"] = stud_td_db
            elif (stud_db_acc.key() == "Out*Date"):
                stud_date_db = stud_db_acc.val()
                stud_db_acc_dict["Out*Date"] = stud_date_db
            elif (stud_db_acc.key() == "Key"):
                stud_key_db = stud_db_acc.val()
                stud_db_acc_dict["Key"] = stud_key_db

        # getting date and time when they logged in
        stud_time = datetime.today().strftime("%H:%M:%S %p")
        print(stud_time)
        now = datetime.now()
        stud_date = now.strftime("%y-%m-%d")
        print(stud_date)

        # adding the date and time to dictionary
        stud_db_acc_dict["In*Date"] = stud_date
        stud_db_acc_dict["In*Time"] = stud_time

        # after inserting date and time
        print(stud_db_acc_dict)

        #need to make a QR Here
        stud_qr_random = qrcode.QRCode(version=3, error_correction=qrcode.ERROR_CORRECT_M
                                       , box_size=10, border=4)
        stud_qr_random.add_data(stud_db_acc_dict)
        stud_qr_random.make(fit=True)
        stud_qrrr = stud_qr_random.make_image(fill_color='black', back_color='blue')
        stud_QR = stud_qrrr.save(r'C:\Users\HOME\PycharmProjects\TryingNew Project\Students_generated_qrcodes\Exit.png')
        print("Random Exit QR had made successfully")

    except:
        print("OOPS! Sorry u didn't Make any Entry Log!!")


#need to generate a random key after usn.



