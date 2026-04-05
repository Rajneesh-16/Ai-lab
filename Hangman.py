import random

words = ['python','ai','code','data','game']
word = random.choice(words)
guessed = set()
tries = 6

stages = [
"""
  +---+
  |   |
      |
      |
      |
      |
=========""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
"""
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
========="""
]

while True:
    print(stages[6-tries])
    display = ''.join(c if c in guessed else '_' for c in word)
    print("Word:", display)

    if '_' not in display:
        print("You Win!")
        break

    if tries == 0:
        print(stages[6])
        print("You Lose! Word was:", word)
        break

    g = input("Guess: ").lower()

    if not g.isalpha() or len(g) != 1:
        print("Enter one letter!")
        continue

    if g in guessed:
        print("Already guessed!")
        continue

    guessed.add(g)

    if g not in word:
        tries -= 1