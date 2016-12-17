print "What would you like to do? ",
response = raw_input ("Type a card to play or 'Draw' to take a card: " )
valid_play = False
while not valid_play:
    selected_card = None
    while selceted_card == None:
        if response.lower() == 'draw':
            valid_play = True
            if len(deck) > 0:
                card = random.choice(deck)
                p_hand.append(card)
                deck.remove(card)
                print "You drew", card.short_name
            else:
                print "There are no cards left in the deck"
                blocked += 1
            return
        else:
            for card in p_hand:
                if response.upper() == card.short_name:
                    selected_card = card
            if selected_card == None:
                response = raw_input("You don't have that card. Try again:")

        if selected_card.rank == '8':
            valid_play = True
            is_eight = True
        elif selected_card.suit == active_suit:
            valid_play = True
        elif selected_card.rank == up_card.rank:
            valid_play = True

        if not valid_play:
            response = raw_input("That's not a legal play. Try again: ")
