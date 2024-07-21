import json
import os
from datetime import datetime

progress_tier_list = [
    1,  # level 1 (1 day needed before revision)
    1,
    1,
    2,
    3,
    5,
    7,
    10,
    15,
    25,
    30
]
time_str_format = '%d/%m/%Y %H:%M:%S'


def record_progress(word, langauge, passed, file_name):
    _create_file_if_not_exists(file_name)

    with open(file_name, 'r+', encoding='utf-8') as file:
        vocabulary = json.load(file)

        if word in vocabulary:
            if langauge in vocabulary[word]:
                if 'level' not in vocabulary[word][langauge]:
                    vocabulary[word][langauge]['level'] = 0

                vocabulary[word][langauge]['last_check_time'] = datetime.now().strftime(time_str_format)
                vocabulary[word][langauge]['level'] += 1 if passed else -1

                if vocabulary[word][langauge]['level'] < 0:
                    vocabulary[word][langauge]['level'] = 0
            else:
                vocabulary[word][langauge] += {
                    'level': 1 if passed else 0,
                    'last_check_time': datetime.now().strftime(time_str_format)
                }
        else:
            vocabulary[word] = {
                langauge: {
                    'level': 1 if passed else 0,
                    'last_check_time': datetime.now().strftime(time_str_format)
                },
            }

        file.seek(0)
        json.dump(vocabulary, file, indent=4)


def is_revision_needed(word, langauge, file_name):
    _create_file_if_not_exists(file_name)

    with open(file_name, 'r', encoding='utf-8') as file:
        vocabulary = json.load(file)

    if word not in vocabulary or \
            langauge not in vocabulary[word] or \
            'last_check_time' not in vocabulary[word][langauge]:
        return True

    last_check_time = datetime.strptime(vocabulary[word][langauge]['last_check_time'], time_str_format)
    level = vocabulary[word][langauge]['level']

    if 'level' not in vocabulary[word][langauge] or level == 0:
        return True

    return (datetime.now() - last_check_time).days >= progress_tier_list[level - 1]


def _create_file_if_not_exists(file_name):
    if not os.path.exists(file_name):
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump({}, file)
