import os
import json 

cityFile = "city.list.json"
json_data=open(cityFile).read()

data = json.loads(json_data)
print(data)