# include random module which provide function for generating random numbers
import random

# function get_roll simulates rolling a six-sided die and
# returns a random number between 1 and 6


def get_roll():
    return random.randint(1,6)

def guess_roll():
    valid = False
    while not valid:
        try:
            guess=int(input("What is your Guess: "))
            if guess >= 1 and guess <= 6:
                valid = True
            else:
                print("Invalid Guess")
                valid = False
        except:
            print("Invalid Data Type")
            valid = False
    return guess

def get_number_of_rounds():
    valid = False
    while not valid:
        try:
            num_of_rounds=int(input("Enter the Number of Rounds: "))
            if num_of_rounds > 0:
                valid = True
            else:
                print("Invalid Number of Rounds")
                valid = False
        except:
            print("Invalid Data Type")
            valid = False
    return num_of_rounds


def determine_scores(player_roll, computer_roll):
    # initialise variables
    player_score = 0
    computer_score = 0

    if player_roll > computer_roll:
        player_score += 1
    elif computer_roll > player_roll:
        computer_score += 1
    return player_score, computer_score

def play_game(player_name):

    number_of_rounds = get_number_of_rounds()
    new_player_score = 0
    new_computer_score = 0
    bonus_points = 0

    for rounds in range(1, number_of_rounds+1):
        player_roll = get_roll()
        computer_roll = get_roll()
        guess = guess_roll()
        player_score, computer_score = determine_scores(player_roll, computer_roll )

        print("")
        print("This is roll: ", rounds)
        print(f"The player roll is: {player_roll}")
        print(f"The computer roll is: {computer_roll}")
    
        if player_roll > computer_roll:
            new_player_score += player_score
            print(f"Well done {player_name}")
        elif computer_roll > player_roll:
            new_computer_score += computer_score
            print(f"Sorry {player_name}, better luck next time!")
        else:
            print("It is a draw")

        if guess == player_roll:
            print("Your Guess is Correct and Earned 2 Bonus Points! ")
            bonus_points += 2
            new_player_score = player_score + 2
        else:
            print("Sorry, Wrong Guess")

        print("")
        print("Scores after roll: ", rounds)
        print(f"{player_name}: {new_player_score}")
        print(f"Computer: {new_computer_score}")
        print("__________________________")
        print("")

    player_score_bonus = new_player_score + bonus_points
    print("")
    print("")
    print("Final scores:")
    print("")
    print(f"Number of Rounds: {number_of_rounds}")
    print(f"Bonus Points: {bonus_points}")
    print(f"Player {player_name} Total Score with Bonus: {player_score_bonus}")
    print(f"Computer Total Score: {new_computer_score}")
    print("")

def main():
    print("")
    print("Welcome to the Dice Roll Challenge against the Computer!")
    print("")
    
    player_name = input("Please enter your name: ")

    play_game(player_name)

if __name__ == "__main__":
    main()