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
            print("\nRock, Paper, Scissors!")
            print("\nRock: Type '1'")
            print("Paper: Type '2'")
            print("Scissors: Type '3'")

            try:
                user_input = int(input("\nEnter: "))
            except ValueError:
                print("\nThat is not a number.")
                continue

            # User input validation conditions.
            choices = [1, 2, 3]
            if user_input not in choices:
                print(f"\n{user_input} is not an valid choice!")
                continue
            elif user_input == 1:
                return "rock"
            elif user_input == 2:
                return "paper"
            elif user_input == 3:
                return "scissors"

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

    def add_player_score(self):
        """Add point to the player score."""
        self.player_score += 1

    def add_computer_score(self):
        """Add point to the computer score."""
        self.computer_score += 1

    def display_scoreboard(self, user_input, computer_input):
        """Display the choice and score."""
        print(f"User: {user_input.title()}")
        print(f"Computer: {computer_input.title()}")
        print(f"{self.player_score} | {self.computer_score}")

    def reset_score(self):
        """Reset player and computer scores to zero."""
        self.player_score = 0
        self.computer_score = 0

    def start_game(self):
        """Starting the rock-paper-scissors game."""
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
                    self.add_player_score()
                    self.display_scoreboard(user_input, computer_input)
                # Computer round win condition.
                elif self.round_win_condition(computer_input, user_input):
                    print("\nRound Lost!")
                    self.add_computer_score()
                    self.display_scoreboard(user_input, computer_input)
                # Round tie condition.
                elif user_input == computer_input:
                    print("\nTie!")
                    self.display_scoreboard(user_input, computer_input)

                # Player game win condition.
                if self.player_score == 3:
                    print("\nWinner!")
                    self.reset_score()
                    break
                # Computer game win condition.
                elif self.computer_score == 3:
                    print("\nYou Lost!")
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
            print("\nPlay Again?")
            print("\nYes: Type '1'")
            print("No: Type '2'")

            try:
                user_input = int(input("\nEnter: "))
            except ValueError:
                print("\nThat is not a number.")
                continue

            # User input validation conditions.
            choices = [1, 2]
            if user_input not in choices:
                print(f"\n{user_input} is not an valid choice!")
                continue
            elif user_input == 1:
                return
            elif user_input == 2:
                quit("\nThank you for playing!")
