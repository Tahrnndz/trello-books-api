# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import json
from decouple import config
API_TOKEN = config('TOKEN')
API_KEY = config('KEY')
DNF_LIST_ID = config('DNF_LIST_ID')
COMPLETED_LIST_ID = config('COMPLETED_LIST_ID')

url = f"https://api.trello.com/1/lists/{DNF_LIST_ID}/cards?key={API_KEY}&token={API_TOKEN}"
headers = {
   "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers
)

json_list = json.loads(response.text)
print()
for i, value in enumerate(json_list):
    name = json_list[i]["name"] 
    print(name)
    description = json_list[i]["desc"].strip().replace('\n',"")
    print(description)

    start_date = description[9:19].strip()
    print("start_date: " + start_date)

    dnf_date = description[description.find('DNF')+4:].strip()
    print("dnf_date: " + dnf_date)

    print()

url = f"https://api.trello.com/1/lists/{COMPLETED_LIST_ID}/cards?key={API_KEY}&token={API_TOKEN}"
headers = {
   "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers
)

json_list = json.loads(response.text)
print('Finished!')
for i, value in enumerate(json_list):
    name = json_list[i]["name"] 
    print(name)
    description = json_list[i]["desc"].strip().replace('\n',"")
    print(description)

    start_date = description[9:19].strip()
    print("start_date: " + start_date)

    completed_date = description[description.find('Com')+11:].strip()
    print("completed_date: " + completed_date)

    print()