# constants.py
# (x - width, y - hieght)
# basic constants
FPS = 200  # ** DO NOT CHANGE **
BACKG_COLOR = (255, 255, 255)
SCREEN = (1920, 1080)  # 1920, 1080
CHAR_SIZE = 50
STARTING_POS = [SCREEN[0]//2, SCREEN[1]//2]
LOWER_BOUND_ADD = 20
VIEW_BOX = (0, -2, 20, 24)  # units is each tile
TILE_SIZE = 100
TILE_ORT = TILE_SIZE//2  # ** DO NOT CHANGE ** Tile orientation (rotation)

# direction, character movement
SPEED = (4, -4)  # ratio 1:1, giving a 45% angle
LEFT = (-SPEED[0], SPEED[1])
RIGHT = (SPEED[0], SPEED[1])

# textures and color
CHAR_COLOR = (255, 100, 0)
STMP_COLOR = (0, 100, 255)
