import requests
import json
import pandas as pd
import os
from datetime import datetime

# Define the API URL and headers
# url = " https://api.fitbit.com/1/user/-/profile.json"

# url = "https://api.fitbit.com/1/user/-/activities/date/2024-07-10.json"
# you can see that data is returned from Fitbit app AND Google Fit app as well!!!

url = "https://api.fitbit.com/1/user/-/activities/list.json?beforeDate=2024-07-11&sort=asc&offset=1&limit=100"

Access_token = 'paste it here from : https://dev.fitbit.com/apps/new'

headers = {
    "accept": "application/x-www-form-urlencoded",
    "authorization": f'Bearer {Access_token}'
}

# Make the GET request
response = requests.get(url, headers=headers)

# Check the response status code
if response.status_code == 200:
    # The request was successful, and you can work with the response data here
    data = response.json()
    
    # Pretty-print the JSON data (optional)
    print(json.dumps(data, indent=4))
    
    # Convert JSON data to a DataFrame
    df = pd.json_normalize(data['activities'])
    
    # Separate "originalStartTime" into date and time
    df['startDate'] = pd.to_datetime(df['originalStartTime']).dt.date
    df['startTime'] = pd.to_datetime(df['originalStartTime']).dt.time
    
    # Drop the original "originalStartTime" column if no longer needed
    df.drop(columns=['originalStartTime'], inplace=True)
    
    # Get today's date and time and format it
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Define the path to the Downloads folder with current date and time in the filename
    downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
    file_path = os.path.join(downloads_folder, f'fitbit_activities_{current_time}.xlsx')
    
    # Save the DataFrame to an Excel file
    df.to_excel(file_path, index=False)
    print(f"Data saved to {file_path}")
    
else:
    # Handle the error or provide appropriate error handling
    print(f"Request failed with status code: {response.status_code}")
