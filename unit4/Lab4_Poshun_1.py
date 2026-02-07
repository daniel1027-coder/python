""""
Deal Cards
Poshun Lin
A program that simulates dealing a hand of cards. 
The program will ask the user how many cards to deal and then generate that many random cards.
No starter code
02-06-2026
"""
import random

card_number= ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
card_suits= ("c","h", "s","d")

number_cards= int(input("How many cards do you want?"))

deck=[]
for number in card_number:
    for suit in card_suits:
        deck.append(number + suit)

random.shuffle(deck)

hand= []
for card in range(number_cards):
    hand.append(deck.pop())

print("The cards in your hand")
for card in hand:
    print(card)

print("Total number of cards:", len(hand))