"""
A simple command-line Blackjack (21) game: player vs dealer.
Player tries to get as close to 21 as possible without going over.
Aces count as 1 or 11. Dealer hits until reaching 17 or more.
"""

import random

suits = ['♠', '♥', '♦', '♣']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {str(i): i for i in range(2, 11)}
values.update({'J': 10, 'Q': 10, 'K': 10, 'A': 11})

def create_deck():
    """Creates and shuffles a standard 52-card deck."""
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def hand_value(hand):
    """Calculates the value of a hand, treating Aces as 1 or 11."""
    value = 0
    aces = 0
    for rank, _ in hand:
        if rank == 'A':
            aces += 1
        value += values[rank]
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def print_hand(hand, hide_first=False):
    """Prints a hand of cards. Optionally hides the first card (for dealer)."""
    if hide_first:
        print('[??]', end=' ')
        for card in hand[1:]:
            print(f"[{card[0]}{card[1]}]", end=' ')
        print()
    else:
        for card in hand:
            print(f"[{card[0]}{card[1]}]", end=' ')
        print()

def blackjack():
    """Main game loop for command-line Blackjack."""
    print("Welcome to Blackjack! Try to beat the dealer.\n")
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    while True:
        print("Your hand:", end=' ')
        print_hand(player_hand)
        print(f"Your total: {hand_value(player_hand)}")
        print("Dealer's hand:", end=' ')
        print_hand(dealer_hand, hide_first=True)
        if hand_value(player_hand) == 21:
            print("Blackjack! Let's see what the dealer has...")
            break
        move = input("Hit or stand? (h/s): ").strip().lower()
        if move == 'h':
            player_hand.append(deck.pop())
            if hand_value(player_hand) > 21:
                print("Your hand:", end=' ')
                print_hand(player_hand)
                print(f"Your total: {hand_value(player_hand)}")
                print("Bust! You lose.")
                return
        elif move == 's':
            break
        else:
            print("Invalid input. Please enter 'h' or 's'.")
    # Dealer's turn
    print("\nDealer's hand:", end=' ')
    print_hand(dealer_hand)
    while hand_value(dealer_hand) < 17:
        print("Dealer hits.")
        dealer_hand.append(deck.pop())
        print_hand(dealer_hand)
    dealer_total = hand_value(dealer_hand)
    player_total = hand_value(player_hand)
    print(f"Dealer's total: {dealer_total}")
    if dealer_total > 21:
        print("Dealer busts! You win!")
    elif dealer_total > player_total:
        print("Dealer wins!")
    elif dealer_total < player_total:
        print("You win!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    blackjack() 