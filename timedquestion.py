
import curses
import time
class TimedQuestion:

    def __init__(self, question, time_limit):
        self.question = question
        self.answers = []
        self.time_limit = time_limit

    def add_answer(self, answer, is_correct=False):
        self.answers.append((answer, is_correct))

    def ask_question(self, stdscr):
        # Disable cursor and enable color
        curses.curs_set(0)
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
        # Enable non-blocking input
        stdscr.nodelay(True)
        # Define question and answers
        current_selection = 0

        time_remaining = self.time_limit

        start = time.time()

        while True:
            seconds_elapsed = (time.time() - start)
            time_remaining = int((self.time_limit - seconds_elapsed) * 10) / 10.0
            stdscr.clear()

            # Display the question
            stdscr.addstr(1, 2, self.question, curses.A_BOLD)
            stdscr.addstr(3, 2, f"ANSWER THE QUESTION IN {time_remaining} SECONDS!", curses.color_pair(int(time_remaining*5) % 2))

            # Display the answers
            for idx, answer in enumerate(self.answers):
                if idx == current_selection:
                    stdscr.addstr(5 + idx, 4, answer[0], curses.color_pair(1))
                else:
                    stdscr.addstr(5 + idx, 4, answer[0])

            # Refresh the screen
            stdscr.refresh()

            # Wait for user input
            key = stdscr.getch()

            # Handle user input
            if key == curses.KEY_UP:
                current_selection = (current_selection - 1) % len(self.answers)
            elif key == curses.KEY_DOWN:
                current_selection = (current_selection + 1) % len(self.answers)
            elif key == ord('\n'):  # Enter key
                # Display selected answer and exit
                stdscr.clear()
                stdscr.addstr(1, 2, f"You selected: {self.answers[current_selection][0]}")
                if self.answers[current_selection][1]:
                    stdscr.addstr(3, 2, f"That was right well done!")
                else:
                    stdscr.addstr(3, 2, f"That was wrong! You lose")
                stdscr.refresh()
                stdscr.nodelay(False)
                stdscr.getch()
                break

            if time_remaining < 0:
                stdscr.clear()
                stdscr.addstr(3, 2, "YOU LOSE!")
                stdscr.refresh()
                stdscr.nodelay(False)
                stdscr.getch()
                break



if __name__ == "__main__":
    q = TimedQuestion("What is your favorite programming language?", 10)
    q.add_answer("Python")
    q.add_answer("VBA", True)
    q.add_answer("TS")
    q.add_answer("JS")
    curses.wrapper(q.ask_question)


