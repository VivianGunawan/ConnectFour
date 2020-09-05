# A Connect-Four Player class   

from board import Board

class Player:

    def __init__(self,checker):
        """construct a new Player object by initializing the two attributes checker and num_moves"""
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
        
    def __repr__(self):
        """returns a string representing a Player object"""
        s='Player ' + self.checker
        return s

    def opponent_checker(self):
        """returns a one-character string representing the checker of the Player object’s opponent"""
        if self.checker=='X':
            opponent ='O'
        else:
            opponent = 'X'
        return opponent

    def next_move(self, board):
        """accepts a Board object as a parameter and returns the column where the player wants to make the next move"""
        self.num_moves += 1
        while True:
            col=int(input('Enter a column: '))
            if board.can_add_to(col):
                return col
            print('Try again!')
        
