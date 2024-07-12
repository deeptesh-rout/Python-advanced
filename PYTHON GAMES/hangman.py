import random

# Function to choose a random word from a list
def choose_word():
    words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'kiwi', 'lemon', 'mango']
    return random.choice(words)

# Function to display the word with guessed letters
def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word

# Function to check if the player has won
def check_win(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True

# Main function to play the game
def play_game():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Guess the word before the hangman is complete.")
    print(display_word(word, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            print("Correct!")
            print(display_word(word, guessed_letters))
            if check_win(word, guessed_letters):
                print("Congratulations! You've guessed the word:", word)
                break
        else:
            attempts -= 1
            print("Incorrect! You have", attempts, "attempts left.")
            if attempts == 0:
                print("Sorry, you've run out of attempts. The word was:", word)
                break

# Run the game
if __name__ == "__main__":
    play_game()
