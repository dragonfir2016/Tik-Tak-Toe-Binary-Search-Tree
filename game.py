class BOard:
    Board
    last_move

    #def person_move -> board, перевірка
    #def freespaces(board) -> free spaces як список таплів і потім коли ми будем ибирати хід як random sample
    #def check_win(board) -> x, 0 and free cell/no free cell
    def tree creation(board) -> tree
    def win-combiantions(tree) -> combination points for left/combination points for right -> next move
    #__str__


class Game:
    """
    Class for game representation.
    """
    def __init__(self, cur_board):
        """
        (Game, Board) -> NoneType
        Creates a new object of Game class.
        """
        self.cur_board = cur_board

    def play(self):
        """
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
