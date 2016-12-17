print "\nYour hand: ",
for card in p_hand:
    print card.short_name,
print "    Up card: ", up_card.short_name
if up_card.rank == '8':
    print"    Suit is", active_suit
