import CardDeck



#Testing Code    
# beer_card = Card('7','hearts')
# print(beer_card)
deck = CardDeck.FrenchDeck()
# for card in deck: #doctest: +ELLIPSIS
#     print(card)
  

suit_values = dict(spades=3,hearts=2, diamonds=1, clubs=0)  
def spades_high(card):
        rank_value = CardDeck.FrenchDeck.ranks.index(card.rank)
        # print(f"card is {card}")
        # print(f"rank_value -->{rank_value}")
        # print(f"card_suit_rank value --->{rank_value * len(suit_values) + suit_values[card.suit]}")
        return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck,key=spades_high):
    print(card)