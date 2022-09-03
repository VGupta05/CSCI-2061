# Vardaan Gupta
# The game is called Rock-Paper-Scissors-Lizard-Spock.
# There are many different ways to win in this game as well as lose.
# You will enter a choice and play your odds to win versus a computer.
# Here are the rules:
# Scissors cuts Paper
# Paper covers Rock
# Rock crushes Lizard
# Lizard poisons Spock
# Spock smashes Scissors
# Scissors decapitates Lizard
# Lizard eats Paper
# Paper disproves Spock
# Spock vaporizes Rock
# Rock crushes Scissors

import random
from time import sleep

global replay
replay = True

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

# Lists containing all valid user inputs
possible_choices = ["r", "p", "c", "l", "s"]

rock_choices = ["r", "R", "rock", "Rock", "ROCK"]
paper_choices = ["p", "P", "paper", "Paper", "PAPER"]
scissors_choices = ["c", "C", "scissors" "Scissors", "SCISSORS"]
lizard_choices = ["l", "L", "lizard", "Lizard", "LIZARD"]
spock_choices = ["s", "S", "spock", "Spock", "SPOCK"]

accepted_yes_list = ["y", "Y", "yes", "Yes", "YES"]
accepted_no_list = ["n", "N", "no", "No", "NO"]


def letter_to_word(choice):
  # Used to turn letter inputs into full words
  if choice in rock_choices:
    return "Rock" # beats Scissors and Lizard
  if choice in paper_choices:
    return "Paper" # beats Rock and Spock
  if choice in scissors_choices:
    return "Scissors" # beats Paper and Lizard
  if choice in lizard_choices:
    return "Lizard" # beats Paper and Spock
  if choice in spock_choices:
    return "Spock" # beats Scissors and Rock


def choice_check(user_choice, cpu_choice):
  # Determining that the user's choice and CPU's choice were the same
  if user_choice == cpu_choice:
    return "tie", ""
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
  cpu_choice = random.choice(possible_choices)
  # User input choice
  user_choice = input("Enter a choice (rock [r], paper [p], scissors [c], lizard [l], spock [s]): ")
  if user_choice not in (rock_choices+paper_choices+scissors_choices+lizard_choices+spock_choices):
    print("Invalid input. Please enter a valid input.")
    input_choice()
  return letter_to_word(user_choice), letter_to_word(cpu_choice)


# sets 'replay' to True or False based on user input
def ask_replay():
  global replay
  replay_choice = input("Would you like to play again? Y/N: ")

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

    sleep(1) # Adds a small delay before revealing the winner

    print(f"Computer chose {cpu_choice}")
    won, action = choice_check(user_choice, cpu_choice)

    if won == "tie":
      print("You tied. Play again!")
      start_game() # automatically replays game
    if won is True:
      print(f"{user_choice} {action} {cpu_choice}")
      print("You won. Congrats!")
      ask_replay() # asks if player would like to replay
    if won is False:
      print(f"{cpu_choice} {action} {user_choice}")
      print("You lost. Try again!")
      ask_replay() # asks if player would like to replay

  print("Thanks for playing. Come back soon.")

start_game()
