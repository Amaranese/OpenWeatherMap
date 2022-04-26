import os
import json 

 
weatherFile = "weatherReport.json"


json_data=open(weatherFile).read()
data = json.loads(json_data)


print("Pulling Weather Reports")
for x in range(0, len(data)):
	print("Printing Report Number " + str(x) +"\n")
	print("CITY NAME   : " + str(data[x]['name']))
	print("Description : " + str(data[x]['weather'][0]['description']))
	print("Humditity   : " + str(data[x]['main']['humidity']))
	print("pressure    : " + str(data[x]['main']['pressure']))
	print("temp        : " + str(data[x]['main']['temp']))
	print("temp_max    : " + str(data[x]['main']['temp_max']))
	print("temp_min    : " + str(data[x]['main']['temp_min']))
	print("Wind speed  : " + str(data[x]['wind']['speed']))
	print("Wind deg    : " + str(data[x]['wind']['deg']))
	print("Coordinates : " + str(data[x]['coord']['lat']) + ',' + str(data[x]['coord']['lon']))
	print("Visibility  : " + str(data[x]['visibility']))
	print("Country     : " + str(data[x]['sys']['country']))


	print("End of City Report \n")
	

