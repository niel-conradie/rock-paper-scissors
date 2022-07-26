from random import choice


class RockPaperScissors:
    """A class to represent a Rock-Paper-Scissors game."""

    def __init__(self):
        """Initialize class attributes."""
        self.player_score = 0
        self.computer_score = 0

    @staticmethod
    def user_input():
        """Requesting user input and validating choice."""
        while True:
            user_input = input("\nRock, Paper, Scissors! ").lower()
            choices = ["rock", "paper", "scissors"]
            if user_input not in choices:
                print(f"\n{user_input} is not an valid choice!")
                continue
            return user_input

    @staticmethod
    def computer_input():
        """Requesting computer input."""
        choices = ["rock", "paper", "scissors"]
        computer_input = choice(choices)
        return computer_input

    @staticmethod
    def round_win_condition(player_1, player_2):
        """Return True if player wins."""
        if (
            (player_1 == "rock" and player_2 == "scissors")
            or (player_1 == "scissors" and player_2 == "paper")
            or (player_1 == "paper" and player_2 == "rock")
        ):
            return True

    def game_win_condition(self):
        """Return True if player or computer score equals 3."""
        if self.player_score == 3:
            print("\nWinner!")
            return True
        if self.computer_score == 3:
            print("\nYou Lost!")
            return True

    def add_player_score(self):
        """Add point to the player score."""
        self.player_score += 1

    def add_computer_score(self):
        """Add point to the computer score."""
        self.computer_score += 1

    def display_scoreboard(self, user_input, computer_input):
        """Display the choice and score."""
        print(f"User: {user_input.title()}")
        print(f"\nComputer: {computer_input.title()}")
        print(f"\n{self.player_score} | {self.computer_score}")

    def reset_score(self):
        """Reset player and computer scores to zero."""
        self.player_score = 0
        self.computer_score = 0

    def start_game(self):
        """Starting the game."""
        while True:
            print("\nFirst to '3' wins!")

            while True:
                # Requesting user input.
                user_input = self.user_input()
                # Requesting computer input.
                computer_input = self.computer_input()

                # Player round win condition.
                if self.round_win_condition(user_input, computer_input):
                    print("\nRound Won!")
                    # Add point to player score.
                    self.add_player_score()
                    # Display scoreboard.
                    self.display_scoreboard(user_input, computer_input)

                # Computer round win condition.
                if self.round_win_condition(computer_input, user_input):
                    print("\nRound Lost!")
                    # Add point to computer score.
                    self.add_computer_score()
                    # Display scoreboard.
                    self.display_scoreboard(user_input, computer_input)

                # Round tie condition.
                if user_input == computer_input:
                    print("\nTie!")
                    # Display scoreboard.
                    self.display_scoreboard(user_input, computer_input)

                # Game win condition.
                if self.game_win_condition() == True:
                    # Reset the scores to zero.
                    self.reset_score()
                    break
                else:
                    continue

            # Requesting user input.
            self.restart()

            continue

    @staticmethod
    def restart():
        """Requesting user input and validating choice."""
        while True:
            user_input = input("\nRestart? Yes/No: ").lower()
            choices = ["yes", "no"]
            if user_input not in choices:
                print("\nPlease type 'yes' or 'no'")
                continue

            # User input conditions.
            if user_input == "yes":
                return
            if user_input == "no":
                print("\nThank you for playing!")
                quit()
