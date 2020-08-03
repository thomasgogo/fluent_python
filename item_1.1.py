# 一摞 python 风格的纸牌

# 如何实现__getitem__和__len__这两个特殊方法
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])
print(Card.rank)


class FrenckDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card('7', 'diamonds')
print(beer_card)

deck = FrenckDeck()
print(len(deck))

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenckDeck.ranks.index(card.rank)
    print('rank_value', rank_value, card.rank, card.suit)
    a = rank_value * len(suit_values) + suit_values[card.suit]
    # print(a)
    return a

for card in sorted(deck, key=spades_high):
    print(card)