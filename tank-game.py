from random import *   # Importing the random module

x = []
z = 0

for d1 in range(8):
    x.append([])
    for d2 in range(8):
        x[d1].append("-")

for d1 in range(8):
    for d2 in range(8):
        if z < 10:
            x[randint(0, 7)][randint(0, 7)] = "T"
            z += 1
        
for d1 in range(8):
    for d2 in range(8):
        print("-", end=" ")
    print()

coordinatex = int(input("Enter the x coordinate: "))
coordinatey = int(input("Enter the y coordinate: "))

def function1(coordinatex, coordinatey):
    if coordinatex < 0 or coordinatex > 7 or coordinatey < 0 or coordinatey > 7 or coordinatex == "" or coordinatey == "":
        print("Please enter a valid coordinate!")
        return False
    
    elif x[coordinatex] and x[coordinatey] != "T":
        print("Sorry, there is no tank at", coordinatex, coordinatey, "coordinates!")
        return False
    
    elif x[coordinatex] and x[coordinatey] == "T":
        p = 1
        print("Congratulations! You have found", p, "tank(s)!")
        p += 1
        return True
    
o = 0

while o < 10:
    if function1(coordinatex, coordinatey) == True:
        break
    elif function1(coordinatex, coordinatey) == False:
        print("You have", 10 - o, "tries left.")
        o += 1
        coordinatex = int(input("Enter the x coordinate: "))
        coordinatey = int(input("Enter the y coordinate: "))
    
