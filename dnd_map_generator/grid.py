# Import required libraries
import copy
import random
from cell import Cell

# Grid class
class Grid:
    def __init__(self, width, height, rez, options):
        self.width = width
        self.height = height
        self.rez = rez
        self.w = self.width // self.rez
        self.h = self.height // self.rez
        self.grid = []
        self.options = options

    # Initialize each spot in the grid with a cell object
    def initiate(self):
        for i in range(self.w):
            self.grid.append([])
            for j in range(self.h):
                cell = Cell(i, j, self.rez, self.options)
                self.grid[i].append(cell)

    # Draw each cell in the grid
    def draw(self, win):
        for row in self.grid:
            for cell in row:
                cell.draw(win)

    # Select a cell using entropy heuristic
    def heuristic_pick(self):
        # Create a copy of the grid and sort it by entropy
        grid_copy = [i for row in self.grid for i in row]
        grid_copy.sort(key=lambda x: x.entropy())

        # Filter the grid to include only cells with entropy greater than 1
        filtered_grid = list(filter(lambda x: x.entropy() > 1, grid_copy))
        if filtered_grid == []:
            return None

        # Filter the grid to include only cells with the smallest entropy
        initial = filtered_grid[0]
        filtered_grid = list(filter(lambda x: x.entropy() == initial.entropy(), filtered_grid))     

        # Return a random cell from the filtered grid
        return random.choice(filtered_grid)

    # Perform the Wave Function Collapse algorithm
    def collapse(self):
        # Pick a cell using entropy heuristic
        pick = self.heuristic_pick()
        if pick:
            pick.observe()
        else:
            return

        # Create a copy of the grid
        next_grid = copy.copy(self.grid)

        # Update the entropy values and superpositions of each cell in the grid
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j].collapsed:
                    next_grid[i][j] = self.grid[i][j]
                else:
                    # cumulative_valid_options will hold the options that will satisfy the "down", "right", "up", "left" 
                    # conditions of each cell in the grid. 
                    cumulative_valid_options = self.options

                    # For each neighboring cell, find the valid options and update the cumulative_valid_options
                    # to include only those options that are valid for all neighbors
                    for direction in ["up", "right", "down", "left"]:
                        neighbor = self.grid[(i + {"up": -1, "down": 1}.get(direction, 0)) % self.w][(j + {"right": 1, "left": -1}.get(direction, 0)) % self.h]
                        valid_options = [option for neighbor_option in neighbor.options for option in getattr(neighbor_option, direction)]
                        cumulative_valid_options = [option for option in cumulative_valid_options if option in valid_options]

                    # Update the options and the collapsed state of the cell
                    next_grid[i][j].options = cumulative_valid_options
                    next_grid[i][j].update()

        # Update the grid
        self.grid = copy.copy(next_grid)
# Import required libraries
import copy
import random
from cell import Cell

# Grid class
class Grid:
    def __init__(self, width, height, rez, options):
        self.width = width
        self.height = height
        self.rez = rez
        self.w = self.width // self.rez
        self.h = self.height // self.rez
        self.grid = []
        self.options = options

    # Initialize each spot in the grid with a cell object
    def initiate(self):
        for i in range(self.w):
            self.grid.append([])
            for j in range(self.h):
                cell = Cell(i, j, self.rez, self.options)
                self.grid[i].append(cell)

    # Draw each cell in the grid
    def draw(self, win):
        for row in self.grid:
            for cell in row:
                cell.draw(win)

    # Select a cell using entropy heuristic
    def heuristic_pick(self):
        # Create a copy of the grid and sort it by entropy
        grid_copy = [i for row in self.grid for i in row]
        grid_copy.sort(key=lambda x: x.entropy())

        # Filter the grid to include only cells with entropy greater than 1
        filtered_grid = list(filter(lambda x: x.entropy() > 1, grid_copy))
        if filtered_grid == []:
            return None

        # Filter the grid to include only cells with the smallest entropy
        initial = filtered_grid[0]
        filtered_grid = list(filter(lambda x: x.entropy() == initial.entropy(), filtered_grid))     

        # Return a random cell from the filtered grid
        return random.choice(filtered_grid)

    # Perform the Wave Function Collapse algorithm
    def collapse(self):
        # Pick a cell using entropy heuristic
        pick = self.heuristic_pick()
        if pick:
            pick.observe()
        else:
            return

        # Create a copy of the grid
        next_grid = copy.copy(self.grid)

        # Update the entropy values and superpositions of each cell in the grid
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j].collapsed:
                    next_grid[i][j] = self.grid[i][j]
                else:
                    # cumulative_valid_options will hold the options that will satisfy the "down", "right", "up", "left" 
                    # conditions of each cell in the grid. 
                    cumulative_valid_options = self.options

                    # For each neighboring cell, find the valid options and update the cumulative_valid_options
                    # to include only those options that are valid for all neighbors
                    for direction in ["up", "right", "down", "left"]:
                        neighbor = self.grid[(i + {"up": -1, "down": 1}.get(direction, 0)) % self.w][(j + {"right": 1, "left": -1}.get(direction, 0)) % self.h]
                        valid_options = [option for neighbor_option in neighbor.options for option in getattr(neighbor_option, direction)]
                        cumulative_valid_options = [option for option in cumulative_valid_options if option in valid_options]

                    # Update the options and the collapsed state of the cell
                    next_grid[i][j].options = cumulative_valid_options
                    next_grid[i][j].update()

        # Update the grid
        self.grid = copy.copy(next_grid)
