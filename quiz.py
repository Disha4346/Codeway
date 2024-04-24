import random

# Define a list of questions with their corresponding answers
questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["A. London", "B. Paris", "C. Rome", "D. Berlin"],
        "answer": "B"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "choices": ["A. Mars", "B. Venus", "C. Jupiter", "D. Saturn"],
        "answer": "C"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "answer": "Harper Lee"
    }
]

def display_question(question):
    print(question["question"])
    if "choices" in question:
        for choice in question["choices"]:
            print(choice)

def evaluate_answer(question, user_answer):
    if "answer" in question:
        return user_answer.lower() == question["answer"].lower()
    return False

def play_quiz():
    score = 0
    total_questions = len(questions)
    
    print("Welcome to the Quiz Game!")
    print("Answer the following questions:")
    print("=============================")
    
    random.shuffle(questions)
    
    for question in questions:
        display_question(question)
        user_answer = input("Your answer: ").strip()
        
        if evaluate_answer(question, user_answer):
            print("Correct!")
            score += 1
        else:
            print("Incorrect! The correct answer is:", question["answer"])
        
        print("-----------------------------")
    
    print("Quiz Completed!")
    print("Your final score is:", score, "out of", total_questions)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        play_quiz()
    elif play_again=="no":
        print("Thank you for playing!")
    else:
        print("Invalid choice")

# Start the quiz
play_quiz()
