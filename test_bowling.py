import unittest
from bowling import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.g = Game()

    def test_zero_roll(self):
        for i in range(20):
            self.g.roll(0)
        score = self.g.score()
        self.assertEqual(score,0)

    def test_all_ones(self):
        for _ in range(20):
            self.g.roll(1)
        self.assertEqual(self.g.score(), 20)

if __name__ == '__main__':
    unittest.main()


