import barrier
from configuration.config import config


class BarriersHandler:
    def __init__(self):
        self.__barriers_list = []
        self.__barriers_amount = config.barrier['barriers_amount']

    @property
    def barriers_coordinates_list(self):
        return [bar.coordinates for bar in self.__barriers_list]

    def __add_barrier(self):
        bar = barrier.Barrier()
        # while not bar.has_free_coord(self.barriers_coordinates_list):
           # bar = barrier.Barrier()

        self.__barriers_list.append(bar)

    def __filter_barriers(self):
        if not self.__barriers_list:
            return

        for bar in self.__barriers_list:
            if not bar.is_actual:
                self.__barriers_list.remove(bar)

    def __set_barriers(self):
        while len(self.__barriers_list) < self.__barriers_amount:
            self.__add_barrier()

    def update_barriers_list(self):
        self.__filter_barriers()
        self.__set_barriers()

    def move_barriers(self):
        for bar in self.__barriers_list:
            bar.move_down()

    def present_barriers(self, surface):
        for bar in self.__barriers_list:
            bar.draw(surface)
