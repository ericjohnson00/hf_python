import random

suits = ["clubs", "diamonds", "hearts", "spades"]
faces = ["jack", "queen", "king", "ace"]
numbered = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]

def draw():
    the_suit = random.choice(suits)
    the_card =  random.choice(faces + numbered)
    return the_card, "of", the_suit

print(draw())

for _ in range(5):
    print(draw())
    
    
deck = set()

type(deck)
len(set())
print(dir(deck))

print(help(deck.add))