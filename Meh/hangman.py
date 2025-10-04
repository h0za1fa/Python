import random
HANGMANPICS = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = [
    "apple", "grape", "pearl", "stone", "chair", "table", "spoon", "brush", "drink",
    "flame", "cloud", "river", "light", "sound", "plant", "dream", "block", "brave",
    "smart", "quick", "laugh", "piano", "storm", "train", "sheep", "house", "bread",
    "field", "sword", "match", "glass", "scale", "sugar", "beach", "world", "space",
    "brain", "truth", "grass", "earth", "water", "heart", "night", "plane", "tiger",
    "eagle", "mouse", "crown", "stone", "smile", "sweet"
]
word=random.choice(words)
wordchar=[]
fail=0

def makelist(word):
    for n in range (0,5):
        char=word[n]
        wordchar.append(char)
    return wordchar

wordchar=makelist(word)
blank=['_','_','_','_','_']
# print(wordchar)
while True:
    letter=input('Enter a letter: ')
    if letter in wordchar:
        for n in range (0,5):
            if letter == wordchar[n]:
                
                blank[n]=letter
    else:
        fail+=1
    print(blank)
    print(HANGMANPICS[fail])
    print('-------------------------------')
    if blank == wordchar:
        print('You saved him!')
    if fail == 6:
        print('He died!')
        print(f'your word was {word}')
        break

    
            