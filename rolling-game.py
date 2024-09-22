import random

def roll_dice():
    return random.randint(1, 6)

def play_game():
    print("Welcome to the Dice Rolling Game!")
    
    # Player rolls
    player_roll = roll_dice()
    print(f"You rolled: {player_roll}")
    
    # Computer rolls
    computer_roll = roll_dice()
    print(f"Computer rolled: {computer_roll}")
    
    # Determine the winner
    if player_roll > computer_roll:
        print("You win!")
    elif player_roll < computer_roll:
        print("Computer wins!")
    else:
        print("It's a tie!")

# Start the game
play_game()
