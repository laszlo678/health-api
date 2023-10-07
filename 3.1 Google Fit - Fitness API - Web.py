'''
1. set-up: https://developers.google.com/fit/rest/v1/get-started
    1.1 set-up Credential -> stay in Testing don't press Publish (you can invite up to 100 collaborators in this state as well)
    1.2 set-up OAuth 2.0 client ID
2. Get Access-token from OAuth Playground when exchanging authorization code for tokens seen in  3.1 fitness api - access code.png 
3. set-up requests  = same as in 1. fitbit.py
    3.1 what can we get from this API: https://developers.google.com/fit/rest/v1/reference
        3.1.0 userID = me  <--- always!
        3.1.1 -> let's see what dataSources there are. Replace down in the code the url with this url:
            url = "https://www.googleapis.com/fitness/v1/users/me/dataSources"

            -> to be able to GET data from these sources we will need to add the "dataStreamID" NOT the "name" at the end of our urls (see later)
            -> it is quite confusing, because in the documentation they only list the names, not the dataStreamIDs (https://developers.google.com/fit/datatypes/activity)
            -> also we would need to use MERGE datasource (these IDs start with "derived", not "raw" -> this is important as thanks to Google Health Connect
                the Fitness API is pulling data from all of our connected apps on our phone. So we want to list the aggregated data not just from 1 source
            
            -> BUT FIRST LET'S GET THE DATASOURCE SAVED IN AN EXCEL -> Use ChatGPT
                write: this is my json response I get, only print the dataStreamIDs, {insert the whole json object response that you get when you called the url}
                write: also get back beside the dataStreamIDs the corresponding name that is given back in the dataType
                write: let's save it to an excel where name is column A and id is B

                in command line install pandas - pip install panda

                SEE CODE BELOW -> comment out corresponding
            
        3.1.2 Now that we have the dataSourceIDs, let's call whichever by adding it to the end of the url
            url = "https://www.googleapis.com/fitness/v1/users/me/dataSources/derived:com.google.step_count.delta:com.google.android.gms:merge_step_deltas"

            -> so this is the json format the we got here, not the data
            -> if we want the actual data, we need to add at the end: /dataPointChanges
            url = "https://www.googleapis.com/fitness/v1/users/me/dataSources/derived:com.google.step_count.delta:com.google.android.gms:merge_step_deltas/dataPointChanges"

        3.1.3 Let's get an excel where we get back the steps with dates

            SEE CODE BELOW -> comment out corresponding

            -> Visualize in excel -> Ask ChatGPT: 
                29-09-2023	21	51
                29-09-2023	21	95
                29-09-2023	21	88
                29-09-2023	21	9
                29-09-2023	21	74
                29-09-2023	21	38
                29-09-2023	21	22
                29-09-2023	21	46
                
                This is my data

                I want a vba that adds together values in column c if in column b the values are same, and deletes the rows that it calculated from only keeping 1 row where the sum shows

                So for example:
                29-09-2023	21	88
                29-09-2023	21	9

                the end result would be this:
                29-09-2023	21	98

                -> F11 -> paste -> save ->F8 -> Run / Create a button for it in Excel Developer Module
                
                -> than in excel press F11 for instant chart view

'''


import requests
import json
import pandas as pd
from datetime import datetime


ACCESS_TOKEN = 'paste here from step 2.'

url = 'paste here from corresponding step'

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# Make the GET request
response = requests.get(url, headers=headers)

#STARTING POINT -> ONLY COMMENT THIS OUT, DONT DELETE!! ->
if response.status_code == 200:
    # The request was successful, and you can work with the response data here
    data = response.json()
    # Pretty-print the JSON data
    print(json.dumps(data, indent=4))
else:
    # Handle the error or provide appropriate error handling
    print(f"Request failed with status code: {response.status_code}")


#TESTs BELOW HERE->

#3.1.1
""" if response.status_code == 200: 
    # The request was successful, and you can work with the response data here
    try:
        data = json.loads(response.content.decode('utf-8'))
        
        # Extract dataStreamId and corresponding name values
        data_stream_info = [(item["dataType"].get("name"), item.get("dataStreamId")) for item in data["dataSource"]]
        
        # Create a DataFrame from the extracted data
        df = pd.DataFrame(data_stream_info, columns=["Name", "ID"])
        
        # Save the DataFrame to an Excel file
        df.to_excel("3.1 name - dataStreamID.xlsx", index=False)
        
        print("Data saved to 3.1 name - dataStreamID.xlsx")
        
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}") """

#3.1.3
""" if response.status_code == 200:
    # The request was successful, and you can work with the response data here
    data = response.json()

    # Extract relevant information
    inserted_data = data.get("insertedDataPoint", [])
    
    # Create lists to store extracted data
    start_times_day = []
    start_times_hour = []
    step_counts = []

    for entry in inserted_data:
        start_time_nanos = entry.get("startTimeNanos")
        step_count = entry.get("value", [{}])[0].get("intVal")

        # Convert nanoseconds to a human-readable date-time format
        start_time_day = datetime.utcfromtimestamp(int(start_time_nanos) / 1e9).strftime('%d-%m-%Y')
        start_time_hour = datetime.utcfromtimestamp(int(start_time_nanos) / 1e9).strftime('%H')
        
        start_times_day.append(start_time_day)
        start_times_hour.append(start_time_hour)
        step_counts.append(step_count)

    # Create a DataFrame
    df = pd.DataFrame({
        "Start DAY": start_times_day,
        "Start HOUR": start_times_hour,
        "Step Count": step_counts
    })

    # Save the DataFrame to an Excel file
    df.to_excel("step_count_day_hour_2.xlsx", index=False)
    
    print("Data saved to .xlsx")
else:
    # Handle the error or provide appropriate error handling
    print(f"Request failed with status code: {response.status_code}") """