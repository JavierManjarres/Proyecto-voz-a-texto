import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.say("hola como estas, mi nombre es javier manjarrés , y soy tu asistente virtual")
engine.runAndWait()
