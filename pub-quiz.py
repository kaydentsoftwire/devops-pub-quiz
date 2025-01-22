# Welcome message for the quiz
print("Welcome to the Pub Quiz!")

# List of questions, options, and answers
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Berlin", "Madrid"],
        "answer": "B"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "22"],
        "answer": "B"
    },
    # Learners can add more questions here following the same structure
]

# Loop through each question
for question in quiz_questions:
    # Display the question and options
    print(question["question"])
    for index, option in enumerate(question["options"]):
        print(chr(ord('A') + index), ':', option)

    # Get the user's answer
    user_answer = (
        input("Your answer (A, B, C, D): ").strip().upper()
    )  # Ensuring the input is uppercase for comparison

    # Check if the answer is correct
    if user_answer == question["answer"]:
        print("Correct!")
        print(" _ ")
        print("|n|")
        print("| |____")
        print("|  l___|")
        print("|  l___|")
        print("|__l___|")
        print("")
    else:
        print(f"Wrong! The correct answer was {question['answer']}.")

# Goodbye message
print("Thanks for playing the Pub Quiz!")
