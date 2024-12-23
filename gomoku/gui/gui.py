import tkinter as tk
from services.services import gameServices

"""
this is going to be the GUI class
"""

class GUI:
    def __init__(self, size, difficulty, player):
        self.root = tk.Tk()
        self.root.title("Gomoku Game")
        self.game = gameServices(size, difficulty)
        self.buttons = [[0 for _ in range(size)] for _ in range(size)]
        self.gameOver = False
        self.createBoardButtons()
        self.startGame(player)
        self.p = player

    def createBoardButtons(self):
        """
        this method will be used to create the buttons for the board
        :return: the buttons for the board
        """
        for i in range(len(self.buttons)):
            for j in range(len(self.buttons[i])):
                button = tk.Button(self.root, text="", width=3, height=2, font=('Comic Sans', 14, 'bold'),
                                   command=lambda row=i, col=j: self.makeMove(row, col), relief=tk.GROOVE)
                button.grid(row=i, column=j, padx=2, pady=2)
                self.buttons[i][j] = button

    def startGame(self, player):
        self.game.startGame(player)

    def makeMove(self, row, col):
        """
        this method will be used to make a move
        :param row: the row of the cell
        :param col: the column of the cell
        :return: a message if the move is invalid
        """
        if not self.gameOver:
            if not self.game.makeMove(row, col):
                print("Invalid move, please try again")
            else:
                self.updateBoard()
                if not self.gameOver:
                    self.game.computerMove()
                    self.updateBoard()
                    self.checkGameOver()

    def updateBoard(self):
        """
        this method will be used to update the board
        :return: the updated board
        """
        for i in range(len(self.buttons)):
            for j in range(len(self.buttons[i])):
                value = self.game.board.grid[i][j]
                text = str(value) if value != '-' else ""

                # set color based on move type
                if value == self.game.player.piece:
                    self.buttons[i][j].configure(bg='pink', fg='white')
                elif value == self.game.computer.piece:
                    self.buttons[i][j].configure(bg='purple', fg='white')
                else:
                    self.buttons[i][j].configure(bg='SystemButtonFace', fg='black')

                self.buttons[i][j]["text"] = text
    def run(self):
        self.root.mainloop()

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


    def checkGameOver(self):
        """
        this will quit the game if it is over
        """
        if self.game.isGameOver():
            self.gameOver = True
            for i in range(len(self.buttons)):
                for j in range(len(self.buttons[i])):
                    self.buttons[i][j].configure(state=tk.DISABLED)
            self.displayGameResult()
            self.root.quit()
            self.root.destroy()
            self.root.mainloop()

