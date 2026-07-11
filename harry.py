#importing the pyttsx3 library to use text-to-speech functionality.
import pyttsx3
engine = pyttsx3.init()
engine.say("Today is a beautiful day")
engine.runAndWait()