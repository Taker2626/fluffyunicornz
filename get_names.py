"""
Gets names from google calendar events for certain days
"""
import httplib2
import os
from time import strftime
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import datetime

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
print(Classes)
