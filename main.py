from powers import Power
from person import Person, bcolors
from tools import Tool
import random

# Initiate Persons
ironman = Person('Iron-Man', 4000, 150, 350, 50, [], [])
antman = Person('Ant-Man\t', 3000, 100, 250, 40, [], [])
thor = Person('Thor\t', 3500, 120, 300, 30, [], [])

thanos = Person('Thanos\t', 10000, 500, 500, 30, [], [])
loki = Person('Loki\t', 6000, 240, 500, 10, [], [])


avengers = [ironman, antman, thor]
villans = [thanos, loki]

running = True
i = 0

# print(bcolors.FAIL + bcolors.BOLD + "A Villan ATTACKS!" + bcolors.ENDC)
print("A Villan ATTACKS!")

while running:
    print("-----------------------------------------")

    print("\n\n")
    print("NAME                 HP                                     Coins")
    for avenger in avengers:
        avenger.get_stats()

    print("\n")
    print("NAME                                   HP                        ")

    for enemy in villans:
        enemy.get_enemy_stats()

    running = False
