import random

with open("words.txt", "r") as file:
    allText = file.read()
    words = allText.split()
    
print(random.choice(words))