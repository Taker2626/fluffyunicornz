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

def make_book(Address):
    Book={}
    for i in range(0,int(((len(Address)-1)/2))):
        Book[Address[i]]=Address[i+1]
    return Book
#-------------------------------------------------------------------------------------------------#
Settings=open(find_all('Email_infos.txt','/Users/normanheil/')[0],'r').read().split('|')
Address=open(find_all('Address_infos.txt','/Users/normanheil/')[0],'r').read().split('|')
Address=make_book(Address)

#-------------------------------------------------------------------------------------------------#













msg=MIMEText('Yeah please excuse me')
msg['Subject']='Excuse'
msg['From']=formataddr([Settings[0],Settings[1]])
msg['to']=formataddr(list(Address.items())[0])
s=smtplib.SMTP('exchange.jacobs-university.de')
s.send_message(msg)
s.quit()
