'''
1. register for fitbit account: https://accounts.fitbit.com/signup
2. register app on fitbit: https://dev.fitbit.com/apps/new
2.1 see example: 1. fitbit register app.png
3. get access token by clicking on 'OAuth 2.0 Tutorial' at the bottom of the page after step 2.
3.1 see location: 1. fitbit get access token.png
4. step through page
4.1 copy access token

5. ask ChatGPT to call curl in python

6. LETS change up the url to get different data
6.1 See what options we have: https://dev.fitbit.com/build/reference/web-api/troubleshooting-guide/web-api-explorer/
6.2 change url accordingly

    get values of types of exercises by days - Get Activity Intraday Time Series - https://api.fitbit.com/1/user/-/activities/steps/date/2023-09-25/2023-09-30/15min.json
        activity types: calories, steps, distance, floors, elevation

    get data by day - Get Activity Summary by Date
    1+2 combined - Get Activity Log List
    summary - Get Lifetime Stats

6.3. visualize -> ask ChatGPT to visualize: panda, excel
'''

import requests
import json

# Define the API URL and headers
url = " https://api.fitbit.com/1/user/-/profile.json"

#url = "https://api.fitbit.com/1/user/-/activities/date/2023-09-26.json"
# you can see that data is returned from Fitbit app AND Google Fit app as well!!!

#url = "https://api.fitbit.com/1/user/-/activities/list.json?beforeDate=2023-09-27&sort=asc&offset=1&limit=100"


Access_token = 'insert here from step 4.1'

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
    
    print(data)

    
    #MAKE IT MORE READABLE! Ask ChatGPT
    # Pretty-print the JSON data
    #print(json.dumps(data, indent=4))
    
else:
    # Handle the error or provide appropriate error handling
    print(f"Request failed with status code: {response.status_code}")

