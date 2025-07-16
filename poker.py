"""
A simple command-line Five Card Draw Poker game for 2-4 players (all human).
Each player is dealt 5 cards, can discard and draw new ones, then the best hand wins.
Basic hand ranking is implemented.
"""

import random

suits = ['♠', '♥', '♦', '♣']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
rank_values = {r: i for i, r in enumerate(ranks, 2)}


def create_deck():
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def print_hand(hand):
    return ' '.join(f"[{r}{s}]" for r, s in hand)

def hand_rank(hand):
    """Returns a tuple for hand ranking comparison."""
    counts = {r: 0 for r in ranks}
    suits_count = {s: 0 for s in suits}
    for r, s in hand:
        counts[r] += 1
        suits_count[s] += 1
    values = sorted([rank_values[r] for r, s in hand], reverse=True)
    is_flush = max(suits_count.values()) == 5
    is_straight = False
    for i in range(len(values) - 4 + 1):
        if all(values[j] - values[j+1] == 1 for j in range(i, i+4)):
            is_straight = True
            straight_high = values[i]
            break
    # Special case: A-2-3-4-5 straight
    if set(values) == {14, 5, 4, 3, 2}:
        is_straight = True
        straight_high = 5
    count_vals = sorted(counts.values(), reverse=True)
    pairs = [r for r in ranks if counts[r] == 2]
    threes = [r for r in ranks if counts[r] == 3]
    fours = [r for r in ranks if counts[r] == 4]
    if is_straight and is_flush:
        return (8, straight_high)
    if fours:
        return (7, rank_values[fours[0]])
    if threes and pairs:
        return (6, rank_values[threes[0]], rank_values[pairs[0]])
    if is_flush:
        return (5, values)
    if is_straight:
        return (4, straight_high)
    if threes:
        return (3, rank_values[threes[0]], values)
    if len(pairs) == 2:
        return (2, max(rank_values[p] for p in pairs), min(rank_values[p] for p in pairs), values)
    if pairs:
        return (1, rank_values[pairs[0]], values)
    return (0, values)

def poker():
    print("Welcome to Five Card Draw Poker!")
    while True:
        try:
            num_players = int(input("Enter number of players (2-4): "))
            if 2 <= num_players <= 4:
                break
            else:
                print("Please enter a number between 2 and 4.")
        except Exception:
            print("Invalid input. Please enter a number.")
    deck = create_deck()
    hands = [[] for _ in range(num_players)]
    for _ in range(5):
        for h in hands:
            h.append(deck.pop())
    # Draw phase
    for i, hand in enumerate(hands):
        print(f"\nPlayer {i+1}'s hand: {print_hand(hand)}")
        while True:
            discard = input("Enter card positions to discard (0-4, space separated), or press Enter to keep all: ").strip()
            if not discard:
                break
            try:
                indices = sorted(set(int(x) for x in discard.split() if 0 <= int(x) < 5), reverse=True)
                if any(not (0 <= idx < 5) for idx in indices):
                    raise ValueError
                for idx in indices:
                    hand.pop(idx)
                for _ in range(len(indices)):
                    hand.append(deck.pop())
                break
            except Exception:
                print("Invalid input. Try again.")
    # Showdown
    print("\nShowdown:")
    hand_ranks = []
    for i, hand in enumerate(hands):
        rank = hand_rank(hand)
        hand_ranks.append((rank, i))
        print(f"Player {i+1}: {print_hand(hand)}")
    hand_ranks.sort(reverse=True)
    best_rank, winner = hand_ranks[0]
    # Check for tie
    winners = [i+1 for r, i in hand_ranks if r == best_rank]
    if len(winners) == 1:
        print(f"\nPlayer {winners[0]} wins!")
    else:
        print(f"\nIt's a tie between players: {', '.join(map(str, winners))}")

if __name__ == "__main__":
    poker() 