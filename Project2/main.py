# ----------------------- Perfect Number Guesser game. -------------------------------

from random import randint


class PerfectGuess :
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.AIGuess = self.generate_ai_number()

    def start(self):
        self.display_instructions()
        self.player_guess()

    def display_instructions(self):
        if self.difficulty == 1:
            print("You have 10 attempts to guess the perfect number between 1 and 10.")
        elif self.difficulty == 2:
            print("You have 7 attempts to guess the perfect number between 1 and 50.")
        elif self.difficulty == 3:
            print("You have 5 attempts to guess the perfect number between 1 and 100.")
        else:
            print("Invalid difficulty level selected.")
            return
        
    
    def generate_ai_number(self):
        if self.difficulty == 1:
            return randint(1, 10)
        elif self.difficulty == 2:
            return randint(1, 50)
        elif self.difficulty == 3:
            return randint(1, 100)
        else:
            return None
        
    def player_guess(self) :
        playerNumber = -1
        attempts = 0
        max_attempts = 10 if self.difficulty == 1 else (7 if self.difficulty == 2 else 5)

        while attempts < max_attempts:
            try:
                playerNumber = int(input("Enter your guess: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            if playerNumber == self.AIGuess:
                print("Congratulations! You've guessed the perfect number.")
                return
            elif playerNumber < self.AIGuess:
                print(f"Hmm... that's not quite right, try a lower number! You have {max_attempts - attempts - 1} tries left")
            else:
                print(f"Hmm... that's not quite right, try a higher number! You have {max_attempts - attempts - 1} tries left")
            attempts += 1

        print(f"Sorry, you've used all your attempts. The perfect number was {self.AIGuess}.")

while True:
    print("Menu : \n1. Easy\n2. Medium\n3. Hard")
    try:
        difficulty = int(input("Select Difficulty Level (1-3): "))
        if difficulty not in [1, 2, 3]:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter 1, 2, or 3.")
        continue

    game = PerfectGuess(difficulty)
    game.start()

    play_again = input("Play again? (y/n): ").strip().lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break