# Final Project - Rochambeau

import random
import sys
from rochambeau_helper_functions import determine_winner

# Create a rock, paper, scissor game where the user has to win 3 out of 5 times vs a CPU
print("Welcome to Rochambeau")

valid_choices = ['rock', 'paper', 'scissors']

# Set number of rounds needed to win the game
try:
    rounds_to_win = sys.argv[1]
except:
    rounds_to_win = input("How many wins do you want to play up to?")
rounds_to_win = int(rounds_to_win)

user_name = input("Enter your name: ")

choice_dict = {user_name: "",
               "CPU": ""}
score_dict = {user_name: 0,
              "CPU": 0}

game_results = []

while (score_dict["CPU"] < rounds_to_win and score_dict[user_name] < rounds_to_win):
    # Variable that allows user to choose rock, paper or scissors after asking for their name
    print(f"Hi {user_name} what is your choice: rock, paper, or scissors?")
    user_choice = None

    while not user_choice in valid_choices:
        user_choice = input("Enter your choice: 'rock', 'paper', 'scissors'\n")
        if not user_choice in valid_choices:
            print("invalid choice (maybe typo?), try again")

    choice_dict[user_name] = user_choice

    # Function that makes CPU choose between rock, paper, and scissors randomly
    cpu_choice = random.choice(valid_choices)
    choice_dict["CPU"] = cpu_choice

    # Print the CPU choice and User choice
    print("\ncpu chose "+ cpu_choice + "\nyou chose "+ user_choice + "\n")

    # Function used to determine results of rock, paper, scissor game
    winner, choice = determine_winner(choice_dict)

    # Update scores
    if not winner is None:
        score_dict[winner] +=1

    print("======================")
    print(score_dict)
    print("======================")  

    # append game result to results list
    result_row = f"{winner},{choice}\n"
    game_results.append(result_row)


# Write the game results out to a file (table with name of who won and what they chose) 
# ask first
save_file = input("Do you want to save results? (y/n)" )
if save_file == "y":
    # write file
    with open("game_output.csv", "w") as savefile_connection:
        savefile_connection.write("winner,choice\n")
        savefile_connection.writelines(game_results)