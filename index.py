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

def function():
    if x[coordinatex][coordinatey] == "T":
        p = 1
        print("Congratulations! You have found", p, "treasure(s)!")
        p =+ 1
        return True
    else:
        print("Sorry, you have not found any treasure.")
        print("Try again!")
        return False

o = 0

while o < 10:
    if function() == True:
        o = o
        coordinatex = int(input("Enter the x coordinate: ")) + 1
        coordinatey = int(input("Enter the y coordinate: ")) + 1
    else:
        print("You have", 10 - o, "tries left.")
        o += 1
        coordinatex = int(input("Enter the x coordinate: "))
        coordinatey = int(input("Enter the y coordinate: "))
    