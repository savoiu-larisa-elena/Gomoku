"""
this is going to be the player class, which will be used by the human in order to play the game
"""

class Player:
    def __init__(self, name, piece=None, difficulty=""):
        self.name = name
        self.piece = piece
        self.difficulty = difficulty

    def move(self, board, difficulty):
        """
        this method will be used by the human player in order to make a move, and it will be implemented further
        :param board: the board object
        :param difficulty: the difficulty selected by the human player
        :return: an error if the method is not implemented
        """
        raise NotImplementedError("The move method is not implemented yet")
