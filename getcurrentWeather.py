import APIconnect
import urllib, json
import os
import urllib.request
from json import dumps
from datetime import datetime

"""
-----------------------------------------------------------------------------------------------
PROGRAM: currentWeather.py
Author: Adam McMurchie
Summary: This program is designed to pull current weather data from openweatermap API.
Transactions are only fired once per minute to prevent abuse of the free service and
ensure that any interface built does not get blocked.

PROGRAM FLOW:

1. Import APIconnect program locally so that API key is used with calls

2. Create and maintain a 'last transaction log file' which captures the date/time of last transaction and the transaction made

3. Check logfile, if last transaction date > 1 minute, proceed with transaction else terminate program

4. Get current weather function triggered to pull current weather for all selected cities

5. Selected cities are pulled from a city.list.json file that is provided by openweathermap, as they advise.


SIMPLE STARTER CODE

selectedCity = "2648110"
# Define the full URL with connecton key to allow transactions
URL = "http://api.openweathermap.org/data/2.5/weather?id=" + selectedCity + "&APPID=" + APIconnect.URLkey
#URL = "http://api.openweathermap.org/data/2.5/weather?q=London&APPID=" + APIconnect.URLkey


with urllib.request.urlopen(URL) as url:
    data = json.loads(url.read().decode())



print(data.id)


"""


# OPEN FILE
filename = 'weatherReport.json' 


#---------------------------------------------------------------------------------------
#       CHECK LAST TIME REPORT WAS UPDATED
#---------------------------------------------------------------------------------------


# Get the current time 
currentTime = datetime.now()

# Pull the last modified date of the file save as last modified date
try:
    mtime = os.path.getmtime(filename)
except OSError:
    mtime = 0
last_modified_date = datetime.fromtimestamp(mtime)


# Calculate the difference between now and the time it was last modified
difference = currentTime - last_modified_date

print("current time is " + str(currentTime))
print("Last modified date is " + str(last_modified_date))
print("difference between the two are " + str(difference))


# If the difference is under one minute - no need to run again (Also prevents abuse of API)
if(difference.total_seconds() < 60):
    print("No Need to run - job is up to date")
    exit()




#---------------------------------------------------------------------------------------
#       PULL DATA FROM OWM AND WRITE TO REPORT FILE
#---------------------------------------------------------------------------------------



f = open(filename,'w')
selectedCity = ["3333229","2648110", "3333225"] # SELECT CITIES FOR REPORTING
weatherReport = "" # Empty var to store responses
weatherArray = []

allData = ""
for city in range(0, len(selectedCity)):
    
    
    # Define the full URL with connecton key to allow transactions, city changes each iteration
    URL = "http://api.openweathermap.org/data/2.5/weather?id=" + selectedCity[city] + "&APPID=" + APIconnect.URLkey
    with urllib.request.urlopen(URL) as url:
        data = json.loads(url.read().decode())
        print(data)
    weatherArray.append(data)
    
    
    
jsonweatherArray = json.dumps(weatherArray)

f.write(str(jsonweatherArray))
f.close() 
    
    





