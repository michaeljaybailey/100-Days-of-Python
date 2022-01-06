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

#Write your code below this line 👇

choice = input("What do you choose? Type Rock, Paper, or Scissors\n").lower()

user_choice = []

user_choice.append(choice)

if user_choice[0] == "rock":
  print(f"You chose {rock}")
elif user_choice[0] == "paper":
  print(f"You chose {paper}")
elif user_choice[0] == "scissors":
  print(f"You chose {scissors}")
else:
  print("Incorrect input")

computer_options = [rock, paper, scissors]
computer_num = len(computer_options)
computer_choice = computer_options[random.randint(0, computer_num - 1)]
if user_choice[0] == "rock" or user_choice[0] == "paper" or user_choice[0] == "scissors":
  print(f"The computer chooses {computer_choice}")

if user_choice[0] == "rock" and computer_choice == rock:
  print("It's a draw!")
elif user_choice[0] == "paper" and computer_choice == paper:
  print("It's a draw!")
elif user_choice[0] == "scissors" and computer_choice == scissors:
  print("It's a draw!")
elif user_choice[0] == "rock" and computer_choice == paper:
  print("You lose!")
elif user_choice[0] == "rock" and computer_choice == scissors:
  print("You win!")
elif user_choice[0] == "paper" and computer_choice == rock:
  print("You win!")
elif user_choice[0] == "paper" and computer_choice == scissors:
  print("You lose!")
elif user_choice[0] == "scissors" and computer_choice == rock:
  print("You lose!")
elif user_choice[0] == "scissors" and computer_choice == paper:
  print("You win!")




