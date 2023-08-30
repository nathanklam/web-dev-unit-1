#not against computer i guess
player1wins = 0
player2wins = 0
player1status = "alive"
player2status = "alive"


#def helper_function(player1input, player2input):


def play_game():
    player1 = input("Player 1, choose rock, paper, or scissors: ")
    player2 = input("Player 2, choose rock, paper, or scissors: ")

    #find out who wins
    if player1 == player2:
        print("tie, try again")
    #this is stupid but uh; add knife, and pen stuff; these triumph over the normal game stuff
    #instead of wins, it just kills the other person ???????
    elif player1 == "gun":
        player1wins += 1
    elif player2 == "gun":
        player1wins += 1
    else:
        print("i havent gotten to this point yet")
    #now for the actual stuff
    #pseudocode
    #helper_function():
        #if one is scissors and one is paper, the person with scissors gets a point
        #if one is paper and one is rock, the person with paper gets a point
        #if one is rock and one is scissors, the person with rock gets a point

play_game()

#print("welcome to a very normal game of rock paper scissors.")
turns = 0
#while turns <= 5:
    #run game, internal parts of function should add 1 to "turns"

    #compare who has the highest number of points at the end or whoever is still alive
    #if (both players are still alive)
        #if player1wins > player2wins
            #
        #elif player2wins < player1wins
            #
    #else (one is dead)
        #if player1status == "dead"
            #
        #elif player2status == "dead"
            #

    #give the victory to that player