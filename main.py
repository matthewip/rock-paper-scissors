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

import random

def print_choice(choice):
  if choice == 0:
    print_choice_with_newline(rock)
  elif choice == 1:
    print_choice_with_newline(paper)
  elif choice == 2:
    print_choice_with_newline(scissors)

def print_choice_with_newline(choice):
  print("\n"+choice)

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print_choice(user_choice)

computer_choice = random.randint(0,2)
print("\nComputer chose: ")
print_choice(computer_choice)

# Computer wins scenarios
if (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 0):
  print("\nYou lose")
# User wins scenarios  
elif (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1) or (user_choice == 0 and computer_choice == 2):
  print("\nYou win")
# Draw scenario
elif (user_choice == computer_choice):
  print("\nDraw.")
