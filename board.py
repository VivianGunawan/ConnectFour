# A Connect Four Board class

class Board:

    def __init__(self, height, width):
        """constructs a new Board object by initializing the three attributes, height, width, slot"""

        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]

    
    def __repr__(self):
        """ Returns a string representation for a Board object."""
        s = ''         # begin with an empty string
        # add one row of slots at a time
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row
            for col in range(self.width):
                s += self.slots[row][col] + '|'
            s += '\n'  # newline at the end of the row

    # Add code here for the hyphens at the bottom of the board
        for col in range(self.width*2 +1):
            s +='-'
        s += '\n'
    # and the numbers underneath it.
        for num in range(self.width):
            a = (num) % 10
            s += ' ' + str(a) 
        return s

    def add_checker(self, checker, col):
        """ put your docstring here"""
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)
    # put the rest of the method here
        h=self.height -1
        for row in range(self.height):
            if h==0:
                break
            elif self.slots[row][col] != ' ':
                h+= -1
        self.slots[h][col]=checker

    def reset(self):
        """Clears all the slots"""
        for row in range(self.height):
            for col in range(self.width):
                self.slots[row][col]=' '

        
    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
        checkers in those columns of the called Board object, 
        starting with 'X'."""
        checker = 'X'   # start by playing 'X'
        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)
        # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def can_add_to(self,col):
        """returns True if it is valid to place a checker in the column col on the calling Board object"""
        if col < 0 or col>self.width-1:
            return False
        else:
            if self.slots[0][col] != ' ':
                return False
            else:
                return True

    def is_full(self):
        """returns True if the called Board object is completely full of checkers, and returns False otherwise"""
        for col in range(self.width):
            if self.can_add_to(col):
                return False
        return True

    def remove_checker(self, col):
        ''' removes the top checker from column col of the called Board object.
        if the column is empty, then does nothing.
        '''
        for row in range(self.height):
            if self.slots[row][col] != ' ':
                self.slots[row][col] = ' '
                return
            
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker."""
        for row in range(self.height):
            for col in range(self.width - 3):
            # Check if the next four columns in this row
            # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False
    
    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker."""
        for col in range(self.width):
            for row in range(self.height-3):
            # Check if the next four rows in this column
            # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col] == checker and \
                   self.slots[row+2][col] == checker and \
                   self.slots[row+3][col] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False
            
    def is_rdiagonal_win(self, checker):
        """ Checks for a diagonal win for the specified checker."""
        for row in range(self.height-3):
            for col in range(self.width-3):
            # Check if the next four diagonals in the board
            # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col+1] == checker and \
                   self.slots[row+2][col+2] == checker and \
                   self.slots[row+3][col+3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False 

    def is_ldiagonal_win(self, checker):
        """ Checks for a diagonal win for the specified checker."""
        for row in range(3,self.height):
            for col in range(self.width-3):
            # Check if the next four diagonals in the board
            # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row-1][col+1] == checker and \
                   self.slots[row-2][col+2] == checker and \
                   self.slots[row-3][col+3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False
        
    def is_win_for(self, checker):
        """ Checks if the stated checker is winning"""
        assert(checker == 'X' or checker == 'O')
    # call the helper functions and use their return values to
    # determine whether to return True or False
        if self.is_horizontal_win(checker)== True:
            return True
        if  self.is_vertical_win(checker) == True:
            return True
        if self.is_ldiagonal_win(checker) == True:
            return True
        if self.is_rdiagonal_win(checker) == True:
            return True
        else:
            return False

        
        
