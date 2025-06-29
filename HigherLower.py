import random

import art
import game_data
print(art.logo)
score = 0

def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def compare(user_guess, first, second):
    if first > second:
        return user_guess == "a"
    else:
        return user_guess == "b"


game_is_running = True
two = random.choice(game_data.data)
while game_is_running:
    one = two
    two =  random.choice(game_data.data)
    print(f"Compare A: {format_data(one)}")
    print(art.vs)
    print(f"Compare B: {format_data(two)}")
    user_input = input("Who has more followers? Type 'A' or 'B'")

    one_follower_count = one["follower_count"]
    two_follower_count = two["follower_count"]

    is_correct = compare(user_input, one_follower_count, two_follower_count)

    if is_correct:
        score += 1
        print(f"You're right. Current score: {score}")
        game_is_running = True
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_is_running = False

