import random
import math

# Warrior & battle class

class Warrior:

    def __init__(self, name='Warrior', health=0, attkMax=0, blockMax=0):
        self.name = name
        self.health = health
        self.attkMax = attkMax
        self.blockMax = blockMax

    def attack(self):
        attkAmt = self.attkMax * (random.random()+ .5)
        return attkAmt

    def block(self):
        blockAmt = self.blockMax * (random.random() + .5)
        return blockAmt

class Battle:

    def startFight(self, warrior1, warrior2):

        while True:
            if self.getAttackResult(warrior1, warrior2) == 'Game Over':
                print('Game Over')
                break

            if self.getAttackResult(warrior2, warrior1) == 'Game Over':
                print('Game Over')
                break

    @staticmethod
    def getAttackResult(warriorA, warriorB):

        warriorAAttkAmt = warriorA.attack()

        warriorBBlockAmt = warriorB.block()


        damage2WarriorB = math.ceil(warriorAAttkAmt - warriorBBlockAmt)

        warriorB.health -= damage2WarriorB

        print("{} attacks {} and deals {} damage".format(warriorA.name,
                                                         warriorB.name, damage2WarriorB))

        print("{} is down to {} health".format(warriorB.name,
                                               warriorB.health))

        if warriorB.health <= 0:
            print("{} has Died and {} is Victorious".format(warriorB.name,
                                                            warriorA.name))

            return "Game Over"
        else:
            return "Fight Again"




def main():

    maximus = Warrior('Maximus', 50, 20, 10)
    galaxon = Warrior('Galaxon', 50, 20, 10)

    battle = Battle()

    battle.startFight(maximus, galaxon)

if __name__ == '__main__':
    main()


# Warriors will have names, health, attacks, and block maximums

# They will have the capabilities to attack and block random amounts

# Attack random() 0.0 to 1.0 * maxAttack + .5

# Block will use random()

# Battle Class capability if loopimg until 1 warrior dies

# Warriors will each get a turn to attack each other

# Function gets 2 warriors

# 1 warrior attacks the other

# Attacks and blocks be integers

