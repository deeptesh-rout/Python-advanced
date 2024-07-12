import random

def main():
    print("Ladies and Gentlemen, a great match between the user and the system. Let's see who will win the match")
    over = int(input("How many overs do you want to play? "))
    print("Total 5 wickets in each team")
    print("It's toss time. What is your call?")
    user_toss = int(input("Head (0), Tail (1): "))

    computer_toss = random.randint(0, 1)
    system_score = 0
    user_score = 0
    user_wickets = 0
    system_wickets = 0

    if computer_toss == user_toss:
        print("Congratulations, you won the toss")
        option = int(input("What do you want to choose, batting or bowling first? [(1): bat or (2): ball] "))

        if option == 1:
            print("You chose batting first (System will bowl to you)")
            print("Enter 1: One run, 2: Two runs, 3: Three runs, 4: Four runs, 5: Five runs, 6: Six runs")

            for i in range(1, over + 1):
                for j in range(1, 7):
                    user_batting = int(input("Bat: "))
                    computer_bowling = random.randint(1, 6)

                    if user_batting != computer_bowling:
                        print(f"You hit: {user_batting} runs, System chose: {computer_bowling}")
                        user_score += user_batting
                    else:
                        user_wickets += 1
                        print(f"Oops, you're out! You: {user_batting}, System chose: {computer_bowling}")

                    if user_wickets == 5:
                        break
                print(f"After completing {i} over(s), the score is {user_score} runs with the loss of {user_wickets} wicket(s)")

            print("Total score:", user_score)
            print(f"2nd innings start in a few sec, now it's your turn to bowl and defend your score (Target): {user_score + 1}")
            
            for i in range(1, over + 1):
                for j in range(1, 7):
                    user_bowling = int(input("Ball: "))
                    computer_batting = random.randint(1, 6)

                    if user_bowling != computer_batting:
                        print(f"System hit: {computer_batting} runs, You chose: {user_bowling}")
                        system_score += computer_batting
                    else:
                        system_wickets += 1
                        print(f"Yes, you got it! {system_wickets} wickets gone. You: {user_bowling}, System chose: {computer_batting}")

                    if system_wickets == 5:
                        break
                print(f"After completing {i} over(s), the score is {system_score} runs with the loss of {system_wickets} wicket(s)")

            if user_score > system_score:
                print(f"Congratulations, you won the game by {user_score - system_score} runs")
            elif user_score < system_score:
                print(f"Oo you lose the game by {5 - system_wickets} wickets, but nice try. Best of luck for the next game")
            else:
                print(f"Oo it is a tie score between you and the system {user_score}-{system_score} runs, well played")
        else:
            print("You chose bowling first (System will bat first...)")
            print("Enter 1: One run, 2: Two runs, 3: Three runs, 4: Four runs, 5: Five runs, 6: Six runs")

            for i in range(1, over + 1):
                for j in range(1, 7):
                    user_bowling = int(input("Ball: "))
                    computer_batting = random.randint(1, 6)

                    if user_bowling != computer_batting:
                        print(f"System hit: {computer_batting} runs, You chose: {user_bowling}")
                        system_score += computer_batting
                    else:
                        system_wickets += 1
                        print(f"Yes, you got it! {system_wickets} wickets gone. You: {user_bowling}, System chose: {computer_batting}")

                    if system_wickets == 5:
                        break
                print(f"After completing {i} over(s), the score is {system_score} runs with the loss of {system_wickets} wicket(s)")

            print("Total score:", system_score)
            print(f"2nd innings start in a few sec, now it's your turn to bat and chase the score (Target): {system_score + 1}")

            for i in range(1, over + 1):
                for j in range(1, 7):
                    user_batting = int(input("Bat: "))
                    computer_bowling = random.randint(1, 6)

                    if user_batting != computer_bowling:
                        print(f"You hit: {user_batting} runs, System chose: {computer_bowling}")
                        user_score += user_batting
                    else:
                        user_wickets += 1
                        print(f"Oops, you're out! You: {user_batting}, System chose: {computer_bowling}")

                    if user_wickets == 5:
                        break
                print(f"After completing {i} over(s), the score is {user_score} runs with the loss of {user_wickets} wicket(s)")

            if user_score > system_score:
                print(f"Congratulations, you won the game by {5 - system_wickets} wickets")
            elif user_score < system_score:
                print(f"You lose the game by {system_score - user_score} runs, but nice try. Best of luck for the next game")
            else:
                print(f"Oo it is a tie score between you and the system {user_score}-{system_score} runs, well played")
    else:
        print("O sorry, you lose the toss")
        computer_choice = random.randint(0, 1)

        if computer_choice == 0:
            print("And the computer won the toss and chose to bat first")
            print("Enter 1: One run, 2: Two runs, 3: Three runs, 4: Four runs, 5: Five runs, 6: Six runs")

            for i in range(1, over + 1):
                for j in range(1, 7):
                    user_bowling = int(input("Ball: "))
                    computer_batting = random.randint(1, 6)

                    if user_bowling != computer_batting:
                        print(f"System hit: {computer_batting} runs, You chose: {user_bowling}")
                        system_score += computer_batting
                    else:
                        system_wickets += 1
                        print(f"Yes, you got it! {system_wickets} wickets gone. You: {user_bowling}, System chose: {computer_batting}")

                    if system_wickets == 5:
                        break
                print(f"After completing {i} over(s), the score is {system_score} runs with the loss of {system_wickets} wicket(s)")

            print("Total score:", system_score)
            print(f"2nd innings start in a few sec, now it's your turn to bat and chase the score (Target): {system_score + 1}")

            for i in range(1, over + 1):
                for j in range(1, 7):
                    user_batting = int(input("Bat: "))
                    computer_bowling = random.randint(1, 6)

                    if user_batting != computer_bowling:
                        print(f"You hit: {user_batting} runs, System chose: {computer_bowling}")
                        user_score += user_batting
                    else:
                        user_wickets += 1
                        print(f"Oops, you're out! You: {user_batting}, System chose: {computer_bowling}")

                    if user_wickets == 5:
                        break
                print(f"After completing {i} over(s), the score is {user_score} runs with the loss of {user_wickets} wicket(s)")

            if user_score > system_score:
                print(f"Congratulations, you won the game by {5 - system_wickets} wickets")
            elif user_score < system_score:
                print(f"You lose the game by {system_score - user_score} runs, but nice try. Best of luck for the next game")
            else:
                print(f"Oo it is a tie score between you and the system {user_score}-{system_score} runs, well played")
        else:
            print("And the computer won the toss and chose to bowl first")
            print("Enter 1: One run, 2: Two runs, 3: Three runs, 4: Four runs, 5: Five runs, 6: Six runs")

            for i in range(1, over + 1):
                for j in range(1, 7):
                    user_batting = int(input("Bat: "))
                    computer_bowling = random.randint(1, 6)

                    if user_batting != computer_bowling:
                        print(f"You hit: {user_batting} runs, System chose: {computer_bowling}")
                        user_score += user_batting
                    else:
                        user_wickets += 1
                        print(f"Oops, you're out! You: {user_batting}, System chose: {computer_bowling}")

                    if user_wickets == 5:
                        break
                print(f"After completing {i} over(s), the score is {user_score} runs with the loss of {user_wickets} wicket(s)")

            print("Total score:", user_score)
            print(f"2nd innings start in a few sec, now it's your turn to bowl and defend your score (Target): {user_score + 1}")

            for i in range(1, over + 1):
                for j in range(1, 7):
                    user_bowling = int(input("Ball: "))
                    computer_batting = random.randint(1, 6)

                    if user_bowling != computer_batting:
                        print(f"System hit: {computer_batting} runs, You chose: {user_bowling}")
                        system_score += computer_batting
                    else:
                        system_wickets += 1
                        print(f"Yes, you got it! {system_wickets} wickets gone. You: {user_bowling}, System chose: {computer_batting}")

                    if system_wickets == 5:
                        break
                print(f"After completing {i} over(s), the score is {system_score} runs with the loss of {system_wickets} wicket(s)")

            if user_score > system_score:
                print(f"Congratulations, you won the game by {user_score - system_score} runs")
            elif user_score < system_score:
                print(f"Oo you lose the game by {5 - system_wickets} wickets, but nice try. Best of luck for the next game")
            else:
                print(f"Oo it is a tie score between you and the system {user_score}-{system_score} runs, well played")

if __name__ == "__main__":
    main()
