from BreakOutOfCycle import BreakOutOfCycle


def check_spelling(word, correct_answer, language):
    while True:
        print(f'what is the translation of word \'{word}\' in \'{language}\'?\'')

        answer = input().lower()

        if answer == 'quit':
            raise BreakOutOfCycle

        if answer in ['reveal', 'r']:
            print(f'The correct answer is \'{correct_answer}\'')
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

'''
    book
    movie
    love
    intellect
    intelligent
    courage
    pride
    answer
    empire
    king
    emperor
    need
    charisma
    muscle
    emotion
    luxury
    age
    cold-blooded
    human
    animal
    trust
    game
    feeling
    puzzle
    country
    gold
    power
    black
    white
    dog
    hate



Book - Buch

Ich lese ein interessantes Buch. (I am reading an interesting book.)
Movie - Film

Wir sehen heute Abend einen Film. (We are watching a movie tonight.)
Love - Liebe

Liebe ist das schönste Gefühl. (Love is the most beautiful feeling.)
Intellect - Intellekt

Sein Intellekt ist beeindruckend. (His intellect is impressive.)
Intelligent - Intelligent

Sie ist eine sehr intelligente Schülerin. (She is a very intelligent student.)
Courage - Mut

Er zeigte großen Mut in der Gefahr. (He showed great courage in danger.)
Pride - Stolz

Sie erfüllt ihre Arbeit mit Stolz. (She does her work with pride.)
Answer - Antwort

Kannst du mir die Antwort geben? (Can you give me the answer?)
Empire - Reich

Das Römische Reich war mächtig. (The Roman Empire was powerful.)
King - König

Der König regierte gerecht. (The king ruled justly.)
Emperor - Kaiser

Der Kaiser besuchte die Stadt. (The emperor visited the city.)
Need - Bedürfnis

Wir haben das Bedürfnis nach Ruhe. (We have a need for peace.)
Charisma - Charisma

Ihr Charisma zieht alle an. (Her charisma attracts everyone.)
Muscle - Muskel

Er trainiert seine Muskeln im Fitnessstudio. (He trains his muscles at the gym.)
Emotion - Emotion

Ihre Emotionen sind schwer zu kontrollieren. (Her emotions are hard to control.)
Luxury - Luxus

Sie lebt in großem Luxus. (She lives in great luxury.)
Age - Alter

Mit dem Alter kommt die Weisheit. (With age comes wisdom.)
Cold-blooded - Kaltblütig

Der Mörder war kaltblütig. (The murderer was cold-blooded.)
Human - Mensch

Der Mensch ist ein soziales Wesen. (The human is a social being.)
Animal - Tier

Im Zoo gibt es viele verschiedene Tiere. (There are many different animals in the zoo.)
Trust - Vertrauen

Vertrauen ist die Basis jeder Beziehung. (Trust is the basis of every relationship.)
Game - Spiel

Lass uns ein Spiel spielen. (Let's play a game.)
Feeling - Gefühl

Ich habe ein gutes Gefühl dabei. (I have a good feeling about it.)
Puzzle - Puzzle

Das Puzzle hat tausend Teile. (The puzzle has a thousand pieces.)
Country - Land

Deutschland ist ein schönes Land. (Germany is a beautiful country.)
Gold - Gold

Das Medaillon ist aus purem Gold. (The medallion is made of pure gold.)
Power - Macht

Der Präsident hat viel Macht. (The president has a lot of power.)
Black - Schwarz

Er trägt immer schwarze Kleidung. (He always wears black clothes.)
White - Weiß

Das Kleid ist schneeweiß. (The dress is snow white.)
Dog - Hund

Der Hund spielt im Garten. (The dog is playing in the garden.)
Hate - Hass

Hass zerstört Beziehungen. (Hate destroys relationships.)

'''

