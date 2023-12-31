import unittest
from bowling import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.g = Game()

    def roll_many(self, n, pins):
        for _ in range(n):
            self.g.roll(pins)

    def test_zero_roll(self):
        self.roll_many(20, 0)
        self.assertEqual(self.g.score(), 0)

    def test_all_ones(self):
        self.roll_many(20, 1)
        self.assertEqual(self.g.score(), 20)

    def test_one_spare(self):
        self.g.roll(5)
        self.g.roll(5)  # spare
        self.g.roll(3)
        self.roll_many(17, 0)
        self.assertEqual(self.g.score(), 16)

    def test_one_strike(self):
        self.g.roll(10)  # strike
        self.g.roll(3)
        self.g.roll(4)
        self.roll_many(16, 0)
        self.assertEqual(self.g.score(), 24)

    def test_perfect_game(self):
        self.roll_many(12, 10)
        self.assertEqual(self.g.score(), 300)


if __name__ == '__main__':
    unittest.main()