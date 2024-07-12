import random

# Function to roll a die
def roll_die():
    return random.randint(1, 6)

# Function to play one turn of the game
def play_turn(player):
    print(f"\n{player}'s turn:")
    total_score = 0
    while True:
        roll = roll_die()
        print(f"You rolled: {roll}")
        if roll == 1:
            print("You rolled a 1! No points earned this turn.")
            return 0
        else:
            total_score += roll
            print(f"Total score this turn: {total_score}")
            choice = input("Roll again (r) or hold (h)? ").lower()
            if choice == 'h':
                return total_score

# Function to determine the winner
def determine_winner(scores):
    max_score = max(scores.values())
    winners = [player for player, score in scores.items() if score == max_score]
    if len(winners) == 1:
        print(f"\n{winners[0]} wins with {max_score} points!")
    else:
        print("\nIt's a tie!")

# Main function to run the game
def pig_game():
    num_players = int(input("Enter the number of players: "))
    players = [input(f"Enter name of player {i+1}: ") for i in range(num_players)]
    scores = {player: 0 for player in players}

    while all(score < 100 for score in scores.values()):
        for player in players:
            input(f"\n{player}, it's your turn. Press Enter to roll.")
            score = play_turn(player)
            scores[player] += score
            print(f"Total score for {player}: {scores[player]}")
            if scores[player] >= 100:
                break

    determine_winner(scores)

# Run the game
pig_game()
