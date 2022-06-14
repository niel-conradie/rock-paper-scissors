from rock_paper_scissors import RockPaperScissors


def run():
    """ Rock, Paper, Scissors. """
    run = RockPaperScissors()

    while True:
        # Requesting user input.
        user_input = run.user_input()

        # Requesting computer input.
        computer_input = run.computer_input()

        # Player round win condition.
        if run.round_win_condition(user_input, computer_input):
            print("\nRound Won!")

        # Computer round win condition.
        if run.round_win_condition(computer_input, user_input):
            print("\nRound Lost!")

        # Round tie condition.
        if user_input == computer_input:
            print("\nTie!")

        # Requesting user input.
        run.restart()

        continue


if __name__ == '__main__':
    run()
