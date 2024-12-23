from services.services import gameServices


class UI:
    def __init__(self, size, difficulty, player):
        self.game = gameServices(size, difficulty)
        self.p = player

    def run(self, player):
        self.game.startGame(player)
        while not self.game.isGameOver():
            self.displayBoard()
            while not self.getAndMakeMove():
                pass
            self.game.computerMove()
        self.displayBoard()
        self.displayGameResult()

    def displayBoard(self):
        """
        this method will be used to display the board
        """
        self.game.board.display()

    def getAndMakeMove(self):
        """
        this method will be used to get the move from the human player and make it
        :return: True if the move is valid, False otherwise
        """
        try:
            row = int(input("Enter the row: "))
            col = int(input("Enter the column: "))
            if self.game.makeMove(row, col):
                return True
            print("Invalid move, please try again")
            return False
        except ValueError:
            print("Invalid input, please enter a number")
            return False

    def displayGameResult(self):
        """
        this method will be used to display the result of the game
        :return: the winner of the game
        """
        winner = self.game.getWinner()

        if winner is not None:
            if winner == 'Player':
                print(f"The winner is {self.p.name}")
        else:
            print("The winner is Computer")