import random
"""
The command to import random module for functions
"""

def player_name():
    username = input("What's your name?")
    return username

player = player_name

def starting_instructions():
  print(f"Hi {player},How are you doing today 😊")
  print("~~~~~ WELCOME TO THE GAME OF R-P-S ~~~~~")
  print("""~~~~~ WINNING RULES ARE ~~~~~:
  1. PAPER VS ROCK --> PAPER WINS
  2. ROCK VS SCISSORS --> ROCK WINS
  3. SCISSORS VS PAPER --> SCISSORS WINS
    """)
  print(""" YOUR CHOICES ARE:
  1. ROCK
  2. PAPER
  3. SCISSORS
  """)

def player_selection():
    player_choice = int(input("Please select 1,2 or 3:"))
    return player_choice

def determining_player_choice(player_choice):
    if player_choice == 1:
        choice = "ROCK"
        print("You have chosen ROCK")
    elif player_choice == 2:
        choice = "PAPER"
        print("You have chosen PAPER")
    else:
        choice = "SCISSORS"
        print("You have chosen SCISSORS") 
    return choice

def comp_decision():
    computer_choice = random.randint(1, 3)
    return computer_choice

def determing_computer_choice(computer_choice):
    if computer_choice == 1:
        opp_choice = "ROCK"
        print("Computer has chosen ROCK")
    elif computer_choice == 2:
        opp_choice = "PAPER"
        print("Computer has chosen PAPER")
    else:
        opp_choice = "SCISSORS" 
        print("Computer has chosen SCISSORS")
    return opp_choice    










 