import tkinter as tk

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 10

    def attack(self, enemy):
        enemy.health -= self.attack_power
        print(f"{self.name} attacks {enemy.name}!")

class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, player):
        player.health -= self.attack_power
        print(f"{self.name} attacks {player.name}!")

def update_health_labels():
    player_health_label.config(text=f"Player Health: {player.health}")
    enemy_health_label.config(text=f"Enemy Health: {enemy.health}")

def attack():
    player.attack(enemy)
    enemy.attack(player)
    update_health_labels()
    if player.health <= 0:
        result_label.config(text=f"{enemy.name} wins!")
    elif enemy.health <= 0:
        result_label.config(text=f"{player.name} wins!")

# Create player and enemy instances
player_name = input("Enter player name: ")
player = Player(player_name)
enemy = Enemy("Enemy 1", 50, 5)

# Create GUI
root = tk.Tk()
root.title("Goofy Game")

player_health_label = tk.Label(root, text=f"Player Health: {player.health}")
player_health_label.pack()

enemy_health_label = tk.Label(root, text=f"Enemy Health: {enemy.health}")
enemy_health_label.pack()

attack_button = tk.Button(root, text="Attack", command=attack)
attack_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()