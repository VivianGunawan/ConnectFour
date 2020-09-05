
# A Connect Four game engine

from board import Board
from player import Player
import random
    
def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(player1, board) == True:
            return board

        if process_move(player2, board) == True:
            return board

def process_move(player, board):
    """perform all of the steps involved in processing a single move by the specified player on the specified board"""
    #Print a message that specifies whose turn it is
    print(str(player)+"'s turn")
    #Obtain the player’s next move
    move=player.next_move(board)
    #Apply the move to the board by using the appropriate Board method
    board.add_checker(player.checker,move)
    #Print a blank line, and then print the board
    print()
    print(board)
    #Check to see if the move resulted in a win or a tie or none
    if board.is_win_for(player.checker):
        print()
        print(str(player)+" wins in "+str(player.num_moves) + ' moves.')
        return True
    if board.is_full():
        print()
        print("It's a tie!")
        return True
    else:
        print()
        return False
        

class RandomPlayer(Player):
    """used for an unintelligent computer player that chooses at random from the available columns"""
    def next_move(self, board):
        """choose at random from the columns in the specified board that are not yet full, and return the index of that randomly selected column"""
        available=[]
        for col in range(board.width):
            if board.can_add_to(col):
                available += [col]
        self.num_moves += 1
        return random.choice(available)
           
    
    
              
