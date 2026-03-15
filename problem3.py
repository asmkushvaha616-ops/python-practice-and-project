# install an external module and use it to perform an operation of your interest
# install a module pyttsx3(use for convert text to voice)
import pyttsx3
engine=pyttsx3.init()
engine.say('hey everyone! i want to say something about Ashmi')
engine.say('ashmi is a  self motivated girl')
engine.runAndWait()