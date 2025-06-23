import time

#treasure chest
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')


cross_road = input("Welcome to Treaure Hunt.\n" \
"Your mission is to find the treasure.\n" \
"You're at a cross road. Where do you wanna go?\n" \
'     Type "left" or "right"\n').lower()
#lake
if cross_road == "left":
    lake = input("You've come to a lake. \n There is an island in the middle of the lake.\n" \
                 '  Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if lake == "wait":
        print("Waiting...")
        time.sleep(2)
        print("The boat has finally arrived!\n" \
                "Boarding the boat now.")
        time.sleep(2)
        island_doors = input("You arrive at the island unharmed.\nThere is a house with 3 doors.\n" \
                        "One red, one yellow, and one blue.\nWhich color do you choose?\n").lower()
        if island_doors == "red":
            print("You found the treasure! You can finally buy a new laptop, you're rich!")
        elif island_doors == "blue" or "yellow":
            print("It's a room full of fire. Game over.")
        else:
            print("invalid input")
    elif lake == "boat":
        print("Swimming to the island now.")
        time.sleep(2)
        print("Uh-oh!...")
        time.sleep(2)
        print("You drowned in the lake and choked to death. Turns out you ain't no Michael Philips huh?\n" \
            "THE END.")
    else:
        print('Invalid input. Please type either "wait" or "swim" to continue')

#mountain
elif cross_road == "right":
    mountain = input("You've come to a mountain. There is a cave at the middle of the mountain.\n" \
                 '  Type "wait" to wait for a ferry. Type "swim" to climb to the cave.').lower()
    if mountain == "wait":
        print("Waiting...")
        time.sleep(2)
        print("The ferry has finally arrived!\n" \
                "Boarding the ferry now.")
        time.sleep(2)
        cave_doors = input("You arrive at the cave unharmed. There is a house with 3 doors.\n" \
                        "One red, one yellow, and one blue. Which color do you choose?\n").lower()
        if cave_doors == "red":
            print("You found the treasure! You can finally buy a new laptop, you're rich!")
        elif cave_doors == "blue" or "yellow":
            print("It's a room full of fire. Game over.")
        else:
            print("invalid input")
    elif mountain == "climb":
        print("Climbing the mountain now.")
        time.sleep(2)
        print("Uh-oh!...")
        time.sleep(2)
        print("You slipped on a rock and died from the fall. Turns out you were pretty bad at hiking huh?\n" \
            "THE END.")
    else:
        print('Invalid input. Please type either "wait" or "climb" to continue.')

#error handling
else:
    print('Invalid input. Please type either "left" or "right" to continue')
