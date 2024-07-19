import speech_recognition as sr
from text_to_speech import text_to_speech


def check_pronunciation(correct_answer, language, recognizer, engine):
    with sr.Microphone() as source:
        text_to_speech('Please wait. Calibrating microphone...', 'en-Us', 120, engine)
        recognizer.adjust_for_ambient_noise(source, duration=3)
        text_to_speech('Microphone calibrated. Listening...', 'en-Us', 120, engine)

        while True:
            audio_data = recognizer.listen(source, phrase_time_limit=5)
            text_to_speech('Recognizing...', 'en-Us', 120, engine)

            try:
                text = recognizer.recognize_google(audio_data, language=language)
                print(f"You said: {text}")

                if correct_answer.lower() == text.lower():
                    text_to_speech('Correct!', 'en-Us', 120, engine)
                    text_to_speech(correct_answer, language, 120, engine)
                    break
                else:
                    text_to_speech('Incorrect!', 'en-Us', 120, engine)
                    text_to_speech('Correct pronunciation should be', 'en-Us', 120, engine)
                    text_to_speech(correct_answer, language, 90, engine)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
                text_to_speech(correct_answer, language, 90, engine)
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
                text_to_speech(correct_answer, language, 90, engine)
