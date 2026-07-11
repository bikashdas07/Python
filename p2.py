# importing the pyttsx3 library to use text-to-speech functionality.
import pyttsx3
engine = pyttsx3.init()
engine.say("Hello, I am Harry, your personal assistant. How can I help you today?")
engine.runAndWait()
