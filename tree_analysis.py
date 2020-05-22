from btree import LinkedBT
import random
import copy


def gen_tree(board):
    """
    """
    tree = LinkedBT()

    def recursion(bord, tree, move):
        poss_move = bord.free_spaces()
        if len(poss_move) == 1:
            cop_board.board[poss_move[0][0]][poss_move[0][1] = move
        else:
            move_1, move_2 = random.sample(poss_move, 2)
            board_1 = copy.deepcopy(board)
            board_2 = copy.deepcopy(board)
            