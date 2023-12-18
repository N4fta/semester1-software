####Basic Rules
#1.Only single letters can be inputed
#2.Have fun:)

import random

##This part generates a random "word"
def generate_nonsense():
    x=[]
    for y in range(random.randint(3, 10)):
        x.append(chr(ord('a')+random.randint(0, 25)))
    z="".join(x)
    return z                     #returns a word in the form of a string

#Prints progress
def print_word(word, shown, guess):
    temp=0
    for y in range(0,len(word)):               #Reveals guessed letters
        if guess==word[y]:
                shown[y]=guess
                temp=1           #so that only incorrect guesses count as tries
    for y in range(40):
        print("\n\n")
    for y in range(0,len(shown)):              #prints current revealed word
        print(shown[y], end=" ")
    print("\n\n\n\n\n\n\n\n\n\n\n")
    if guess=="cheatcode":       #Fun things and Easter Eggs
        print("\n",word)
    elif guess=="".join(word):
        temp=2
    return word, shown, temp
    
    
    
#Game Loop
while 1:
    #Initialization (stuff that runs once per game)
    word=list("autocarro")#generate_nonsense())
    tries=-1
    guess="0"
    shown=[]
    for y in range(0,len(word)):
        shown.insert(y,"*")
    
    #Main Game (Looping part/Guesses)
    while 1:
        word, shown, temp =print_word(word, shown,guess)
        if "*" not in shown:
            break
        if temp==2:
            break
        elif temp !=1:
            tries+=1
        print("\nNumber of guesses: "+str(tries))
        guess=input("Please input a guess: ")
        guess=guess.lower()
    print("\nCongratulations! You have won in "+str(tries)+" tries!")
    if input("\nWould you like to play again?(y/n)").lower()!="y":
        break