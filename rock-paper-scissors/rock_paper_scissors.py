import random


class RockPaperScissors:
    """ A class to represent a Rock-Paper-Scissors game. """

    def __init__(self):
        """ Initialize class attributes. """
        self.player_score = 0
        self.computer_score = 0

    @staticmethod
    def user_input():
        """ Requesting user input and validating choice. """
        while True:
            user_input = input("\nRock, Paper, Scissors! ").lower()
            choices = ['rock', 'paper', 'scissors']
            if user_input not in choices:
                print(f"\n{user_input} is not an valid choice!")
                continue
            return user_input

    @staticmethod
    def computer_input():
        """ Requesting computer input. """
        choices = ['rock', 'paper', 'scissors']
        computer_input = random.choice(choices)
        return computer_input

    @staticmethod
    def round_win_condition(player_1, player_2):
        """ Return True if player wins. """
        if (player_1 == 'rock' and player_2 == 'scissors') or \
           (player_1 == 'scissors' and player_2 == 'paper') or \
           (player_1 == 'paper' and player_2 == 'rock'):
            return True

    def add_player_score(self):
        """ Add point to the player score. """
        self.player_score += 1

    def add_computer_score(self):
        """ Add point to the computer score. """
        self.computer_score += 1

    def display_scoreboard(self, user_input, computer_input):
        """ Display the choice and score. """
        print(f"User: {user_input.title()}"
              f"Computer: {computer_input.title()}"
              f"{self.player_score} | {self.computer_score}")

    @staticmethod
    def restart():
        """ Requesting user input and validating choice. """
        while True:
            user_input = input("\nRestart? Yes/No: ").lower()
            choices = ['yes', 'no']
            if user_input not in choices:
                print("\nPlease type 'yes' or 'no'")
                continue

            # User input conditions.
            if user_input == 'yes':
                return
            if user_input == 'no':
                print("\nThank you for playing!")
                quit()
