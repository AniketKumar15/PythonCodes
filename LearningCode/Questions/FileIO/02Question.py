# High Score Maker
import random


def game():
    name = input("Enter Your Name: ")
    score = random.randint(1, 100)
    print(f"{name}, your score is {score}")

    high_score = 0

    with open("HighScore.txt", "r") as f :
       content = f.read().strip()
       if content.isdigit():
                high_score = int(content)

    if(score > high_score):
        print("Yaa! New High Score")
        with open("HighScore.txt", "w") as f :
            f.write(name + ": " + str(score))
    else:
        print("Better Luck Next Time")

game()
    
