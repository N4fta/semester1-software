import random
import time
from playsound import playsound


def generate_code(difficulty):
    if difficulty=="n":
        i,r=6,4
    elif difficulty=="h":
        i,r=8,4
    elif difficulty=="extreme":
        i,r=9,5
    x=[]
    for y in range(r):
        x.append(str(random.randint(1, i)))
    z="".join(x)
    z=int(z)
    return z  #returns an integer

def manual_code(difficulty):
    code=0
    i=0
    if difficulty=="n":
        while 1:
            code=input("Input a 4-digit code with numbers between 1-6: ")
            try:
                int(code)
            except:
                print("The Mastermind is disappointed.")
                i+=1
                if i>=3:
                    print("The EXTREME difficulty has been selected")
                    difficulty="extreme"
                    break
            for y in code:
                y=int(y)
                if y<1 or y>6:
                    code="11111"
                    break
            if len(code)!=4:
                print("The Mastermind is disappointed.")
                i+=1
                if i>=3:
                    print("The EXTREME difficulty has been selected")
                    difficulty="extreme"
                    break
            else:
                break
    elif difficulty=="h":
        while 1:
            code=input("Input a 4-digit code with numbers between 1-8: ")
            try:
                int(code)
            except:
                print("The Mastermind is disappointed.")
                i+=1
                if i>=3:
                    print("The EXTREME difficulty has been selected")
                    difficulty="extreme"
                    break
            for y in code:
                y=int(y)
                if y<1 or y>8:
                    code="11111"
                    break
            if len(code)!=4:
                print("The Mastermind is disappointed.")
                i+=1
                if i>=3:
                    print("The EXTREME difficulty has been selected")
                    difficulty="extreme"
                    break
            else:
                break
    if difficulty=="extreme":
        while 1:
            code=input("Input a 5-digit code with numbers between 0-9: ")
            try:
                int(code)
            except:
                print("The Mastermind is disappointed.")
                i+=1
                if i>=3:
                    print("The code has been automatically generated")
                    code=generate_code(difficulty)
                    break
            if len(code)!=5:
                print("The Mastermind is disappointed.")
                i+=1
                if i>=3:
                    print("The code has been automatically generated")
                    code=generate_code(difficulty)
                    break
            else:
                break
    code=int(code)
    return code  #returns an integer

def initialize(difficulty, y):
    i=0
    o=0
    while 1:
        if  not isinstance(difficulty, str) or difficulty !="n" and difficulty !="h" and difficulty !="extreme":
            if i==0:
                difficulty=input("What difficulty do you wish for?(N,H,EXTREME) ")
                difficulty=difficulty.lower()
                i+=1
                continue
            print("The Mastermind is disappointed.")
            i+=1
            if i>3:
                print("The EXTREME difficulty has been selected")
                difficulty="extreme"
                continue
            difficulty=input("What difficulty do you wish for?(N,H,EXTREME) ")
            difficulty=difficulty.lower()
            continue
        if not isinstance(y, str) or y!="y" and y!="n":
            if o==0:
                y=input("Will you input your own code?(Y/N) ")
                y=y.lower()
                o+=1
                continue
            print("The Mastermind is disappointed.")
            o+=1
            if o>4:
                print("The EXTREME difficulty has been selected and the code will be generated automatically.")
                difficulty="extreme"
                y="n"
                continue
            y=input("Will you input your own code?(Y/N) ")
            y=y.lower()
            continue
        break
    if y=="y":
        code=manual_code(difficulty)
    elif y=="n":
        code=generate_code(difficulty)

    #shown is the string that shows how many digits you guessed right
    shown=[]
    for y in str(code):
        shown.append("*")

    #digits is a list of the numbers of code to compare against shown
    digits=list(str(code))
    return code, difficulty,shown, digits, y   

