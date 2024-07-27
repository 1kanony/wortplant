import json
import os
from datetime import datetime, timedelta

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


def record_progress(word_attrs, langauge, passed, file_name):
    _create_file_if_not_exists(file_name)

    with open(file_name, 'r+', encoding='utf-8') as file:
        vocabulary = json.load(file)

        if word_attrs in vocabulary:
            if langauge in vocabulary[word_attrs]:
                if 'level' not in vocabulary[word_attrs][langauge]:
                    vocabulary[word_attrs][langauge]['level'] = 0

                vocabulary[word_attrs][langauge]['last_check_time'] = datetime.now().strftime(time_str_format)
                vocabulary[word_attrs][langauge]['level'] += 1 if passed else -1

                if vocabulary[word_attrs][langauge]['level'] < 0:
                    vocabulary[word_attrs][langauge]['level'] = 0
            else:
                vocabulary[word_attrs][langauge] += {
                    'level': 1 if passed else 0,
                    'last_check_time': datetime.now().strftime(time_str_format)
                }
        else:
            vocabulary[word_attrs] = {
                langauge: {
                    'level': 1 if passed else 0,
                    'last_check_time': datetime.now().strftime(time_str_format)
                },
            }

        file.seek(0)
        json.dump(vocabulary, file, indent=4)


def is_revision_needed(word_attrs, langauge, file_name):
    _create_file_if_not_exists(file_name)

    with open(file_name, 'r', encoding='utf-8') as file:
        vocabulary = json.load(file)

    if word_attrs not in vocabulary or \
            langauge not in vocabulary[word_attrs] or \
            'last_check_time' not in vocabulary[word_attrs][langauge]:
        return True

    last_check_time = datetime.strptime(vocabulary[word_attrs][langauge]['last_check_time'], time_str_format)
    level = vocabulary[word_attrs][langauge]['level']

    if 'level' not in vocabulary[word_attrs][langauge] or level == 0:
        return True

    if len(progress_tier_list) < level:
        return False

    kwargs = {'hour': 0, 'minute': 0, 'second': 0, 'microsecond': 0}

    actual_datetime = datetime.now().replace(**kwargs)
    available_datetime = last_check_time.replace(**kwargs) + timedelta(days=progress_tier_list[level - 1])

    return actual_datetime >= available_datetime


def _create_file_if_not_exists(file_name):
    if not os.path.exists(file_name):
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump({}, file)
