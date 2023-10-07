from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import requests
import json
import subprocess  # Import subprocess to run the cURL command

# If modifying these scopes, delete the file : token.json so it regenerates it.
SCOPES = ['https://www.googleapis.com/auth/fitness.activity.read', 
          'https://www.googleapis.com/auth/fitness.location.read',
          'https://www.googleapis.com/auth/fitness.body.read', 
          'https://www.googleapis.com/auth/fitness.nutrition.read',
          'https://www.googleapis.com/auth/fitness.blood_pressure.read', 
          'https://www.googleapis.com/auth/fitness.blood_glucose.read',
          'https://www.googleapis.com/auth/fitness.oxygen_saturation.read', 
          'https://www.googleapis.com/auth/fitness.body_temperature.read',
          'https://www.googleapis.com/auth/fitness.reproductive_health.read']

def main():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(' .json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Insert your cURL command here
        access_token = creds.token  # Get the access token from your credentials
        curl_command = f'curl -H "Authorization: Bearer {access_token}" "https://www.googleapis.com/fitness/v1/users/me/dataSources/raw:com.google.step_count.delta:com.fitbit.FitbitMobile:health_platform/dataPointChanges"'
        
        # Execute the cURL command
        result = subprocess.run(curl_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Print the cURL command's output
        print(result.stdout)
        print(result.stderr)

    except HttpError as err:
        print(err)

if __name__ == '__main__':
    main()
