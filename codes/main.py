from card_game import *
import pandas as pd
import matplotlib.pyplot as plt

# Test Units
# Task 1
def test_deck_creation():
    deck = create_deck()
    assert len(deck) == 40, "Deck should have 40 cards"
    if True:
      print("Deck contains 40 cards!")

def test_shuffle():
    deck = create_deck()
    shuffled_deck = shuffle_deck(deck)
    assert deck != shuffled_deck, "Deck should be shuffled"
    if True:
      print("Deck is shuffled!")

# Task 2
def test_draw_card_from_empty_draw_pile():
    deck = create_deck()
    player = Player("Test Player")
    player.draw_pile = []
    player.discard_pile.append(5)  # Add a card to discard pile
    player.draw_card(deck)
    assert player.draw_pile == [5], "Card drawn from discard pile on empty draw"
    if True:
        print("Discard pile was shuffled into draw pile when the draw pile is empty!")

# Task 3
def test_higher_card_wins():
    deck = create_deck()
    deck = shuffle_deck(deck)
    player1 = "Player 1"
    player2 = "Player 2"
    game = Game(player1, player2, deck)
    game.play_a_turn()
    return

# Task 4
def test_play_a_game():
    deck = create_deck()
    deck = shuffle_deck(deck)
    player1 = "Player 1"
    player2 = "Player 2"
    game = Game(player1, player2, deck)
    game.play_a_game()
    return

if __name__ == "__main__":
    # Run test units
    #test_deck_creation()
    #test_shuffle()
    #test_draw_card_from_empty_draw_pile()
    #test_higher_card_wins()
    test_play_a_game()

    # Simulates the game 100,000 times to find the distribution of number of rounds required for completion
    #number_of_rounds = []
    #for i in range(100000):
    #    number_of_rounds.append(test_play_a_game())
    #df = pd.DataFrame(number_of_rounds, columns=['number of rounds'])
    #df.to_excel('card_game.xlsx', index=True)
    #print("Results saved to card_game.xlsx")

    data = pd.read_excel('card_game.xlsx')
    data['number of rounds'].hist(bins=1000)
    plt.xlabel('Number Of Rounds')
    plt.ylabel('Frequency')
    plt.title('Number of rounds to finish the card game')
    plt.savefig('Distribution.svg', format='svg')
    plt.show()
