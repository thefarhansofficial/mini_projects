from pytube import YouTube
import pyttsx3

link = "https://youtu.be/k8YiqM0Y-78"
youtube_1 = YouTube(link)
engine = pyttsx3.init()
engine.say(youtube_1.title)



print(youtube_1.title)
print(youtube_1.thumbnail_url)
videos = youtube_1.streams.all()
print("program will give you the list of different stream to download the video")
engine.say(f"Select the video stream in which you want to download: ")
engine.runAndWait()
vid = list(enumerate(videos))
for i in vid:
    print(i)
print()


stream = int(input("enter: "))
videos[stream].download()
engine.say(f"you downloaded the video succesfully")
print('successfully')
engine.runAndWait()
