from random import randint, choice

OPERATORS = ['+', '-']


def calculate(num_1, math_sign, num_2):
    result = eval(str(num_1) + math_sign + str(num_2))
    return result


def question_and_answer():
    num_1, num_2, = randint(10, 20), randint(4, 15)
    random_math_sign = choice(OPERATORS)

    question = f"Вопрос. Какой ответ будет в этом примере?\n" \
               f"{num_1} {random_math_sign} {num_2}"
    correct_answer = str(calculate(num_1, random_math_sign, num_2,))

    return question, correct_answer
