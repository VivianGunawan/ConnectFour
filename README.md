# ConnectFour

🗓 Fall 2017

---

## Project Description

A simple implementation of Connect Four written using Object-Oriented Principles in Python that supports PvP and 2 different PvE modes. 

The first PvE mode selects a random unfilled column on the board.

The second PvE mode uses *lookaheads* to select the most ideal column on the board.

---

## How to run

In Python Interpreter

```python
>>> import ai
>>> import board
>>> import game
>>> import player
# PvP Mode
>>> game.connect_four(player.Player('X'),player.Player('O'))
# PvE Mode (Random column select)
>>> game.connect_four(player.Player('X'),game.RandomPlayer('O'))
# PvE Mode (Lookahead select)
# example below tiebreaks by selecting the left column, 
# and have a single lookahead step.
>>> game.connect_four(player.Player('X'),ai. AIPlayer('O', 'LEFT', 1))
```
