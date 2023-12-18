import random

print('''Welcome to the Guess the number Game.
I will think of a number between 1-100 and you will try and guess it.
If you guess wrong, I'll tell you if you should guess higher or lower and this will repeat until you guess correctly.
I will also count the number of attempts you take to score you.''')
Game="y"
HighScore=0


while Game=="y":
    if HighScore==0:
        print("\nGood luck")
    else:
        print("Good luck\n\n\n\n\n\n\n")
    Answer=random.randint(1,100)
    attempts=0
    Guess=0

    while Guess!=Answer:
        while True:
            Guess=int(input("Enter a guess: "))
            if Guess<=100 and Guess >=1:
                break
            print("Please Input a number between 1-100")
        attempts+=1
        if Guess>Answer:
            print("Try lower")
        if Guess<Answer:
            print("Try higher")
    if attempts<HighScore or HighScore==0:
        HighScore=attempts
    print(f'You finally got it right! Congratulations!\nAnd it only took {attempts} attempts.\nFYI your High score is {HighScore}')
    Game=input("Do you want to play again?(Y/N)")
    Game=Game.lower()