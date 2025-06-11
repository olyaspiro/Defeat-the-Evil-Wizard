import random

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health
        self.blocking = False
        self.evading = False

    def attack(self, opponent):
        # Prevents attack range errors if attack_power is low
        low = max(0, self.attack_power - 5)
        damage = random.randint(low, self.attack_power + 5)

        if opponent.evading:
            print(f"{opponent.name} evaded the attack!")
            opponent.evading = False
        elif opponent.blocking:
            print(f"{opponent.name} blocked the attack!")
            opponent.blocking = False
        else:
            opponent.health -= damage
            opponent.health = max(0, opponent.health)  # Ensure health doesn't go negative
            print(f"{self.name} attacks {opponent.name} for {damage} damage!")
            if opponent.health <= 0:
                print(f"{opponent.name} has been defeated!")

    def heal(self):
        heal_amount = random.randint(10, 20)
        old_health = self.health
        self.health = min(self.max_health, self.health + heal_amount)
        actual_healed = self.health - old_health
        print(f"{self.name} heals for {actual_healed}. Current health: {self.health}")

    def display_stats(self):
        print(f"{self.name} - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, 140, 25)

    def special_ability(self, opponent):
        damage = self.attack_power + 10
        opponent.health -= damage
        opponent.health = max(0, opponent.health)
        print(f"{self.name} uses Power Strike for {damage} damage!")

    def heal(self):
        self.blocking = True
        print(f"{self.name} prepares to block the next attack!")


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, 100, 35)

    def special_ability(self, opponent):
        damage = self.attack_power + 15
        opponent.health -= damage
        opponent.health = max(0, opponent.health)
        print(f"{self.name} casts Fireball for {damage} damage!")

    def heal(self):
        old_health = self.health
        self.health = min(self.max_health, self.health + 20)
        actual_healed = self.health - old_health
        print(f"{self.name} uses Healing Light and restores {actual_healed} health! Current health: {self.health}")


class Archer(Character):
    def __init__(self, name):
        super().__init__(name, 90, 20)

    def special_ability(self, opponent):
        damage = self.attack_power * 2
        opponent.health -= damage
        opponent.health = max(0, opponent.health)
        print(f"{self.name} uses Quick Shot for {damage} total damage!")

    def heal(self):
        self.evading = True
        print(f"{self.name} prepares to evade the next attack!")


class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, 120, 22)

    def special_ability(self, opponent):
        damage = self.attack_power + 12
        opponent.health -= damage
        opponent.health = max(0, opponent.health)
        print(f"{self.name} uses Holy Strike for {damage} damage!")

    def heal(self):
        self.blocking = True
        print(f"{self.name} activates Divine Shield to block the next attack!")


class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, 150, 15)

    def regenerate(self):
        regen = random.randint(5, 10)
        old_health = self.health
        self.health = min(self.max_health, self.health + regen)
        actual_regen = self.health - old_health
        print(f"{self.name} regenerates {actual_regen} health! Now at {self.health}")
