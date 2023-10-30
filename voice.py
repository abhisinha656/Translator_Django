import speech_recognition as sr

def main():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening... Say something.")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        print("Request to Google API failed; {0}".format(e))

if __name__ == "__main__":
    main()
