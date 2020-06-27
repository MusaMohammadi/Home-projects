from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set playerdesc to False
player = False

while player == False:
#set playerdesc to True
    playerdesc = input("Rock, Paper, Scissors?")
    if playerdesc == computer:
        print("Tie!")
    elif playerdesc == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", playerdesc)
        else:
            print("You win!", playerdesc, "smashes", computer)
    elif playerdesc == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", playerdesc)
        else:
            print("You win!", playerdesc, "covers", computer)
    elif playerdesc == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", playerdesc)
        else:
            print("You win!", playerdesc, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    #playerdesc was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]