# include random module which provide function for generating random numbers
import random

# function get_roll simulates rolling a six-sided die and
# returns a random number between 1 and 6

def get_roll():
    return random.randint(1,6)
#enddef 

# function determine_scores compares the player roll against the computer roll
# and generates their scores

def determine_scores(player_roll, computer_roll):
    # initialise variables
    player_score = 0
    computer_score = 0

    if player_roll > computer_roll:
        player_score += 1
    elif computer_roll > player_roll:
        computer_score += 1
    #endif
    return player_score, computer_score

#enddef

# function play_game gets the player and computer roll by calling function get_roll()
# It passes the rolls to function determine_scores.
# Depending on the outcome it displays an appropriate message

def play_game(player_name):
    player_roll = get_roll()
    computer_roll = get_roll()

    print(f"The player roll is: {player_roll}")
    print(f"The computer roll is: {computer_roll}")

    player_score, computer_score = determine_scores(player_roll, computer_roll)

    if player_score > computer_score:
        print(f"Well done {player_name}")
    elif computer_score > player_score:
        print(f"Sorry {player_name}, better luck next time!")
    else:
        print("It is a draw")
    #endif

    print("_____________")
    print("Final scores")
    print("-------------")
    print(f"{player_name}: {player_score}")
    print(f"Computer: {computer_score}")

#enddef

# subroutine main gets the input, calls play_game function
def main():
    print("Welcome to the Dice Roll Challenge against the Computer!")
    
    player_name = input("Please enter your name: ")

    play_game(player_name)

#enddef

# this is where the program starts

if __name__ == "__main__":
    main()
#endif