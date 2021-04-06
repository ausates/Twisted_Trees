class Player:
    def __init__(self, name, race, hp, attack, defense):
        self.name = name
        self.race = race
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def char_create(self):
        self.name = input("insert name here: ")
        self.race = input("insert race here: ")
        if self.race == "dragon":
            self.hp = 100
            self.attack = 50
            self.defense = 50
        elif self.race == "orc":
            self.hp = 100
            self.attack = 50
            self.defense = 50

    def show(self):
        print(self.name.capitalize(), self.race.capitalize(), "hp = ", self.hp,
              " attack = ", self.attack, " defense = ", self.defense)

    def lvl_up(self):
        print("Yay! I leveled up! (or... you leveled up?) (we?) anyway...")
        print("Your stats will now increase.")
        self.hp = self.hp + 10
        self.attack = self.attack + 10
        self.defense = self.defense + 10

class NPC:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def show(self):
        print(self.name.capitalize(), "hp = ", self.hp,
              " attack = ", self.attack, " defense = ", self.defense)


a = Player("","","","","")

a.char_create()

a.show()

class Level:
    pass

class One(Level):
    npc = NPC("Bob", 10, 10, 10)
    npc.show()
    a.lvl_up()
    a.show()

class Two(Level):
    a.lvl_up()
    a.lvl_up()
    a.show()