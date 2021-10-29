import json, requests
import time


base_url = "https://www.cricbuzz.com/api/cricket-match/commentary/"

match = str(input("Enter Match ID: "))

url = base_url + match

batsman_six_0 = 0

while True:

    response = requests.request("GET", url)

    line = json.loads(response.text)
    #print(line)
 


    batsman_name = str(line['miniscore']['batsmanStriker']['batName'])

    batsman_six_1 = str(line['miniscore']['batsmanStriker']['batSixes'])


    print(".")
    print(".")


    if batsman_six_1>batsman_six_0:
        
        print("Hi !!"+ batsman_name, " has scored ", batsman_six_1, "sixes ..")
        
        batsman_six_1 = batsman_six_0
    
    time.sleep(3)