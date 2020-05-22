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
from btree import LinkedBT
from btnode import BTNode

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

Your next move should be entered in this format: 0 2 , where 0 is a ROW and 2 is a COLUMN.


So now let us start, you will make the first move.""")
        move = 0
        while True:
            print(f'Board after {move} move:')
            move += 1
            print(self.board)
            right_input = False
            pl_move = input('Please enter your move: ').replace(',', ' ').split(' ')
            while not right_input:
                try:
                    post = (int(pl_move[0]), int(pl_move[1]))
                    if not self.board.is_valid_move(post):
                        raise Exception
                    right_input = True
                except:
                    pl_move = input('Please enter valid move: ').replace(',', ' ').split(' ')
            self.board.board[post[0]][post[1]] = 'x'
            print(f'Board after {move} move:')
            print(self.board)
            move += 1
            if self.board.check_state():
                win = self.board.check_state()
                print('-----------------------------------')
                print(f'Hooray, {win} wins.')
                break
            comp_tree = gen_tree(self.board)
            tree_left = LinkedBT()
            tree_left.root = comp_tree.root.left
            tree_right = LinkedBT()
            tree_right.root = comp_tree.root.right
            left_wins = count_wins(tree_left)
            right_wins = count_wins(tree_right)
            if left_wins > right_wins:
                self.board = tree_left.root.data
            else:
                self.board = tree_right.root.data

            if self.board.check_state():
                win = self.board.check_state()
                print('-----------------------------------')
                print(f'Hooray, {win} wins.')
                break

if __name__ == "__main__":
    g = Game()
    g.play()