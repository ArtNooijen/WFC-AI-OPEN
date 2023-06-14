from typing import List
from Logic.Pattern import Pattern
from Logic.directions import Directions

class Index:    
    
    def __init__(self, patterns: List[Pattern], output_size):
        dirs = Directions(output_size).give_dirs()
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