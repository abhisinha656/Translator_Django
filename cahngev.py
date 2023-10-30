import speech_recognition as sr
from googletrans import Translator, LANGUAGES

def main():
    translator = Translator()
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening... Say something.")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
        input_text = text
        detected_language = translator.detect(input_text).lang
        print(f"Detected Language: {LANGUAGES[detected_language]}")

        target_language = "hi"
        translated_text = translator.translate(input_text, dest=target_language)
        print(f"Translation to {LANGUAGES[target_language]}: {translated_text.text}")
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        print("Request to Google API failed; {0}".format(e))
 

if __name__ == "__main__":
    main()
