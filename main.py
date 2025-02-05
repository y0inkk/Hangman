import random


def get_word():
    with open("words.txt", "r") as file:
        allText = file.read()
        words = allText.split()
    return random.choice(words)


def underscores():
    for i in randomWord:
        print("_", end=" ")


unformattedRW = get_word()
randomWord = unformattedRW.lower()

stages = [
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]


def gameloop():
    print("------------------ Welcome to Hangman by Shrey ------------------")
    length = len(randomWord)
    stages_length = len(stages)
    chances = 7
    isPlaying = True
    underscores()
    print(f"\nThe word has {length} letters")

    while isPlaying:
        length = len(randomWord)
        userInput = str(input("\nEnter guess: "))

        if len(userInput) > length:
            print(f"\nTry guessing the word which has {length} letters")
            continue
        elif len(userInput) < length:
            print(f"\nTry guessing the word which has {length} letters")
            continue

        chances -= 1
        print("letters exist in word: ")
        for i in randomWord:
            if i in userInput:
                print(i, end=" ")
            else:
                print("_", end=" ")

        if userInput == randomWord:
            print()
            print(f"\nYou won!! The word was: {randomWord}")
            isPlaying = False
            break
        else:
            print(stages[stages_length - 1])
            stages_length -= 1

        if chances == 0:
            print()
            print(f"You lost. Do try again")
            print(f"The word was: {randomWord}")
            isPlaying = False
            break

        print(f"Lives: {chances} \n-----------------")
        


if __name__ == "__main__":

    play_input = str(input("\nDo you want to play(y/n): "))

    if play_input == "y":
        gameloop()
