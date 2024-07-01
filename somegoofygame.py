import tkinter as tk
import random

# Game window setup
root = tk.Tk()
root.title("Space Invaders")
canvas = tk.Canvas(root, width=600, height=600, bg="black")
canvas.pack()

# Player spaceship
player = canvas.create_rectangle(275, 550, 325, 570, fill="blue")

# Movement controls
def move_left(event):
    x, y, x2, y2 = canvas.coords(player)
    if x > 0:
        canvas.move(player, -20, 0)

def move_right(event):
    x, y, x2, y2 = canvas.coords(player)
    if x2 < 600:
        canvas.move(player, 20, 0)

root.bind("<Left>", move_left)
root.bind("<Right>", move_right)

# Shooting mechanism
def shoot(event):
    x, y, x2, y2 = canvas.coords(player)
    bullet = canvas.create_rectangle((x+x2)/2, y, (x+x2)/2 + 5, y-20, fill="yellow")
    bullet_move(bullet)

def bullet_move(bullet):
    canvas.move(bullet, 0, -10)
    if canvas.coords(bullet)[1] > 0:
        root.after(100, lambda: bullet_move(bullet))
    else:
        canvas.delete(bullet)

root.bind("<space>", shoot)

# Aliens setup
aliens = []
def create_aliens():
    for i in range(5):
        for j in range(5):
            alien = canvas.create_rectangle(50 + j*100, 30 + i*60, 100 + j*100, 80 + i*60, fill="red")
            aliens.append(alien)

create_aliens()

# Game loop (simplified)
def game_loop():
    # Move aliens, check for collisions, etc. (to be implemented)
    root.after(100, game_loop)

game_loop()

root.mainloop()

# Next steps:
# - Implement alien movement:
#   - Move aliens to the right
#   - When they reach the edge, move them down and change direction
# - Implement collision detection:
#   - Check if the bullet hits an alien
#   - Check if an alien hits the player
# - Implement game over conditions:
#   - When an alien hits the player
#   - When all aliens are destroyed
# - Implement scoring:
#   - Keep track of the score
#   - Display the score on the screen