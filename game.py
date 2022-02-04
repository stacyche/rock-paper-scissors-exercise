# this is the "game.py" file...
import os 

player_name = os.getenv("PLAYER_NAME", default="Player One")

print("Welcome ", player_name, " to my Rock-Paper-Scissors game!")
print("Rock, Paper, Scissors, Shoot!")

#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md


#ASK FOR USER INPUT
user_choice = input("Please choose one of: 'rock', 'paper', 'scissors'")

print("USER CHOSE", user_choice)


#VALIDATIONS
valid_options = ["rock","ROCK", "Rock", "paper", "Paper", "PAPER", "scissors", "Scissors", "SCISSORS"]

if user_choice in valid_options: 
    print("Valid")
else: 
    print("Oops, invalid input.")
    exit()


#COMPUTER CHOICE

import random 

options = ("rock", "paper", "scissors")

computer_choice = random.choice(options)

print("COMPUTER CHOSE:", computer_choice)

#DETERMINE THE WINNER 
if user_choice == computer_choice: 
    print("Both players played", user_choice, "It's a tie!")
elif user_choice == "paper": 
    if computer_choice == "rock":
        print("Paper covers rock, you won!")
    else: 
        print("Scissors cut paper, you lost! It's ok.")
elif user_choice == "scissors": 
    if computer_choice == "paper": 
        print("Scissors cut paper, you won!")
    else: 
        print("Rock crushes scissors, you lost! It's ok.")
elif user_choice == "rock": 
    if computer_choice == "scissors": 
        print("Rock crushes scissors, you won!")
    else: 
        print("Paper covers rock, you lost! It's ok.")


#FINAL RESULTS 
print("Thanks for playing. Please play again!")