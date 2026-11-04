"""
PS 54 - Hangman Game
Rungta International Skills University | School of Information Technology | BCA
Language: Python 3   Concepts: Strings, Lists, Loops, Random
"""

import random

# ---------------------------------------------------------------
# Set TEST_MODE = True  -> secret word is fixed to 'python' (for the 4 test cases)
# Set TEST_MODE = False -> secret word is chosen randomly from WORDS
# ---------------------------------------------------------------
TEST_MODE = True

WORDS = ["python", "program", "variable", "function", "keyboard",
         "computer", "software", "internet", "database", "network"]
MAX_WRONG = 6


def choose_word():
    """Return the secret word (fixed in test mode, random otherwise)."""
    if TEST_MODE:
        return "python"
    return random.choice(WORDS)


def show_progress(word, guessed):
    """Return the word with unguessed letters shown as underscores."""
    return " ".join(ch if ch in guessed else "_" for ch in word)


def play():
    word = choose_word()
    guessed = []          # all valid letters guessed so far (correct + wrong)
    wrong = 0

    print("=== HANGMAN GAME ===")
    print(f"Guess the word. You can make {MAX_WRONG} wrong guesses.\n")

    while wrong < MAX_WRONG and not all(ch in guessed for ch in word):
        print("Progress:", show_progress(word, guessed))
        guess = input("Enter a letter: ").strip().lower()

        # Validate: exactly one alphabetic character
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Enter a single letter.")
            continue

        # Repeated letter: no attempt is lost
        if guess in guessed:
            print(f"You already guessed '{guess}'. Try another letter.")
            continue

        guessed.append(guess)
        if guess in word:
            print(f"{guess}: Correct")
        else:
            wrong += 1
            print(f"{guess}: Wrong ({wrong}/{MAX_WRONG})")

    # Game result
    if all(ch in guessed for ch in word):
        print("Progress:", show_progress(word, guessed))
        print(f"You won! The word was {word}.")
    else:
        print(f"Game Over! The word was {word}.")
    print(f"Wrong guesses: {wrong}/{MAX_WRONG}")


if __name__ == "__main__":
    play()

