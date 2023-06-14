import matplotlib.pyplot as plt
import math
from Logic.Pattern import Pattern
class PatternLogic:
   
    def get_all_rotations(self, pixelMatrix):
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
       
    def calculate_patterns_weights_propability(self, N,input_size,pixels):
        patterns = []
        weights = {} 
        probability = {} 
        for y in range(input_size[0]-(N-1)): # row 
            for x in range(input_size[1]-(N-1)): # column
                pattern = []
                for k in pixels[y:y+N]:
                    pattern.append([int(i) for i in k[x:x+N]]) # change array to int really quick
                
                rotation = self.get_all_rotations(pattern)
                pattern_rotations = rotation
                
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
        return patterns, weights, probability
