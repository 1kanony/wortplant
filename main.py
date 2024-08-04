import speech_recognition as sr
import pyttsx3
import json
from Exceptions import BreakOutOfCycle, Reveal
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


def split_word_attrs(word_attrs):
    all_info = word_attrs.split('_')
    word = all_info[0]
    attrs = ', '.join(all_info[1:])

    return word, attrs


def cycle(recognizer, engine):
    spelling_chances = 3
    pronunciation_chances = 10
    progress_file = 'progress.json'
    language = 'de'

    for word_attrs, data in retrieve_words():
        word, attrs = split_word_attrs(word_attrs)

        try:
            if not is_revision_needed(word_attrs, language, progress_file):
                continue

            try:
                check_spelling_passed = check_spelling(word, attrs, data['translation'], language, spelling_chances)
            except Reveal:
                pronounce(data['translation'], language, engine)
                check_spelling_passed = False

            # give_example(data['example'], 'de', 'en', engine)
            check_pronunciation_passed = True or check_pronunciation(  # checking pronunciation using Google Translate
                data['translation'],
                language,
                recognizer,
                engine,
                pronunciation_chances
            )

            record_progress(word_attrs, language, check_spelling_passed and check_pronunciation_passed, progress_file)
        except BreakOutOfCycle:
            break


if __name__ == "__main__":
    cycle(sr.Recognizer(), pyttsx3.init())
