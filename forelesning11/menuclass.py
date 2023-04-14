#Menu Class

"""
1.) Open an account
2.) Help
3.) Exit

"""

class Menu:
    def __init__(self):
        pass

    def add_options(self):
        pass

    def get_input(self):
        pass

mainMenu = Menu()

mainMenu.add_options("Open an account")
mainMenu.add_options("Help")
mainMenu.add_options("EXit")

choice = mainMenu.get_input()
print("Your choice is: ", choice)


