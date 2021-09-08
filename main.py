from collections import deque

# Deck 1 D58B35926B92C7C4C7E8D3DAA2
# Deck 2 8E47C38A2DEA43467EB9566B95

# Create two lists (deque lists) given the users input
# Hard code the decks cause I don't want to copy/paste these in to the command line every time
# p1s_deck, p2s_deck = [deque(s) for s in (input(), input())]
# A-E (10 -> A, Jack -> B, Queen -> C, King -> D, Ace -> E) are hexadecimal numbers for 10-14 (10 -> 10, Jack -> 11, Queen -> 12, King -> 13, Ace -> 14) hence the 0x prefix for each of the letters
p1s_deck = deque([0xD, 5, 8, 0xB, 3, 5, 9, 2, 6, 0xB, 9, 2, 0xC, 7,
                  0xC, 4, 0xC, 7, 0xE, 8, 0xD, 3, 0xD, 0xA, 0xA, 2])

p2s_deck = deque([8, 0xE, 4, 7, 0xC, 3, 8, 0xA, 2, 0xD, 0xE, 0xA,
                  4, 3, 4, 6, 7, 0xE, 0xB, 9, 5, 6, 6, 0xB, 9, 5])

# Make the deck all 0xE (Ace card) if you want to force one person to win for testing
# Ex. Player 1: D58B35926B92C7C4C7E8D3DAA2
#     Player 2: EEEEEEEEEEEEEEEEEEEEEEEEEE
# Player 2 will win this game

print("Top of the deck <----------------------------------------------------------------> Bottom of the deck")
round = 1  # I added this to keep track of what round we're on

# Try: except: is a way to catch errors in python without crashing the program, the finally: part runs at the end
try:
    while p1s_deck and p2s_deck:  # While loop that iterates through the whole deck
        # pop means take out or subtract, push means put in or add

        # pops/removes the leftmost list item aka the top card from the deck
        # popleft() returns the element that was removed, so p1s_cards now contains a list with just one card (the card that was removed from the deck and placed on the table)
        p1s_cards = [p1s_deck.popleft()]
        p2s_cards = [p2s_deck.popleft()]

        # Checks for "war" (if the cards on the table are the same)
        # p1s_cards[-1] is the last element in the list aka the topmost card on the table
        while p1s_cards[-1] == p2s_cards[-1]:
            # If the cards are the same, remove another card from the player's deck and add it to the list of the player's cards on the table
            # Repeat this step until the topmost cards do not match, since there could be multiple wars in a row
            p1s_cards.append(p1s_deck.popleft())
            p2s_cards.append(p2s_deck.popleft())
            p1s_cards.append(p1s_deck.popleft())
            p2s_cards.append(p2s_deck.popleft())

        # Check which card is higher ranked from the topmost card from each player on the table
        if p1s_cards[-1] > p2s_cards[-1]:
            # extend(iterable) - This function is used to add multiple values at the right end of deque. The argument passed is an iterable.
            # "iterable" just means a list that can be iterated through

            # if player1 won the round, add all of the cards on the table to the bottom of their deck
            p1s_deck.extend(p2s_cards+p1s_cards)
        else:
            # if player2 won the round, add all of the cards on the table to the bottom of their deck
            p2s_deck.extend(p1s_cards+p2s_cards)

        # Output for inspecting each round as it happens
        print(f"Round {round}")
        # print("Player 1's deck:")
        print(f"{p1s_deck}")
        # print("Player 2's deck:")
        print(f"{p2s_deck}\n\n")
        round += 1
except IndexError:
    pass
finally:
    # Is the length of the first deck > 0 (Do they still have cards left)? Print true, otherwise print false... If the length (aka number of cards) of the deck is 0 that means they ran out of cards
    # print(len(p1s_deck) > 0)

    # A more descriptive way to do this
    if len(p1s_deck) > 0:
        print("Player 1 is the winner")
    else:
        print("Player 2 is the winner")

