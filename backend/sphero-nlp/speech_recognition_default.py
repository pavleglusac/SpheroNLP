import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Recite nešto...")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio, language="sr-RS")
    print("Prepoznat tekst: " + text)

except sr.UnknownValueError:
    print("Govor nije prepoznat")

except sr.RequestError as e:
    print("Greška pri obradi zahtjeva: {0}".format(e))
