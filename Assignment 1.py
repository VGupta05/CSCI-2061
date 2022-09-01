# Vardaan Gupta
# The game is called Rock-Paper-Scissors-Lizard-Spock.
# There are many different ways to win in this game as well as lose.
# You will enter a choice and play your odds to win.

import random
from time import sleep
global replay

# Each key represented by a move is storing a list of dictionaries which has the title of move it is beating and a action associated with it in the win statement.
choice = {
    "Rock": [
        {"title": "Paper", "action": "cuts"},
        {"title": "Lizards", "action": "decapitates"}],
    "Paper": [
        {"title": "Rock", "action": "covers"},
        {"title": "Spock", "action": "disproves"}],
    "Scissors": [
        {"title": "Lizard", "aciton": "crushes"},
        {"title": "Scissors", "action": "crushes"}],
    "Lizard": [
        {"title": "Spock", "action": "poisons"},
        {"title": "Paper", "action": "eats"}],
    "Spock": [
        {"title": "Scissors", "action": "smashes"},
        {"title": "Rock", "action": "vaporizes"}]
}

possible_choice = ["r", "p", "c", "l", "s"]
possible_rock_choice = ["r", "R", "rock", "Rock", "ROCK"]
possible_paper_choice = ["p", "P", "paper", "Paper", "PAPER"]
possible_scissors_choice = ["c", "C", "scissors" "Scissors", "SCISSORS"]
possible_lizard_choice = ["l", "L", "lizard", "Lizard", "LIZARD"]
possible_spock_choice = ["s", "S", "spock", "Spock", "SPOCK"]

replay = True

def letter_to_word(choice): # Used to turn letter inputs into full words
    if choice in possible_rock_choices:
        return "Rock" # beats Scissors and Lizard
    if choice in possible_paper_choices:
        return "Paper" # beats Rock and Spock
    if choice in possible_scissors_choices:
        return "Scissors" # beats Paper and Lizard
    if choice in possible_lizard_choices:
        return "Lizard" # beats Paper and Spock
    if choice in possible_spock_choices:
        return "Spock" # beats Scissors and Rock

def choice_check(user_choice, cpu_choice):
    # Determining that the user's choice and CPU's choice were the same
    if user_choice == cpu_choice:
        return None, ""
    # Determining that the user won
    for player in choice[user_choice]:
        if cpu_choice is player["title"]:
            return True, player["action"]
    # Determining that the CPU won
    for player in choice[cpu_choice]:
        if user_choice is player["title"]:
            return False, player["action"]

# If the user inputted an invalid input, print this
def input_choice():
    # Random cpu choice
    cpu_choice = random.choice(possible_choice)
    # User based input choice
    user_choice = input("Enter a choice (rock [r], paper [p], scissors [c], lizard [l], spock [s]): ")
    if user_choice not in choice:
        print("Invalid input. Please enter a valid input.")
        input_choice()
    return letter_to_word(user_choice), letter_to_word(cpu_choice)

# Returns True or False whether or not the game should continue
def ask_replay():
    replay_choice = input("Would you like to play again? Y/N: ")
    accepted_yes_list = ["y", "Y", "yes", "Yes", "YES"]
    accepted_no_list = ["n", "N", "no", "No", "NO"]
    if replay_choice in accepted_yes_list:
        replay = True
    elif replay_choice in accepted_no_list:
        replay = False
    else:
        print("Please enter Y/N")
        ask_replay()

def start_game():
    while replay is True:
        user_choice, cpu_choice = input_choice()
        print(f"You chose {user_choice}")
        # Adds delay so not instant winner reveal
        i = 0
        while i < 5:
            sleep(1/4)
            print(".")
            i += 1
        print(f"Computer chose {cpu_choice}")
        won, action = choice_check(user_choice, cpu_choice)
        if won is None:
            print("You tied. Play again!")
            start_game()
        if won is True:
            print(f"{user_choice} {action} {cpu_choice}")
            print("You won. Congrats!")
            ask_replay()
        if won is False:
            print(f"{cpu_choice} {action} {user_choice}")
            print("You lost. Try again!")
            ask_replay()
    print("Thanks for playing. Come back soon.")

start_game()
