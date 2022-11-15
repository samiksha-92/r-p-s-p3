import random

"""
The command to import random module for functions
"""

def main():
    """
    The main function invokes smaller functions and conditional statements

    """

    def player_name():
        """
        This functions inputs the name of the user as a string

        """
        username = input("Please enter your name here:")
        return username

    def comp_decision():
        """
        This functions generates a random integar for computer using
        random module

        """
        computer_choice = random.randint(1,3)
        return computer_choice

    player = player_name()
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

    user_choice = int(input("Please select 1,2 or 3:"))

    print()

    while user_choice < 1 or user_choice > 3:
        """
        Check if the user's choice is invalid or valid
        """
        print("Invalid response")
        user_choice = int(input("Please select 1,2 or 3"))

    if user_choice == 1:
        choice = "ROCK 🪨"
    elif user_choice == 2:
        choice = "PAPER 📄"
    else:
        choice = "SCISSORS ✂️"

    print (f"The user's choice is {choice}")
    print("Now it is time for Computer 👩🏻‍💻 to make a choice ")
    comp_choice = comp_decision()

    if comp_choice == 1:
        opp_choice = "ROCK 🪨 "
    elif comp_choice == 2:
        opp_choice = "Paper 📄"  
    else:
        opp_choice = "SCISSORS ✂️"      

    print(f"The Computer has chosen {opp_choice}")  
    

