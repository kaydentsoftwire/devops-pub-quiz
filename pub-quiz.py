import curses
import time

# List of questions, options, and answers
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Berlin", "Madrid"],
        "answer_index": 1,
        "results": [],
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "22"],
        "answer_index": 1,
        "time_limit": 10,
        "results": [],
    },
    {
        "question": "What is your favourite colour?",
        "options": ["A) blu", "B) yello", "C) purpl", "D) grey" ],
        "answer_index": "",
        "results": ["exists"],
    }
    # Learners can add more questions here following the same structure
]

# # Loop through each question
# for question in quiz_questions:
#     # Display the question and options
#     print(question["question"])
#     for option in question["options"]:
#         print(option)
    
#     # Get the user's answer
#     user_answer = input("Your answer (A, B, C, D): ").strip().upper() # Ensuring the input is uppercase for comparison
    
#     # Check if the answer is correct
#     if question["answer"] != "" and user_answer == question["answer"]:
#         print("Correct!")
#         print(" _ ")
#         print("|n|")
#         print("| |____")
#         print("|  l___|")
#         print("|  l___|")
#         print("|__l___|")
#         print("")
#     elif question["results"] != []:
#         print(f"{'\033[96m'}Wrong. This is your favourite colour{'\033[0m'}")

#     else:
#         print(f"Wrong! The correct answer was {question['answer']}.")

def init_curses(stdscr):
    # Disable cursor and enable color
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_CYAN)
    # Enable non-blocking input
    stdscr.nodelay(True)


def main(stdscr):
    init_curses(stdscr)

    stdscr.addstr(1, 2, "Welcome to the Pub Quiz!")

    stdscr.addstr(3, 4, "Press any key to continue...")
    stdscr.nodelay(False)
    stdscr.getkey()
    stdscr.clear()
    stdscr.refresh()

    stdscr.nodelay(True)

    # Loop through each question
    for question in quiz_questions:
        start = time.time()
        current_selection = 0
        while True:
            stdscr.nodelay(True)
            stdscr.clear()
            stdscr.addstr(1, 2, question["question"], curses.A_BOLD)

            if "time_limit" in question:
                seconds_elapsed = time.time() - start
                time_remaining = (
                    int((int(question["time_limit"]) - seconds_elapsed) * 10) / 10.0
                )
                stdscr.addstr(
                    3,
                    2,
                    f"ANSWER THE QUESTION IN {time_remaining} SECONDS!",
                    curses.color_pair(int(time_remaining * 5) % 2),
                )

            # Display the answers
            for idx, answer in enumerate(question["options"]):
                if idx == current_selection:
                    stdscr.addstr(5 + idx, 4, answer, curses.color_pair(1))
                else:
                    stdscr.addstr(5 + idx, 4, answer)

            # Refresh the screen
            stdscr.refresh()

            # Wait for user input
            key = stdscr.getch()

            # Handle user input
            if key == curses.KEY_UP:
                current_selection = (current_selection - 1) % len(question["options"])
            elif key == curses.KEY_DOWN:
                current_selection = (current_selection + 1) % len(question["options"])
            elif key == ord("\n"):  # Enter key
                # Display selected answer and exit
                stdscr.clear()
                stdscr.addstr(
                    1, 2, f"You selected: {question['options'][current_selection]}"
                )
                if question["answer_index"] != "" and current_selection == question["answer_index"]:
                    stdscr.addstr(3, 2, "That was right well done!")
                    stdscr.addstr(5, 2, " _ ")
                    stdscr.addstr(6, 2, "|n|")
                    stdscr.addstr(7, 2, "| |____")
                    stdscr.addstr(8, 2, "|  l___|")
                    stdscr.addstr(9, 2, "|  l___|")
                    stdscr.addstr(10, 2, "|__l___|")
                    stdscr.addstr(11, 2, "")
                elif question["results"] != []:
                    stdscr.addstr(3, 2, "Wrong. This is your favourite colour", curses.color_pair(3))    
                else:
                    stdscr.addstr(3, 2, "That was wrong! You lose")
                stdscr.refresh()
                stdscr.nodelay(False)
                stdscr.getch()
                break

            if "time_limit" in question and time_remaining < 0:
                stdscr.clear()
                stdscr.addstr(3, 2, "YOU LOSE!")
                stdscr.refresh()
                stdscr.nodelay(False)
                stdscr.getch()
                break

        # Goodbye message
        print("Thanks for playing the Pub Quiz!")


if __name__ == "__main__":
    curses.wrapper(main)
