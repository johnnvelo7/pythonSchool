quiz_questions = [
    "What is the capital of Norway?",
    "What is the currency of Norway?",
    "What is the largest city in Norway?",
    "When is constitution day (the national day) of Norway?",
    "What color is the background of the Norwegian flag?",
    "How many countries does Norway border?",
    "What is the name of the university in Trondheim?",
    "How long is the border between Norway and Russia?",
    "Where in Norway is Stavanger?",
    "From which Norwegian city did the world’s famous composer Edvard Grieg come?",
]
quiz_answers = [
    ["Oslo", "Bergen", "Trondheim", "Stavanger"],
    ["Euro", "Pound", "Krone", "Deutsche Mark"],
    ["Oslo", "Stavanger", "Bergen", "Trondheim"],
    ["27th May", "17th May", "17th April", "27th April"],
    ["Red", "White", "Blue", "Yellow"],
    ["1", "2", "3", "4"],
    ["UiS", "UiO", "NMBU", "NTNU"],
    ["96km", "196km", "296km", "396km"],
    ["North", "South", "South-West", "South-East"],
    ["Oslo", "Bergen", "Stavanger", "Tromsø"]
]
correct_answers = [
    "Oslo",
    "Krone",
    "Oslo",
    "17th May",
    "Red",
    "3",
    "NTNU",
    "196km",
    "South-West",
    "Bergen"
]

login_info_dict = {'PGR107': 'Python'}

# LOGIN FUNCTION
def Login_info():
    while True:
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        if username in login_info_dict and login_info_dict[username] == password:
            print("Login successful!")
            break
        else:
            print("Invalid username and/or password. Please try again.")

# QUIZ FUNCTION
def Quiz():
    num_correct_answers = 0
    num_wrong_answers = 0
    user_answers = []

    for question_number, question in enumerate(quiz_questions):
        print(f"Question {question_number + 1}: {question}")
        for i, answer in enumerate(quiz_answers[question_number]):
            print(f"{i + 1}. {answer}")

        while True:
            user_answer = input("Enter your answer (1-4): ")
            if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
                user_answer = int(user_answer)
                break
            else:
                print("Please enter a valid answer (1-4).")

        user_answers.append(user_answer)

        if quiz_answers[question_number][user_answer - 1] == correct_answers[question_number]:
            print("Correct!\n")
            num_correct_answers += 1
        else:
            print("Wrong!\n")
            num_wrong_answers += 1

    print(
        f"Quiz completed! You answered {num_correct_answers} questions correctly and {num_wrong_answers} questions incorrectly.\n")

    if num_wrong_answers > 0:
        print("Here are the correct answers for the questions you got wrong:")
        for question_number, question in enumerate(quiz_questions):
            if quiz_answers[question_number][int(user_answers[question_number]) - 1] != correct_answers[question_number]:
                print(f"\nQuestion: {question}")
                print(f"Your answer: {quiz_answers[question_number][int(user_answers[question_number]) - 1]}")
                print(f"Correct answer: {correct_answers[question_number]}")

# main code
print("Hello, let's test your knowledge about Norway. Good luck!")
Login_info()
Quiz()
