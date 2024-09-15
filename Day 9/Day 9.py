from art import logo
print(logo)

def find_highest_bidder(bidding_dic):
    winner = ""
    highest_bid = 0

    max(bidding_dic)

    for bidder in bidding_dic:
        bid_amt = int(bidding_dic[bidder])
        if bid_amt > highest_bid:
            highest_bid = bid_amt
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}.")


bids = {}

continue_bidding = True

while continue_bidding:
    name = input("What is your name?: ")
    price = input("What is your bid?: $")
    bids[name] = price
    should_continue = input("Are there any other bidders? Yes or No. \n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 30)


