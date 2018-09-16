class Config:

    class Field:
        CELL_SIZE = 20
        CELL_COUNT = 32
        CANV_INDENTS = 10
        CANV_COLOR = "#f1f1f0"
        #CANV_COLOR = "#d7e0eb"
        VICINITY_DIST = CELL_SIZE * 3/8

    class GUI:
        #COLOR = '#c2d2e9'
        #COLOR = '#c8bd00'
        COLOR = '#75706f'

    class Point:
        PLAYER1_COLOR = 'red'
        PLAYER2_COLOR = '#00498e'
        UNUSED_COLOR = 'gray'
        RADIUS = 4
        COVER_RADIUS = 5

    class StartMenu:
        COLORPRESS = 'gray'
        COLORFG = '#ffca00'
        FONT = 'Ubuntu 64'
        GEOM = '600x170+200+200'

    class GameMenu:
        COLORPRESS = '#f9ec8f'
        COLORFG = '#ffca00'
        SIZE = 275
        FONT = 'Ubuntu 43'
