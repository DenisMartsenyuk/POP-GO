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
        COLOR = 'white'

    class Point:
        PLAYER1_COLOR = 'red'
        PLAYER2_COLOR = '#00498e'
        UNUSED_COLOR = 'gray'
        RADIUS = 4
        COVER_RADIUS = 5

    class StartMenu:
        COLORPRESS = 'gray'
        COLORFG = '#00aab7'
        FONT = 'Ubuntu 64'
        GEOM = '600x170+200+200'

    class Sph:
        r = 40

    class GameMenu:
        COLORPRESS = '#007A83'
        COLORBG = '#00aab7'
        COLORTEXT = 'white'
        COLORFG = '#00aab7'
        SIZE = 160
        FONT = 'BebasNeueRegular 54'

    class Client:
        HOST = "ejudge.mikkerlo.ru"
        PORT = 1337
