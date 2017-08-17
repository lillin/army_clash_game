class Unit:
    """Generic unit class"""

    def __init__(self, hp=2, damage=1):
        self._hp = hp
        self._damage = damage
        self._type = 'Unit'

    def __repr__(self):
        return repr(self._type)

    def is_alive(self):
        return self._hp > 0

    def clash(self, unit):
        self.clash_back(unit)
        unit.clash_back(self)

    def clash_back(self, unit):
        """abstract"""


class Warrior(Unit):
    """Child class of Unit class
    unit Warrior
    """

    def __init__(self):
        super().__init__()
        self._type = 'Warrior'

    def clash_back(self, unit):
        if unit._type == 'Archer':
            # double damage
            unit._hp -= self._damage * 2
        else:
            unit._hp -= self._damage

    def print_info(self):
        # print info about Warrior
        print('Has 2 health point, ')


class Archer(Unit):
    """Child class of Unit class
    unit Archer
    """

    def __init__(self):
        super().__init__()
        self._type = 'Archer'

    def clash_back(self, unit):
        if unit._type == 'Mage':
            # double damage
            unit._hp -= self._damage * 2
        else:
            unit._hp -= self._damage


class Mage(Unit):
    """Child class of Unit class
    unit Mage
    """

    def __init__(self):
        super().__init__()
        self._type = 'Mage'

    def clash_back(self, unit):
        if unit._type == 'Warrior':
            # double damage
            unit._hp -= self._damage * 2
        else:
            unit._hp -= self._damage


def main():
    unit_one = Warrior()
    unit_two = Archer()
    unit_three = Mage()
    unit_one.clash(unit_two)
    unit_three.clash(unit_one)
    unit_two.clash(unit_one)
    print(unit_one._hp)
    print(unit_two._hp)
    print(unit_three._hp)


if __name__ == '__main__':
    main()
