<<<<<<< HEAD
# PS 54 – Hangman Game

**University:** Rungta International Skills University
**School:** School of Information Technology
**Programme:** Bachelor of Computer Application (BCA)
**Language:** Python 3  |  **Concepts:** Strings, Lists, Loops, Random

## Project Overview
A console-based word guessing game. The program picks a hidden word and the player
guesses it one letter at a time. The player is allowed a maximum of **6 wrong guesses**.

## Objectives
- Practise string handling, lists and loops in Python.
- Use the `random` module to choose a secret word from a list.
- Validate user input and handle repeated guesses correctly.

## Features
- Secret word chosen randomly from a list of words (fixed to `python` in test mode).
- Word displayed with unguessed letters as underscores (e.g. `p y _ _ _ _`).
- Tracks correct and wrong guesses; game ends on a win or after 6 wrong guesses.
- Input validation: only a single alphabetic letter is accepted.
- Letters are case-insensitive (`P` and `p` are the same).
- A repeated letter is **not** counted as a wrong guess (no attempt is lost).

## Requirements
- Python 3.x (no external libraries; uses only the built-in `random` module)

## Files
| File | Description |
|------|-------------|
| `one.py` | Complete game code |
| `README.md` | Project documentation |
| `Test_Case_Screenshots.pdf` | Input/output screenshots for all 4 test cases |

## How to Run
```bash
python one.py
```
At the top of `one.py`:
- `TEST_MODE = True`  → secret word is fixed to `python` (used for the test cases).
- `TEST_MODE = False` → secret word is chosen randomly from the word list.

## Input / Output
- **Input:** one letter per prompt (`Enter a letter:`).
- **Output:** current progress, `Correct` / `Wrong (n/6)` messages, and the final result
  (`You won!` or `Game Over!`) with the number of wrong guesses.

## Test Cases (secret word = `python`)
| # | Scenario | Guesses | Expected Result | Status |
|---|----------|---------|-----------------|--------|
| 1 | Normal input | p, y, t, h, o, n | Progress updates each turn; `You won!`; Wrong guesses: 0/6 | Pass |
| 2 | Boundary / minimum | a, b, c, d, e, f | Wrong (1/6) … Wrong (6/6); `Game Over!` | Pass |
| 3 | Invalid input | 1, ab, p, p, … | `Invalid input. Enter a single letter.` (×2); `p: Correct`; `You already guessed 'p'. Try another letter.` (no attempt lost) | Pass |
| 4 | Different valid scenario | p, z, y, x, t, h, o, n | p Correct, z Wrong (1/6), y Correct, x Wrong (2/6) … `You won!`; Wrong guesses: 2/6 | Pass |

Screenshots of every test case are in `Test_Case_Screenshots.pdf`.

## Sample Run
```
Progress: _ _ _ _ _ _
Enter a letter: p
p: Correct
Progress: p _ _ _ _ _
Enter a letter: z
z: Wrong (1/6)
...
You won! The word was python.
Wrong guesses: 2/6
```

## Logic Summary
1. Choose the secret word (`random.choice`, or `python` in test mode).
2. Loop until the word is fully guessed or 6 wrong guesses are made.
3. Validate the input; reject non-letters and multi-character input.
4. Ignore repeated letters (no penalty); otherwise mark Correct or Wrong.
5. Print the final result and the wrong-guess count.
=======
# Python-first-project
>>>>>>> d30d9de945155af14bbde9565b26acb8805bef88
