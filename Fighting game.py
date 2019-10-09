import random
from inspect import stack


class Fighter:
    def __init__(self, name, health, defense, strength):
        self.name = name
        self.health = health
        self.defense = defense
        self.strength = strength

    def punch(self, who):
# Check if the attacker strength is smaller then the opponent defense
        if(self.strength - who.defense < 0):
            print("This attack has no effect. Enemy defense was too hight")

        else:
            who.health -= self.strength - who.defense

# Check name of function that call this method to print if it's punch or special attack
            if (stack()[1].function == "special" ):
                print(f"{self.name} used special attack on {who.name} "
                      f"and take him {self.strength - who.defense} points of health!")

            else:
                print(f"{self.name} punch {who.name} and take him {self.strength - who.defense} points of health!")

    def kick(self, who):
# Check if the attacker strength is smaller then the opponent defense
        if (self.strength * 1.5 < who.defense * 1.1):
            print("This attack has no effect. Enemy defense was too hight")

        else:
            who.health -= (self.strength * 1.5) - (who.defense * 1.1)
            print(f"{self.name} kick {who.name} and take him "
                  f"{(self.strength * 1.5) - (who.defense * 1.1)} points of health!")

    def __str__(self):
        return (f"\nStats of {self.name}: \n"
                f"health = {self.health}\n"
                f"defense = {self.defense}\n"
                f"strength = {self.strength}")


class Warrior(Fighter):

    def __init__(self):
        super().__init__("Warrior", 100, 10, 50)

    def punch(self, who):
        super().punch(who)

    def kick(self, who):
        super().kick(who)

    def special(self, who):

        self.strength += ((100 - self.health) * 0.25)
        self.health -= 10
        print(f"{self.name} used special ability")

    def can_special(self):
        return self.health <= 10


class Knight(Fighter):

    def __init__(self):
        super().__init__("Knight", 100, 20, 40)

    def punch(self, who):
        super().punch(who)

    def kick(self, who):
        super().kick(who)

    def special(self, who):

        self.defense *= 1.3
        self.health -= 10
        print(f"{self.name} used special ability")

    def can_special(self):
        return self.health <= 10


class Magician(Fighter):

    def __init__(self):
        super().__init__("Magician", 100, 10, 30)

    def punch(self, who):
        super().punch(who)

    def kick(self, who):
        super().kick(who)

    def special(self, who):

        self.strength += 30
        super().punch(who)
        self.strength -= 30
        self.health -= 20

    def can_special(self):
        return self.health < 20


def game():
    while (True):
        print("Fighting game")
        dec = int(input("Fighters:\n1. Warrior\n- health: 100\n- defense: 10\n- strenght: 50\n"
                                 "Special ability = Rare(The less health you have, the more strenght you'll get.)\n"
                                 "Special ability is permanently and take 10 points of health\n"
                                 "\n2. Knight\n- health: 100\n- defense: 15\n- strenght: 40\n"
                                 "Special ability = Focus on shield(Increase your defense by 30%.)\n"
                                 "Special ability is permanently and take 10 points of health\n"
                                 "\n3. Magician\n- health: 100\n- defense: 10\n- strenght: 30\n"
                                 "Special ability = Crucio(Magic attack with 200% of your strength.)\n"
                                 "Special ability take 20 points of health\n"
                                 "\nYour choice (num): "))

# Assign Fighter to user
        if (dec == 1):
            user = Warrior()

        elif (dec == 2):
            user = Knight()

        elif (dec == 3):
            user = Magician()

        else:
            print("Put correct number!")
            continue

# Assign Fighter to computer
        dec2 = int(input("Your enemy (num): "))

        if (dec2 == 1):
            computer = Warrior()

        elif (dec2 == 2):
            computer = Knight()

        elif (dec2 == 3):
            computer = Magician()

        else:
            print("Put correct number!")
            continue

        action(user, computer)
        break
def action(user, computer):

# Assign turn to current player
    turn = user
    not_turn = computer

    while (True):

# Show statistics
        print(turn)

# Select action and then run correct method
        if (turn == computer):
            dec = random.choice("PKS")
        else:
            dec = input(f"What you do {turn.name}? P - Punch, K - Kick, S - Special: ").upper()

        if (dec == "P"):
            turn.punch(not_turn)

        elif (dec == "K"):
            turn.kick(not_turn)

        elif (dec == "S"):

# Check if health level allow to use this action
            if (turn.can_special() == True):
                print("Your health not allow for this action, try something different")
                continue

            else:
                turn.special(not_turn)

        else:
            print("Choose correct action")

# Check if enemy is alive
        if (not_turn.health <= 0):

# Only Magician can use special action when his health is the same what his special action cost
            if (turn.name == "Magician" and turn.health == 0):
                print("Brave! You sacrificed yourself to win this battle.")

            print(f"The winner is {turn.name}!")
            break

# Change turn
        if (turn == user):
            turn = computer
            not_turn = user

        else:
            turn = user
            not_turn = computer

# run a game
try:
    game()
except ValueError:
    print("Name of error: ValueError")
    game()
except:
    print("Unexpected error")
