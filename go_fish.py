"""
A simple command-line Go Fish game for 2-4 human players.
Players ask each other for cards to collect books of four cards of the same rank.
The player with the most books at the end wins.
"""

import random
from collections import defaultdict, Counter

suits = ['♠', '♥', '♦', '♣']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


def create_deck():
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def print_hand(hand):
    counts = Counter(r for r, s in hand)
    return ' '.join(f"{r}({counts[r]})" for r in sorted(counts))

def go_fish():
    print("Welcome to Go Fish!")
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
    hand_size = 7 if num_players == 2 else 5
    hands = [[] for _ in range(num_players)]
    books = [set() for _ in range(num_players)]
    for _ in range(hand_size):
        for h in hands:
            h.append(deck.pop())
    current = 0
    while True:
        # Check for game end
        if all(not h for h in hands) and not deck:
            break
        player = current
        print(f"\nPlayer {player+1}'s turn.")
        print(f"Your hand: {print_hand(hands[player])}")
        # Check for new books
        counts = Counter(r for r, s in hands[player])
        for r in list(counts):
            if counts[r] == 4:
                print(f"You completed a book of {r}s!")
                books[player].add(r)
                hands[player] = [card for card in hands[player] if card[0] != r]
        if not hands[player]:
            if deck:
                print("Your hand is empty. Drawing a card...")
                hands[player].append(deck.pop())
            else:
                print("No cards left to draw.")
                current = (current + 1) % num_players
                continue
        # Ask another player
        while True:
            try:
                ask = int(input(f"Which player do you want to ask? (1-{num_players}, not yourself): ")) - 1
                if ask == player or not (0 <= ask < num_players):
                    print("Invalid player. Try again.")
                    continue
                if not hands[ask]:
                    print("That player has no cards. Try again.")
                    continue
                break
            except Exception:
                print("Invalid input. Try again.")
        while True:
            rank = input(f"Which rank do you want to ask for? (e.g., 4, J, A): ").strip().upper()
            if rank not in ranks:
                print("Invalid rank. Try again.")
                continue
            if any(card[0] == rank for card in hands[player]):
                break
            else:
                print("You must have at least one card of that rank in your hand.")
        # Process ask
        ask_cards = [card for card in hands[ask] if card[0] == rank]
        if ask_cards:
            print(f"Player {ask+1} gives you {len(ask_cards)} card(s) of rank {rank}!")
            hands[player].extend(ask_cards)
            hands[ask] = [card for card in hands[ask] if card[0] != rank]
            # Check for new books after receiving
            counts = Counter(r for r, s in hands[player])
            for r in list(counts):
                if counts[r] == 4:
                    print(f"You completed a book of {r}s!")
                    books[player].add(r)
                    hands[player] = [card for card in hands[player] if card[0] != r]
            # Player goes again
            continue
        else:
            print(f"Go Fish! Drawing a card...")
            if deck:
                drawn = deck.pop()
                print(f"You drew: {drawn[0]}{drawn[1]}")
                hands[player].append(drawn)
                # Check for new book
                counts = Counter(r for r, s in hands[player])
                if counts[drawn[0]] == 4:
                    print(f"You completed a book of {drawn[0]}s!")
                    books[player].add(drawn[0])
                    hands[player] = [card for card in hands[player] if card[0] != drawn[0]]
            else:
                print("No cards left to draw.")
            # Next player's turn
            current = (current + 1) % num_players
    # Game over
    print("\nGame over! Book counts:")
    for i, b in enumerate(books):
        print(f"Player {i+1}: {len(b)} books ({', '.join(sorted(b)) if b else 'none'})")
    max_books = max(len(b) for b in books)
    winners = [i+1 for i, b in enumerate(books) if len(b) == max_books]
    if len(winners) == 1:
        print(f"Player {winners[0]} wins!")
    else:
        print(f"It's a tie between players: {', '.join(map(str, winners))}")

if __name__ == "__main__":
    go_fish() 