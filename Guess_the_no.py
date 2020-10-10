# Let a no be stored in a variable 
n = 11
print("welcome to the Game!\nYou get 3 guesses. You have to guess a no. within it.\n"+
        "you will also get hint on unsuccessful guess\nStart guessing" )
# ask for the input of the user until he gets no right
guess = 3
while(guess>0):
    a = int(input("Enter a no "))
    if guess == 1:
        print("Oops! Wrong Guess\nYou LOST you have no more guesses")
        break
    if a != n:
        print("Oops! Wrong Guess")
        print("The No is less than your guess") if a > n else print("The No is greater than your guess")
        guess -= 1
    else : 
        print("You Won! you got the right ans")
        break