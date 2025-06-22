import art
import random
print(art.logo)


EASY_TURNS = 10
HARD_TURNS = 5


def guess_the_number(user_guess, number, turns):
    if user_guess < number:
        print(f"Too low.\nGuess again.")
        return turns -1
    elif user_guess > number:
        print(f"Too high.\nGuess again.")
        return turns - 1
    else:
        print(f"You got it. The number was {number}")


print("Welcome to the Number Guessing Game!")

print("I'm thinking of a number between 1 and 100.")



def set_difficulty():
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if choice == "easy":
        return EASY_TURNS
    else:
        return HARD_TURNS


def game():
    numbers = []
    for i in range(1, 101):
        numbers.append(i)
    num = random.choice(numbers)
    guess = 0
    turns = set_difficulty()
    while guess != num:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = guess_the_number(guess, num, turns)


    if guess == 0:
        print("You lose. No attempts left")
        return
    elif guess != num:
        print("Guess again")

game()







