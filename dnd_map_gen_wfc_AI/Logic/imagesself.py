import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import random
import math

from typing import List

class onlyColorChangePixels():
    def __init__(self):
        self.cr1 = [[216, 216, 216, 216],
                    [216, 228, 228, 228],
                    [216, 228, 252, 228],
                    [216, 228, 228, 228]]        
        self.cr2 = [[180, 180, 180, 180],
                    [180, 192, 192, 192],
                    [180, 192, 204, 192],
                    [180, 192, 192, 192]]
        self.cr3 = [[108, 108, 108, 108],
                    [108, 120, 120, 120],
                    [108, 120, 132, 120],
                    [108, 120, 120, 120]]
        self.cr4 = [[144, 144, 144, 144],
                    [144, 156, 156, 156],
                    [144, 156, 168, 156],
                    [144, 156, 156, 156]]
        self.cr5 = [[72, 72, 72, 72],
                    [72, 84, 84, 84],
                    [72, 84, 96, 84],
                    [72, 84, 84, 84]]
        self.cr6 = [[36, 36, 36, 36],
                    [36, 48, 48, 48],
                    [36, 48, 60, 48],
                    [36, 48, 48, 48]]
        self.cr7 = [[0, 0, 0, 0],
                    [0, 12, 12, 12],
                    [0, 12, 24, 12],
                    [0, 12, 12, 12]]


difficulty = 7
input_size = (4, 4)
output_size = (25, 25)#10/50 !
default_color = 'Spectral'
colorChangePixels = onlyColorChangePixels()  # Create an instance of the class

if difficulty == 1:
    pixels = colorChangePixels.cr1
if difficulty == 2:
    pixels = colorChangePixels.cr2
if difficulty == 3:
    pixels = colorChangePixels.cr3
if difficulty == 4:
    pixels = colorChangePixels.cr4
if difficulty == 5:
    pixels = colorChangePixels.cr5
if difficulty == 6:
    pixels = colorChangePixels.cr6
if difficulty == 7:
    pixels = colorChangePixels.cr7
plt.imshow(pixels, cmap= default_color, vmin=0, vmax=255) 

# valid colors 'Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r'
plt.show()

class Pattern:
    def __init__(self, pixels):
        self.pixels = pixels
        
    def __len__(self):
        return 1
    
def get_all_rotations(pixelMatrix):
    """
    Return original array as well as rotated by 90, 180 and 270 degrees in the form of tuples
    """
    pixelMatrix_rotated_1 = [[pixelMatrix[j][i] for j in range(len(pixelMatrix))] for i in range(len(pixelMatrix[0])-1,-1,-1)]
    pixelMatrix_rotated_2 = [[pixelMatrix_rotated_1[j][i] for j in range(len(pixelMatrix_rotated_1))] for i in range(len(pixelMatrix_rotated_1[0])-1,-1,-1)]
    pixelMatrix_rotated_3 = [[pixelMatrix_rotated_2[j][i] for j in range(len(pixelMatrix_rotated_2))] for i in range(len(pixelMatrix_rotated_2[0])-1,-1,-1)]
    return tuple(tuple(row) for row in pixelMatrix), \
            tuple(tuple(row) for row in pixelMatrix_rotated_1), \
            tuple(tuple(row) for row in pixelMatrix_rotated_2), \
            tuple(tuple(row) for row in pixelMatrix_rotated_3)

N = 2 # pattern size



patterns = []
weights = {} 
probability = {} 
for y in range(input_size[0]-(N-1)): # row 
    for x in range(input_size[1]-(N-1)): # column
        pattern = []
        for k in pixels[y:y+N]:
            pattern.append([int(i) for i in k[x:x+N]]) # change array to int really quick
        pattern_rotations = get_all_rotations(pattern)
        
        for rotation in pattern_rotations:
            if rotation not in weights:
                weights[rotation] = 1
            else:
                weights[rotation] += 1
        
        patterns.extend(pattern_rotations)
        
# remove duplicates
patterns_without_duplicates = []
for patt in patterns:
    if patt not in patterns_without_duplicates:
        patterns_without_duplicates.append(patt)
