"""
FrenchDeck: A Python Card Deck Implementation

This module demonstrates several key Python concepts for beginners:

1. NAMEDTUPLES: 
   - Immutable, lightweight classes with named fields
   - Alternative to regular classes when you just need data containers
   - Automatically provides __repr__, __eq__, and other methods

2. SPECIAL METHODS (Magic Methods):
   - __init__: Constructor that runs when creating an instance
   - __len__: Enables len(deck) to work on your custom class
   - __getitem__: Enables indexing (deck[0]) and slicing (deck[1:5])
   - These make your class work with Python's built-in functions

3. LIST COMPREHENSIONS:
   - Concise way to create lists: [expression for item in iterable]
   - Nested comprehensions: [Card(r,s) for s in suits for r in ranks]
   - Equivalent to nested for loops but more Pythonic

4. CLASS vs INSTANCE ATTRIBUTES:
   - Class attributes (ranks, suits): shared by all instances
   - Instance attributes (self._cards): unique to each instance

5. PYTHON DATA MODEL:
   - By implementing __len__ and __getitem__, the deck works with:
     * len(), max(), min(), in operator, for loops, slicing, random.choice()
   - This is the "Python way" - make objects behave like built-in types

KEY LEARNING POINTS:
- Immutability: namedtuple cards can't be changed after creation
- Duck typing: If it walks like a sequence, Python treats it like one
- The power of special methods to integrate with Python's ecosystem
"""

import collections

# Create a Card namedtuple with rank and suit fields
# namedtuple creates a lightweight class with named fields
# Useful to define things like a database record, a class of object
# that are just bundles of attributes
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    # Class attributes for all cards in a standard deck
    # ranks: 2-10 as strings, plus face cards J, Q, K, A
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    # suits: standard four suits as a list
    suits = 'spades diamonds clubs hearts'.split()
    # suit values for ranking (spades highest, clubs lowest)
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def __init__(self):
        # Initialize the deck by creating all 52 cards
        # Nested list comprehension: for each suit, create cards for all ranks
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        # Return the number of cards in the deck (enables len(deck))
        return len(self._cards)

    def __getitem__(self, position):
        # Enable indexing and slicing (deck[0], deck[1:5], etc.)
        return self._cards[position]
    
    def __repr__(self):
        # Return a string representation that could recreate the object
        # Following Python convention: repr should be unambiguous and ideally executable
        return f'FrenchDeck()'
    
    def spades_high(self, card):
        # Calculate card value with spades being highest suit
        # rank_value: position of rank in ranks list (2=0, 3=1, ..., A=12)
        rank_value = FrenchDeck.ranks.index(card.rank)
        # multiply by 4 (number of suits) and add suit value for unique ranking
        return rank_value * len(self.suit_values) + self.suit_values[card.suit]


if __name__ == "__main__":
    from random import choice
    
    print("=== French Deck Examples ===\n")
    
    # Create a new deck
    deck = FrenchDeck()
    print(f"Created deck with {len(deck)} cards\n")
    
    # Getting specific cards by index
    print("--- Getting cards by index ---")
    print(f"First card: {deck[0]}")
    print(f"Last card: {deck[-1]}")
    print(f"Cards 5-7: {deck[5:8]}\n")
    
    # Getting a random card using choice()
    print("--- Getting random cards ---")
    print(f"Random card 1: {choice(deck)}")
    print(f"Random card 2: {choice(deck)}")
    print(f"Random card 3: {choice(deck)}\n")
    
    # Iterating over the deck to find specific cards
    print("--- Finding specific cards ---")
    target_rank = 'A'
    aces = [card for card in deck if card.rank == target_rank]
    print(f"All Aces: {aces}")
    
    target_suit = 'hearts'
    hearts = [card for card in deck if card.suit == target_suit]
    print(f"All Hearts: {hearts[:5]}... (showing first 5)\n")
    
    # Checking if the deck contains specific cards
    print("--- Checking card membership ---")
    ace_of_spades = Card('A', 'spades')
    king_of_hearts = Card('K', 'hearts')
    fake_card = Card('15', 'rockets')
    
    print(f"Deck contains {ace_of_spades}: {ace_of_spades in deck}")
    print(f"Deck contains {king_of_hearts}: {king_of_hearts in deck}")
    print(f"Deck contains {fake_card}: {fake_card in deck}\n")
    
    # Using other built-in functions
    print("--- Other built-in examples ---")
    print(f"Total cards: {len(deck)}")
    print(f"First 3 cards: {list(deck[:3])}")
    print(f"All suits in deck: {set(card.suit for card in deck)}")
    print(f"All ranks in deck: {set(card.rank for card in deck)}")
    
    # Reverse iteration
    print(f"Last 3 cards (reversed): {list(reversed(deck[-3:]))}")
    
    # Using max/min (requires comparison, but we can use strings)
    print(f"Highest rank card (alphabetically): {max(deck, key=lambda card: card.rank)}")
    print(f"Lowest rank card (alphabetically): {min(deck, key=lambda card: card.rank)}")
    
    # Using the spades_high ranking system
    print("\n--- Card ranking with spades_high ---")
    sample_cards = [Card('2', 'clubs'), Card('2', 'spades'), Card('A', 'clubs'), Card('A', 'spades')]
    for card in sample_cards:
        print(f"{card}: {deck.spades_high(card)}")
    
    highest_card = max(deck, key=deck.spades_high)
    lowest_card = min(deck, key=deck.spades_high)
    print(f"Highest value card: {highest_card} (value: {deck.spades_high(highest_card)})")
    print(f"Lowest value card: {lowest_card} (value: {deck.spades_high(lowest_card)})")
    
    # For loop
    for card in deck:
        print(card)

    # For loop can also be reversed
    for card in reversed(deck):
        print(card)