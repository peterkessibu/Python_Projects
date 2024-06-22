import random

rules = '''
        It's Rock, Paper, Scissors.
        Winner gets one point till the point limit is reached.
        Loosers,no loosers
        '''

def calculate_winner(player, computer):
    #Determines the winner based on player and computer choices.
    if player == computer:
        return "Tie"  
    elif player == "rock":
        return "win" if computer == "scissors" else "lose"
    elif player == "scissors":
        return "win" if computer == "paper" else "lose"
    elif player == "paper":
        return "win" if computer == "rock" else "lose"
    else:
        return None  

def update_points(winner, player_points, computer_points):
    #Updates player and computer points based on the winner.
    if winner == "win":
        player_points += 1
    elif winner == "lose":
        computer_points += 1
    return player_points, computer_points

def main():
    choices = ["rock", "paper", "scissors"]

    # Get user name and point limits
    user_name = input("Enter your name: ")
    point_limit = int(input("Enter your point limit to win: "))

    # Initialize player and computer points
    player_points = 0
    computer_points = 0

    while True:
        computer = random.choice(choices)
        player = None
        while player not in choices:
            player = input(f"{user_name}, Pick between Rock, Paper, Scissors?: ").lower()

        winner = calculate_winner(player, computer)
        player_points, computer_points = update_points(winner, player_points, computer_points)

        print(f"Computer chose: {computer}")
        print(f"{user_name} chose: {player}")

        if winner == "win":
            print(f"{user_name} Wins this round!")
        elif winner == "lose":
            print("Computer Wins this round!")
        else:
            print("It's a Tie!")

        print(f"{user_name}'s Score: {player_points}")
        print(f"Computer's Score: {computer_points}")

        # Check for point limits
        if player_points >= point_limit:
            print(f"{user_name} Wins! Reached point limit of {point_limit}")
            break
        elif computer_points >= point_limit:
            print(f"Computer Wins! Reached point limit of {point_limit}")
            break

        play_again = input("Play again? Yes(y) or No(n): ").lower()
        if play_again != "y":
            break

    print("Bye!")

if __name__ == "__main__":
    main()
