import random

# Task 1: Create a shuffled deck of cards
# Create a deck of cards
def create_deck():
    deck = []
    for i in range(4):
        for j in range(10):
            deck.append(j)
    return deck

# Shuffle the deck of cards
def shuffle_deck(deck):
    shuffled_deck = deck.copy()
    for i in range(len(shuffled_deck) - 1, 0, -1):
        j = random.randint(0, i)
        shuffled_deck[i], shuffled_deck[j] = shuffled_deck[j], shuffled_deck[i]
    return shuffled_deck

# Task 2: Draw cards
class Player:
    def __init__(self, name):
        self.name = name
        self.draw_pile = []
        self.discard_pile = []

    def draw_card(self,deck):
        if len(self.draw_pile) == 0:
            if len(self.discard_pile) > 0:
                self.draw_pile = shuffle_deck(self.discard_pile)
                self.discard_pile = []
        drawn_card = self.draw_pile[-1]
        return drawn_card

# Task 3: Play a turn
class Game:
    def __init__(self, playerA, playerB, deck):
        self.player1_name = playerA
        self.player2_name = playerB
        self.player1 = Player(playerA)
        self.player2 = Player(playerB)
        self.player1.draw_pile = deck[0:20]
        self.player2.draw_pile = deck[20:40]
        self.cards_to_append = []

    def play_a_turn(self):
        player1_card = self.player1.draw_card(self.player1.draw_pile)
        player2_card = self.player2.draw_card(self.player2.draw_pile)
        self.cards_to_append.extend([player1_card, player2_card])
        print(self.player1.name + " (discard pile: " + str(len(self.player1.discard_pile)) + " cards, draw pile: " + str(len(self.player1.draw_pile)) + " cards): " + str(player1_card))
        print(self.player2.name + " (discard pile: " + str(len(self.player2.discard_pile)) + " cards, draw pile: " + str(len(self.player2.draw_pile)) + " cards): " + str(player2_card))
        if player1_card > player2_card:
            self.player1.discard_pile.extend(self.cards_to_append)
            self.cards_to_append = []
            print("Player 1 wins this round")
        elif player2_card > player1_card:
            self.player2.discard_pile.extend(self.cards_to_append)
            self.cards_to_append = []
            print("Player 2 wins this round")
        elif player1_card == player2_card:
            dummy_variable = 0
            print("No winner in this round")
        self.player1.draw_pile.pop()
        self.player2.draw_pile.pop()

# Task 4: Console Output
    def play_a_game(self):
        while True:
            self.play_a_turn()
            if self.player1.draw_pile == [] and self.player1.discard_pile == []:
                print(self.player2.name + " wins the game!")
                return
            if self.player2.draw_pile == [] and self.player2.discard_pile == []:
                print(self.player1.name + " wins the game!")
                return