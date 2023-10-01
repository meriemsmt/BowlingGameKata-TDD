import unittest
from bowling import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.g = Game()

    def test_can_roll(self):
        for i in range(20):
            self.g.roll(0)
        score = self.g.score()
        self.assertEqual(score,0)

if __name__ == '__main__':
    unittest.main()


