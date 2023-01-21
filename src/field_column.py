class Column:
    def __init__(self, col_num: int):
        self.number_of_column = col_num
        self.column_coord = None
        self.is_free = True
        self.barrier = None

    def set_barrier(self, barrier):
        self.is_free = False
        self.barrier = barrier
        self.column_coord = self.number_of_column * self.barrier.image_w

    def draw_barrier(self, surface):
        surface.blit(self.barrier.image_path, (self.column_coord, self.barrier.position))