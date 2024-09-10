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

options_list = [rock, paper, scissors]

num = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: \n"))
if 0 <= num <= 2:
    action = options_list[num]
    print("You chose:")
    print(action)

    print("Computer chose:")
    computer_choice = random.choice(options_list)
    print(computer_choice)

    if (action == rock and computer_choice == scissors) or \
            (action == paper and computer_choice == rock) or \
            (action == scissors and computer_choice == paper):
        print("You win!")
    elif (action == rock and computer_choice == paper) or \
            (action == paper and computer_choice == scissors) or \
            (action == scissors and computer_choice == rock):
        print("You lose!")
    else:
        print("It's a draw")
else:
    print("You typed an invalid number, you lose!")
