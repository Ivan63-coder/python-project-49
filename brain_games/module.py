from .cli import welcome_user


def game_run(game_question, get_question_and_answer):
    name = welcome_user()
    print(game_question)
    
    for _ in range(3):
        question, correct_answer = get_question_and_answer()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip().lower()
        if user_answer == str(correct_answer):
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
