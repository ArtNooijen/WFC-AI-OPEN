class Cell:
    def __init__(self, value):
        self.collapsed = False
        if isinstance(value, list):
            self.options = value
        else:
            self.options = [i for i in range(value)]
