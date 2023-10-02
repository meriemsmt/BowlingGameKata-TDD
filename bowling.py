class Game:
    def __init__(self):
        # Since the next roll matters in a spare, we need a list
        self._rolls = []

    def roll(self, pins):
        # At each roll, we append the pin
        self._rolls.append(pins)

    def score(self):
        return sum(self._rolls)



