from BreakOutOfCycle import BreakOutOfCycle


def check_spelling(word, correct_answer, language, chances):
    tries = 0

    while True:
        tries += 1

        print(f'what is the translation of word \'{word}\' in \'{language}\'?\'')

        answer = input().lower()

        if answer == 'quit':
            raise BreakOutOfCycle

        if answer in ['reveal', 'r']:
            print(f'The correct answer is \'{correct_answer}\'')
            tries = chances + 1
            break

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
