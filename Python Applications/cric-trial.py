import json, requests, time
from boltiot import Sms, Bolt
import bolt_conf

mybolt = Bolt(bolt_conf.API_KEY, bolt_conf.DEVICE_ID)

base_url = "https://www.cricbuzz.com/api/cricket-match/commentary/"

match = str(input("Enter Match ID: "))

url = base_url + match

while True:

    response = requests.request("GET", url)

    line = json.loads(response.text)
    #print(line)

    batsman_name = str(line['miniscore']['batsmanNonStriker']['batName'])
    batsman_runs = int(line['miniscore']['batsmanNonStriker']['batRuns'])
    

    print(".")
    print(".")

    print("Hi !! "+ batsman_name, " has scored ", batsman_runs, "runs ..")
    
    mybolt.analogWrite(0,"150")
    time.sleep(0.2)
    mybolt.digitalWrite(0,"LOW")
    mybolt.analogWrite(0,"150")
    time.sleep(0.2)
    mybolt.digitalWrite(0,"LOW")

    time.sleep(5)
