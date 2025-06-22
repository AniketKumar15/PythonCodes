'''
1 is snake
2 is water
3 is Gun

1 win with 2, 1 loose with 3
2 win with 3, 2 loose with 1
3 win with 1, 3 loose with 2

'''
import random

choices = {1: "Snake", 2: "Water", 3: "Gun"}

def SEG():
    computerPick = random.randint(1,3)

    playerPick = int(input("Enter Your Choice : "))

    if(playerPick > 3 or playerPick < 1):
        print("Invalid Input")
    else:
        if( playerPick == computerPick):
            print("Match Draw")
            print("You chose:", choices[playerPick])
            print("Computer chose:", choices[computerPick])
        elif (playerPick == 1 and computerPick == 2) or \
                (playerPick == 2 and computerPick == 3) or \
                (playerPick == 3 and computerPick == 1):
            print("Player Win")
            print("You chose:", choices[playerPick])
            print("Computer chose:", choices[computerPick])
        else:
            print("Computer Win")
            print("You chose:", choices[playerPick])
            print("Computer chose:", choices[computerPick])



playerOrNot = input("Do You Want to play [Y, N] : ")

while playerOrNot == 'Y' or playerOrNot == 'y':
    SEG()
    playerOrNot = input("Do You Want to play [Y, N] : ")
else:
    print("Thank You For Play")