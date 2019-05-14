class Config:

    class Field:
        CELL_SIZE = 20
        CELL_COUNT = 32
        CANV_INDENTS = 10
        CANV_COLOR = "#f1f1f0"
        RECT_COLOR = "#e6be00"
        #CANV_COLOR = "#d7e0eb"
        VICINITY_DIST = CELL_SIZE * 3/8

    class GUI:
        #COLOR = '#c2d2e9'
        #COLOR = '#c8bd00'
        COLOR = 'black'

    class Point:
        PLAYER1_COLOR = 'red'
        PLAYER2_COLOR = '#00498e'
        UNUSED_COLOR = '#e6be00'
        RADIUS = 4
        COVER_RADIUS = 5

    class StartMenu:
        COLORPRESS = 'gray'
        #COLORFG = '#00aab7'
        # золото
        COLORFG = '#e6be00'
        FONT = 'BebasNeueRegular 99'
        GEOM = '480x180+500+300'
        R = 20
        GEOMX = 480
        GEOMY = 200

    class Sph:
        r = 40

    class GameMenu:
        COLORPRESS = '#007A83'
        #золото
        #COLORBG = '#e6be00'
        #COLORTEXT = 'e6be00'
        #COLORFG = '#00aab7'
        # золото
        COLORFG = '#e6be00'
        SIZE = 160
        FONT = 'BebasNeueRegular 54'
    
    class Client:
        HOST = "ejudge.mikkerlo.ru"
        PORT = 1337
