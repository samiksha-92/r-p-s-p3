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

    def winning_message():

        """
        This function returns a random message when the player wins a round

        """
        win_list = ["The extra energy required to make another effort is the secret of winning.",
        "Go all in for what you want and you shall win", "Everyone has the will to win but only have the coirage to prepare to win, You are one of them", 
        "One must always play fairly when one has the winning cards.",
        "Winning does not always mean being first. Winning means you are doing better than you have ever done before."
        ]

        message = random.choice(win_list)
        return message


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
        opp_choice = "ROCK 🪨"
    elif comp_choice == 2:
        opp_choice = "PAPER 📄"  
    else:
        opp_choice = "SCISSORS ✂️"      

    print(f"The Computer has chosen {opp_choice}")  

    if((choice == "PAPER 📄" and opp_choice == "ROCK 🪨") or (choice =="ROCK 🪨" and opp_choice == "PAPER 📄")):
        outcome = "PAPER"
        print("PAPER WINS")
    elif((choice == "SCISSORS ✂️" and opp_choice == "ROCK 🪨") or (choice == "ROCK 🪨" and opp_choice == "SCISSORS ✂️")):
        outcome = "ROCK"
        print("ROCK WINS")
    elif (choice == opp_choice):
        outcome = "TIE"
        print("IT'S A TIE")
    else:
        outcome = "SCISSORS"
        print("SCISSORS WIN")

    score = 0
    num_ties = 0
    computer_scoreboard = 0 
    player_win_quote = winning_message()  

    if outcome == "TIE":
        num_ties = num_ties + 1   
    elif outcome == choice:
        score += 1
        print("Player wins the round")
    else:
        computer_scoreboard += 1
        print("Computer wins the round")

    print(f"{player} your score is : {score}")

    print(f"Computer score is : {computer_scoreboard}")

    print(f" tie score is :{num_ties}")

    if computer_scoreboard > score:
        print(f"{player_win_quote}")
    else:
        print(f"{encourage_message}")    
    
        



main()




      




