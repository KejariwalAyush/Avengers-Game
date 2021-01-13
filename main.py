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

avenger_powers = [thunder, ironfist, robo, charge, drink]
# Add tvillan powers as well

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

avenger_tools = [
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
ironman = Person('Iron-Man', 4000, 150, 350, 50, avenger_powers, avenger_tools)
antman = Person('Ant-Man\t', 3000, 100, 250, 40, avenger_powers, avenger_tools)
thor = Person('Thor\t', 3500, 120, 300, 30, avenger_powers, avenger_tools)

thanos = Person('Thanos\t', 20000, 500, 500, 30, [], [])
loki = Person('Loki\t', 13000, 240, 500, 10, [], [])


avengers = [ironman, antman, thor]
villans = [thanos, loki]

running = True
i = 0

print("Villans ATTACKS your Place!")

while running:
    print("-----------------------------------------")
    print("\n")
    print("NAME                 HP                                     Coins")
    for avenger in avengers:
        avenger.get_stats()
    print("\n")
    print("NAME                                   HP                        ")
    for villan in villans:
        villan.get_enemy_stats()

    # Check if battle is over

    # Check if Player won
    if len(villans) == 0:
        print("You win!")
        running = False
        break

    # Check if Enemy won
    elif len(avengers) == 0:
        print("Your Villans have defeated you!")
        running = False
        break

    # else:
    #     print('Tied')
    #     running = False
    #     break

    # Avenger Attacks
    for avenger in avengers:
        if len(villans) == 0 or len(avengers) == 0:
            break
        avenger.choose_action()
        inp = input("    Choose action: ")
        if inp == 'quit':
            print('\n\nThanks for playing AVENGERS, See you Soon!\n')
            running = False
            exit(0)
        choice = int(inp) - 1

        tvillan = villans[random.randrange(0, len(villans))]

        # Use of simple attack
        if choice == 0:
            damage = avenger.generate_damage()
            tvillan.take_damage(damage)
            print('You Attacked '+tvillan.name.replace('\t', '') +
                  ' for', damage, 'points of damage.')

            if tvillan.get_hp() == 0:
                print(tvillan.name.replace('\t', '') +
                      ' has Died.'+'\n\nYou Win!')
                villans.remove(tvillan)
                continue

        # for use of powers
        elif choice == 1:
            avenger.choose_power()
            power_choice = int(input('\tChoose Power: '))-1

            if power_choice == -1:
                continue

            power = avenger.powers[power_choice]
            pdamage = power.generate_damage()

            if power.cost > avenger.get_coins():
                print('\nNot Enough Coins.\n')
                continue

            avenger.reduce_coins(power.cost)

            if power.type == 'good':
                avenger.take_heal(pdamage)
                print('You used '+power.name+' for',
                      pdamage, 'points for healing yourself')
                continue
            elif power.type == 'bad':
                tvillan.take_damage(pdamage)
                print('You used '+power.name+' for',
                      pdamage, 'points of damage')

            if tvillan.get_hp() == 0:
                print(tvillan.name.replace('\t', '') +
                      ' has Died.'+'\n\nYou Win!')
                villans.remove(tvillan)
                continue

        # for use of tools
        elif choice == 2:
            avenger.choose_tools()
            tool_choice = int(input('\tChoose Tool: ')) - 1

            if tool_choice == -1:
                continue

            tool = avenger.tools[tool_choice]['tool']
            if avenger.tools[tool_choice]['qty'] <= 0:
                continue
            avenger.tools[tool_choice]['qty'] -= 1

            if tool.type == 'bad':
                tvillan.take_damage(tool.prop)
                print('You used ' + tool.name+' for',
                      tool.prop, 'points of damage')
            elif tool.type == 'good':
                avenger.take_heal(tool.prop)
                print('You used ' + tool.name+' for',
                      tool.prop, 'points for healing yourself')
                if tool.name == 'MediCare':
                    continue
            else:
                tvillan.take_damage(tool.prop)
                print('You used '+tool.name+' for' + tool.desc)
                if tvillan.get_hp() == 0:
                    print(tvillan.name.replace('\t', '') +
                          ' has Died.'+'\n\nYou Win!')
                    villans.remove(tvillan)
                continue

            if tvillan.get_hp() == 0:
                print(tvillan.name.replace('\t', '') +
                      ' has Died.'+'\n\nYou Win!')
                villans.remove(tvillan)
                continue

    if len(avengers) == 0 or len(villans) == 0:
        continue
    # Villan attacks back
    i = 1
    while i <= 2 or len(villans) == 0:
        i += 1
        tvillan = villans[random.randrange(0, len(villans))]
        vdamage = tvillan.generate_damage()
        tavenger = avengers[random.randrange(0, len(avengers))]
        tavenger.take_damage(vdamage)
        print(tvillan.name.replace('\t', '') +
              ' attacked you for', vdamage, 'points of damage to '+tavenger.name)
        if tavenger.get_hp() == 0:
            print(tavenger.name+' has been defeated by the Villans.\n\nYou Lose!')
            avengers.remove(tavenger)
