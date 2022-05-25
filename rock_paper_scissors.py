import random


def win_condition(player_1, player_2):
    """ Return True if player wins. """
    if (player_1 == 'rock' and player_2 == 'scissors') or \
       (player_1 == 'scissors' and player_2 == 'paper') or \
       (player_1 == 'paper' and player_2 == 'rock'):
        return True


def play():
    """ Rock, Paper, Scissors. """
    # Requesting player and computer inputs.
    player_input = input("Rock, Paper, Scissors! ")
    computer_input = random.choice(['rock', 'paper', 'scissors'])

    # Round Won/Lost/Tie conditions.
    if win_condition(player_input, computer_input):
        print("\nRound Won!")
    if win_condition(computer_input, player_input):
        print("\nRound Lost!")
    if player_input == computer_input:
        print("\nTie!")


if __name__ == '__main__':
    play()
