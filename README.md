
Api'S Description:

This application contained 3 API's
1. GetAd - you send some parameters and it will return the xml file.
2. Impression - you send some parameters and it saves impressions in a database based on the parameters and return 200 response.
3. GetStats - you send a filter type and it will give you a json document with Fill rat.

Using python version - Python 3.6.9

Then run command - cd advertisement

Run with Docker Compose:

Run this commands for docker installation-
1. sudo apt-get install -y docker.io
2. Check version - docker -v
3. sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
4. If prmission denied then run - sudo docker-compose run web bash
5. Check compose version - docker-compose -v


To migrate the database open new terminal in project directory and type:
1. sudo docker-compose run web bash
2. python manage.py migrate

To run the program in local server use the following command:
1. sudo docker-compose build
2. sudo docker-compose up
Then go to http://127.0.0.1:8000 in your browser 

To migrate the database open new terminal in project directory and type:
1. sudo docker-compose run web bash
2. python manage.py migrate

To check api's:
1. For get advertisement -  http://0.0.0.0:8000/GetAd/
2. For get impression - http://0.0.0.0:8000/Impression/
3. For get stats - http://0.0.0.0:8000/GetStats/


Code explanation:
1. Create models(tables) - There are 2 tables:
   1. Username -  Username with username,advertisement count and impression count field.
   2. Sdkversion - Sdkversion with sdk version, advertise count and impression count field.

2. Create views(API) - There are 3 API:

   1. Get advertisement Api - Getadvertisement in which you send some parameters and if the same user requests for   an ad, increase the ad count per user and save it into a database.
   Same for the sdk version if the user sends the same version, increase the ad count per sdk version and save into the database.
   Also it returns the xml file containing the advertisement clip.
   2. Get Impression Api - GetImpression in which you send some parameters and if the same user requests for   an impression, increase the impression count per user and save it into a database.
   Same for the sdk version if the user sends the same version, increase the impression count per sdk version and save into the database.
   3. Get Stats Api - GetStats in which you send some filter parameters and it will calculate the fill rate by using ad count and impression count of user and sdk version both. Then return json content with fill rate.
