from random import randint, choice

OPERATORS = ['+', '-']


def calculate(num_1, math_sign_1, num_2, math_sign_2, num_3):
    result = eval(str(num_1) + math_sign_1 + str(num_2) + math_sign_2 + str(num_3))
    return result


def question_and_answer():
    num_1, num_2, num_3 = randint(10, 20), randint(4, 15), randint(1, 10)
    random_math_sign_1 = choice(OPERATORS)
    random_math_sign_2 = choice(OPERATORS)

    question = f"Вопрос. Какой ответ будет в этом примере?\n" \
               f"{num_1} {random_math_sign_1} {num_2} {random_math_sign_2} {num_3}"
    correct_answer = str(calculate(num_1, random_math_sign_1, num_2, random_math_sign_2, num_3))

    return question, correct_answer
