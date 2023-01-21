# colors
COLOR_BLUE = (0, 0, 255)
COLOR_BLACK = (0, 0, 0)

# window params
WIDTH, HEIGHT = 320, 480
MIN_X = -5
MAX_X = 260
LABEL = "SpaceWars"
FPS = 60
BACK_GROUND_IMAGE_PATH = "src/images/bg.png"

# player params
PLAYER_IMAGE_PATH = "src/images/space-ship.png"
PLAYER_X = WIDTH // 2
PLAYER_Y = HEIGHT - (HEIGHT // 5)
PLAYER_SPEED = 5

# barrier params
BARRIER_IMAGE_PATH1 = "src/images/space-ship.png"
BARRIER_IMAGE_PATH2 = "src/images/space-ship.png"
BARRIER_IMAGE_PATH3 = "src/images/space-ship.png"
BARRIERS_LIST = [BARRIER_IMAGE_PATH1, BARRIER_IMAGE_PATH2, BARRIER_IMAGE_PATH3]
BARRIERS_WIDTH = 64
BARRIERS_HEIGHT = 64

# columns params
COLUMNS_COUNT = WIDTH // BARRIERS_WIDTH
COLUMN_WIDTH = WIDTH // COLUMNS_COUNT
