print("Welcome to the Pub Quiz!")

quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) London", "B) Paris", "C) Berlin", "D) Madrid"],
        "answer": "B"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["A) 3", "B) 4", "C) 5", "D) 22"],
        "answer": "B"
    },
]

for question in quiz_questions:
    print(question["question"])
    for option in question["options"]:
        print(option)
    
    user_answer = input("Your answer (A, B, C, D): ").strip().upper() # Ensuring the input is uppercase for comparison
    
    if user_answer == question["answer"]:
        print("Correct!")
    else:
        print(f"Wrong! The correct answer was {question['answer']}.")

print("Thanks for playing the Pub Quiz!")
