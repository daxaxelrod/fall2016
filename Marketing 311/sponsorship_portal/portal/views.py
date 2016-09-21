from django.shortcuts import render
from django.http import HttpResponse

import httplib2
import json
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools


# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
CLIENT_SECRET_FILE = '../sponsorship-with-sheets-8544b228d0ec.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


# from working stt
# def get_speech_service():
#     credentials = GoogleCredentials.get_application_default().create_scoped(
#         ['https://www.googleapis.com/auth/cloud-platform'])
#     http = httplib2.Http()
#     credentials.authorize(http)
#
#     return discovery.build(
#         'speech', 'v1beta1', http=http, discoveryServiceUrl=DISCOVERY_URL)


def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        print('Storing credentials to ' + credential_path)
    return credentials

def home(request):
    credentials  = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)
    spreadsheet_id = "1zoz18BR6c5Yt9ZuzvAUfm0rZZX_KNXEWnw"
    range_name = "Class Data!A2:E"
    results = service.spreadsheets().values.get(
        spreadSheetId = spreadsheet_id,
        range=range_name
    ).execute()
    values =results.get('values', [])

    if not values:
        print("No data found")
    else:
        print("Info below")
        for row in values:
            print("%s %s" % (row[0], row[4]))

    results_dict = {}
    return HttpResponse(json.dump(results_dict))