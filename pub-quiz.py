import string

alphabet = list(string.ascii_uppercase)

print("Welcome to the Pub Quiz!")

quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "22"],
        "answer": "4"
    },
]

for question in quiz_questions:
    print(question["question"])

    optionsString = ""

    for index, option in enumerate(question["options"]):
        letter = alphabet[index % 26]
        print(f"{letter}) {option}")
        optionsString += f"{letter}, "
    
    user_answer_letter = input(f"Your answer ({optionsString[:-2]}): ").strip().upper()
    
    user_answer_index = alphabet.index(user_answer_letter)

    if question["options"][user_answer_index] == question["answer"]:
        print("Correct!")
    else:
        print(f"Wrong! The correct answer was {question['answer']}.")

print("Thanks for playing the Pub Quiz!")
