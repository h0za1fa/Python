import random
# words = ["picture", "teacher", "morning", "holiday", "animals", "brother", "friends", "monster", "chicken", "calling"]
words=['eeeeeee','aaaaaaa']
word=random.choice(words)
wordchar=[]

def makelist(word):
    for n in range (0,7):
        char=word[n]
        wordchar.append(char)
    return wordchar

def find_index(letter,wordchar):
    if letter in wordchar:
        pos=wordchar.index(letter)
    else:
        pos=None
    return pos

wordchar=makelist(word)
blank=['_','_','_','_','_','_','_']
# print(wordchar)
while True:
    letter=input('Enter a letter: ')
    for n in range(0,7):
        indexes=find_index(letter,wordchar)
        if indexes != None:
            blank[indexes]=letter
    print(blank)
            