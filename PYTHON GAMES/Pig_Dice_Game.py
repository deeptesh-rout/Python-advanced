import random

def roll_die():
    """Simulate rolling a six-sided die."""
    return random.randint(1, 6)

def take_turn(player):
    """Simulate a player's turn."""
    turn_total = 0
    while True:
        roll = roll_die()
        print(f"{player} rolled a {roll}")
        if roll == 1:
            print(f"{player} loses their turn total.")
            return 0
        else:
            turn_total += roll
            print(f"{player}'s turn total is now {turn_total}")
            choice = input(f"{player}, do you want to 'hold' or 'roll' again? ").lower()
            if choice == 'hold':
                return turn_total

def play_game():
    """Play a game of Pig."""
    player1_score = 0
    player2_score = 0
    target_score = 100
    
    while player1_score < target_score and player2_score < target_score:
        print("\nPlayer 1's turn")
        player1_score += take_turn("Player 1")
        print(f"Player 1's total score is now {player1_score}")
        
        if player1_score >= target_score:
            print("Player 1 wins!")
            break
        
        print("\nPlayer 2's turn")
        player2_score += take_turn("Player 2")
        print(f"Player 2's total score is now {player2_score}")
        
        if player2_score >= target_score:
            print("Player 2 wins!")
            break

if __name__ == "__main__":
    play_game()
