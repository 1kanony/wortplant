from text_to_speech import text_to_speech


def give_example(example, learning_language, known_language, engine):
    if not example:
        return

    text_to_speech('For example', known_language, 120, engine)
    text_to_speech(example[known_language], known_language, 120, engine)

    text_to_speech(example[learning_language], learning_language, 120, engine)
