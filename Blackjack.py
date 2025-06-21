from os import remove

import art
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    if computer_score == user_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"



def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    continue_playing = True

    user_cards.append(deal_card())
    user_cards.append(deal_card())

    computer_cards.append(deal_card())
    computer_cards.append(deal_card())

    while continue_playing:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: [{user_cards}], current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            continue_playing = False
        else:
            question = input("Do you want to draw another card. Type 'y' or 'n': ")
            if question == "y":
                user_cards.append(deal_card())
                calculate_score(user_cards)
            else:
                continue_playing = False

    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of blackjack. Type 'y' or 'n': ") == "y":
    print("\n" * 100)
    play_game()
