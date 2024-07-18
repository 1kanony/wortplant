def text_to_speech(text, language, rate, engine):
    engine.setProperty('rate', rate)
    engine.setProperty('volume', 0.9)

    voices = engine.getProperty('voices')
    if language == 'de':
        for voice in voices:
            if 'german' in voice.name.lower():
                engine.setProperty('voice', voice.id)
                break
    else:
        for voice in voices:
            if 'english' in voice.name.lower():
                engine.setProperty('voice', voice.id)
                break

    # Convert the text to speech
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()
