from Exceptions import BreakOutOfCycle, Reveal


def check_spelling(word, attrs, correct_answer, language, chances):
    tries = 0

    while True:
        tries += 1

        _ask_word(word, attrs, language)

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


def _ask_word(word, attrs, language):
    print(f'what is the translation of word \'{word}'
          f'{' (' + attrs + ')' if attrs else ''}\' in \'{language}\'?\'')
