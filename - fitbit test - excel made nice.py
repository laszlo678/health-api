import os
import requests
import pandas as pd
from datetime import datetime

url = "https://api.fitbit.com/1/user/-/activities/list.json?beforeDate=2024-07-09&sort=asc&offset=1&limit=100"


# Create a file in Windows, in the same folder location as this .py file called: access_token.txt 
# when done, this line of code will run nicely
token_file = os.path.join(os.path.dirname(__file__), 'access_token.txt')

# Read access token from file
with open(token_file, 'r') as f:
    Access_token = f.read().strip()

headers = {
    "accept": "application/json",
    "authorization": f'Bearer {Access_token}'
}

# Make the GET request
response = requests.get(url, headers=headers)

# Check the response status code
if response.status_code == 200:
    # The request was successful, and you can work with the response data here
    data = response.json()
    
    # Update "duration" to represent time in minutes
    if 'activities' in data:
        activities = data['activities']
        
        for activity in activities:
            if 'duration' in activity:
                duration_ms = activity['duration']
                duration_minutes = duration_ms / 60000  # Convert milliseconds to minutes
                
                 # Limit duration_minutes to 2 decimal places
                duration_minutes = round(duration_minutes, 2)

                # Update the activity dictionary with the duration in minutes
                activity['duration'] = duration_minutes

            if 'originalStartTime' in activity:
                    originalStartTime = activity['originalStartTime']
                    
                    # Parse the datetime string
                    dt = datetime.fromisoformat(originalStartTime)
                    
                    # Extract date and time components
                    date_part = dt.date()  # Extracts date as 'YYYY-MM-DD' format
                    time_part = dt.time()  # Extracts time as 'HH:MM:SS' format
                    
                    # Convert time_part to string if needed
                    time_part_str = time_part.strftime("%H:%M:%S")  # Format time as 'HH:MM:SS'
                    
                    # Update activity dictionary with date and time parts
                    activity['startDate'] = str(date_part)  # Store date as string
                    activity['startTime'] = time_part_str  # Store time as string
        # Normalize the JSON data into a DataFrame
        df = pd.json_normalize(activities)
    else:
        # Handle case when 'activities' key is not present
        df = pd.DataFrame()
    
    # Generate the filename with the current date and time
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"/Users/Laszlo/Downloads/fitbit_data_{current_time}.xlsx"  # Example filename
    
    # Save the DataFrame to an Excel file
    df.to_excel(filename, index=False)
    
    print(f"Data saved to {filename}")
else:
    # Handle the error or provide appropriate error handling
    print(f"Request failed with status code: {response.status_code}")
