import speech_recognition as sr



def capture_voice():

    recognizer = sr.Recognizer()


    try:

        with sr.Microphone() as source:

            print(
                "Listening..."
            )


            audio = recognizer.listen(
                source,
                timeout=5
            )


        text = recognizer.recognize_google(
            audio
        )


        return text



    except sr.WaitTimeoutError:

        return "No voice detected"



    except sr.UnknownValueError:

        return "Could not understand speech"



    except Exception as e:

        print(
            "Voice error:",
            e
        )

        return None