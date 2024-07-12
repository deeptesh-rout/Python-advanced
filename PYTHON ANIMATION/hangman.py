import random

def choose_word():
    # List of words for the game
    words = ["apple", "banana", "orange", "strawberry", "pineapple", "grape", "watermelon"]
    
    # Choose a random word from the list
    return random.choice(words)

def display_word(word, guessed_letters):
    # Display the word with dashes for letters not guessed yet
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    # Choose a word for the game
    word = choose_word()
    # Set up initial variables
    guessed_letters = []
    attempts = 6
    
    print("Welcome to Hangman!")
    
    while attempts > 0:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Attempts left: {attempts}")
        
        # Get the player's guess
        guess = input("Guess a letter: ").lower()
        
        # Check if the guess is a single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        # Add the letter to the list of guessed letters
        guessed_letters.append(guess)
        
        # Check if the letter is in the word
        if guess in word:
            print("Correct guess!")
            # Check if the player has guessed all the letters
            if all(letter in guessed_letters for letter in word):
                print(f"\nCongratulations! You've guessed the word '{word}' correctly!")
                break
        else:
            print("Incorrect guess!")
            attempts -= 1
        
    else:
        print("\nSorry, you're out of attempts! The word was:", word)

# Run the game
hangman()
