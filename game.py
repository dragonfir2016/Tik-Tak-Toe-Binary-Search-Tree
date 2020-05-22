"""
game = Game()
game.play()
    create board
    while true:
        person move
        chevk win:
            break
        computer tree
        computer move
        check win:
            break
"""
from board import Board
from tree_analysis import gen_tree, count_wins

class Game:
    """
    Class for game representation.
    """
    def __init__(self):
        """
        (Game) -> NoneType
        Creates a new object of Game class.
        """
        self.board = Board([[0,0 ,0], [0,0,0], [0,0,0]])

    def play(self):
        """
        """
        print("""This is a game of tic-tac-toe, and you will be playing against computer.
You will be shown a current board state and after that you will have to enter the postion
where you want ot make move.

Your next move should be entered in this format: 0 2 , where 0 is a line and 2 is a row.

So now let us start, you will make the first move.""")
        while True:
            move = 0
            print(f'Board after {move} move:')
            move += 1
            print(self.board)
            right_input = False
            while not right_input:
                pl_move = input('Please enter your move: ').split()
                try:
                    post = (int(pl_move[0], int(pl_move[1])))
                    if not self.board.is_valid_move(position):
                        raise Exception
                    right_input = True
                except:
                    print('Please enter valid move: ')
            self.board.board[post[0]][post[1]] = 'x'
            if self.board.check_state():
                win = self.board.check_state()
                print(self.board)
                print(f'Hooray, {win} wins.')
                break
            comp_tree = gen_tree(self.board)
            