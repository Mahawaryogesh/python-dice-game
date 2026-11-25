# Python Dice Game

A beginner-friendly command-line dice game built using Python.

Roll a virtual dice, track your scores, achieve consecutive high rolls, and try to get three sixes to win the game!

## Features

- Random dice generation (1–6)
- High roll and low roll detection
- Total roll counter
- Jackpot detection when rolling a 6
- Winning condition after three sixes
- High and low score tracking
- Consecutive high-roll streak tracking
- Best streak tracking
- High-roll percentage calculation
- Quit the game anytime using `q` or `Q`

## Technologies Used

- Python 3
- Python's built-in `random` module

No external packages are required.

## Project Structure

```text
python-dice-game/
├── Dice_Game.py
├── README.md
└── .gitignore
```

## How to Run

1. Install Python 3.
2. Clone or download this repository.
3. Open the project folder in VS Code, PyCharm, or a terminal.
4. Run:

```bash
python Dice_Game.py
```

On some Windows installations, you may need:

```bash
py Dice_Game.py
```

## How to Play

1. Press Enter to roll the dice.
2. A random number between 1 and 6 is generated.
3. Numbers 1–3 are low rolls.
4. Numbers 4–6 are high rolls.
5. Rolling a 6 gives you a jackpot.
6. Get three sixes to win the game.
7. Enter `q` or `Q` to quit.

## Sample Output

```text
================================
       PYTHON DICE GAME
================================
Roll the dice and try your luck!
Get three sixes to win the game.

Press Enter to roll or Q to quit:

You rolled: 6
JACKPOT! You got a 6!

Press Enter to roll or Q to quit:

You rolled: 4
Great! High roll!

================================
          GAME RESULTS
================================
Total rolls: 2
High rolls: 2
Low rolls: 0
Number of sixes: 1
Best high streak: 2
High roll percentage: 100.0 %

Thanks for playing!
================================
```

*This is illustrative sample output. Actual dice results are random.*

## Python Concepts Practiced

- Variables and data types
- User input with `input()`
- Random number generation
- `while` loops
- Conditional statements (`if`, `elif`, `else`)
- `break`
- Counters and accumulators
- Arithmetic operations
- Tracking consecutive values

## Author

Created as a beginner Python practice project.

## License

This project is licensed under the MIT License. See the `LICENSE` file.