def integrety_check(guess, r):
    #getting correct values for difficulty
    if difficulty=="extreme":
        r=5
    elif difficulty=="h":
        r,d=4,8
    elif difficulty=="n":
        r,d=4,6
    else:
        print("Something went wrong")
    
    #if temp becomes true theres something wrong with the input
    temp=False
    try:
        int(guess)
    except:
        temp=True
        return temp
    if len(guess)!=r:
        temp=True
    #checking digits are in appropriate range
    elif r!=5:
        guess_list=list(str(guess))
        for y in range(r-1):
            if not (int(guess_list[y])>0 and int(guess_list[y])<=d):
                temp=True
    return temp

def check_guess(digits, shown, guess_list):

    #Reveals guessed letters
    for y in range(0,len(guess_list)):
        if guess_list[y]==digits[y]:
                shown[y]=guess_list[y]
                guess_list[y]=-1       #removes the guesses in the right spot from the follow up code

    #Counts correct letters not in the right spot
    n=[]
    for y in range(0,len(guess_list)):
        if guess_list[y]!=-1:
            if guess_list.count(guess_list[y])>=digits.count(guess_list[y])-shown.count(guess_list[y]):
                n.append(digits.count(guess_list[y])-shown.count(guess_list[y]))
            elif guess_list.count(guess_list[y])<digits.count(guess_list[y])-shown.count(guess_list[y]):
                n.append(guess_list.count(guess_list[y]))
            else:
                print("Something definitely went wrong")
            for x in range(0,len(guess_list)):             #removing duplicate guesses so program doesnt repeat itself
                if guess_list[y]==guess_list[x] and y!=x:
                    guess_list[x]=-1
        else:
            n.append(0)
    return shown, n


######################################## Intro Game
print("""\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n                Welcome to the Mastermind Game
          
          In this game there will be a 4-digit code you have to guess. This code
          can be inputed by you or ramdomly choosen in the menu.
          You can also choose between three difficulties. In normal mode the
          digits of the code vary between 1-6 and you have 10 lives, in hardmode
          they vary between 1-8 and you have 7 lives, finally in EXTREME MURDER 
          MODE they vary between 0-9, the code is 5-digits long and you have 5 lives.
                
          Note: The code can have repeating digits.

          Rules:
          1.You input a valid integer, it must be as long as the code you are guessing
          2.If you get a number right and in the correct place the Mastermind will inform you
          3.If you get a number right but it is in the wrong place the Mastermind will also inform you
          4.You have a limited number of lives, if you can not solve it before then...May God have Mercy on your soul...
          """)
input("\n\n\n\n\n          Are you ready? ")
for i in range(3):
    print("          .")
    time.sleep(1)
print("          No you are not, I hope you make it out alive")
time.sleep(2)
yes_list=["yes", "ye", "y", "yup", "ya", "of course", "absolutely", "start", "restart"]





