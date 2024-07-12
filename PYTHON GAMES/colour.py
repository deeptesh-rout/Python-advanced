import random
import time

# List of colors
colors = ['Red', 'Blue', 'Green', 'Yellow', 'Orange', 'Purple', 'Brown', 'Black', 'White', 'Pink']

def color_game():
    score = 0
    time_limit = 30  # 30 seconds for the game
    start_time = time.time()

    print("Color Game! Type the color of the word, not the word text.")
    print("You have 30 seconds. Type 'quit' to exit the game.")
    print("Example: If the word is 'Red' but displayed in blue color, you should type 'Blue'.\n")

    while True:
        # Pick a random color name and display color
        color_name = random.choice(colors)
        display_color = random.choice(colors)

        while color_name == display_color:  # Ensure the word text and color are different
            display_color = random.choice(colors)

        print(f"\033[1;{color_to_ansi(display_color)}m{color_name}\033[0m")  # Display the word in color

        # Get the user's answer
        user_input = input("Enter the color of the text: ").strip().capitalize()

        # Check if time limit is reached
        if time.time() - start_time > time_limit:
            print("Time's up!")
            break

        # Check if the user wants to quit
        if user_input.lower() == 'quit':
            break

        # Check if the answer is correct
        if user_input == display_color:
            score += 1
            print("Correct!")
        else:
            print("Wrong!")

    print(f"\nGame over! Your score: {score}")

def color_to_ansi(color):
    ansi_colors = {
        'Black': '30',
        'Red': '31',
        'Green': '32',
        'Yellow': '33',
        'Blue': '34',
        'Purple': '35',
        'Brown': '36',
        'White': '37',
        'Pink': '35',  # using purple for pink as there is no ANSI code for pink
        'Orange': '33'  # using yellow for orange as there is no ANSI code for orange
    }
    return ansi_colors.get(color, '37')

if __name__ == "__main__":
    color_game()
