player1_name = input('Input player 1 name: ')
player1_score = int(input('Input score: '))
player2_name = input('Input player 2 name: ')
player2_score = int(input('Input score: '))

if player1_score>player2_score:
    print("Player 1 \""+ str(player1_name) + "\" has won, with a score of " + str(player1_score))
elif player1_score<player2_score:
    print("Player 2 \""+ str(player2_name) + "\" has won, with a score of " + str(player2_score))
elif player1_score == player2_score:
    print("Players 1 and 2 have the same score, "+ str(player2_score) +" , the match is a draw")
