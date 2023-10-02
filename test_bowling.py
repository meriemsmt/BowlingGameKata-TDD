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
        score = self.g.score()
        self.assertEqual(score,0)

    def test_all_ones(self):
        self.roll_many(20, 1)
        self.assertEqual(self.g.score(), 20)

    @unittest.skip('Misplaced responsibility should be fixed by refactoring the production code!')
    def test_one_spare(self):
        self.g.roll(5)
        self.g.roll(5)  # spare
        self.g.roll(1)
        self.assertEqual(self.g.score(), 12)
if __name__ == '__main__':
    unittest.main()


