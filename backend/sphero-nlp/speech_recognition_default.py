import speech_recognition as sr
from translator.translators import ChatGPTTranslator, MockTranslator
from language import Language, parser

text_translator = ChatGPTTranslator()
recognizer = sr.Recognizer()

def execute_code(code_model):
    try:
        exec(code_model.to_python())
    except Exception as e:
        print(e)
        return str(e)
    return "Success"


with sr.Microphone() as source:
    print("Recite nešto...")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio, language="sr-RS")
    code = text_translator.translate(text)
    print(code)
    code_model = parser.parse(code)
    print("*"*50)
    print(code_model)
    print("*"*50)
    print(code_model.to_python())
    execute_code(code_model)
    print("Prepoznat tekst: " + text)

except sr.UnknownValueError:
    print("Govor nije prepoznat")

except sr.RequestError as e:
    print("Greška pri obradi zahtjeva: {0}".format(e))
