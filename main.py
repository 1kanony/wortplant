import speech_recognition as sr
import pyttsx3
import json
from BreakOutOfCycle import BreakOutOfCycle
from check_pronunciation import check_pronunciation
from pronounce import pronounce
from check_spelling import check_spelling
from examples import give_example
from progress import record_progress, is_revision_needed


def retrieve_words(file_name='translations.json'):
    with open(file_name, 'r', encoding='utf-8') as file:
        vocabulary = json.load(file)

    for german_word, data in vocabulary['Wortschatz'].items():
        yield german_word, data


def cycle(recognizer, engine):
    spelling_chances = 3
    pronunciation_chances = 10
    progress_file = 'progress.json'
    language = 'de'

    for word, data in retrieve_words():
        try:
            if not is_revision_needed(word, language, progress_file):
                continue

            check_spelling_passed = check_spelling(word, data['translation'], language, spelling_chances)
            # pronounce(data['translation'], language, engine)
            # # give_example(data['example'], 'de', 'en', engine)
            check_pronunciation_passed = check_pronunciation(
                data['translation'],
                language,
                recognizer,
                engine,
                pronunciation_chances
            )

            record_progress(word, language, check_spelling_passed and check_pronunciation_passed, progress_file)
        except BreakOutOfCycle:
            break


if __name__ == "__main__":
    cycle(sr.Recognizer(), pyttsx3.init())
