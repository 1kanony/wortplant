from Exceptions import BreakOutOfCycle, Reveal
import random


def check_spelling(word, attrs, correct_answer, language, chances):
    tries = 0

    correct_answer, text = _ask_word(word, attrs, correct_answer, language)

    while True:
        tries += 1

        print(text)

        answer = input().lower()

        if answer == 'quit':
            raise BreakOutOfCycle

        if answer in ['reveal', 'r']:
            print(f'The correct answer is \'{correct_answer}\'')
            raise Reveal

        if len(answer) != len(correct_answer):
            print('Incorrect!')
            print('Type [r]eveal to show answer')
            continue

        if answer == correct_answer.lower():
            print('Correct!')
            break
        else:
            print('Incorrect!')

    return tries <= chances


def _ask_word(word, attrs, correct_answer, language):
    en_lang = word
    en_lang_with_attrs = f'{en_lang}{' (' + attrs + ')' if attrs else ''}'
    other_lang = correct_answer

    if random.choice([True, False]):
        text = f'what is the translation of word \'{en_lang_with_attrs}\' in \'{language}\'?\''
    else:
        text = f'what is the translation of word \'{other_lang}\' in \'en\'?\''
        correct_answer = en_lang

    return correct_answer, text
