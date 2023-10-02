class Game(object):

    def __init__(self):
        self._rolls = []

    def roll(self, pins):
        self._rolls.append(pins)

    def score(self):
        score = 0
        box_in_frame = 0
        for frame in range(10):
            if self._is_spare(box_in_frame):
                score += 10 + self._rolls[box_in_frame + 2]
                box_in_frame += 2
            else:
                score += self._rolls[box_in_frame] + self._rolls[box_in_frame + 1]
                box_in_frame += 2
        return score
    
    def _is_spare(self, box_in_frame):
        return self._rolls[box_in_frame] + self._rolls[box_in_frame + 1] == 10