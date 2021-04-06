class Player:
    def __init__(self, name, race, hp, attack, defense):
        self.name = name
        self.race = race
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def get_name(self):
        print(self.name)

    def show(self):
        print(self.name, " ", self.race.capitalize(), " ", self.hp, " ", self.attack, " ", self.defense)


a = Player("Austin", "dragon", 100, 100, 100)

a.get_name()
a.show()

def testinstancing():
    a.show()

testinstancing()

a.name = input("Please type name here")

def testinstancing_2():
    a.show()

testinstancing_2()