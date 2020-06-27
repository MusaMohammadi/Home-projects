from random import randint

#Create a list of options of the user to play
t = ["Rock", "Paper", "Scissors"]

#Assign a random play to the computer
compPlay = t[randint(0,2)]

#set player to false 
player = False

while player == False:
    player = input("Rock, Paper or Scissors?")
    if player == computer:
        print("ooooo that's a tie")
    elif player == "Rock":
        if computer == "Paper" or computer == "Scissors":
            print("You lose!", computer, "covers", player)
        else 
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cuts", player)
        else 
            print("You win!", player, "smashes", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!", computer, "covers", player)
        else 
            print("You win!", player, "smashes", computer)
    else: 
        print("thats not a valid play. Please check your spelling")
        
    player = False 
    computer = t[randint(0,2)]