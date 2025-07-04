import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            # Return everything if requested draw exceeds available
            drawn = self.contents.copy()
            self.contents.clear()
            return drawn

        # Draw random balls without replacement
        drawn = random.sample(self.contents, num_balls)
        for ball in drawn:
            self.contents.remove(ball)
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)

        drawn_counter = {}
        for ball in drawn_balls:
            drawn_counter[ball] = drawn_counter.get(ball, 0) + 1

        success = True
        for color, expected_count in expected_balls.items():
            if drawn_counter.get(color, 0) < expected_count:
                success = False
                break

        if success:
            success_count += 1

    return success_count / num_experiments
