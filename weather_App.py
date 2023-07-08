import requests  #this  module helps to access the data from other sites
import json   #converts string output to a dictionary
import pyttsx3

CITY = input("Enter the name of the city\n")

URl = f"https://api.weatherapi.com/v1/current.json?key=604c51a9d5f24b50b6981510230807&q={CITY}"

r = requests.get(URl)
print(r.text)
Wdic = json.loads(r.text)
rdic = json.loads(r.text)
lUdic = json.loads(r.text)

if __name__ == '__main__':
    print("Welcome to RoboSpeaker created by FARHAN")
    print("The RoboSpeaker will give an update about the CITY you and the region where the CITY Entered lies ")
    w = Wdic["current"]["temp_c"]
    region = rdic["location"]["region"]
    last_updated = lUdic["current"]["last_updated"]
    print("TEMPERATURE", Wdic["current"]["temp_c"])
    print("STATE", rdic["location"]["region"])
    print("LAST_UPDATED_INFO", lUdic["current"]["last_updated"])
    engine = pyttsx3.init()
    engine.say(f"The current temperature in {CITY} is {w} Degrees")
    engine.say(f"The {CITY} lies is in the state of {region} ")
    engine.say(f"THE information about temperature of {CITY} was last updated at {last_updated}")
    engine.runAndWait()

    print("      THANK YOU        ")

