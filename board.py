class Board:
    """
    Class for board representation.
    """
    def __init__(self, board, last_move, last_m_pos):
        """
        (Board, list, str, tuple) -> NoneType
        Creates a new object of Board class.
        """
        self.board = board
        self.last_move = last_move
        self.last_m_pos = last_m_pos

    def check_state(self):
        """
        (Board) -> str
        Checks current state on the board and returns if there is a win or a draw.
        """
        for pos in range(3):
            if self.board[pos][0] == self.board[pos][1] == self.board[pos][2]:
                if self.board[pos][0]:
                    return self.board[pos][0]
            elif self.board[0][pos] == self.board[1][pos] == self.board[2][pos]:
                if self.board[0][pos]:
                    return self.board[pos][0]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] or \
           self.board[0][2] == self.board[1][1] == self.board[2][0]:
           if self.board[1][1]:
               return self.board[1][1]

        if len(self.free_spaces()) == 0:
            return 'Draw'
        return

    def free_spaces(self):
        """
        (Board) -> NoneType
        Returns list of free spaces if there are any.
        """
        free_spaces = []
        for i in range(3):
            for j in range(3):
                if not self.board[i][j]:
                    free_spaces.append((i, j))
        return free_spaces

    def is_valid_move(self, move):
        """
        (Board, tuple) -> bool
        Checks whether the move is valid.
        """
        return move in self.free_spaces()

    def __str__(self):
        """
        (Board) -> str
        Returns a string represenation of a board.
        """
        board = ''
        for line in range(3):
            board += '[' + ' '.join([el if el else '0' for el in self.board[line]]) + ']' + '\n'
        return board[:-1]


b = Board([['w','w','s'], ['k','l','x'], ['m',0,'w']], 1, 2)
print(b)
print(b.check_state())
print(b.free_spaces())