"""
Design the data structures for a generic deck of cards. Explain how you would
subclass the data structures to implement blackjack.

Deck of cards:
-Need to have order -> [list]
-Shuffle
-Draw

Black jack:
-How many decks of cards
-Deal (shows 1 dealer card)
-Bet

Hand:
-Hit
-Bet
-Bust
-Split

"""
import random

class DeckofCards:
    def __init__(self, decks = 1):
        self.cards = self.create_deck(decks)
        self.decks = decks
                    
    def create_deck(self, decks):
        cards = ['A', 'K', 'Q', 'J', '10', '9','8','7','6','5','4','3','2']
        suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
        deck = [(c, s) for c in cards for s in suits] * decks
        return deck

    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards

    def draw(self):
        return self.cards.pop(0)
    
class BlackjackTable(DeckofCards):
    # players is a list of player names
    def __init__(self, decks=1, table_max=5):
        super().__init__(decks)
        self.players = [Dealer().name] + ([0]*(table_max))
        self.table_max = table_max

    def add_player(self, player):
        new_player = Player(player)
        for seat in range(1, self.table_max+1):
            if self.players[seat] == 0:
                self.players[seat] = new_player
                return print(f'{player} placed at seat {seat}')
        return print("Table is full")

    def remove_player(self, player):
        for seat in range(1, self.table_max+1):
            if self.players[seat].name == player:
                self.players[seat] = 0
                return print(f'{player} removed from seat {seat}')
        return print(f"{player} is not at the table")
    
    def see_table(self):
        for player in self.players:
            print(player)

    # def deal_table(self):



    
class Dealer:
    def __init__(self):
        self.name = 'Dealer'

    def __str__(self) -> str:
        return f'{self.name}'
    


class Player:
    def __init__(self, player):
        self.name = player
        self.bet = 0
        self.hand = []

    def __str__(self) -> str:
        return f'{self.name}'
    
    # def betting(self, quantity):

    # def hit(self):
    
    # def stay(self):
    
    # def split(self):


    


# Testing:

deck = DeckofCards(2)
blackjack = BlackjackTable(5,5)
blackjack.add_player('1')
blackjack.add_player('2')
blackjack.add_player('3')
blackjack.add_player('4')
blackjack.add_player('5')
blackjack.add_player('6')
blackjack.see_table()
blackjack.remove_player('1')