patterns = patterns_without_duplicates

sum_of_weights = 0
for weight in weights:
    sum_of_weights += weights[weight]

for pattern in patterns:
    probability[pattern] = weights[pattern] / sum_of_weights
    
# convert patterns from tuples into Pattern objects
patterns = [Pattern(p) for p in patterns]
weights = {pattern:weights[pattern.pixels] for pattern in patterns}
probability = {pattern:probability[pattern.pixels] for pattern in patterns}

# show 
plt.figure(figsize=(10,10))
for m in range(len(patterns)):
    axs = plt.subplot(4, math.ceil(len(patterns)/4), m+1)
    axs.imshow(patterns[m].pixels, cmap= default_color, vmin=0, vmax=255)
    axs.set_xticks([])
    axs.set_yticks([])
    plt.title("weight: %.0f prob: %.2f"%(weights[patterns[m]], probability[patterns[m]]))
plt.show()

UP = (0, -1)
LEFT = (-1, 0)
DOWN = (0, 1)
RIGHT = (1, 0)
UP_LEFT = (-1, -1)
UP_RIGHT = (1, -1)
DOWN_LEFT = (-1, 1)
DOWN_RIGHT = (1, 1)
dirs = [UP, DOWN, LEFT, RIGHT, UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT]

def valid_dirs(pos):
    x, y = pos
    
    valid_directions = []

    if x == 0:
        valid_directions.extend([RIGHT])
        if y == 0:
            valid_directions.extend([DOWN, DOWN_RIGHT])
        elif y == output_size[1]-1:
            valid_directions.extend([UP, UP_RIGHT])
        else:
            valid_directions.extend([DOWN, DOWN_RIGHT, UP, UP_RIGHT])
    elif x == output_size[0]-1:
        valid_directions.extend([LEFT])
        if y == 0:
            valid_directions.extend([DOWN, DOWN_LEFT])
        elif y == output_size[1]-1:
            valid_directions.extend([UP, UP_LEFT])
        else:
            valid_directions.extend([DOWN, DOWN_LEFT, UP, UP_LEFT])
    else:
        valid_directions.extend([LEFT, RIGHT])
        if y == 0:
            valid_directions.extend([DOWN, DOWN_LEFT, DOWN_RIGHT])
        elif y == output_size[1]-1:
            valid_directions.extend([UP, UP_LEFT, UP_RIGHT])
        else: 
            valid_directions.extend([UP, UP_LEFT, UP_RIGHT, DOWN, DOWN_LEFT, DOWN_RIGHT])
    
    return valid_directions

class Index:    
    def __init__(self, patterns: List[Pattern]):
        self.data = {}
        for pattern in patterns:
            self.data[pattern] = {}
            for d in dirs: 
                self.data[pattern][d] = []
    
    def add_rule(self, pattern: Pattern, relative_position: tuple, next_pattern: Pattern):
        self.data[pattern][relative_position].append(next_pattern)
        
        
    def check_possibility(self, pattern: Pattern, check_pattern: Pattern, relative_pos: tuple):
        if isinstance(pattern, list):
            pattern = pattern[0]
            
        return check_pattern in self.data[pattern][relative_pos]

index = Index(patterns)

def get_offset_tiles(pattern: Pattern, offset: tuple):
    if offset == (0, 0):
        return pattern.pixels
    if offset == (-1, -1):
        return tuple([pattern.pixels[1][1]])
    if offset == (0, -1):
        return tuple(pattern.pixels[1][:])
    if offset == (1, -1):
        return tuple([pattern.pixels[1][0]])
    if offset == (-1, 0):
        return tuple([pattern.pixels[0][1], pattern.pixels[1][1]])
    if offset == (1, 0):
        return tuple([pattern.pixels[0][0], pattern.pixels[1][0]])
    if offset == (-1, 1):
        return tuple([pattern.pixels[0][1]])
    if offset == (0, 1):
        return tuple(pattern.pixels[0][:])
    if offset == (1, 1):
        return tuple([pattern.pixels[0][0]])

