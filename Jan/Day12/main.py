################################
##### Number-guessing Game #####
################################
import random

#Beginning of the Game
guesses = 0
print("-The Number-guessing Game-")
print("There is a Number between 1 and 100! Can you quess it correctly?")
correct_input = False

#Player Chooses the dificulty of the game and checks for a valid input
while not correct_input:
    difficulty = input("Choose a Difficulty. Type 'easy' or 'hard': ")
    if difficulty == "hard":
        guesses = 5
        correct_input = True
    elif difficulty == "easy":
        guesses = 10
        correct_input = True
    else:
        print("Wrong input")

# A random number gets generated
number = random.randint(1,100)
playing = True

#The game takes place and finishes, when the player guessed correctly or closes if not
while playing:
    if guesses == 0:
        print(f"You have no more attempts left. The number was: {number}")
        print("Better luck next time buddy :P")
        playing = False
    else:
        print(f"You have {guesses} attempts remaining to find the number!")
        guess = int(input("Make a guess: "))
        if guess > number:
            print("Too high.")
            guesses -= 1
        elif guess < number:
            print("Too low")
            guesses -= 1
        else:
            print("You guessed correctly")
            print("That was the right number!")
            playing = False
