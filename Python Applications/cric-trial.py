import json, requests, time
from boltiot import Sms, Bolt
import bolt_conf


mybolt = Bolt(bolt_conf.API_KEY, bolt_conf.DEVICE_ID)

base_url = "https://www.cricbuzz.com/api/cricket-match/commentary/"

match = str(input("Enter Match ID: "))

url = base_url + match

batsman_six_0 = 0
batsman_four_0 = 0

while True:

    response = requests.request("GET", url)

    line = json.loads(response.text)
    #print(line)

    batsman_name = str(line['miniscore']['batsmanNonStriker']['batName'])
    batsman_six_1 = str(line['miniscore']['batsmanNonStriker']['batSixes'])
    batsman_four_1 = str(line['miniscore']['batsmanNonStriker']['batFours'])


    print(".")
    print(".")

    print("Hi !!"+ batsman_name, " has scored ", batsman_six_1, "sixes ..")
    print(".")
    print(".")
    print("Hi !!"+ batsman_name, " has scored ", batsman_four_1, "fours ..")
    mybolt.analogWrite(0,"150")
    time.sleep(0.2)
    mybolt.digitalWrite(0,"LOW")
    mybolt.analogWrite(0,"150")
    time.sleep(0.2)
    mybolt.digitalWrite(0,"LOW")

    time.sleep(5)