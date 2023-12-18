####Basic Rules
#1.Only small letters
#2.Only single letters can be inputed
#3.Have fun:)

###This part generates a random "word"
#Feel free to replace z by your  own word and comment out this part
import random
x=[]
for y in range(random.randint(3, 10)):
    x.append(chr(ord('a')+random.randint(0, 25)))
z="".join(x)

word=list(z)
count=0
tries=0
shown=[]
while count<len(word):
    shown.insert(count,"*")
    count+=1
guess="*"
while 1:
    count=0
    while count<len(word):
        if guess==word[count]:
            shown[count]=guess
        count+=1
    count=0
    while count<len(shown):
        print(shown[count], end=" ")
        count+=1
    print("")
    if "*" not in shown:
        break
    print("Number of guesses: "+str(tries))
    guess=input("Please input a guess: ")
    tries+=1
    if guess=="Cheatcode":  ##Fun things and Easter Eggs
        print(z)
    elif guess==z:
        break
print("Congratulations! You have won in "+str(tries)+" tries!")