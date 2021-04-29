import time
import random
import sys
from character import Character
from character import NPC
from character import bad_input
from item import item

def d_p(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)
    print("")

class Story(Character):
    def __init__(self):
        pass
    def intro(Character):
        print("Welcome to Twisted Trees.")
        time.sleep(.5)
        playedBefore = input("Have you played before (yes/no): ")
        print(playedBefore)



player = Character("A", "human", "shaman", 100, 100, 100, 100, 100, 100, 100, 100, "")
Story.intro(player)
Character.player_creation(player)
Character.get_char_stats(player)
Character.get_char_info(player)
Character.fightIntro(player)
Character.fight(player, robber)