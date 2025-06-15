import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
print(game[choice])

computer = random.randint(0, 2)
print(f"Computer chose:")
print(game[computer])

if choice >=3 or choice < 0:
    print("Invalid number. You lose")
if choice == 0 and computer == 2:
    print("You win")
elif choice == 2 and computer == 0:
    print("You lose")
elif choice > computer:
    print("You win")
elif computer > choice:
    print("You lose")
elif computer == choice:
    print("It is a draw")

