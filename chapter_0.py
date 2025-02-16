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

for suit in suits:
    for card in faces + numbered:
        deck.add((card, "of", suit))
        
print(len(deck))

print(deck)

print()

card = random.choice(list(deck))
print(card)

# for _  in range(5):
#     card = random.choice(list(deck))
#     print(card)
#     deck.remove(card)
    
print(len(deck))
deck.remove(card)
print(len(deck))

# Sharpen your pencil pg25

def draw():
    card = random.choice(list(deck))
    deck.remove(card)
    return card

print(draw())

card = ("ace", "of", "hearts")

# card in deck

if card in deck:
    print("Yes")
else:
    print("No")
    