# health-api
How to get personal data from Fitbit -> Google Fit through Fitness api for WEB API / Desktop app

----
0. Why?
    - Wearables have positive health contributions.
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
    - why? You can do your own market research (which OS, which device, which brand, which app) it's just not the scope of this :D

    https://accounts.fitbit.com/signup
    https://dev.fitbit.com/apps/new
    fill in with anything: ![image](https://github.com/laszlo678/health-api/assets/105205264/66449295-4c7b-4859-8c8b-13368375c980)
    set up access token by clicking on 'OAuth 2.0 Tutorial': ![image](https://github.com/laszlo678/health-api/assets/105205264/f0336ff2-33ec-4cc5-82e8-a3b0d4a66313)



    see file: 1. fitbit.py for steps

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

3. Google Health Connect:
     - Stores raw data from various health app in 1 place (Google Fit, Fitbit, Samsung Health, MyFitnessPal, Leap Fitness, Garmin, Strava...)
       ![image](https://github.com/laszlo678/health-api/assets/105205264/c351b4f3-8bda-4e92-a068-fd591b7d23b8)

4. Google Fitness API - Google FIT
     - now that all the data from our apps get written from one to another, we can get all of them from 1 place...Google
       (while we can, as Google is killing these left and right. some past examples: https://www.reddit.com/r/GoogleFit/comments/e8l8t8/any_way_to_view_google_fit_data_on_pc/?rdt=48629)

   3.1 Fitness API - Web application
   
   3.2 Fitness API - Desktop app
