import time
import sys
import random
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)

class Player:
    def __init__(self, name, race):
        self.name = name
        self.race = race

    def fight(self,):
       delay_print("Let's fight.")

class NPC:
    def __init__(self, name, hp, atk, df, mage, rng):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.df = df
        self.mage = mage
        self.rng = rng

a = Player("", "")
def game():
    intro()

def intro():
    print("Welcome to my game of Snakes!")
    # time.sleep(2)
    # print(".")
    # time.sleep(.3)
    # print("..")
    # time.sleep(.4)
    # print("...")
    # time.sleep(.2)
    # delay_print("Well... my Python text-based RPG meant to illuminate what I have learned about Python.")
    # delay_print("\nSince you're seeing this, I can obviously print, and I even have a delay print function.")
    # print("\nwow, right?")
    # time.sleep(.5)
    # print("\nAnyway...")
    # time.sleep(.5)
    # delay_print("A game requires some kinda input, yes?")
    # delay_print(" \nSo, let's give it a try.")
    # print("\nAre you ready to play?")
    # time.sleep(.5)
    # print("Please type below.")
    # time.sleep(.5)
    # answer = ""
    # while answer.casefold() == "":
    #     answer = input("Please answer (yes/no): ")
    #     if answer.casefold() == "yes":
    #         delay_print("Great, we're playing a game, now.")
    #     elif answer.casefold() == "no":
    #         print("Well, you are no fun.")
    #         delay_print(" You\n will\n just\n have\n to\n come\n again\n later.")
    #         exit()
    #     elif answer.casefold() != "yes" or "no":
    #         print("please try again, friend.")
    # delay_print("Awesome, we have done some user input, and gotten out of a loop.")
    # delay_print("\nYou may notta known it, but you were almost in a loop that could go on and on and")
    # time.sleep(1)
    # delay_print("\n............ on.")
    # delay_print("But enufffff about that. Let's go ahead and build your character.")
    # time.sleep(.5)
    # print("Are you ready to skip to the 'Character Creation function?'")
    # answer_2 = ""
    # while answer_2 == "":
    #     print("Just let me know below: ")
    #     answer_2 = input("Please answer (yes/no): ")
    #     if answer_2.casefold() == "yes":
    #         print("Let's go!!!!!")
    #         char_create()
    #     elif answer_2.casefold() == "no":
    #         print("The only other option is to quit. Bye. Bye.")
    #         time.sleep(1.5)
    #         exit()
    #     elif answer_2.casefold() != "yes" or "no":
    #         print("Please, try again. You can type 'yes' or 'no'.")
    #         print("This game is NOT case-sensitive. :)")
    #         time.sleep(1.5)
    char_create()

def char_create():
    # delay_print("_"*30)
    # delay_print("\n" + "_"*25)
    # delay_print("\n" + "_"*20)
    # delay_print("\n" + "_"*15)
    # delay_print("\nWELCOME TO CHARACTER CREATION!!!")
    # delay_print("\n" + "_"*15)
    # delay_print("\n" + "_"*20)
    # delay_print("\n" + "_"*25)
    # delay_print("\n" + "_"*30)
    # time.sleep(2)
    # delay_print("\nI've told you so much, but I forgot my manners.")
    # delay_print("\nPlease tell me your name.")
    # print("\n"*2 + "Type your character's name below.")
    a = Player("", "")
    a.name = ""
    while a.name == "":
        a.name = input("Please type your name here: ")
        print("Okay, you said your name is " + a.name.capitalize() + " , is that right?")
        time.sleep(1)
        answer = ""
        while answer == "":
            answer = input("Please answer (yes/no): ")
            if answer.casefold() == "yes":
                print("Okay, " + a.name.capitalize() + " nice to meet yuh.")
            elif answer.casefold() == "no":
                print("Okay, let's try again.")
                a.name = input("Please type your name here: ")
            else:
                answer = ""
    time.sleep(.5)
    print("So, " + a.name.capitalize() + " this world has 4 races.")

    a_1 = ""
    while a_1 == "":
        print("Do you already know about these races?")
        a_1 = input("Yes or no?: ")
        if a_1.casefold() == "yes":
            print("Then we will continue on.")
        elif a_1.casefold() == "no":
            print("Would you like me to tell you about them then?")
            a_2 = input("Yes or no?: ")
            if a_2.casefold() == "yes":
                print("4 races... yada yada yada yada")
            elif a_2.casefold() == "no":
                print("Let's move on, then.")
            else:
                print("\n")
                print("It looks like you gave an invalid input.")
                print("Let's try again.")
                print("\n")
                a_1 = ""
    delay_print("You can be a Dragon, Elf, Orc, or Human.")
    delay_print("Below, please type your choice with CORRECT spelling.")
    delay_print("Capitalization does NOT matter.")
    a.race = ""
    while a.race == "":
        a.race = input("Please type your character's (one) race.: ")
    print(str(a.name.capitalize() + " " + a.race))
    test()

def test():
    print(a.name.capitalize() + " " + a.race.capitalize())
    a.fight()

game()
