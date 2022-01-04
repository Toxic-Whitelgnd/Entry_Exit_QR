#trying to create new project
#create qr code for database
#if we scan it will connect to databse and store our details with time.
#for exit it will scan another qr code  and it will store it in the database with close time.

#
# a = "20btrca23"
# b = a.split('20')
# c = b[1]
# print(c)
# i = 0
# d = ''
# for x in a:
#     print(x)
#     i += 1
#     d +=x
#     print(i)
#     if(i == 2):
#         print("reached if")
#         print(d)
#         break

'''if(stud_usn != None):
    print("Reached if condition")
    stud_usn_split = stud_usn.split()'''

#to scan the qr code
import time

'''
import cv2
a = cv2.QRCodeDetector()
a.detectAndDecode(cv2.imread("nsme.jpg"))
'''
'''
to get a dat from database
user=db.child('usn').get()
print(user.val())
for users in user.each():
    print(user.val())

'''

# a = ['aerwe','sdfs']
# print(a[0])
#
# c = 'sdfs'
# a.append(c)
# print(a)
#
# entry_log_qrcode("random.png")

# import os
#
# for root,dirs,files in os.walk(r'C:\Users\HOME\PycharmProjects\TryingNew Project\Student_profiles'):
#     for file in files:
#         if file.endswith('.txt'):
#             print(os.path.join(file))
#             transfer_file = os.path.join(file)
#             print(transfer_file)


# from pathlib import Path
# import shutil
#
# file_source = r'C:\Users\HOME\PycharmProjects\TryingNew Project'
# file_destination = r'C:\Users\HOME\PycharmProjects\TryingNew Project\Student_profiles'
#
# get_files = '20btrca099.txt'
#
# for file in Path(file_source).glob(get_files):
#     shutil.move(os.path.join(file_source,file),file_destination)



# shutil.move(file_source+get_files,file_destination)
# print("Transfered succesfully")

# from datetime import datetime
# print(datetime.today().strftime("%H:%M:%S %p"))
# print(time.strftime("%x"))
#
# now = datetime.now()
# print(now.strftime("%y-%m-%d"))

'''a=input("Want to view the profile and save the file? y or n :")
    if(a == 'y' or 'Y'):
        for x,y in stud_usn.items():
            print(stud_usn[x])
            stud_usn_filename = str(stud_usn_temp)
            f = open(stud_usn_filename+".txt",'a')
            #f.write(x)
            #f.write('\t')
            f.write(y)
            f.write('\n')
            f.close()
    else:
        print(';}')'''

#     if (stud_db_acc.key() == "Name"):
        #             stud_name_db = stud_db_acc.val()
        #             stud_db_acc_dict["Name"] = stud_name_db
        #             active = 0
        #     elif (stud_db_acc.key() == "USN"):
        #             stud_USN_db = stud_db_acc.val()
        #             stud_db_acc_dict["USN"] = stud_USN_db
        #             active = 0
        #     elif (stud_db_acc.key() == "sem"):
        #             stud_sem_db = stud_db_acc.val()
        #             stud_db_acc_dict["sem"] = stud_sem_db
        #             active = 0
        #     elif (stud_db_acc.key() == "Branch"):
        #             stud_branch_db = stud_db_acc.val()
        #             stud_db_acc_dict["Branch"] = stud_branch_db
        #             active = 0
        #     elif (stud_db_acc.key() == "Mobileno"):
        #             stud_mobilno_db = stud_db_acc.val()
        #             stud_db_acc_dict["Mobileno"] = stud_mobilno_db
        #             active = 0
        #     elif (stud_db_acc.key() == "Out*Time"):
        #             stud_Time_db = stud_db_acc.val()
        #             stud_db_acc_dict["Out*Time"] = stud_Time_db
        #             active = 0
        #     elif (stud_db_acc.key() == "reason"):
        #             stud_reason_db = stud_db_acc.val()
        #             stud_db_acc_dict["reason"] = stud_reason_db
        #             active = 0
        #     elif (stud_db_acc.key() == "time*day"):
        #             stud_td_db = stud_db_acc.val()
        #             stud_db_acc_dict["time*day"] = stud_td_db
        #             active = 0
        #     elif (stud_db_acc.key() == "Out*Date"):
        #             stud_date_db = stud_db_acc.val()
        #             stud_db_acc_dict["Out*Date"] = stud_date_db
        #             active = 0
        #     elif (stud_db_acc.key() == "Key"):
        #             stud_key_db = stud_db_acc.val()
        #             stud_db_acc_dict["Key"] = stud_key_db
        #             active = 0
        #     elif (stud_db_acc.key() == "In*Time"):
        #             stud_Intime_db = stud_db_acc.val()
        #             stud_db_acc_dict["In*Time"] = stud_Intime_db
        #             active = 1
        #     elif (stud_db_acc.key() == "In*Date"):
        #             stud_InDate_db = stud_db_acc.val()
        #             stud_db_acc_dict["In*Date"] = stud_InDate_db
        #             active = 1
        #
        # #need to satart code from here
        # print("active:"+str(active))

a = {
    'name':'adfsdf',
    'in*time':'2432wr',
    'usn':'sfgdsdfe'
}

b = 'in*time'
if b in a.keys():
    print("present")
else:
    print("Not present")