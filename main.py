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

# Tools for persons
hammer = Tool('Hammer', 'bad', 'Damages 900 HP of enemy.', 900)
granade = Tool('Granade', 'bad', 'Damage 1200 HP', 1200)
arrow = Tool('Arrow', 'bad', 'Damages 600 HP', 600)

mediCare = Tool('MediCare', 'good',
                'Heals 500 HP and protects you from next damage', 500)
health = Tool('Health', 'good', 'Heals 1000 HP', 1000)
superhealth = Tool('Super-Health', 'good', 'Heals max HP possible', 99999)

sheild = Tool('Sheild', 'both',
              'Nullify next Villan attack & damage them with 200 HP', 200)
sheildpro = Tool('SheildPro', 'both',
                 'Nullify next Villan attack & damage them with 1500 HP', 1500)

ironman_tools = [
    {'tool': hammer, 'qty': 10},
    {'tool': granade, 'qty': 5},
    {'tool': arrow, 'qty': 15},
    {'tool': mediCare, 'qty': 10},
    {'tool': health, 'qty': 5},
    {'tool': superhealth, 'qty': 2},
    {'tool': sheild, 'qty': 15},
    {'tool': sheildpro, 'qty': 3},
]

# Initiate Persons
ironman = Person('Iron-Man', 4000, 150, 350, 50, ironman_powers, ironman_tools)
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
            continue

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
            print('You used '+power.name+' for', pdamage, 'points of damage')

        if loki.get_hp() == 0:
            print(loki.name.replace('\t', '') + ' has Died.'+'\n\nYou Win!')
            running = False
            continue

    # for use of tools
    elif choice == 2:
        ironman.choose_tools()
        tool_choice = int(input('\tChoose Tool: ')) - 1

        if tool_choice == -1:
            continue

        tool = ironman.tools[tool_choice]['tool']
        ironman.tools[tool_choice]['qty'] -= 1

        if tool.type == 'bad':
            loki.take_damage(tool.prop)
            print('You used ' + tool.name+' for',
                  tool.prop, 'points of damage')
        elif tool.type == 'good':
            ironman.take_heal(tool.prop)
            print('You used ' + tool.name+' for',
                  tool.prop, 'points for healing yourself')
            if tool.name == 'MediCare':
                continue
        else:
            loki.take_damage(tool.prop)
            print('You used '+tool.name+' for' + tool.desc)
            if loki.get_hp() == 0:
                print(loki.name.replace('\t', '') +
                      ' has Died.'+'\n\nYou Win!')
                running = False
            continue

        if loki.get_hp() == 0:
            print(loki.name.replace('\t', '') + ' has Died.'+'\n\nYou Win!')
            running = False
            continue

    # else:
    #     running = False

    # Villan attacks back
    vdamage = loki.generate_damage()
    ironman.take_damage(vdamage)
    print(loki.name.replace('\t', '') +
          ' attacked you for', vdamage, 'points of damage.')
    if ironman.get_hp() == 0:
        print(ironman.name.replace('\t', '') +
              ' has been defeated by the Villans.\n\nYou Lose!')
        running = False
