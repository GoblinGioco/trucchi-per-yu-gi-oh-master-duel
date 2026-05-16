from analyzer.core import Deck

# Load your custom decklist
my_deck = Deck.from_ydk("decks/my_combo_deck.ydk")
print(f"Opening Hand Brick Probability: {my_deck.brick_rate()}%")
