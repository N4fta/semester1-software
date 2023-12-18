classdic = {
    "ICT":313,
    "Chemistry":578,
    "Megatronics":101,
    "English":312,
    "Physics":109,
    "Biomed":105,
    "Free period": "Go home"
}
#Classroom numbers are in string form to easily print

Name=input("Hello student, please input your name and the class you wish the know the room of.\nName: ")
Class=input("Class: ")

if Class in classdic:
        print("Hello "+Name+", go to room "+str(classdic[Class])+" for "+Class+" class")
else:
        print("I don't know which room that class is in.")