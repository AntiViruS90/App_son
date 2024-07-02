from random import choice, randint
import re


def random_russian_letters():
    random_num = randint(1, 10)
    russian_letters = ''.join(chr(letter) for letter in range(1040, 1104) if re.match(r'[А-Яа-я]', chr(letter)))
    result = ''.join([choice(russian_letters) for _ in range(random_num)])

    return result


def question_and_answer():
    letters = random_russian_letters()
    question = f'Напиши такие же буквы как на экране: {letters}'
    correct_answer = letters

    return question, correct_answer

