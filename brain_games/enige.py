import prompt

ROUNDS_COUNT = 3


def run_game(game_module):
    """
    Запускает любую игру.

    Args:
        game_module: модуль игры, содержащий:
            - DESCRIPTION: описание правил
            - generate_question_and_answer(): функция генерации вопроса и ответа
    """
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    print(game_module.DESCRIPTION)

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game_module.generate_question_and_answer()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ").strip()

        if user_answer != str(correct_answer):
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")