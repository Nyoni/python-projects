""" 2D Arcade Game skeleton to build my platform on
    
    Author: Tafadzwa Nyoni - Guizer Technologies """


import arcade   #importing the arcade library

class Platformer(arcade.Window):    #define class used to run the whole game. methods of this class are called to update game state, proicess input, & draw items on screen
    def __init__(self):     #Initializes the game code. Add code that handles actions that are taken when the game first starts 
        pass

    def setup(self):    #sets up the game to be begin playing. Add code that may need to be repeated throughout the game. eg initialize new levels on success or reset the current level on failure
        """This function sets game for the current level"""
        pass

    def on_key_press(self, key: int, modifiers: int ):  ##on key press & release allows for processing keyboard input independently.      #
        """Processes key presses

        -key(int)---> which key was pressed
        -modifiers(int)---> which modifiers where down at the time
        """

    def on_key_release(self, key: int, modifiers: int):
        """Processes key releases"""

    def on_update(self, delta_time: float):
        """Updates the position of game objects

        -delta_time(float)---> time after last call
        """
        pass

    def on_draw(self):  #where everything displayed in your game drawn
        pass


if __name__ == "__main__": #main entry point of the game
    window = Platformer()   #game object window based on the class defined
    window.setup()  #setup the game by calling window.setup
    arcade.run()    #start game loop by calling arcade.run            