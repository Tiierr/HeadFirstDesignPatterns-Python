from Wizard import Wizard
from Ork import Ork

class WizardWorld(object):

    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t------ Wizard World ———'

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork()
