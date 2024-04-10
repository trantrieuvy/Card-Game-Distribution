# Card Game Distribution

## Introduction:

This project simulates a simple card game between two players. The deck consists only of number cards (40 cards total) and is shuffled using the Fisher-Yates Shuffle Algorithm. Each player receives a draw pile of 20 cards dealt face-down from the shuffled deck. They also maintain a separate discard pile.

During each turn, both players draw the top card from their draw pile. If a player's draw pile is empty, the discard pile is shuffled and becomes the new draw pile. The game ends when one player has no cards remaining in either their draw or discard pile (that player loses).

On each turn, players reveal their drawn cards and compare the values. The player with the higher card takes both cards and places them face-up in their discard pile. If the cards have the same value, a "tie" occurs. In this case, the winner of the next turn claims both cards and any other cards involved in previous ties.

The game is simulated 100,000 times to analyze the distribution of the number of rounds required for completion.

## Preparation

1. Create virtual Python environment
  ```shell
  conda create -name Card_Game python=3.11
  ```
2. Activate environment
  ```shell
  conda activate Card_Game
  ```
3. Install dependencies
  ```shell
  pip install -r requirements.txt
  ```
  
## Experiments
The codes to stimulate the game is found in [codes](/codes).

The result of one game is similar to the following:

Player 1 (discard pile: 0 cards, draw pile: 20 cards): 4

Player 2 (discard pile: 0 cards, draw pile: 20 cards): 6

Player 2 wins this round

Player 1 (discard pile: 0 cards, draw pile: 19 cards): 8

Player 2 (discard pile: 2 cards, draw pile: 19 cards): 8

No winner in this round

...

Player 1 (discard pile: 30 cards, draw pile: 9 cards): 6

Player 2 (discard pile: 0 cards, draw pile: 1 cards): 2

Player 1 wins this round

Player 1 wins the game!

## Result

After 100,000 runs of the game, the distribution of number of rounds required for completion is illustrated below:
![Distribution of number of rounds](/Distribution.svg "Distribution of number of rounds")

A left-skewed distribution is found, likely due to the rules of the game. Most games are completed between 100 and 200 rounds, which means an avarage game would take an extremely long time in real life. Some games even exceed 3,000 rounds to finish! Games like these would be impossible to complete in real life.

## Author

- [@trantrieuvy](https://www.github.com/trantrieuvy)

