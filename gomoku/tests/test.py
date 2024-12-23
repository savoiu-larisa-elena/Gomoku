import unittest
from services.services import gameServices
from domain.humanPlayer import Player

" this is going to be the test class for the game services "

class Tests(unittest.TestCase):
    def setUp(self):
        self.game = gameServices(15, "easy")
        self.player = Player("Player", "X", "easy")

    def testGame(self):
        self.game.startGame(self.player)
        self.game.makeMove(0, 0)
        self.game.computerMove()
        self.assertFalse(self.game.isGameOver())
        self.assertFalse(self.game.checkTie())
        self.assertEqual(self.game.getWinner(), None)

if __name__ == '__main__':
    unittest.main()