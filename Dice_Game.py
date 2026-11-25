import random

# Game statistics
roll_count = 0
six_count = 0
high_score = 0
low_score = 0

# Streak tracking
high_streak = 0
best_streak = 0

print("================================")
print("       PYTHON DICE GAME")
print("================================")
print("Roll the dice and try your luck!")
print("Get three sixes to win the game.")

while True:
    choice = input("\nPress Enter to roll or Q to quit: ")

    if choice.lower() == "q":
        break

    roll_count += 1

    # Generate a random dice number between 1 and 6
    dice = random.randint(1, 6)
    print("\nYou rolled:", dice)

    # Check high and low rolls
    if dice >= 4:
        high_score += 1
        high_streak += 1

        # Update best high streak
        if high_streak > best_streak:
            best_streak = high_streak

        if dice == 6:
            six_count += 1
            print("JACKPOT! You got a 6!")

            # Winning condition
            if six_count == 3:
                print("CONGRATULATIONS! YOU WON!")
                break
        else:
            print("Great! High roll!")
    else:
        low_score += 1
        high_streak = 0
        print("Low roll!")

# Display final game results
print("\n================================")
print("          GAME RESULTS")
print("================================")
print("Total rolls:", roll_count)
print("High rolls:", high_score)
print("Low rolls:", low_score)
print("Number of sixes:", six_count)
print("Best high streak:", best_streak)

# Calculate high roll percentage safely
if roll_count > 0:
    high_percentage = (high_score / roll_count) * 100
    print("High roll percentage:", round(high_percentage, 2), "%")
else:
    print("High roll percentage: 0%")

print("\nThanks for playing!")
print("================================")
