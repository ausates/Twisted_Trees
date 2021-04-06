import time
import random
import sys
from character import d_p
from character import Character
from character import NPC
from character import bad_input

def intro():
    d_p("Welcome to RPG, a text based RPG.")
    q_1 = ""
    while q_1 == "":
        q_1 = input("Have you played RPG before? (yes/no): ")
        if q_1.lower() == "yes":
            pass
        elif q_1.lower() == "no":
            pass
        else:
            bad_input()
            q_1 = ""
    d_p("First, we need to build your character.")
    q_2 = ""
    while q_2 == "":
        q_2 = input("Do you know about character races in RPG? (yes/ no): ").lower()
        if q_2 == "yes":
            print("Great, we will skip the races intro.")
        elif q_2 == "no":
            pass
        else:
            bad_input()
            q_2 = ""
    q_3 = ""
    while q_3 == "":
        d_p("Okay, final question.")
        q_3 = input("Do you know about character classes and attributes in RPG? (yes/no): ").lower()
        if q_3 == "yes":
            print("great, we will skip the classes intro, and build your character.")
        elif q_3 == "no":
            pass
        else:
            bad_input()
            q_3 = ""


def starting_level():
    Character.fight(player, robber)
    Character.get_char_info(player)
    Character.get_char_stats(player)

player = Character("", "", "", 10, 10, 10, 10, 10, 10, 10, 10)
robber = NPC("Robber", "human", "fighter", 50, 10, 1, 1, 50, 1, 1, random.random())
intro()
Character.player_creation(player)
starting_level()