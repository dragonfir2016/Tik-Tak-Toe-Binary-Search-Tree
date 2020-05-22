class Board:
    """
    Class for board representation.
    """
    def __init__(self, board):
        """
        (Board, list, str, tuple) -> NoneType
        Creates a new object of Board class.
        """
        self.board = board

    def check_state(self):
        """
        (Board) -> str
        Checks current state on the board and returns if there is a win or
        a draw.
        """
        for ps in range(3):
            if self.board[ps][0] == self.board[ps][1] == self.board[ps][2]:
                if self.board[ps][0]:
                    return self.board[ps][0]
            elif self.board[0][ps] == self.board[1][ps] == self.board[2][ps]:
                if self.board[0][ps]:
                    return self.board[ps][0]
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
            line = ' '.join([el if el else '0' for el in self.board[line]])
            board += '[' + line + ']' + '\n'
        return board[:-1]
