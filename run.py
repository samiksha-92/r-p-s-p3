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
        computer_choice = random.randint(1, 3)
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

    # Initialize scores
    player_score = 0
    num_ties = 0
    computer_score = 0

    while True:
        user_choice = int(input("Please select 1,2 or 3:\n"))
        print()
        while user_choice < 1 or user_choice > 3:
            print("Invalid response")
            user_choice = int(input("Please select 1,2 or 3\n"))
        if user_choice == 1:
            choice = "ROCK 🪨"
        elif user_choice == 2:
            choice = "PAPER 📄"
        else:
            choice = "SCISSORS ✂️"
            print(f"The user's choice is {choice}")
        print("Now it is time for Computer 👩🏻‍💻 to make a choice ")
        comp_choice = comp_decision()
        if comp_choice == 1:
            opp_choice = "ROCK 🪨"
        elif comp_choice == 2:
            opp_choice = "PAPER 📄"
        else:
            opp_choice = "SCISSORS ✂️"

        print(f"The Computer has chosen {opp_choice}")

        if ((choice == "PAPER 📄" and opp_choice == "ROCK 🪨") or (choice == "ROCK 🪨" and opp_choice == "PAPER 📄")):
            outcome = "PAPER"
        if ((choice == "PAPER 📄" and opp_choice == "ROCK 🪨") or (choice == "ROCK 🪨" and opp_choice == "PAPER 📄")):
            outcome = "PAPER 📄"
            print("PAPER WINS")
        elif ((choice == "SCISSORS ✂️" and opp_choice == "ROCK 🪨") or (choice == "ROCK 🪨" and opp_choice == "SCISSORS ✂️")):
            outcome = "ROCK 🪨"
            print("ROCK WINS")
        elif (choice == opp_choice):
            outcome = "TIE"
            print("IT'S A TIE")
        else:
            outcome = "SCISSORS"
            print("SCISSORS WIN ✂️")

        print()

        player_win_quote = winning_message()

        if outcome == "TIE":
            num_ties += 1
        elif outcome == choice:
            player_score += 1
            print("Player wins the round")
        else:
            computer_score += 1
            print("Computer wins the round")

        print()
        print(f"{player} your score is : {player_score}")

        print()

        print(f"Computer score is : {computer_score}")

        print()

        print(f"Rounds tied :{num_ties}")

        if player_score > computer_score:
            print(f"{player_win_quote}")
        else:
            print("Ready to take down the computer one more time 💪")

        continue_choice = input(
            "Enter any key to play another round or press q to quit\n")
        if continue_choice == "q":
            break

    print(f"Thanks for playing {player}")


main()
