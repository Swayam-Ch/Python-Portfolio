# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
print(art.logo)

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_amount = 0
    for bidder in bidding_dictionary:
        amount = bidding_dictionary[bidder]
        if amount > highest_amount:
            highest_amount = amount
            winner = bidder

    print(f"The winner is {winner} wih a bid of ${highest_amount}")

bids = {}
continueBidding = True
while continueBidding:
    name_input = input("What is yur name: ")
    user_bid = int(input("What is your bid: $"))
    bids[name_input] = user_bid
    question = input("Are there any other bidders? Type 'yes or 'no'.").lower()
    if question == "no":
        continueBidding = False
        find_highest_bidder(bids)
    elif question == "yes":
        print("\n" * 100)

















