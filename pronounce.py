from BreakOutOfCycle import BreakOutOfCycle
from text_to_speech import text_to_speech


def pronounce(text, language, engine):
    # Pronounce as much as user feels needing

    text_to_speech(text, language, 100, engine)

    while True:
        print('Would you like to listen [a]gain or it is [e]nough?')

        answer = input().lower()

        if answer == 'quit':
            raise BreakOutOfCycle

        if answer in ['enough', 'e']:
            break

        if answer in ['again', 'a']:
            text_to_speech(text, language, 100, engine)