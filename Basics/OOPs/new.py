class Character:
    def __init__(self, name, health, attack, blood):            # with constructor
        self.name = name
        self.health= health
        self.attack = attack
        self.blood = blood

    def attackEnemy(self):
        print(f'{self.name} attacks with power {self.attack}')
        print(f'Blood color is {self.blood}\n')


warrior = Character("Thor", 100, 75, 'Gold')
warrior.attackEnemy()

mage = Character("Wanda", 80, 120, 'Red')
mage.attackEnemy()


