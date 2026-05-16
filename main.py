import math

class ProbabilityCalculator:
    def __init__(self, deck_size=40, hand_size=5):
        self.N = deck_size  # Total cards in deck
        self.n = hand_size  # Cards drawn in opening hand

    def hypergeometric_pmf(self, k, K):
        """
        Calculates the probability of drawing exactly k copies of a card,
        given K copies exist in a deck of size N, drawing n cards.
        """
        try:
            num = math.comb(K, k) * math.comb(self.N - K, self.n - k)
            den = math.comb(self.N, self.n)
            return round((num / den) * 100, 2)
        except ValueError:
            return 0.0

    def get_combo_odds(self, copies_in_deck):
        """Returns the probability of seeing at least 1 copy in the opening hand."""
        fail_odds = self.hypergeometric_pmf(0, copies_in_deck)
        return round(100.0 - fail_odds, 2)

if __name__ == "__main__":
    print("--- Yu-Gi-Oh! Master Duel Deck Consistency Tool ---")
    calc = ProbabilityCalculator(deck_size=40, hand_size=5)
    
    # Example: Running a 3-of starter card
    starter_probability = calc.get_combo_odds(copies_in_deck=3)
    print(f"Probability of drawing at least 1 starter (3 copies in deck): {starter_probability}%")
    
    # Example: Running a 2-of hand trap
    hand_trap_probability = calc.get_combo_odds(copies_in_deck=2)
    print(f"Probability of drawing at least 1 hand trap (2 copies in deck): {hand_trap_probability}%")
