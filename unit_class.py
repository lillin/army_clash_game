

class Unit:
    """Generic unit class"""

    def __init__(self, hp=2, damage=1):
        self._hp = hp
        self._damage = damage
        self._type = 'Unit'
        self._status = True

    def is_alive(self, unit):
        # check unit status
        if unit._hp == 0:
            unit._status = False
            print('Your unit is dead')
        else:
            print('Your unit is alive')

    def clash(self, unit):
        unit._hp -= self._damage
        self.is_alive(unit)


class Warrior(Unit):
    """Child class of Unit class
    unit Warrior
    """

    def __init__(self):
        super().__init__()
        self._type = 'Warrior'

    def clash(self, unit):
        if unit._type == 'Archer':
            # double damage
            unit._hp -= self._damage * 2
        else:
            unit._hp -= self._damage
        self.is_alive(unit)


class Archer(Unit):
    """Child class of Unit class
    unit Archer
    """

    def __init__(self):
        super().__init__()
        self._type = 'Archer'

    def clash(self, unit):
        if unit._type == 'Mage':
            # double damage
            unit._hp -= self._damage * 2
        else:
            unit._hp -= self._damage
        self.is_alive(unit)


class Mage(Unit):
    """Child class of Unit class
    unit Mage
    """

    def __init__(self):
        super().__init__()
        self._type = 'Mage'

    def clash(self, unit):
        if unit._type == 'Warrior':
            # double damage
            unit._hp -= self._damage * 2
        else:
            unit._hp -= self._damage
        self.is_alive(unit)


def main():
    unit_one = Warrior()
    unit_two = Archer()
    unit_three = Mage()
    unit_one.clash(unit_two)
    unit_three.clash(unit_one)
    unit_two.clash(unit_one)

if __name__ == '__main__':
    main()
