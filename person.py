import random


class Person:
    def __init__(self, name, hp, coins, attack, defence, powers, tools):
        super().__init__()
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxcoins = coins
        self.coins = coins
        self.attacklow = attack-10
        self.attackhigh = attack+10
        self.defence = defence
        self.powers = powers
        self.tools = tools
        self.actions = ['Attack', 'Powers', 'Tools']

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_coins(self):
        return self.coins

    def get_max_coins(self):
        return self.maxcoins

    def reduce_coins(self, cost):
        self.coins -= cost

    def generate_damage(self):
        return random.randrange(self.attacklow, self.attackhigh)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def take_heal(self, heal):
        self.hp += heal
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        return self.hp

    def choose_action(self):
        i = 1
        print('\n\t'+self.name)
        print('\t Actions:')
        for action in self.actions:
            print('\t\t'+str(i)+'.', action)
            i += 1

    def choose_power(self):
        i = 1
        print('\n\t'+self.name)
        print('\t Powers:')
        for power in self.powers:
            print('\t\t'+str(i)+'.', power.name, '\tCosts:', power.cost)
            i += 1

    def choose_tools(self):
        i = 1
        print('\n\t'+self.name)
        print('\t Tools:')
        for tool in self.tools:
            print('\t\t'+str(i)+'.', tool['tool'].name,
                  '(', tool['qty'], 'x)', '\tDesc:', tool['tool'].desc)
            i += 1

    # Gives stats of avenger i.e, all things like coins and hp
    def get_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 4

        coins_bar = ""
        coins_ticks = (self.coins / self.maxcoins) * 100 / 10

        while bar_ticks > 0:
            # hp_bar += "█"
            hp_bar += "#"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while coins_ticks > 0:
            # coins_bar += "█"
            coins_bar += "#"
            coins_ticks -= 1

        while len(coins_bar) < 10:
            coins_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        coins_string = str(self.coins) + "/" + str(self.maxcoins)
        current_coins = ""

        if len(coins_string) < 7:
            decreased = 7 - len(coins_string)
            while decreased > 0:
                current_coins += " "
                decreased -= 1

            current_coins += coins_string

        else:
            current_coins = coins_string

        print("                       _________________________              __________ ")
        print(self.name + "    " + current_hp + " |" + hp_bar +
              "|    " + current_coins + " |" + coins_bar + "|")

    # Gives a stats of enemy i.e, only hp
    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 2

        while bar_ticks > 0:
            # hp_bar += "█"
            hp_bar += "#"
            bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 11:
            decreased = 11 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        print("                       __________________________________________________ ")
        print(self.name + "  " +
              current_hp + " |" + hp_bar + "|")
