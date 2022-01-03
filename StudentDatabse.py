import qrcode
import cv2
import pyrebase
from qrtools import QR
'''from firebase import firebase
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)'''

firebaseConfig = {
  'apiKey': "AIzaSyBX2uZdHQF9N__6Hkxipcbt5nwo5LUWhqU",
  'authDomain': "tryingnewproject.firebaseapp.com",
  'databaseURL': "https://tryingnewproject-default-rtdb.firebaseio.com",
  'projectId': "tryingnewproject",
  'storageBucket': "tryingnewproject.appspot.com",
  'messagingSenderId': "988075396346",
  'appId': "1:988075396346:web:32538a58f2bec61249cd43",
  'measurementId': "G-SF9PHKFGLB"
}
# firebase = pyrebase.initialize_app(firebaseConfig)
#
# db = firebase.database()
#
# a=db.child('78VO0PQMM6').child('20btrce12').get()
# for x in a.each():
#   print(x.key(),x.val())
# #pusing data
# #db.child(usn).set(data)

qr = QR(data=u"fuck u boi")

qr.encode()






'''
a = "hello welcome to  student data base"

b = qrcode.make(a)
b.save("stud_db_qr.jpg")

#to read the qr file

c = cv2.QRCodeDetector()
val,points,straightcode = c.detectAndDecode(cv2.imread("raj.jpg"))
print(val)'''