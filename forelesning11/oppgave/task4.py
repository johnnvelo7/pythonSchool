class MyLetter:
    def __init__(self, letter_from, letter_to):
        self.letter_from = letter_from
        self.letter_to = letter_to
        self.body = []

    def add_line(self, line):
        self.body.append(line)

    def get_text(self):
        letter = f"Dear {self.letter_to}: \n\n"
        for line in self.body:
            letter += line + '\n'
        letter += "\nSincerly,\n\n" + self.letter_from
        return letter

letter = MyLetter("Sabrina", "John")
letter.add_line("I like you")
letter.add_line("I miss you")
print(letter.get_text())