"""
this is going to be the board class, where the game is played
"""


class Board:
    def __init__(self, size):
        self.size = size  # size of the board
        self.grid = [['-' for _ in range(size)] for _ in range(size)]  # the board itself

    def isEmpty(self, row, col):
        """
        checks if the cell is empty
        :param row: the row of the cell
        :param col: the column of the cell
        :return: True if the cell is empty, False otherwise
        """
        return self.grid[row][col] == '-'

    def place(self, row, col, piece):
        """
        places a piece on the board
        :param row: the row of the cell
        :param col: the column of the cell
        :param piece: the piece to place
        """
        self.grid[row][col] = piece

    def display(self):
        """
        displays the board, using the ansi colours for a fancier look
        """
        colIndices = "  " + "  ".join(
            f"\033[34m{i: 2}\033[36m" for i in range(self.size))  # column indices with cyan colour
        print(colIndices)

        for i in range(self.size):
            rowValues = f"\033[34m{i: 2}\033[36m | "  # row indices with cyan colour
            for j in range(self.size):
                if self.grid[i][j] == 'X':
                    rowValues += "\033[92mX\033[35m | "  # magenta colour for X (player)
                elif self.grid[i][j] == 'O':
                    rowValues += "\033[91mO\033[0m | "  # red colour for O (computer)
                else:
                    rowValues += "- | "  # if the move is empty then just an empty cell
            print(rowValues)

        boardOutline = "    " + "\033[34m" + "-" * (
                4 * self.size + 1) + "\033[36m"  # cyan colour for the board outline
        print(boardOutline)

    def isBoardFull(self):
        """
        checks if the board is full
        :return: True if the board is full, False otherwise
        """
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == '-':
                    return False
        return True

    def checkWin(self, piece):
        """
        check who won the game
        :return: the name of the one who won the game
        """
        for i in range(self.size):
            for j in range(self.size):
                if self.checkLine(i, j, piece, 1, 0) or self.checkLine(i, j, piece, 0, 1) or self.checkLine(i, j, piece,
                                                                                                        1, 1) or self.checkLine(
                    i, j, piece, 1, -1):
                    if(piece == 'X'):
                        return 'Player'
                    if(piece == 'O'):
                        return 'Computer'
        return None
    def checkLine(self, row, col, piece, rowDirection=0, colDirection=0):
        """
        checks if the player has won in a specific line
        :param row: the row of the move
        :param col: the column of the move
        :param piece: the piece of the player
        :param rowDirection: the direction of the row
        :param colDirection: the direction of the column
        :return: True if the player has won in that line, False otherwise
        """
        count = 0
        for _ in range(5):
            if not (0 <= row < len(self.grid) and 0 <= col < len(self.grid[row])):
                break
            if self.grid[row][col] == piece:
                count += 1
                if count == 5:
                    return True
            else:
                count = 0  # Reset the count if the sequence is interrupted
            row += rowDirection
            col += colDirection
        return False

    def checkDirection(self, row, col, piece, direction):
        """
        checks if the player has won in a specific direction
        :param row: the row of the move
        :param col: the column of the move
        :param piece: the piece of the player
        :param direction: the direction to evaluate
        :return: True if the player has won in that direction, False otherwise
        """
        for step in [-4, -3, -2, -1, 0, 1, 2, 3, 4]:
            if step == 0:
                continue
            newRow = row + step * direction[0]
            newCol = col + step * direction[1]
            if 0 <= newRow < self.size and 0 <= newCol < self.size:
                if self.grid[newRow][newCol] == piece:
                    return True
        return False

    def isGameOver(self, row, col, piece):
        """
        checks if the game is over
        :param row: the row of the move
        :param col: the column of the move
        :param piece: the piece of the player
        :return: True if the game is over, False otherwise
        """
        return self.checkWin(piece) or self.isBoardFull()
