import random

def generate_choice():
    choices = ["rock", "paper", "scissor"]
    computer_choice = random.choice(choices)
    print("Computer chose " + computer_choice)
    return computer_choice


def Take_user_input():
    return input("Enter your choice (rock, paper,scissor): ")


def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie"
    elif (
            (player_choice == "rock" and computer_choice == "scissor") or
            (player_choice == "paper" and computer_choice == "rock") or
            (player_choice == "scissor" and computer_choice == "paper")
    ):
        return "You Won"
    else:
        return "Computer Won"


def get_user_choice():
    while True:
        choices = ["rock", "paper", "scissor"]
        choice_input = Take_user_input()

        if choice_input in choices:
            return choice_input
        else:
            print("Invalid , try again.")


def rps_game():
    print("Welcome to the Game")
    player_choice = get_user_choice()
    computer_choice = generate_choice()
    winner = get_winner(player_choice, computer_choice)
    print(winner)

rps_game()