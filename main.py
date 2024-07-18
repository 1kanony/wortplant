import speech_recognition as sr
import pyttsx3
import json
from BreakOutOfCycle import BreakOutOfCycle
from check_pronunciation import check_pronunciation
from pronounce import pronounce


def retrieve_words(file_name='translations.json'):
    with open(file_name, 'r', encoding='utf-8') as file:
        vocabulary = json.load(file)

    for german_word, english_translation in vocabulary['Wortschatz'].items():
        yield german_word, english_translation


def check_translation(word, correct_answer, language):
    while True:
        print(f'what is the translation of word \'{word}\' in \'{language}\'?\'')

        answer = input()

        if answer.lower() == 'quit':
            raise BreakOutOfCycle

        if len(answer) != len(correct_answer):
            print('Incorrect!')
            continue

        if answer.lower() == correct_answer.lower():
            print('Correct!')
            break
        else:
            print('Incorrect!')


def cycle(recognizer, engine):
    for german, english in retrieve_words():
        try:
            check_translation(english, german, 'de')
            # check_pronunciation(german, 'de', recognizer, engine)
            pronounce(german, 'de', engine)
        except BreakOutOfCycle:
            break


if __name__ == "__main__":
    cycle(sr.Recognizer(), pyttsx3.init())
