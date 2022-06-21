from rock_paper_scissors import RockPaperScissors


def run():
    """ Rock, Paper, Scissors. """
    run = RockPaperScissors()

    while True:
        print("\nFirst to '3' wins!")

        while True:
            # Requesting user input.
            user_input = run.user_input()
            # Requesting computer input.
            computer_input = run.computer_input()

            # Player round win condition.
            if run.round_win_condition(user_input, computer_input):
                print("\nRound Won!")
                # Add point to player score.
                run.add_player_score()
                # Display scoreboard.
                run.display_scoreboard(user_input, computer_input)

            # Computer round win condition.
            if run.round_win_condition(computer_input, user_input):
                print("\nRound Lost!")
                # Add point to computer score.
                run.add_computer_score()
                # Display scoreboard.
                run.display_scoreboard(user_input, computer_input)

            # Round tie condition.
            if user_input == computer_input:
                print("\nTie!")
                # Display scoreboard.
                run.display_scoreboard(user_input, computer_input)

            # Game win condition.
            if run.game_win_condition() == True:
                # Reset the scores to zero.
                run.reset_score()
                break
            else:
                continue

        # Requesting user input.
        run.restart()

        continue


if __name__ == '__main__':
    run()
