# Import the necessary libraries
import pygame
import random

# Initialize pygame
pygame.init()

# Set the font for any text you want to display
font = pygame.font.Font("./assets/custom_fonts/Poppins/Poppins-Light.ttf", 16)

# Define the Cell class. Each cell represents a tile in the final map.
class Cell:
    # The constructor for the Cell class. It takes the x and y coordinates of the cell,
    # the resolution of the cell (how big it is), and the possible tiles that can be in this cell.
    def __init__(self, x, y, rez, options):
        self.x = x
        self.y = y
        self.rez = rez
        self.options = options
        self.collapsed = False

    # The draw method for the Cell class. It draws the tile on the screen if there is only one option left.
    def draw(self, win):        
        if len(self.options) == 1:
            self.options[0].draw(win, self.y * self.rez, self.x * self.rez)
            
    # The entropy method returns the number of possible options for this cell. 
    # The more options, the higher the entropy.
    def entropy(self):
        return len(self.options)

    # The update method checks if the cell has been collapsed (i.e., there is only one option left).
    def update(self):
        self.collapsed = bool(self.entropy() == 1)

    # The observe method randomly chooses one of the options and collapses the cell to that state.
    def observe(self):
        try:
            self.options = [random.choice(self.options)]
            self.collapsed = True
        except:
            return
