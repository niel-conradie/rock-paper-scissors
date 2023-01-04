from sys import exit

from rock_paper_scissors import RockPaperScissors


def run():
    """Rock, Paper, Scissors."""
    run = RockPaperScissors()

    try:
        # Starting the game.
        run.start_game()
    except KeyboardInterrupt:
        # Stopping the game.
        exit("\n\nProgram Terminated")


if __name__ == "__main__":
    run()
