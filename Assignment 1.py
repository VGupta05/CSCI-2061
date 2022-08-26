# Vardaan Gupta
# The game is called Rock-Paper-Scissors-Lizard-Spock.
# There are many different ways to win in this game as well as lose.
# You will enter a choice and play your odds to win.

import random

def start_game():
    print("The game is called Rock-Paper-Scissors-Lizard-Spock.")
    print("There are many different ways to win in this game as well as lose.")
    print("You will enter a choice and play your odds to win.")
    user_choice = input("Enter a choice (rock [r], paper [p], scissors [s], lizard [l], spock [S]): ") # User based input choice
    possible_choices = ['r', 'p', 's', 'l', 'S']
    if user_choice not in possible_choices:
        print("invalid input") # If the user inputted an invalid input, print this
        start_game()
    cpu_choice = get_computer_choice(possible_choices) # Based off get_computer_choice's random choice from the possible_choices list

    print(f"CPU chose {letter_to_word(cpu_choice)}") # What the CPU chose
    print(f"You chose {letter_to_word(user_choice)}") # What the user chose

    if run_game_logic(user_choice, cpu_choice): # run_game_logic defined below to determine who won via the dictionary
        cpu_word = letter_to_word(cpu_choice) # Writes out the CPU choice in full word
        player_word = letter_to_word(user_choice) # Writes out the user's choice in full word
        print(f"You win! {player_word} beats {cpu_word}")
    else:
        cpu_word = letter_to_word(cpu_choice)
        player_word = letter_to_word(user_choice)
        print(f"You Lost! {cpu_word} beats {player_word}")
    retry = input("Would you like to play again? y for yes, n for no ") == "y"
    while retry == True:
        start_game()
    else:
        print("Thanks for playing!")
        exit()

def get_computer_choice(possible_choices):
    computer_choice = random.choice(possible_choices) # CPU's randomized choice from the list of possible_choices
    return computer_choice

def letter_to_word(choice): # Used to turn letter inputs into full words
    if choice == 'r':
        return "Rock" # beats Scissors and Lizard
    if choice == 'p':
        return "Paper" # beats Rock and Spock
    if choice == 's':
        return "Scissors" # beats Paper and Lizard
    if choice == 'l':
        return "Lizard" # beats Paper and Spock
    if choice == 'S':
        return "Spock" # beats Scissors and Rock


win_logic_dict = { # Dictionary determining which inputs beat which counter-inputs
    "r" : ["s", "l"],
    "p" : ["r", "S"],
    "s" : ["p", "l"],
    "l" : ["p", "S"],
    "S" : ["s", "r"]
}

def run_game_logic(user_choice, cpu_choice):
    if user_choice == cpu_choice: # Determining that the user's choice and CPU's choice were the same
        print(f"Both players selected {letter_to_word(user_choice)} It\'s a tie!")
        print("Please enter a new selection and start over")
        start_game()
    if cpu_choice in win_logic_dict[user_choice]: # If the CPU's choice was written in the dictionary's list under the respective user's choice, then return True and print that they won
        return True
    return False

start_game()
