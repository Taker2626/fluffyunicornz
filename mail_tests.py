import os
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
#MIMEText is a type storing by deafult the message, Then adds Header information modyfing the Variable e. msg['Subject']="Subject"
#needed modification : 'Subject', 'From','To'
#-------------------------------------------------------------------------------------------------#
def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result

#-------------------------------------------------------------------------------------------------#
msg=MIMEText('This is just a test')
msg['Subject']='HaHaHa'
msg['From']=formataddr(['Norman Heil','n.heil@jacobs-university.de'])
msg['to']='normanheil@yahoo.de'
s=smtplib.SMTP('exchange.jacobs-university.de')
s.send_message(msg)
s.quit()
