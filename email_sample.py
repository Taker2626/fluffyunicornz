import os
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import httplib2
import os
from time import strftime
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import datetime

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
"""
Gets names from google calendar events for certain days
"""

#----------------------------------------------------------------------------------------#
def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials
#----------------------------------------------------------------------------------------#
ID='hhkerkpn67nhllmdkg13lhlaog@group.calendar.google.com'
startDate=datetime.datetime(year=2016, month=10, day=17).isoformat()+'Z'
endDate=datetime.datetime(year=2016, month=10, day=19).isoformat()+'Z'
credentials = get_credentials()
http = credentials.authorize(httplib2.Http())
service = discovery.build('calendar', 'v3', http=http)
event=service.events().list(
    calendarId=ID,timeMin=startDate,timeMax=endDate,singleEvents=True,
    orderBy='startTime').execute()
event=event.get('items',[])
Classes=''
if not event:
    Classes.append("None_found")
for events in event:
    start = str(events['start'].get('dateTime').split('T')[0])
    Classes+=events['summary']+';'+events['description']+';'+start+';'
#-------------------------------------------------------------------------------------------------#












msg=MIMEText('Yeah please excuse me')
msg['Subject']='Excuse'
msg['From']=formataddr([Settings[0],Settings[1]])
msg['to']=formataddr(list(Address.items())[0])
s=smtplib.SMTP('exchange.jacobs-university.de')
s.send_message(msg)
s.quit()
