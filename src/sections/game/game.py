from configuration.config import config
from src.sections.game.player import Player
from src.sections.game.barriers_handler import BarriersHandler
from src.sections.screen_section import ScreenSection


class Game(ScreenSection):
    def __init__(self, surface, bg_image):
        super().__init__(surface, bg_image)
        self._player = Player()
        self._barriers_handler = BarriersHandler()

    # check if player haven't crashed on barrier
    def _review_win(self):
        if not self._barriers_handler.barriers_coordinates_list:
            return True

        player_x, player_y = self._player.coordinates
        for barrier_x, barrier_y in self._barriers_handler.barriers_coordinates_list:
            left_top_x = barrier_x <= player_x <= barrier_x + config.barrier['width']
            left_top_y = barrier_y <= player_y <= barrier_y + config.barrier['height']

            right_top_x = barrier_x <= player_x + config.player['width'] <= barrier_x + config.barrier['width']
            right_top_y = barrier_y <= player_y <= barrier_y + config.barrier['height']

            if (left_top_x and left_top_y) or (right_top_x and right_top_y):
                return False
        return True

    # main loop of the game
    def run(self):
        while self._review_win():
            self._check_for_exit()

            self._player.move()
            self._player.draw(self._surface)

            self._barriers_handler.update_barriers_list()
            self._barriers_handler.move_barriers()
            self._barriers_handler.present_barriers(self._surface)

            self._refresh()

            self._clock.tick(config.window['fps'])
