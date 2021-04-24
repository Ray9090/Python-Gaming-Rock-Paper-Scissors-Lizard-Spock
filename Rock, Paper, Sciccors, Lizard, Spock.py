from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

player1 = t[randint(0,4)]

player2 = False

while player2 == False:

    player2 = input("Rock, Paper, Scissors, Lizard, Spock?\n")
    
    if player2 == player1:
        print("Tie!!!")
        
    elif player2 == "Rock":
        if player1 == "Paper":
            print("You lose.", player1, "covers", player2)
        elif player1 == "Lizard":
            print("You win.", player2, "Crushes", player1)
        elif player1 == "Spock":
            print("You Lose.", player1, "Vaporizes", player2)    
        else:
            print("You win.", player2, "smashes", player1)
            
    elif player2 == "Paper":
        if player1 == "Scissors":
            print("You lose.", player1, "cut", player2)
        elif player1 == "Lizard":
            print("You lose.", player1, "eats", player2)
        elif player1 == "Spock":
            print("You win.", player2, "disproves", player1)
        else:
            print("You win.", player2, "covers", player1)
            
    elif player2 == "Scissors":
        if player1 == "Rock":
            print("You lose.", player1, "smashes", player2)
        elif player1 == "Lizard":
            print("You win.", player2, "decapitates", player1)
        elif player1 == "Spock":
            print("You lose.", player1, "smashes", player2)
        else:
            print("You win.", player2, "cut", player1)
    
    elif player2 == "Lizard":
        if player1 == "Rock":
            print("You lose.", player1, "crushes", player2)
        elif player1 == "Paper":
            print("You win.", player2, "eats", player1)
        elif player1 == "Scissors":
            print("You Lose.", player1, "decapitates", player2)
        else:
            print("You win", player2, "poisons", player1)
    
    elif player2 == "Spock":
        if player1 == "Rock":
            print("You win.", player2, "vapories", player1)
        elif player1 == "Paper":
            print("You lose.", player1, "disproves", player2)
        elif player1 == "Scissors":
            print("You win.", player2, "smashes", player1)
        else:
            print("You lose.", player1, "poisons", player2)
    
    else:
        print("Try Again!")
    
    player2 = False
    player1 = t[randint(0,4)]
    
