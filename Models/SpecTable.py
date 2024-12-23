class SpecTable:
    def __init__(self, num_cols:int):
        self.data = []
        self.current_cell = {"x": 2,"y":0} # first two cols are not input texts
        self.num_cols = num_cols
        
    def get_current_cell(self):
        return self.current_cell

    def shift_current_cell_left(self):
        if self.current_cell["x"] > 2:
            self.current_cell["x"] -= 1

        print(self.current_cell)

    def shift_current_cell_right(self):
        if self.current_cell["x"] < self.num_cols - 1:
            self.current_cell["x"] += 1

        print(self.current_cell)
        
    def shift_current_cell_up(self):
        if self.current_cell["y"] > 0:
            self.current_cell["y"] -= 1

        print(self.current_cell)

    def shift_current_cell_down(self):
        if self.current_cell["y"] < len(self.data) - 1:
            self.current_cell["y"] += 1

        print(self.current_cell)



    


