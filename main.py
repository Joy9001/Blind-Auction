import os

import art

auction_bids = {}
choice = True
while (choice):
  print(art.logo)
  print("Welcome to the secret auction program\n")
  name = input("What's your name?: ")
  bid = int(input("What's your bid?: $"))
  auction_bids[name] = bid
  another = input("Are there any other bidders? Type 'yes' or 'no': ")
  if (another == "no"):
    choice = False
    os.system('clear')
    break
  os.system('clear')

max_bid = 0
max_bidder = ""
for key in auction_bids:
  if (auction_bids[key] > max_bid):
    max_bid = auction_bids[key]
    max_bidder = key

print(
    f"The winner of the auction is {max_bidder} with highest bid ${max_bid}\n")
