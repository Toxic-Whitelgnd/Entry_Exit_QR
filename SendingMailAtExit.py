import smtplib
from email.message import EmailMessage

def sendmail(name,emailid,time,reason,outime,outdate,intime,indate):
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)

    #debugging the date
    print(outdate)

    msg=EmailMessage()
    msg['From'] = "akatsukiorganisationdev999@gmail.com"
    print("succesfull")
    msg['To'] = str(emailid)
    msg['Subject']="Your OutGoing Report!!"
    msg.set_content(f" Hello Mr/Mrs {name} , Your Details \n\n <------------------------------------------------------------->>\n\n"
                    f"\t\t\t Reason:{reason} \n\n \t\t\t Time:{time} \n\n\n"
                    f"\t\t Your OutGoing Date.... \n\n<-------------------------------------------------------------> \n\n "
                    f"\t\t Out*Time:{str(outime)} \n\n "
                    f"\t\t Out*Date:{str(outdate)} \n\n"
                    f"\t\t In*Time:{str(intime)} \n\n"
                    f"\t\t In*Date:{str(indate)} \n\n"
                    f"\t 🟥🟧🟨 Don't Reply , Your Journey Completed🟦🟪🟫 \t\t ")

    server.login("akatsukiorganisationdev999@gmail.com","lgrztplkwseotosn")
    server.send_message(msg)

    server.quit()
    print("fully succesfull")