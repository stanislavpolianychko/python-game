import barrier
from configuration.config import config


class BarriersHandler:
    def __init__(self):
        self.__barriers_list = []
        self.__barriers_amount = config.barrier['barriers_amount']

    @property
    def barriers_coordinates_list(self):
        return [bar.coordinates for bar in self.__barriers_list]

    def update_barriers_list(self):
        self.__filter_barriers()
        self.__add_barriers()

    def __set_barrier(self):
        bar = barrier.Barrier()
        while bar.coordinates in self.barriers_coordinates_list:
            bar = barrier.Barrier()
        self.__barriers_list.append(bar)

    def __filter_barriers(self):
        for bar in self.__barriers_list:
            if not bar.is_actual:
                self.__barriers_list.remove(bar)

    def __add_barriers(self):
        while len(self.__barriers_list) < self.__barriers_amount:
            self.__set_barrier()