rules_num = 0
for pattern in patterns:
    for d in dirs:
        for pattern_next in patterns:
            overlap = get_offset_tiles(pattern_next, d)
            og_dir = tuple([d[0]*-1, d[1]*-1])
            part_of_og_pattern = get_offset_tiles(pattern, og_dir)
            if (overlap) == (part_of_og_pattern):
                index.add_rule(pattern, d, pattern_next)
                rules_num+=1


def initialize_wave_function(size):    
    coefficients = []
    
    for col in range(size[0]):
        row = []
        for r in range(size[1]):
            row.append(patterns)
        coefficients.append(row)
    return coefficients

coefficients = initialize_wave_function(output_size)

def is_fully_collapsed():
    for col in coefficients:
        for entry in col:
            if(len(entry)>1):
                return False
    return True

def get_possible_patterns_at_position(position):
    x, y = position
    possible_patterns = coefficients[x][y]
    return possible_patterns

def get_shannon_entropy(position):

    x, y = position
    entropy = 0
    
    # A cell with one valid pattern has 0 entropy
    if len(coefficients[x][y]) == 1:
        return 0
    
    for pattern in coefficients[x][y]:
        entropy += probability[pattern] * math.log(probability[pattern], 2)
    entropy *= -1
    
    entropy -= random.uniform(0, 0.1)
    return entropy

def get_min_entropy_pos():
    minEntropy = None
    minEntropyPos = None
    
    for x, col in enumerate(coefficients):
        for y, row in enumerate(col):
            entropy = get_shannon_entropy((x, y))
            
            if entropy == 0:
                continue
            
            if minEntropy is None or entropy < minEntropy:
                minEntropy = entropy
                minEntropyPos = (x, y)
    return minEntropyPos


def observe():
    min_entropy_pos = get_min_entropy_pos()
    
    if min_entropy_pos == None:
        print("All tiles have 0 entropy")
        return
    
    possible_patterns = get_possible_patterns_at_position(min_entropy_pos)
    
    max_p = 0
    for pattern in possible_patterns:
        if max_p < probability[pattern]:
            max_p == probability[pattern]
    
    
    semi_random_pattern = random.choice([pat for pat in possible_patterns 
                                         if probability[pat]
                                         >=max_p])
    # TODO dont forget to check the probability of the pattern
    coefficients[min_entropy_pos[0]][min_entropy_pos[1]] = semi_random_pattern
    
    return min_entropy_pos


def propagate(min_entropy_pos):
    stack = [min_entropy_pos]
    
    while len(stack) > 0:
        pos = stack.pop()
        
        possible_patterns = get_possible_patterns_at_position(pos)
        for d in valid_dirs(pos):
            adjacent_pos = (pos[0] + d[0], pos[1] + d[1])
            possible_patterns_at_adjacent = get_possible_patterns_at_position(adjacent_pos)
            
            if not isinstance(possible_patterns_at_adjacent, list):
                possible_patterns_at_adjacent = [possible_patterns_at_adjacent]
            for possible_pattern_at_adjacent in possible_patterns_at_adjacent:
                if len(possible_patterns) > 1:
                    is_possible = any([index.check_possibility(pattern, possible_pattern_at_adjacent, d) for pattern in possible_patterns])
                else:
                    is_possible = index.check_possibility(possible_patterns, possible_pattern_at_adjacent, d)                    

                if not is_possible:
                    x, y = adjacent_pos
                    coefficients[x][y] = [patt for patt in coefficients[x][y] if patt.pixels != possible_pattern_at_adjacent.pixels]
                        
                    if adjacent_pos not in stack:
                        stack.append(adjacent_pos)


while not is_fully_collapsed():
    min_entropy_pos = observe()
    propagate(min_entropy_pos)                    

final_pixels = []

for coefficient in coefficients:
    row = []
    for item in coefficient:
        first_pixel = item.pixels[0][0] if not isinstance(item, list) else item[0].pixels[0][0]
        row.append(first_pixel)
    final_pixels.append(row)

plt.imshow(final_pixels, cmap=default_color, vmin=0, vmax=255)
plt.show()