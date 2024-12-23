from repository.boardRepository import boardRepository
from domain.computerPlayer import computerPlayer
from domain.board import Board

"""
this is going to be the service class, which will be used to manage the game
"""


class gameServices:
    def __init__(self, size, difficulty):
        self.boardRepo = boardRepository()
        self.board = Board(size)
        self.player = None
        self.computer = computerPlayer(difficulty)
        self.difficulty = difficulty
        self.lastMoveBy = None

    def startGame(self, player):
        """
        this method will be used to start the game
        :param: the player object
        """
        self.player = player
        self.boardRepo.saveBoard(self.board)

    def makeMove(self, row, col):
        """
        this method will be used to make a move
        :param row: the row of the cell
        :param col: the column of the cell
        """
        self.lastMoveBy = self.player
        if self.board.isEmpty(row, col):
            self.board.place(row, col, self.player.piece)
            self.boardRepo.saveBoard(self.board)
            return True
        return False

    def computerMove(self):
        """
        this method will be used to make the computer move
        """
        self.lastMoveBy = self.computer
        x, y = self.computer.move(self.board, self.difficulty)
        self.board.place(x, y, self.computer.piece)
        self.boardRepo.saveBoard(self.board)

    def isGameOver(self):
        """
        this method will be used to check if the game is over
        :return: True if the game is over, False otherwise
        """
        return self.board.isBoardFull() or self.board.checkWin(self.player.piece) or self.board.checkWin(
            self.computer.piece)

    def checkTie(self):
        """
        this method will be used to check if the game is a tie
        :return: True if the game is a tie, False otherwise
        """
        return self.board.isBoardFull() and not self.board.checkWin(self.player.piece) and not self.board.checkWin(
            self.computer.piece)

    def getWinner(self):
        """
        this method will be used to get the winner of the game
        :return: the winner of the game
        """
        return self.board.checkWin(self.player.piece)
