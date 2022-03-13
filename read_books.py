# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import json
from decouple import config

import openpyxl, csv
# define filename and file path of source and target files
# source_file = '/Users/Admin/OneDrive/0000.Journals/0000.DailyJournalArchive.txt'
target_file = '/Users/Admin/test.xlsx'

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
    column = i + 1
   #  print(i)
   #  print(column)
    name = json_list[i]["name"] 
   #  print(name)
    description = json_list[i]["desc"].strip().replace('\n',"")
   #  print(description)

    start_date = description[9:19].strip()
   #  print("start_date: " + start_date)

    dnf_date = description[description.find('DNF')+4:].strip()
   #  print("dnf_date: " + dnf_date)

   #  print()

    wb = openpyxl.load_workbook(target_file)
    sheet = wb.active
    name_col = "A"+str(column)
    start_col = "B"+str(column)
    dnf_col = "C"+str(column)
    status_col = "D"+str(column)
    sheet[name_col] = name
    sheet[start_col] = start_date
    sheet[dnf_col] = dnf_date
    sheet[status_col] = "Did Not Finish"
    wb.save(target_file)   

wb.save(target_file)    


url = f"https://api.trello.com/1/lists/{COMPLETED_LIST_ID}/cards?key={API_KEY}&token={API_TOKEN}"
headers = {
   "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers
)
print('Column: ' + str(column))
json_list = json.loads(response.text)
print('Finished!')
for i, value in enumerate(json_list):
    column += 1
    name = json_list[i]["name"] 
   #  print(name)
    description = json_list[i]["desc"].strip().replace('\n',"")
   #  print(description)

    start_date = description[9:19].strip()
   #  print("start_date: " + start_date)

    completed_date = description[description.find('Com')+11:].strip()
   #  print("completed_date: " + completed_date)

   #  print()
    wb = openpyxl.load_workbook(target_file)
    sheet = wb.active
    name_col = "A"+str(column)
    start_col = "B"+str(column)
    completed_col = "C"+str(column)
    status_col = "D"+str(column)
    sheet[name_col] = name
    sheet[start_col] = start_date
    sheet[completed_col] = completed_date
    sheet[status_col] = "Completed"
    wb.save(target_file)   

wb.save(target_file)    