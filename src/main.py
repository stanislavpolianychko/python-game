import game_window
import constants as const

win = game_window.Window((const.WIDTH, const.HEIGHT), const.LABEL)
win.start_mainloop(const.FPS)
