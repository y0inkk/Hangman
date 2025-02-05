import random

def get_word():
    with open("words.txt", "r") as file:
        allText = file.read()
        words = allText.split()
    return random.choice(words)   



def underscores():
    for i in randomWord:
        print("_", end=" ")
    
randomWord = get_word()
print(randomWord)


stages = ['''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']



    


def gameloop():
    stages_length = len(stages)
    chances = 7
    isPlaying = True
    underscores()
    
    while isPlaying:
        length = len(randomWord)
        print()
        userInput = str(input("\nEnter guess: "))
        
        if len(userInput) > length:
            print(f"\nTry guessing the word which has {length} letters")
            continue
        elif len(userInput) < length:
            print(f"\nTry guessing the word which has {length} letters")
            continue
        
        chances -=1
        print("\nletter exist in word: ")
        for i in randomWord:
            if i in userInput:
                print(i, end=" ")
            else:
                print("_", end=" ")
                    

        
        
        if userInput == randomWord:
            print()
            print(f"\nYay, you won!! The word was: {randomWord}")
            isPlaying=False
            break
        else:
            print(f"\nchances left: {chances}")
            print(stages[stages_length - 1])
            stages_length -=1
        
            
        if chances == 0:
            print()
            print(f"\nYou lost. Do try again")
            isPlaying = False
            break
        
    
        

if __name__ == "__main__":
    
    gameloop()
    