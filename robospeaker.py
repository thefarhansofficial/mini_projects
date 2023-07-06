import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker created by FARHAN")
    while True:
        x = input("Enter what you want me to speak: ")
        if x == "e":
            print("you have entered 'e' means you want to end conversation with me THANK YOU !! ")
            break
        engine = pyttsx3.init()
        engine.say(x)
        engine.runAndWait()


