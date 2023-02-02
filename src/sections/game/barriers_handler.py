from src.sections.game import barrier
from configuration.config import config


class BarriersHandler:
    """Class, which helps to handle all barriers on game field."""
    def __init__(self):
        self._barriers_list = []
        self._barriers_amount = config.barrier['barriers_amount']

    # property to get a list with all barriers coordinates
    @property
    def barriers_coordinates_list(self):
        return [bar.coordinates for bar in self._barriers_list]

    # add unique barrier
    def _add_barrier(self):
        bar = barrier.Barrier()
        while not bar.has_free_coord(self.barriers_coordinates_list):
            bar = barrier.Barrier()

        self._barriers_list.append(bar)

    # del all barriers, which are out of the window range
    def _filter_barriers(self):
        if not self._barriers_list:
            return

        for bar in self._barriers_list:
            if not bar.is_actual:
                self._barriers_list.remove(bar)

    # set necessary count of barriers
    def _set_barriers(self):
        while len(self._barriers_list) < self._barriers_amount:
            self._add_barrier()

    # del old barriers and add new
    def update_barriers_list(self):
        self._filter_barriers()
        self._set_barriers()

    # move down all barriers
    def move_barriers(self):
        for bar in self._barriers_list:
            bar.move_down()

    # show barriers in window
    def present_barriers(self, surface):
        for bar in self._barriers_list:
            bar.draw(surface)
