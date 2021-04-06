class Test:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def set_name(self):
        self.first = input("Insert FIRST name here: ")
        self.last = input("Insert LAST name here: ")

    def get_name(self):
        name = "{} {}".format(self.first.capitalize(), self.last.capitalize())
        print(name)
### The .format is so nice for inserting these strings into variables.
###


a = Test("", "")
a.set_name()
a.get_name()