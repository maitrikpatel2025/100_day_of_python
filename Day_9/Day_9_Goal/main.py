from art import logo

print(logo)

auction = [
           ]

def auction_members(member_name, member_bid_price):
    auc_mem = {}
    auc_mem["name"] = member_name
    auc_mem["bid"] = member_bid_price
    auction.append(auc_mem)

def winner():
    start_bid = 0
    for member in range(0, len(auction)):
        winner_bid = auction[member]["bid"]
        winner_name = auction[member]["name"]
        if int(winner_bid) > start_bid:
            start_bid = winner_bid

    print(f"{winner_name} is a winner of Auction. he bid ${winner_bid}")

end_auction = False
while not end_auction:
    name = str(input("Enter your name"))
    bid_price = int(input("Enter your Bid Price : $"))
    auction_members(name, bid_price)
    another_member = input("Do you want to enter another member in auction\n if yes type 'Yes' or 'No' : ")
    if another_member.lower() == 'yes':
        name = str(input("Enter your name"))
        bid_price = int(input("Enter your Bid Price : $"))
        another_member = input("Do you want to enter another member in auction\n if yes type 'Yes' or 'No' : ")
        auction_members(name, bid_price)
    elif another_member.lower() == "no":
        end_auction = True
        winner()
        break
    else:
        print("try again")
        another_member = input("Do you want to enter another member in auction\n if yes type 'Yes' or 'No' : ")


# Another solution

from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner1 = ""
  # bidding_record = {"Angela": 123, "James", "321"}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner1 = bidder
  print(f"The winner is {winner1} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":

