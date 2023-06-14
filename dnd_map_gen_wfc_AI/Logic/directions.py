class Directions:
    UP = (0, -1)
    LEFT = (-1, 0)
    DOWN = (0, 1)
    RIGHT = (1, 0)
    UP_LEFT = (-1, -1)
    UP_RIGHT = (1, -1)
    DOWN_LEFT = (-1, 1)
    DOWN_RIGHT = (1, 1)
    dirs = [UP, DOWN, LEFT, RIGHT, UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT]

    def __init__(self, output_size):
        self.output_size = output_size

    def give_dirs(self):
        return self.dirs
    def valid_dirs(self, pos):
        x, y = pos

        valid_directions = []

        if x == 0:
            valid_directions.extend([self.RIGHT])
            if y == 0:
                valid_directions.extend([self.DOWN, self.DOWN_RIGHT])
            elif y == self.output_size[1] - 1:
                valid_directions.extend([self.UP, self.UP_RIGHT])
            else:
                valid_directions.extend([self.DOWN, self.DOWN_RIGHT, self.UP, self.UP_RIGHT])
        elif x == self.output_size[0] - 1:
            valid_directions.extend([self.LEFT])
            if y == 0:
                valid_directions.extend([self.DOWN, self.DOWN_LEFT])
            elif y == self.output_size[1] - 1:
                valid_directions.extend([self.UP, self.UP_LEFT])
            else:
                valid_directions.extend([self.DOWN, self.DOWN_LEFT, self.UP, self.UP_LEFT])
        else:
            valid_directions.extend([self.LEFT, self.RIGHT])
            if y == 0:
                valid_directions.extend([self.DOWN, self.DOWN_LEFT, self.DOWN_RIGHT])
            elif y == self.output_size[1] - 1:
                valid_directions.extend([self.UP, self.UP_LEFT, self.UP_RIGHT])
            else: 
                valid_directions.extend([self.UP, self.UP_LEFT, self.UP_RIGHT, self.DOWN, self.DOWN_LEFT, self.DOWN_RIGHT])

        return valid_directions
