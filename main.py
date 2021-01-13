from powers import Power
from person import Person, bcolors
from tools import Tool
import random

# Powers for persons


# Initiate Persons
ironman = Person('Iron-Man', 4000, 150, 350, 50, [], [])
# antman = Person('Ant-Man\t', 3000, 100, 250, 40, [], [])
# thor = Person('Thor\t', 3500, 120, 300, 30, [], [])

# thanos = Person('Thanos\t', 10000, 500, 500, 30, [], [])
loki = Person('Loki\t', 6000, 240, 500, 10, [], [])


# avengers = [ironman, antman, thor]
# villans = [thanos, loki]

running = True
i = 0

# print(bcolors.FAIL + bcolors.BOLD + "A Villan ATTACKS!" + bcolors.ENDC)
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

    if choice == 0:
        damage = ironman.generate_damage()
        loki.take_damage(damage)
        print('You Attacked '+loki.name.replace('\t', '') +
              ' for', damage, 'points of damage.')

        if loki.get_hp() == 0:
            print(loki.name.replace('\t', '') + ' has Died.'+'\n\nYou Win!')
            running = False
            # del loki

    elif choice == 1:
        continue

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
              ' has got defeated by the Villans.\n\nYou Lose!')
        running = False
