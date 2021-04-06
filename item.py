from character import Character

player = Character("A", "human", "shaman", 100, 100, 100, 100, 100, 100, 100, 100, "sword")

class item(Character):

    def axe(Character):
        Character.inv += "Axe "
        Character.attack += 10

    def great_axe(Character):
        Character.inv += "Great Axe "
        Character.attack += 15
        Character.speed -= 1
        Character.stealth -= 1

    def sword(Character):
        Character.inv += "Sword "
        Character.attack += 10

    def dagger(Character):
        Character.inv += "Dagger "
        Character.attack += 5
        Character.speed += 1
        Character.stealth += 1

    def broad_sword(Character):
        Character.inv += "Broad Sword "
        Character.attack += 15
        Character.speed -= 1
        Character.stealth -= 1

    def staff(Character):
        Character.inv += "Staff "
        Character.magic += 10

    def wand(Character):
        Character.inv += "Wand "
        Character.magic += 5
        Character.speed += 1
        Character.stealth +=1

    def short_bow(Character):
        Character.inv += "Short Bow "
        Character.range += 5
        Character.speed += 1

    def long_bow(Character):
        Character.inv += "Long Bow "
        Character.range += 10

    def cross_bow(Character):
        Character.inv += "Cross Bow "
        Character.range += 15
        Character.speed -= 1

    def buckler(Character):
        Character.inv += "Buckler "
        Character.defense += 5
