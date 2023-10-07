# health-api
How to get personal data from Fitbit + Google Fit through Fitness API for WEB API / Desktop app

Install Fitbit + Google FIT on your phone -> generate some data!

----
0. Why?
    - Wearables have positive health contributions (BUT unorganized raw data doesn't help healthcare professionals!)
    - https://www.jmir.org/2020/10/e23954/
        - "Our final sample comprised 41 articles reporting the results of 37 studies. For Fitbit-based interventions, we found a **statistically significant increase in daily step count** and moderate-to-vigorous **physical activity**, a **significant decrease in weight** "
         - "setting activity goals was the most important intervention component."
     
           
    - Research: Wearables can track and predict health outcomes but only if done right
    - https://academic.oup.com/jamia/article/25/9/1221/5047137?login=false
      - In 2018 out of 135 studies utilizing wearable technology in clinical outcome prediction* only 8 was relevant (studies that derived a model predicting mortality, readmissions, and/or ED visits that incorporated data from any wearable technology.)
      - "They found that duration of sedentary bouts and the total number of steps were associated with readmissions. Their multifactorial model of Fitbit collected step counts and other patient activity was able to predict readmission in 88.3% of cases. The model that used only Fitbit collected step counts predicted readmission accurately only 67.1% of the time. In a follow-up study, the authors found that in 71 patients with metastatic peritoneal cancer, higher mean daily step counts were predictive of 30- and 60-day readmissions even after adjusting for other risk factors."
      
    - Fitbit already has a library of research done with their devices: https://www.fitabase.com/research-library/
    - A publication that points out challenges and solution for trials done by Fitbit: https://mhealth.jmir.org/2021/3/e25289/
    - And third-party commercial data collection platforms already exist that help with accessing multitude of participant data: Fitabit demo - https://www.youtube.com/watch?v=39_D35Q42p8 


    - Personal tracking:
        Research platforms are not free, but I still want to analyse my data.
         
1. Let's start with Fitbit
    - why Fitbit? You can do your own market research (which OS, which device, which brand, which app) it's just not the scope of this :D

    https://accounts.fitbit.com/signup
    https://dev.fitbit.com/apps/new
    fill in with anything: ![image](https://github.com/laszlo678/health-api/assets/105205264/66449295-4c7b-4859-8c8b-13368375c980)
    set up access token by clicking on 'OAuth 2.0 Tutorial': ![image](https://github.com/laszlo678/health-api/assets/105205264/f0336ff2-33ec-4cc5-82e8-a3b0d4a66313)



    **see file "1. fitbit.py" for steps + code**

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

2. Google Health Connect:
   - Stores raw data from various health app in 1 place (Google Fit, Fitbit, Samsung Health, MyFitnessPal, Leap Fitness, Garmin, Strava...)
       ![image](https://github.com/laszlo678/health-api/assets/105205264/c351b4f3-8bda-4e92-a068-fd591b7d23b8)
   - Let's download the app, so we can integrate data from our Fitbit + Google Fit
         https://play.google.com/store/apps/details?id=com.google.android.apps.healthdata
     

3. Google Fitness API - Google FIT
     - now that all the data from our apps get written from one to another, we can get all of them from 1 place...Google
       (while we can, as Google is killing these left and right. some past examples: https://www.reddit.com/r/GoogleFit/comments/e8l8t8/any_way_to_view_google_fit_data_on_pc/?rdt=48629)

   3.1 Fitness API - Web application
       -> this is easier to call than the 3.2 but you will need to go into the OAuth Playground to get the Access code -> harder to collaborate

      **see file "3.1 Google Fit - Fitness API - Web.py" for steps + code**

        1. set-up: https://developers.google.com/fit/rest/v1/get-started
            1.1 set-up Credential -> stay in TESTING don't press Publish (you can invite up to 100 collaborators in this state as well + google does)
            1.2 set-up OAuth 2.0 client ID -> 
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
                    
                    -> BUT FIRST LET'S GET THE DATASOURCE SAVED IN AN EXCEL -> Use ChatGPT for example:
                        write: this is my json response I get, only print the dataStreamIDs, {insert the whole json object response that you get when you called the url}
                        write: also get back beside the dataStreamIDs the corresponding name that is given back in the dataType
                        write: let's save it to an excel where name is column A and id is B
                        -> adjust code to personal liking
                
                        in command line install pandas - pip install panda
                
                        SEE CODE BELOW -> comment out corresponding
                    
                3.1.2 Now that we have the dataSourceIDs, let's call whichever by adding it to the end of the url
                   -> you can read the documentation which scope is for what: https://developers.google.com/identity/protocols/oauth2/scopes#fitness
           
                    url = "https://www.googleapis.com/fitness/v1/users/me/dataSources/derived:com.google.step_count.delta:com.google.android.gms:merge_step_deltas"
                
                    -> so this is the json format the we got here, not the data
                    -> if we want the actual data, we need to add at the end: /dataPointChanges
                    url = "https://www.googleapis.com/fitness/v1/users/me/dataSources/derived:com.google.step_count.delta:com.google.android.gms:merge_step_deltas/dataPointChanges"
                
                3.1.3 Let's get an excel where we get back the steps with dates
                
                    SEE CODE BELOW -> comment out corresponding
                
                    -> Visualize in excel -> Ask ChatGPT: 
                        "29-09-2023	21	51
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
                        29-09-2023	21	98"
                
                        -> F11 -> paste -> save ->F8 -> Run / Create a button for it in Excel Developer Module
                        
                        -> than in excel press F11 for instant chart view
   
   3.2 Fitness API - Desktop app

       """
            3.2.1 set up similar as in 3.1.1 but (Under Application type, select Desktop app) + (Under redirect link write: http://localhost, leave url for javascript empty)
            3.2.2 Set up authorization for a desktop app -> I have copied this from this youtube video's github as I have not found elsewhere: https://www.youtube.com/watch?v=irhhMLKDBZ8
                3.2.2.1 download credentials to a credentials.json file
                3.2.2.2 adjust scopes to your liking - more info: https://developers.google.com/fit/datatypes#authorization_scopes
            3.2.3 Visualize as in 3.1
        """
   
**                **see file "3.2 Google Fit - Fitness API - Desktop app.py" for code** 
**
  


        
