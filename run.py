from os import path
import pyglet
import random

from engine.game import Game
from lab import FastMonster


def get_random():
    return random.uniform(0.05, 0.90)

# ------- Your Code Here -------


# ------- End Code Here -------
if __name__ == '__main__':
    game.start_game()
    pyglet.app.run()
