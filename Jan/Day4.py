import random

rock = '''      #0
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''     #1
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''  #2
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# User is choosing his weapon of choise and it gets converted into a number
choise = input("Use your power! Rock (R), Paper (P) or Scissors (S): ")

# Generates the choise of the Computer
enemys_choise = random.randint(0, 2)

# Evaluates the game in every possible outcome:
if (choise == "R"):
    if (enemys_choise == 2):
        print("The computer choose Scissors. You win :)")
    elif(enemys_choise == 1):
        print("The computer choose Paper. You lose :(")
    elif(enemys_choise == 0):
        print("The computer choose Rock. It's a draw!")
elif(choise == "P"):
    if (enemys_choise == 0):
        print("The computer choose Rock. You win :)")
    elif(enemys_choise == 2):
        print("The computer choose Scissors. You lose :(")
    elif(enemys_choise == 1):
        print("The computer choose Paper. It's a draw!")
elif(choise == "S"):
    if (enemys_choise == 1):
        print("The computer choose Paper. You win :)")
    elif(enemys_choise == 0):
        print("The computer choose Stone. You lose :(")
    elif(enemys_choise == 2):
        print("The computer choose Scissors. It's a draw!")