############################################# Main Game
while 1:
    for i in range(25):
        print("\n")
    print("The Mastermind welcomes you to his Game\n\n")
    y=""
    difficulty=""
    code, difficulty, shown, digits, y=initialize(difficulty,y)
    print("Let the games begin!")

    #Lives
    if difficulty=="extreme":
        lives,tries=5,5
    elif difficulty=="h":
        lives,tries=7,7
    elif difficulty=="n":
        lives,tries=10,10
    else:
        print("Something went wrong")

    i=0
    winner=False
    temp=""
    for i in range(25):
        print("\n")
    i=0

    
    ################################################## Game Loop
    while winner==False:

        #Asking for a guess
        guess=input('\n\nLives left: '+str(lives)+'\n\nThe Mastermind invites you to take a guess: ')
        if guess=="cheatcode":                                         #Fun things and Easter Eggs
            print("\n",(code))
            continue
        print("")

        #Checking if input is valid
        if integrety_check(guess,difficulty):
            i+=1
            lives-=1
            print("The Mastermind is disappointed.")
            if i>=3 and difficulty!="extreme":
                print("The code has been reset, the EXTREME difficulty has been selected and your lives have been set to 5.")
                difficulty,y="extreme","n"
                code, difficulty, shown, digits, y=initialize(difficulty,y)
                if lives<5:
                    print("You found an exploit. Congratulations.")
                    lives=5
                else:
                    lives=5
                i=0
                #Checking if all lives were spent
                if lives<=0:
                    break
                continue
            elif i>=3 and difficulty=="extreme":
                difficulty,y="extreme","n"
                code, difficulty, shown, digits, y=initialize(difficulty,y)
                print("The code has been reset, but your lives haven't")
                i=0
                #Checking if all lives were spent
                if lives<=0:
                    break
                continue
            #Checking if all lives were spent
            if lives<=0:
                break
            continue
        guess_list=list(str(guess))

        #checking the guess against the code, updating "shown" accordingly and printing it
        shown, n=check_guess(digits,shown,guess_list)
        for y in range(len(n)):
            while n[y]>0:
                print("You're not wrong, but neither are you right. Try "+str(guess_list[y])+" in another spot.")
                n[y]-=1
        
        print("\n",shown)
        lives-=1
        time.sleep(0.5)

        #Check to see if code has been fully guessed
        for y in range(0, len(shown)):
            if  shown[y]!=digits[y]:
                winner=False
                break
            else:
                winner=True

        #Checking if all lives were spent
        if lives<=0:
            break

    if winner==False:
        print("\n\nI am sorry, I truly am")
        playsound('Study Week3\Exercises Week3\jumpscare.mp3')
        print('''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢉⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡅⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠄⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⣉⣁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣈⡏⠹⡟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣦⡀⠀⠈⣿⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⠃⣰⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⠘⣿⣤⡀⢀⡀⠀⠀⠉⠻⡟⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⢉⣁⣡⣤⣴⡾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣾⣹⣿⣾⢿⣆⣠⠀⠀⢁⠈⣿⡿⠀⠈⣿⠟⠀⠈⠹⣿⡏⠀⠀⠈⣿⡟⠁⠸⣿⠃⣼⣏⢀⡆⣴⣿⣿⡟⡅⣿⢱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣹⣿⡿⢿⣶⣷⣼⣷⣟⠁⠀⠀⡟⠀⠀⠀⠀⣽⡇⠀⠀⠀⠨⠄⠀⠀⢙⡀⢃⣸⣾⣿⣼⣿⢸⣧⣷⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣷⡈⣷⡈⣻⣿⣼⣦⣀⣰⠃⠀⠀⠀⠀⠙⠁⠀⡀⠀⠊⣠⣀⣤⣾⣷⡌⣯⣿⢟⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡺⠇⢹⣿⣿⣿⡿⣿⣤⣀⣀⣤⣤⣴⣄⠀⠃⣄⣀⢿⡿⠛⠿⣿⠙⣿⣷⣼⣧⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣾⠹⣿⡿⠁⢹⡃⠈⠉⣿⠁⠊⡿⠀⠈⣿⠀⢸⡇⠀⠀⢿⡄⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣿⠁⣠⣾⠇⠀⢠⣧⠀⢠⡇⠀⢀⣿⡀⢸⣇⠀⢠⣸⣷⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣦⣠⣾⣿⣶⣾⣷⣤⣸⣿⣿⣾⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
            ''')
        break

    ########################################################### Conclusion
    print("\nCongratulations you can live another day. Took you "+str(tries-lives)+" tries to get there but you did get there.")
    time.sleep(5)
    print("You can go now, bye bye")
    time.sleep(4)
    print("Seriously leave.")
    time.sleep(5)
    for i in range(5):
        print(".")
        time.sleep(1)
    temp=input("Are you crazy do you want to be put through that again?! ")
    temp=temp.lower()
    if temp in yes_list :
        for i in range(5):
            print(".")
            time.sleep(1)
        print("*sights* It's your live...good luck I guess")
        time.sleep(1.5)
    else:
        print("So you are still sane, good. I'll take you out then.")
        time.sleep(1.5)
        print("The Mastermind awaits your return")
        break
input("Press enter to quit")