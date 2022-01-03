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



