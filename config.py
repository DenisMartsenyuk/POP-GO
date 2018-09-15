class Config:

    class Field:
        CELL_SIZE = 20
        CELL_COUNT = 32
        CANV_INDENTS = 10
        CANV_COLOR = "#bedce3"
        VICINITY_DIST = CELL_SIZE * 3/8

    class Point:
        PLAYER1_COLOR = 'red'
        PLAYER2_COLOR = 'blue'
        UNUSED_COLOR = 'red'
        RADIUS = 2
        COVER_RADIUS = 5

    class StartMenu:
        COLOR = 'white'

    class GameMenu:
        COLOR = 'white'
        SIZE =  250
