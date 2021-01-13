from powers import Power
from person import Person
from tools import Tool
import random

# Powers for persons
thunder = Power('Thunder', 15, 620, 'bad')
ironfist = Power('Iron-Fist', 5, 500, 'bad')
robo = Power('Iron-Robot', 35, 1000, 'bad')

charge = Power('Charge HP', 15, 500, 'good')
drink = Power('Boost HP', 5, 150, 'good')

ironman_powers = [thunder, ironfist, robo, charge, drink]
# Add loki powers as well

# Initiate Persons
ironman = Person('Iron-Man', 4000, 150, 350, 50, ironman_powers, [])
# antman = Person('Ant-Man\t', 3000, 100, 250, 40, [], [])
# thor = Person('Thor\t', 3500, 120, 300, 30, [], [])

# thanos = Person('Thanos\t', 10000, 500, 500, 30, [], [])
loki = Person('Loki\t', 6000, 240, 500, 10, [], [])


# avengers = [ironman, antman, thor]
# villans = [thanos, loki]

running = True
i = 0

print("A Villan ATTACKS!")

while running:
    print("-----------------------------------------")
    # print("\n")
    print("NAME                 HP                                     Coins")
    ironman.get_stats()
    # print("\n")
    # print("NAME                                   HP                        ")
    loki.get_enemy_stats()

    # Avenger Attacks
    ironman.choose_action()
    choice = int(input('\tChoose Action: ')) - 1

    # Use of simple attack
    if choice == 0:
        damage = ironman.generate_damage()
        loki.take_damage(damage)
        print('You Attacked '+loki.name.replace('\t', '') +
              ' for', damage, 'points of damage.')

        if loki.get_hp() == 0:
            print(loki.name.replace('\t', '') + ' has Died.'+'\n\nYou Win!')
            running = False

    # for use of powers
    elif choice == 1:
        ironman.choose_power()
        power_choice = int(input('\tChoose Power: '))-1

        if power_choice == -1:
            continue

        power = ironman.powers[power_choice]
        pdamage = power.generate_damage()

        if power.cost > ironman.get_coins():
            print('\nNot Enough Coins.\n')
            continue

        ironman.reduce_coins(power.cost)

        if power.type == 'good':
            ironman.take_heal(pdamage)
            print('You used '+power.name+' for',
                  pdamage, 'points for healing yourself')
            continue
        elif power.type == 'bad':
            loki.take_damage(pdamage)
            print('You used '+power.name+' for', pdamage, 'points for damage')

        if loki.get_hp() == 0:
            print(loki.name.replace('\t', '') + ' has Died.'+'\n\nYou Win!')
            running = False

    # for use of tools
    elif choice == 2:
        continue

    else:
        running = False

    # Villan attacks back
    vdamage = loki.generate_damage()
    ironman.take_damage(vdamage)
    print(loki.name.replace('\t', '') +
          ' attacked you for', vdamage, 'points of damage.')
    if ironman.get_hp() == 0:
        print(ironman.name.replace('\t', '') +
              ' has been defeated by the Villans.\n\nYou Lose!')
        running = False
