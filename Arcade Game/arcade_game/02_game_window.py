import arcade 
import pathLib

#Game constants
#Window dimensions

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Guizer Arcade"

#Assets path
ASSETS_PATH = pathlib.Path(__file).resolve().parent.parent / "assets"

class Platformer(arcade.window):
    def __init__(self) -> None:
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        #List to hold different sets of sprites
        self.coins = None
        self.background = None
        self.walls = None
        self.ladders = None
        self.goals = None
        self.enemies = None

        #one sprite for the player
        self.player = None

        #physics engine inodikwa
        self.pysics_engine = None

        #keeping score
        self.score = 0

        #keeping track of the level yatiri
        self.level = 1

        #load up our sounds here
        self.coin_sound = arcade.load_sound(
            str(ASSETS_PATH / "sounds"/ "coin.wav")
        )
        self.jump_sound = arcade.load_sound(
            str(ASSETS_PATH / "sounds"/ "jump.wav")

        )
        self.victory_sound = aracade.load_sound(
            str(ASSETS_PATH / "sounds"/ "victory.wav")
        )