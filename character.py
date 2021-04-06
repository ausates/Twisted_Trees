import random
import time
import sys

def d_p(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)
    print("")

def bad_input():
    print("Bad input.")
    time.sleep(1)
    print("Please try again when prompted.")
    time.sleep(1)

class Character:
    def __init__(self, name, race, cls, attack, defense, magic, range, hp, stealth, speed, luck, inventory):
        self.name = name
        self.race = race
        self.cls = cls
        self.attack = attack
        self.defense = defense
        self.magic = magic
        self.range = range
        self.hp = hp
        self.stealth = stealth
        self.speed = speed
        self.luck = luck
        self.inv = inventory

    def get_char_info(Character):
        print(Character.name.capitalize(), Character.race.capitalize(), Character.cls.capitalize(),f"Inventory:{Character.inv}")
        time.sleep(2)

    def get_char_stats(Character):
        d_p(f"Attack = {Character.attack}, Defense = {Character.defense}, Magic = {Character.magic}, Range = {Character.range}")
        d_p(f"HP = {Character.hp}, Stealth = {Character.stealth}, Speed = {Character.speed}, Luck = {Character.luck}")
        time.sleep(2)

    def dragon_base(Character):
        Character.race = "dragon"
        Character.attack = 150
        Character.defense = 150
        Character.magic = 1
        Character.range = 1
        Character.hp = 100
        Character.stealth = 2
        Character.speed = 3

    def orc_base(Character):
        Character.race = "orc"
        Character.attack = 75
        Character.defense = 75
        Character.magic = 50
        Character.range = 00
        Character.hp = 75
        Character.stealth = 1
        Character.speed = 3

    def human_base(Character):
        Character.race = "human"
        Character.attack = 50
        Character.defense = 50
        Character.magic = 50
        Character.range = 50
        Character.hp = 60
        Character.stealth = 5
        Character.speed = 3

    def elf_base(Character):
        Character.race = "elf"
        Character.attack = 40
        Character.defense = 50
        Character.magic = 75
        Character.range = 75
        Character.hp = 50
        Character.stealth = 6
        Character.speed = 6

    def dwarf_base(Character):
        Character.race = "dwarf"
        Character.attack = 100
        Character.defense = 100
        Character.magic = 1
        Character.range = 1
        Character.hp = 100
        Character.stealth = 2
        Character.speed = 3

    def shaman(Character):
        d_p("A shaman uses magic to cripple an opponent's speed, while sapping life from them.")
        d_p("Shaman's use wards to prevent enemies from harming them, and spirit energy to attack them.")
        d_p("You have gained stats towards magic and defense, and your hp will randomly recover during fights.")
        d_p("You have lost all stats in attack and range.")

        Character.cls = "shaman"
        Character.magic += 60
        Character.defense += 30
        Character.attack = 1
        Character.range = 1

    def berserker(Character):
        d_p("A berserker cares nothing for defense and relies on reflexes to avoid damage during a relentless attack.")
        d_p("Berserkers gain speed and attack bonuses during fights at the cost of defense.")
        d_p("You have gained a massive attack bonus, and a slight speed bonus, but your defense has dropped.")
        d_p("You have lost all stats in range and magic.")

        Character.cls = "berserker"
        Character.attack += 75
        Character.defense -= 25
        Character.speed += 2
        Character.range = 1
        Character.magic = 1

    def rogue(Character):
        d_p("A rogue uses range to attack from afar and speed to attack quickly in near quarters.")
        d_p("Due to a rogue's stealth, they often are successful in one attack assassinations.")
        d_p("You have gained bonuses in stealth, speed, and range, and a slight bonus in attack.")

        Character.cls = "rogue"
        Character.attack += 10
        Character.range += 30
        Character.speed += 4
        Character.stealth += 5

    def warrior(Character):
        d_p("A warrior uses speed with attack and defense skills to handle opponents head on.")
        d_p("You have gained bonuses in attack, defense, and hp, but have lost all stats in range and mage")

        Character.cls = "warrior"
        Character.attack += 40
        Character.defense += 40
        Character.hp += 10
        Character.magic = 1
        Character.range = 1
        Character.speed += 1

    def ranger(Character):
        d_p("A ranger uses ranged weapons to handle enemies from afar.")
        d_p("Often, rangers are able to get off two attacks before an enemy can attack.")
        d_p("You have gained bonuses in range at the cost of attack and magic.")

        Character.cls = "ranger"
        Character.range += 75
        Character.speed += 1
        Character.attack = 1
        Character.magic = 1

    def mage(Character):
        d_p("A mage uses energy to bend reality, especially the elements, to fight.")
        d_p("You have gained a massive magic bonus, at the cost of attack and range.")

        Character.cls = "mage"
        Character.magic += 75
        Character.speed +=1
        Character.attack = 1
        Character.range = 1
    def hunter(Character):
        d_p("So you have chosen to be a dragon.")
        d_p("You are the last of your people, and have thus raised yourself by hunting in the wild.")
        d_p("You start with massive stats, but your story will unfold with many mysteries.")
        d_p("Be on the lookout for those like you as the story unfolds.")

        Character.cls = "hunter"


    def player_creation(Character):
        ### build race attributes and class attributes
        ### Add fancy stuff around mechanics
        print("Let's build your character.")
        time.sleep(1)
        print("Please do NOT type until the text has finished displaying.")
        time.sleep(1)
        print("Typing beforehand will cause return errors, and your character will not be properly built.")
        time.sleep(1)
        Character.name = input("What is your name? ").lower()

        races = ["dragon", "orc", "elf", "dwarf", "human"]
        print("let's select your race. You can be {} or {}.".format(", ".join(races[0:-1]), races[-1]))
        Character.race = ""
        while Character.race == "":
            Character.race = input("What race would you like to be: ").lower()
            if not Character.race in races:
                bad_input()
                Character.race = ""
            getattr(Character, Character.race + "_base")()

        classes = ("mage", "ranger", "warrior", "rogue", "berserker", "shaman")
        Character.cls = ""
        while Character.cls == "":
            if Character.race == "dragon":
                Character.hunter()
            else:
                Character.cls = input("What class would you like to be: ").lower()
                if not Character.cls in classes:
                    bad_input()
                    Character.cls = ""
                getattr(Character, Character.cls)()


        luck = random.randint(1, 10)
        Character.luck = luck


    def fight(Character, NPC):
        ### To do tasks
        ### continue loop so that NPC.speed > character plays...
        ### finish the loop without -hp showing
        ### create a class based fighting style, so that robbers don't use magic... lol
        # create functions that can be called in fights based on character class

        def char_fight_attack():
            d_p("You can make an accurate attack, a strong attack, or a very aggressive attack.")
            d_p("At the prompt, type the number corresponding to your desired attack.")
            a = ""
            while a == "":
                a = input("[1] accurate, [2] strong, [3] very aggressive: ")
                if a == "1":
                    attack = (Character.attack * random.randint(1, 2))
                    b = 0
                elif a == "2":
                    attack = (Character.attack * random.randint(1, 3))
                    b = 1
                elif a == "3":
                    attack = (Character.attack * random.randint(0, 6))
                    b = 2
                else:
                    bad_input()
            defense = (NPC.defense * random.randint(1, 4))
            total = (attack / defense) + 1
            health = (NPC.hp - total)
            NPC.hp = health // 1
            attack_tuple = ("Accurate", "Strong", "Very Aggressive")
            d_p("{} used {} attack.".format(Character.name.capitalize(), attack_tuple[b]))
            if total < NPC.hp:
                print(f"{Character.name.capitalize()} did {int(total)} damage!")
            if NPC.hp > 0:
                print(int(NPC.hp))
            elif NPC.hp < 0:
                print(f"{NPC.name} died!")
        def char_fight_mage():
            d_p("You can use an elemental spell of water, fire, or lightening.")
            d_p("At the prompt, type the number corresponding to your desired attack.")
            a = ""
            while a == "":
                a = input("[1] (water) accurate, [2] (fire) strong, [3] (lightening) very aggressive: ")
                if a == "1":
                    attack = (Character.magic * random.randint(1, 2))
                    b = 0
                elif a == "2":
                    attack = (Character.magic * random.randint(1, 3))
                    b = 1
                elif a == "3":
                    attack = (Character.magic * random.randint(0, 6))
                    b = 2
                else:
                    bad_input()
            magic_tuple = ("water", "fire", "lightening")
            print("{} used {}".format(Character.name.capitalize(), magic_tuple[b]))
            attack = (Character.magic * 2 * random.randint(1, 2))
            defense = (NPC.defense * random.randint(1, 4))
            total = (attack / defense) + 1
            health = (NPC.hp - total)
            NPC.hp = health // 1
            if NPC.hp > 0:
                print(int(NPC.hp))

        def char_fight_range():
            print("You used a ranged attack.")
            attack = (Character.range * random.randint(1, 4))
            defense = (NPC.defense * random.randint(1, 4))
            total = (attack / defense)
            health = (NPC.hp - total)
            NPC.hp = health // 1
            if NPC.hp > 0:
                (int(NPC.hp))
            elif NPC.hp <= 0:
                print(f"{NPC.name} died!")
            if ((Character.speed - NPC.speed) > NPC.speed) and NPC.hp > 0:
                d_p(f"{Character.name.capitalize()} was twice as fast as {NPC.name}, and was able to get off an extra shot")
                attack = (Character.attack * random.randint(1, 4))
                defense = (NPC.defense * random.randint(1, 4))
                total = (attack / defense) + 1
                health = (NPC.hp - total)
                NPC.hp = health // 1
                if NPC.hp > 0:
                    print(int(NPC.hp))

        def char_fight_rogue():
            if Character.speed > NPC.speed:
                first_move = True
                while first_move == True:
                    d_p("You make the first move. You can use a stealth attack, a regular attack, or a ranged attack.")
                    first_move = input("Choose your move [1] stealth [2] regular [3] ranged: ")
                    if first_move == "1":
                        if Character.stealth < NPC.speed:
                            attack = 0
                        elif Character.stealth > NPC.speed:
                            attack = (Character.attack * random.randint(2, 10))
                        b = 0
                        defense = (NPC.defense * random.randint(1, 4))
                        total = (attack / defense)
                        health = (NPC.hp - total)
                        NPC.hp = health // 1
                        first_move = False
                    elif first_move == "2":
                        attack = (Character.attack * random.randint(1, 2))
                        b = 1
                        defense = (NPC.defense * random.randint(1, 4))
                        total = (attack / defense)
                        health = (NPC.hp - total)
                        NPC.hp = health // 1
                        first_move = False
                    elif first_move == "3":
                        attack = (Character.attack * random.randint(0, 6))
                        b = 2
                        attack = (Character.range * random.randint(1, 4))
                        defense = (NPC.defense * random.randint(1, 4))
                        total = (attack / defense)
                        health = (NPC.hp - total)
                        NPC.hp = health // 1
                        first_move = False
                    else:
                        bad_input()
                        first_move = True
                    if NPC.hp > 0:
                        print(int(NPC.hp))
                npc_fight()
                while first_move == False:
                    while Character.hp > 0 and NPC.hp > 0:
                        d_p("You can use a ranged attack or a physical attack.")
                        a = ""
                        while a == "":
                            a = input("[1] ranged attack [2] physical attack: ")
                            if a == "1":
                                char_fight_range()
                            elif a == "2":
                                char_fight_attack()
                            else:
                                bad_input()
                        if NPC.hp > 0:
                            npc_fight()
                        if NPC.hp < 0:
                            first_move = ""
        def char_fight_shaman():
            d_p("You can use a spirit attack, a defensive ward, or an hp boost.")
            d_p("At the prompt, type the number corresponding to your desired attack.")
            a = ""
            while a == "":
                a = input("[1] spirit attack, [2] defensive ward, [3] hp boost: ")
                if a == "1":
                    attack = (Character.magic * random.randint(1, 3) + (Character.hp/NPC.hp))
                    print("You stole your opponent's spirit energy to attack them.")
                    attack = (Character.magic * 2 * random.randint(1, 2))
                    defense = (NPC.defense * random.randint(1, 4))
                    total = (attack / defense) + 1
                    health = (NPC.hp - total)
                    NPC.hp = health // 1
                    if NPC.hp > 0:
                        print(NPC.hp)
                elif a == "2":
                    defense = ((Character.defense * (1 + random.random())) // 1)
                    Character.defense = defense
                    print("You create a defensive ward.")
                    print(int(Character.defense))

                elif a == "3":
                    sha_health = (Character.hp + random.randint(10, 100))
                    Character.hp = sha_health
                    print(f"Your hp is now {Character.hp}.")
                else:
                    bad_input()


        def npc_fight():
            if NPC.cls == "fighter":
                print(f"{NPC.name} attacked!")
                attack = (NPC.attack * random.randint(1, 4))
                defense = (Character.defense * random.randint(1, 4))
                total = (attack / defense) + 1
                health = (Character.hp - total)
                Character.hp = health // 1
                print(int(Character.hp))
            elif NPC.cls == "mage":
                d_p(f"{NPC.name} used magic to attack!")
                attack = (NPC.magic * random.randint(1, 4))
                defense = (Character.defense * random.randint(1, 4))
                total = (attack / defense) + 1
                health = (Character.hp - total)
                Character.hp = health // 1
                print(int(Character.hp))
            elif NPC.cls == "ranger":
                d_p(f"{NPC.name} used a ranged attack!")
                attack = (NPC.attack * random.randint(1, 4))
                defense = (Character.defense * random.randint(1, 4))
                total = (attack / defense)
                health = (Character.hp - total)
                Character.hp = health // 1
                print(int(Character.hp))
                if (NPC.speed - Character.speed) > Character.speed:
                    d_p(f"{NPC.name} was twice as fast as {Character.name}, and was able to get off an extra shot")
                    attack = (NPC.attack * random.randint(1, 4))
                    defense = (Character.defense * random.randint(1, 4))
                    total = (attack / defense) - 1
                    health = (Character.hp - total)
                    Character.hp = health // 1
                    print(int(Character.hp))

        a_health = Character.hp
        a_defense = Character.defense
        while Character.hp > 0 and NPC.hp > 0:
            if Character.speed >= NPC.speed:
                print(f"{Character.name.capitalize()}'s turn.")
                time.sleep(1)
                if Character.cls in ("berserker", "warrior", "hunter"):
                    fight_sequence = True
                    while fight_sequence == True:
                        char_fight_attack()
                        if NPC.hp > 0:
                            npc_fight()
                        if NPC.hp <= 0:
                            print(f"{NPC.name} lost.")
                            fight_sequence = False
                if Character.cls == "mage":
                    fight_sequence = True
                    while fight_sequence == True:
                        char_fight_mage()
                        if NPC.hp > 0:
                            npc_fight()
                        if NPC.hp <= 0:
                            print(f"{NPC.name} lost.")
                            fight_sequence = False
                if Character.cls == "rogue":
                    char_fight_rogue()
                if Character.cls == "shaman":
                    fight_sequence = True
                    while fight_sequence == True:
                        char_fight_shaman()
                        if NPC.hp > 0:
                            npc_fight()
                        if NPC.hp <= 0:
                            print(f"{NPC.name} lost.")
                            fight_sequence = False


            elif NPC.speed > Character.speed:
                pass
        if Character.hp > 0:
            Character.hp = a_health
            Character.defense = a_defense
        if Character.hp < 0:
            print("GAME OVER")
            exit()




class NPC:
    def __init__(self, name, race, cls, attack, defense, magic, range, hp, stealth, speed, luck):
        self.name = name
        self.race = race
        self.cls = cls
        self.attack = attack
        self.defense = defense
        self.magic = magic
        self.range = range
        self.hp = hp
        self.stealth = stealth
        self.speed = speed
        self.luck = luck

    ### define robber, mage, boss, and other NPC stats
#
player = Character("A", "human", "shaman", 100, 100, 100, 100, 100, 100, 100, 100, "")
robber = NPC("Robber", "human", "fighter", 50, 10, 1, 1, 50, 1, 1, random.random())
# rogue_mage = NPC("Rogue Mage", "human", "mage", 0, 10, 15, 0, 25, 0, 110, 10)
# NPC1 = robber
# NPC2 = rogue_mage


Character.player_creation(player)
Character.get_char_stats(player)
Character.get_char_info(player)
Character.fight(player, robber)
print(player.hp)