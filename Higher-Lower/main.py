import art
import game_data
import random
from replit import clear
# person_a = random.choice(game_data.data)
# person_b = random.choice(game_data.data)

def random_account():
  return random.choice(game_data.data)


def check_answer(guess, a_follows, b_follows):
  if a_follows > b_follows:
    return guess == "a"
  else:
    return guess == "b"

def game():
  print(art.logo)
  score = 0
  # print(person_a["follower_count"])
  # print(person_b["follower_count"])
  person_a = random.choice(game_data.data)
  person_b = random.choice(game_data.data)
  game_go_on = True
  while game_go_on:
    person_a = person_b
    person_b = random_account()

    while person_a == person_b:
      person_b = random_account
    print(f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}")
    
    print(art.vs)
    
    print(f"Against B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}")
    
    guess = input("Who has more followers? Type 'A' or 'B'").lower() 
  
    a_follows = person_a["follower_count"]
    b_follows = person_b["follower_count"]
    correct = check_answer(guess, a_follows, b_follows)
    clear()
    print(art.logo)
    if correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_go_on = False
      print(f"Sorry, that's wrong. Final score: {score}")

  
  # print(answer)
  
  
  # print(f"Your score is {score}")

game()


