import speech_recognition as sr
import pyttsx3
import json
from BreakOutOfCycle import BreakOutOfCycle
from check_pronunciation import check_pronunciation
from pronounce import pronounce
from check_spelling import check_spelling


def retrieve_words(file_name='translations.json'):
    with open(file_name, 'r', encoding='utf-8') as file:
        vocabulary = json.load(file)

    for german_word, english_translation in vocabulary['Wortschatz'].items():
        yield german_word, english_translation


def cycle(recognizer, engine):
    for german, english in retrieve_words():
        try:
            check_spelling(english, german, 'de')
            # check_pronunciation(german, 'de', recognizer, engine)
            pronounce(german, 'de', engine)
        except BreakOutOfCycle:
            break


if __name__ == "__main__":
    cycle(sr.Recognizer(), pyttsx3.init())
