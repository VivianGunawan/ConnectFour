# A Connect Four AI Player class

import random  
from game import *

class AIPlayer(Player):
    def __init__(self, checker, tiebreak, lookahead):
        """used for a more intelligent computer player that chooses at random from the available columns"""
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self):
        """returns a string representing an AIPlayer"""
        return('Player ' + self.checker + ' (' + self.tiebreak + ', ' + str(self.lookahead)+ ')')

    def max_score_column(self, scores):
        """takes a list scores containing a score for each column of the board, and that returns the index of the column with the maximum score"""
        lt=[i for i in range(len(scores)) if scores[i]==max(scores)]
        if self.tiebreak=='LEFT':
            return lt[0]
        if self.tiebreak=='RIGHT':
            return lt[-1]
        if self.tiebreak=='RANDOM':
            return random.choice(lt)

    def scores_for(self, board):
        """takes a Board object board and determines the called AIPlayer‘s scores for the columns in board"""
        scores = [0] * len(range(board.width))
        for col in range(board.width):
            if not board.can_add_to(col):
                scores[col] = -1
            elif board.is_win_for(self.checker):
                scores[col] = 100
            elif board.is_win_for(self.opponent_checker()):
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                board.add_checker(self.checker, col)
                other_player = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead-1)
                other_scores = other_player.scores_for(board)
                if max(other_scores) == 0:
                    scores[col] = 100
                elif max(other_scores) == 100:
                    scores[col] = 0
                elif max(other_scores) == 50:
                    scores[col] = 50
                board.remove_checker(col)
        return scores

    def next_move(self, board):
        """return the called AIPlayer‘s judgment of its best possible move"""
        self.num_moves += 1
        scores=self.scores_for(board)
        return self.max_score_column(scores)
    
        
        
    
