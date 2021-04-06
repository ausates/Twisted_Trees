class Question_Loop:

    def __init__(self, number, min=0, max=100):
        self.number = number
        self.min = min
        self.max = max

    def get_answer(self):
        guess = input(f'Please guess a number beween {self.min} - {self.max}: ')
        if self.valid_answer(guess):
            return int(guess)
        else:
            print(f"Please try again with a valid number {self.min} - {self.max}")
            return self.get_answer()
                # this is SUPER useful!!! return the function so I don't have to build endless while loops