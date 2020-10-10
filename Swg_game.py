# This is a computer version of Snake, Water , Gun game
# Play against the computer 
import random

options = {1:"Snake", 2:"Water", 3:"Gun"}
def comp():
    return random.choice(list(options.keys()))

score = {"player":0, "computer":0}
print("Welcome to the Game!\nHere you have choose your character from no. 1.Snake 2.Water 3.Gun")
print("The computer will also choose a character\nThe winning criteria is\n\n")
print("The Gun wins over snake, snake wins over water, and water wins over gun")


def find_winner(player1, player2, score):
    if player1 == 1 and player2 ==2 :
        score['player'] += 1
        print("You Win!\n")
    elif player1==1 and player2==3:
        score['computer'] += 1
        print("Computer Wins!\n")
    elif player1==2 and player2 == 1:
        score['computer'] +=1
        print("Computer Wins!\n")
    elif player1==2 and player2 == 3:
        score['player'] += 1
        print("You Win!\n")
    elif player1 == 3 and player2 == 1:
        score['player']+=1
        print("You Win!\n")
    elif player1 == 3 and player2 == 2:
        score['computer']+=1
        print("Computer Wins!\n")
    else:
        print("Game Tie!\n")


for i in range(5):
    choose = int(input("Choose your character = "))
    compuin = comp()
    print("Computer's character =", options[compuin])
    find_winner(choose, compuin, score)

print("Final Score\n", [i for i in score.items()])
print("Thank you for playing the game")
        
