class Tally:
    def __init__(self):
        self.value = 0

    def click(self):
        self.value += 1
        # increment by 1
    def undo(self):
        if self.value > 0:
            self.value -= 1
            if self.value == 0:
                print("You cant go lower")
    def reset(self):
        self.value = 0

    def get_value(self):
        return self.value

#  t = the object of Tally class
t = Tally()

t.click()
t.click()
t.click()


print(t.get_value())
