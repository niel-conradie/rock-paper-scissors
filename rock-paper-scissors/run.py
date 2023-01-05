from rock_paper_scissors import RockPaperScissors


if __name__ == "__main__":
    run = RockPaperScissors()

    try:
        # Starting the game.
        run.start_game()
    except KeyboardInterrupt:
        # Stopping the game.
        quit("\n\nProgram Terminated")
