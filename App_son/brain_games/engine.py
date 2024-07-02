import prompt


def run(game):
    print('Добро пожаловать на фабрику знаний')
    user_name = prompt.string('Как тебя зовут? ')

    print(f'Привет, {user_name}')

    cnt_question = 0
    cnt_answer = 0

    while True:
        (question, correct_answer) = game.question_and_answer()
        print(question)
        cnt_question += 1
        user_answer = prompt.string("Твой ответ: ")

        if user_answer.lower() != 'выход':
            if user_answer == correct_answer:
                print("Правильно!")
                print()
                cnt_answer += 1
            else:
                print(f"'{user_answer}' - это не правильный ответ :-(\n"
                      f"Правильный ответ: {correct_answer}\n"
                      f"Ничего страшного, {user_name}. Ты можешь попробовать ещё раз :-)\n")
        else:
            print(
                f'Количество задач было: {cnt_question}\n'
                f'Количество правильных ответов было: {cnt_answer}\n'
                f'ТЫ МОЛОДЕЦ! ОТЛИЧНЫЙ РЕЗУЛЬТАТ!'
            )

            break
