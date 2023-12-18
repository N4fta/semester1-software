import random
password="password"

attempts=0
while attempts<3:
    Attempt=input("Please enter your password: ")
    if Attempt==password:
        print("Password Correct")
        #Here we would proceed with the login
        break
    else:
        attempts+=1
        print("Password incorrect, "+str(3-attempts)+" attempts remmaining")

#####Account Blocking
if attempts>=3:     #This is just a failsafe so an account isn't blocked on accident
    password=str(random.randint(100000,999999))