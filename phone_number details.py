import phonenumbers
import pyttsx3
from phonenumbers import timezone,geocoder,carrier
number = input("Enter a number that should include (+91): ")
phone_no = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone_no)
cr = carrier.name_for_number(phone_no,"en")
registration = geocoder.description_for_number(phone_no,"en")
engine = pyttsx3.init()
engine.say(f"the timezone of {number} is {time}")
engine.say(f"the carrier of {number} is {cr}")
engine.say(f"the number is registered in {registration}")
print("the given number is",number)
print(f"the timezone of the {number} is ", time)
print(f"the carrier of the {number} is ",cr)
print("the number is registered in", registration)
engine.runAndWait()
print("          THANK YOU             ")






