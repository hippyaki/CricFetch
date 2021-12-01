import json, requests
import time


base_url = "https://www.cricbuzz.com/api/cricket-match/commentary/"

match = str(input("Enter Match ID: "))

url = base_url + match

batsman_runs_0 = 0

while True:

    response = requests.request("GET", url)

    line = json.loads(response.text)
    #print(line)
 


    batsman_name = str(line['miniscore']['batsmanStriker']['batName'])

    #batsman_six_1 = int(line['miniscore']['batsmanStriker']['batSixes'])

    batsman_runs_1 = int(line['miniscore']['batsmanStriker']['batRuns'])


    print(".")
    
    if batsman_runs_1>batsman_runs_0:
        
        print("Hi !!"+ batsman_name, " has scored ", batsman_runs_1, "runs ..")
        
        batsman_runs_0 = batsman_runs_1
    
    time.sleep(3)
