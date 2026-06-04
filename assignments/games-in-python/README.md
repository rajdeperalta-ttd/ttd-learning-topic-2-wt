
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game using Python. In this assignment, you will practice string manipulation, loops, conditionals, and user input while managing game state from start to finish.

## 📝 Tasks

### 🛠️	Create the Core Hangman Game Loop

#### Description
Write a program that selects a random word from a predefined list and runs a turn-based guessing loop. On each turn, the player enters one letter and the game updates the displayed progress.

#### Requirements
Completed program should:

- Randomly choose one word from a predefined list when the game starts.
- Display the hidden word using underscores for unknown letters (for example: `_ _ _ _ _`).
- Ask the user to guess one letter each turn and reveal all matching positions.
- Continue looping until the player either guesses the full word or runs out of attempts.


### 🛠️	Track Attempts and Show Endgame Messages

#### Description
Add tracking for incorrect guesses and print a clear final result. The game should inform the player whether they won or lost and display the correct word at the end.

#### Requirements
Completed program should:

- Track the number of incorrect guesses remaining and decrease it only for wrong letters.
- Prevent crashes for repeated guesses by handling them gracefully.
- End with a win message when all letters are guessed correctly.
- End with a lose message when attempts reach zero and show the secret word.
