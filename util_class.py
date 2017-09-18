import random
from army_class import *
from user_class import *


class Util:

    def generate_army(self, max_row, max_units_in_a_row):
        return [[random.choice([Warrior(), Archer(), Mage()]) for _ in range(max_units_in_a_row)] for _ in range(max_row)]

