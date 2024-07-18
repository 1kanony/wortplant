import speech_recognition as sr
import pyttsx3
import json
from BreakOutOfCycle import BreakOutOfCycle
from check_pronunciation import check_pronunciation
from pronounce import pronounce
from check_spelling import check_spelling
from examples import give_example


def retrieve_words(file_name='translations.json'):
    with open(file_name, 'r', encoding='utf-8') as file:
        vocabulary = json.load(file)

    for german_word, data in vocabulary['Wortschatz'].items():
        yield german_word, data


def cycle(recognizer, engine):
    for german, data in retrieve_words():
        try:
            check_spelling(data['translation'], german, 'de')
            pronounce(german, 'de', engine)
            give_example(data['example'], 'de', 'en', engine)
            # check_pronunciation(german, 'de', recognizer, engine)
        except BreakOutOfCycle:
            break


if __name__ == "__main__":
    cycle(sr.Recognizer(), pyttsx3.init())
