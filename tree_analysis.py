from btree import LinkedBT
from btnode import BTNode
from board import Board
import random
import copy


def gen_tree(board):
    """
    """
    tree = LinkedBT()
    tree.add(board)

    def recursion(node, move):
        board = node.data
        poss_move = board.free_spaces()
        next_move = 'x' if move == 'n' else 'n'
        if len(poss_move) == 1:
            pos = poss_move[0]
            board.board[pos[0]][pos[1]] = next_move
        else:
            pos_1, pos_2 = random.sample(poss_move, 2)
            board_1 = copy.deepcopy(board)
            board_2 = copy.deepcopy(board)
            board_1.board[pos_1[0]][pos_1[1]] = next_move
            board_2.board[pos_2[0]][pos_2[1]] = next_move
            node.left = BTNode(board_1)
            node.right = BTNode(board_2)
            recursion(node.left, next_move)
            recursion(node.right, next_move)
    
    recursion(tree.root, 'x')
    return tree

def count_wins(tree):
    def recursion(node):
            if not node.left and not node.right:
                res = node.data
                res = res.check_state()
                if res == 'n':
                    return 1
                elif res == 'x':
                    return -1
                else:
                    return 0
            else:
                return recursion(node.left) + recursion(node.right)
    return recursion(tree.root)
    
if __name__ == "__main__":
    
   tr = gen_tree(Board([[0,0 ,0], [0,0,0], [0,0,0]]))
   print(count_wins(tr))
   print(tr)