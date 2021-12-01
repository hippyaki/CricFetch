from boltiot import Bolt
import bolt_conf
import json, requests, time

mybolt = Bolt(bolt_conf.API_KEY, bolt_conf.DEVICE_ID)

base_url = "https://www.cricbuzz.com/api/cricket-match/commentary/"

match = str(input("Enter Match ID: "))

url = base_url + match

batsman_six_0 = 0
batsman_four_0 = 0


def six():
    mybolt.analogWrite(0,"150")
    time.sleep(0.3)
    mybolt.digitalWrite(0,"LOW")
    mybolt.analogWrite(0,"150")
    time.sleep(0.3)
    mybolt.digitalWrite(0,"LOW")
    mybolt.analogWrite(0,"150")
    time.sleep(0.3)
    mybolt.digitalWrite(0,"LOW")

def four():
    mybolt.analogWrite(0,"150")
    time.sleep(0.3)
    mybolt.digitalWrite(0,"LOW")
    mybolt.analogWrite(0,"150")
    time.sleep(0.3)
    mybolt.digitalWrite(0,"LOW")

while True:

    response = requests.request("GET", url)

    line = json.loads(response.text)
    #print(line)

    batsman_name = str(line['miniscore']['batsmanStriker']['batName'])
    batsman_six_1 = int(line['miniscore']['batsmanStriker']['batSixes'])
    batsman_four_1 =int(line['miniscore']['batsmanStriker']['batFours'])

    print(".")
    print(".") 

    if batsman_six_1>batsman_six_0:
        
        print("Another Six !!")
        
        six()
        
        print(".")
        print("Hi !!"+ batsman_name, " has scored ", batsman_six_1, "sixes ..")
        
        batsman_six_0 = batsman_six_1


    if batsman_four_1>batsman_four_0:

        print("Another Four !!")
        
        four()

        print(".") 
        print("Hi !!"+ batsman_name, " has scored ", batsman_four_1, "fours ..")
        
        batsman_four_0 = batsman_four_1

    
    time.sleep(3)
