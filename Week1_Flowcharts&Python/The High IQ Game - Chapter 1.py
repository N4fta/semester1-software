A="Y"
while (A=="Y" or A=="y"):
    N=int(input('Type any number lower than 10: '))
#check if intenger
    if N>=10:
        print("Invalid Input")
    elif N==9:
        print("You win!")
    else:
        print(str(N+1)+" I win!")

    A=input('Would you like to try again?(Y/N)')