from banner import logo,vs
from data import data
import random
import os

print(logo)

def format_data(account):
    """Take the account data and returns the printable format."""
    return f"{account["name"]}, a {account["description"]}, from {account["country"]}"

def check_answer(guess, a_followers,b_followers):
    """Take the user guess and follower counts and returns if they got it right. """
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    

score = 0
game_should_countinue = True

account_b = random.choice(data)

while game_should_countinue:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B':").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess,a_follower_count,b_follower_count)

    os.system('cls')
    print(logo)

    if is_correct:
        score+=1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_should_countinue = False