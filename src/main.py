import game_window
from configuration.config import config

win = game_window.Window((config.window['width'], config.window['height']), config.window['label'])
win.start_mainloop()
