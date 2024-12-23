import random
from domain.humanPlayer import Player

"""
this is going to be the computer player class, which will be used by the computer in order to play the game
"""


class computerPlayer(Player):
    def __init__(self, difficulty):
        super().__init__("Computer", "O",
                         difficulty)  # the computer will always be the second player, and will have the piece "O"

    def move(self, board, difficulty):
        """
        this is going to be the algorithm that decides the best move for the computer based on the difficulty selected
        :param board: the board object
        :param difficulty: the difficulty selected by the human player
        :return: the coordinates of the move
        """

        if difficulty == "easy":
            return self.easyMove(board)

        if difficulty == "medium":
            return self.mediumMove(board)

        if difficulty == "hard":
            return self.hardMove(board)

    def easyMove(self, board):
        """
        this is the algorithm for the easy difficulty, the computer will just put it in a random place on the board
        :param board: the board object
        :return: the coordinates of the move in a tuple
        """
        while True:
            x = random.randint(0, board.size - 1)
            y = random.randint(0, board.size - 1)
            if board.isEmpty(x, y):
                return x, y

    def mediumMove(self, board):
        """
        this is the algorithm for the medium difficulty, the computer will try to go for a winning move if it is available or blocking the human player's winning move
        :param board: the board object
        :return: the coordinates of the move in a tuple
        """
        # check for winning move
        for i in range(board.size):
            for j in range(board.size):
                if board.isEmpty(i, j):
                    board.place(i, j, self.piece)
                    if board.checkWin(self.piece):
                        return i, j
                    board.place(i, j, '-')
        # check for blocking move
        for i in range(board.size):
            for j in range(board.size):
                if board.isEmpty(i, j):
                    board.place(i, j, 'X')
                    if board.checkWin('X'):
                        board.place(i, j, '-')
                        return i, j
                    board.place(i, j, '-')
        # if no winning or blocking move is available, place the piece randomly
        return self.easyMove(board)

    def hardMove(self, board):
        """
        this is the algorithm for the hard difficulty, the computer will try to prioritize moves that create a winning move in the next turn while also blocking the human player's winning move
        :param board: the board object
        :return: the coordinates of the move in a tuple
        """

        # a simple heuristic approach to prioritize moves that create a winning move in the next turn
        bestMove = None
        bestScore = float('-inf')

        for i in range(board.size):
            for j in range(board.size):
                if board.isEmpty(i, j):
                    board.place(i, j, self.piece)
                    score = self.evaluateMove(board, i, j)
                    board.place(i, j, '-')
                    if score > bestScore:
                        bestScore = score
                        bestMove = (i, j)
        return bestMove if bestMove is not None else self.easyMove(board)

    def evaluateMove(self, board, row, col):
        """
        this method evaluates the move based on the number of pieces in a row, column, diagonal, or anti-diagonal
        :param board: the board object
        :param row: the row of the move
        :param col: the column of the move
        :return: the score of the move
        """
        score = 0
        for direction in [(0, 1), (1, 0), (1, 1), (1, -1)]:
            score += self.evaluateLine(board, row, col, direction)
        return score

    def evaluateLine(self, board, row, col, direction):
        """
        this method evaluates the line based on the number of pieces in a row, column, diagonal, or anti-diagonal
        :param board: the board object
        :param row: the row of the move
        :param col: the column of the move
        :param direction: the direction to evaluate
        :return: the score of the line
        """
        score = 0
        maxLength = 5
        for step in range(-maxLength + 1, maxLength):
            current_score = 0
            for i in range(maxLength):
                newRow = row + (step + i) * direction[0]
                newCol = col + (step + i) * direction[1]

                if 0 <= newRow < board.size and 0 <= newCol < board.size:
                    piece = board.grid[newRow][newCol]
                    if piece == self.piece:
                        current_score += 1
                    elif piece == 'X':
                        current_score -= 1

            score = max(score, current_score)

        return score

    def evaluateBoard(self, board):
        """
        this method evaluates the board based on current positions of the pieces
        :param board: the board object
        :return: the score of the board
        """
        score = 0
        for i in range(board.size):
            for j in range(board.size):
                if board.grid[i][j] == self.piece:
                    score += self.evaluateMove(board, i, j)
                elif board.grid[i][j] == 'X':
                    score -= self.evaluateMove(board, i, j)
        return score
