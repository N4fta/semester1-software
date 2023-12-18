# This version contains function definitions
# but the functions have not been implemented
# Analysing marks in Long Jump

# Function for reading the marks of a player:
def read_marks(nameOfPlayer):
    scores=[]
    temp=0
    while 1:    
        temp=input('Please input marks for player '+ nameOfPlayer+ '(or press "enter" to exit):')
        if temp =="x":
            scores.append("None")
        elif temp=="":
            break
        else:
            scores.append(int(temp))
    return scores


# Function for calculating the best mark of a player:
def find_best(marks):
    best=0
    for i in marks:
        if not isinstance(i, int):
            continue
        elif i>best:
            best=i
    return best


# Function for calculating the winner or winners,
# given their best marks:
def determine_winner(nameA, nameB, bestA, bestB):

    """ Assumes 'bestA' and 'bestB' are each either None or an integer.
        Returns a list possibly including each of 'nameA' and 'nameB'
                depending on the best marks between 'bestA' and 'bestB'. """

    if bestA == None:
        if bestB == None:
            winners = []
        else:
            winners = [nameB]
    else:
        if bestB == None:
            winners = [nameA]
        else:
            if bestA > bestB:
                winners = [nameA]
            elif bestA < bestB:
                winners = [nameB]
            else:
                winners = [nameA, nameB]
    
    return winners

# Function for outputting the winner or winners,
# if there are any:
def output_winner_result(namesOfWinners):

    """ Assumes 'namesOfWinners' is a list of strings.
        Returns nothing but prints a result. """

    if len(namesOfWinners) == 0:
        print("Nobody wins.")
    elif len(namesOfWinners) == 1:
        print("Player", namesOfWinners[0], "wins.")
    else:
        print("It is a tie between player", namesOfWinners[0],
                "and player", namesOfWinners[1] + ".")

# Main program:

# Read the marks for both player A and player B:
marksA = read_marks("A")
marksB = read_marks("B")

# Calculate the best mark for both player A and player B:
bestA = find_best(marksA)
bestB = find_best(marksB)

# Calculate the winners and output the result:
winners = determine_winner("A", "B", bestA, bestB)
output_winner_result(winners)
