class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 10

    def attack(self, enemy):
        enemy.health -= self.attack_power
        print(f"{self.name} attacks {enem4y.name}!")

class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, player):
        player.health -= self.attack_power
        print(f"{self.name} attacks {player.name}!")

# Create player and enemy instances
player_name = input("Enter player name: ")
player = Player(player_name)
enemy = Enemy("Enemy 1", 50, 5)

# Game loop
while player.health > 0 and enemy.health > 0:
    action = input("Enter 'a' to attack or 'q' to quit: ")
    if action == 'a':
        player.attack(enemy)
        enemy.attack(player)
    elif action == 'q':
        print("Game over.")
        break
    else:
        print("Invalid input. Try again.")

# Determine the winner
if player.health > 0:
    print(f"{player.name} wins!")
else:
    print(f"{enemy.name} wins!")