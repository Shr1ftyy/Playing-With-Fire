#!C:/Users/Syeam/AppData/Local/Programs/Python/Python37/python.exe
print("Importing Dependencies...")
import math 
import random 
import time
import os 
import sys

print("\n\n________DEPENDENCIES SUCCESSFULLY LOADED________")
time.sleep(1)

# Clears the screen
try:
    os.system('cls')
except:
    os.system('clear') 

GAME_LOGO = """


   ▄███████▄  ▄█          ▄████████ ▄██   ▄    ▄█  ███▄▄▄▄      ▄██████▄        ▄█     █▄   ▄█      ███        ▄█    █▄            ▄████████  ▄█     ▄████████    ▄████████
  ███    ███ ███         ███    ███ ███   ██▄ ███  ███▀▀▀██▄   ███    ███      ███     ███ ███  ▀█████████▄   ███    ███          ███    ███ ███    ███    ███   ███    ███
  ███    ███ ███         ███    ███ ███▄▄▄███ ███▌ ███   ███   ███    █▀       ███     ███ ███▌    ▀███▀▀██   ███    ███          ███    █▀  ███▌   ███    ███   ███    █▀
  ███    ███ ███         ███    ███ ▀▀▀▀▀▀███ ███▌ ███   ███  ▄███             ███     ███ ███▌     ███   ▀  ▄███▄▄▄▄███▄▄       ▄███▄▄▄     ███▌  ▄███▄▄▄▄██▀  ▄███▄▄▄
▀█████████▀  ███       ▀███████████ ▄██   ███ ███▌ ███   ███ ▀▀███ ████▄       ███     ███ ███▌     ███     ▀▀███▀▀▀▀███▀       ▀▀███▀▀▀     ███▌ ▀▀███▀▀▀▀▀   ▀▀███▀▀▀
  ███        ███         ███    ███ ███   ███ ███  ███   ███   ███    ███      ███     ███ ███      ███       ███    ███          ███        ███  ▀███████████   ███    █▄
  ███        ███▌    ▄   ███    ███ ███   ███ ███  ███   ███   ███    ███      ███ ▄█▄ ███ ███      ███       ███    ███          ███        ███    ███    ███   ███    ███
 ▄████▀      █████▄▄██   ███    █▀   ▀█████▀  █▀    ▀█   █▀    ████████▀        ▀███▀███▀  █▀      ▄████▀     ███    █▀           ███        █▀     ███    ███   ██████████
             ▀                                                                                                                                      ███    ███


"""

game_over = """


   ▄██████▄     ▄████████   ▄▄▄▄███▄▄▄▄      ▄████████       ▄██████▄   ▄█    █▄     ▄████████    ▄████████
  ███    ███   ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███      ███    ███ ███    ███   ███    ███   ███    ███
  ███    █▀    ███    ███ ███   ███   ███   ███    █▀       ███    ███ ███    ███   ███    █▀    ███    ███
 ▄███          ███    ███ ███   ███   ███  ▄███▄▄▄          ███    ███ ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀
▀▀███ ████▄  ▀███████████ ███   ███   ███ ▀▀███▀▀▀          ███    ███ ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀
  ███    ███   ███    ███ ███   ███   ███   ███    █▄       ███    ███ ███    ███   ███    █▄  ▀███████████
  ███    ███   ███    ███ ███   ███   ███   ███    ███      ███    ███ ███    ███   ███    ███   ███    ███
  ████████▀    ███    █▀   ▀█   ███   █▀    ██████████       ▀██████▀   ▀██████▀    ██████████   ███    ███
                                                                                                 ███    ███


"""


menu_gui = f"""
        ________________________________________

                Welcome to:
                {GAME_LOGO}

                >>>  (1) Start A New Game       <<<
                >>>  (2) Load Game(coming soon!)<<<
                >>>  (3) How to Play            <<<
                >>>  (4) Quit                   <<<

        ________________________________________
         """

# CONSTANTS
AT_MENU = True
actionCounter = 0
run = True
intro = True

promptText = "\nWhat would you like to do?:\n> "

# Inventory
inventory = []
# Essential items needed for higher scores
items = ["phone, flashlight, backpack, carkey"]
score = 0
time_left = 50 # NEED TO CHANGE THIS
directions = ["go north", "go east", "go south", "go west"]
actions = ["take", "use"]

"""
World list layout (by index):
    0 - Room name
    1 - Connections to rooms by directions
    2 - Message when you enter the room - will print along with objects if there are any in the room
    3 - Objects in the room
    4 - Interactive objects in the room
    5 - Items inside those interactive objects (based upon index of interactive object inside the room) 
"""

world = [["bedroom", [["east","hallway_one"],["west","dank"]], "You are in your bedroom, there is smoke coming out of your window, To your east is a door.",["phone"], ["drawer"],[[]]],
        ["hallway_one",[["east","office"],["west","bedroom"],["north","bathroom"],["south","hallway_two"]],"You are now in your hallway"], 
        ["hallway_two",[["south","living_room"],["east", "kitchen"],["west","patio"]],"You are now in the second section of your hallway"],
        ["patio",[["east","hallway_two"]],"You are now in your patio, you see smoke and fire eating away at your fence"],
        ["kitchen",[["west","hallway_two"]],"You are now in your kitchen"],
        ["living_room",[["north","hallway_two"]],"You arrive in your living room. It is dark"],
        ]

while run: 
    if AT_MENU:
        print(menu_gui) 
        command = input(promptText)
        if command == '1':
            AT_MENU = False
            current_room = world[0]
            print("Starting Game...")
        elif command == '2':
            print("Loading feature coming soon!")
        elif command == '3':
            try:
                os.system('cls')
            except:
                os.system('clear')
            print(""" How To Play:
            Commands:
                Movement:
                'go north' 
                'go west' 
                'go east'
                'go south' 

                Interaction:
                'take {item name}'
                'open {interactive item}'
                'use {item} on {interactive item}'
                'inv' - lists items in your inventory
                   """ )
            done = input("[PRESS ANY KEY TO CLOSE]\n>")
            if len(done) >= 0:
                try:
                    os.system('cls')
                except:
                    os.system('clear')
        elif command == '4':
            exit()
        else:
            print("Please input a valid option")
            command = input(promptText).lower.strip()

    elif AT_MENU == False:
# <<<<<<<<<GAME LOOP STARTS HERE>>>>>>>>>>>
        print(f"STEPS REMAINING: {time_left}")
        if intro:
            items = ""
            time.sleep(1)
            print("""You wake up in your bedroom, it is very dark and there is smoke all around you. As you lazily 
                You continously cough as you attempt to get out of bed. You feel weak. As you vision begins to set
                in you see that the source of the smoke is coming from outside and seeping in through your window  
                To your east is a door, and your phone lies on a table next to your bed...""")	
            try:
                if len(current_room[3]) or len(current_room[4]) > 0:
                    for item in current_room[3]:
                        items += (f"{item}, ")
                    for item in current_room[4]:
                        items += (f"{item}, ")

                    print(f"You see a {items}")
            except:
                pass

        else: 
            print(current_room[2])
            items = ""
            try:
                if len(current_room[3]) or len(current_room[4]) > 0:
                    for item in current_room[3]:
                        items += (f"{item}, ")
                    for item in current_room[4]:
                        items += (f"{item}, ")

                    print(f"You see a {items}")
            except:
                pass

        command = input(promptText).lower().strip() # Commands are not caps sensitive, thus, they are lowercased once input is received
        if command == "exit" or command == "quit":
            print("Exiting game..")
            sys.exit()

        # Checks if command is valid
        if command in directions: 
            found_room = False
            for connections in current_room[1]:
                if command.split(" ")[1] == connections[0]:
                    for room in world:
                        if room[0] == connections[1]:
                            current_room = world[world.index(room)]
                            intro = False
                            time_left -= 1
                            found_room = True

            if not found_room:
                print("You cannot go that way")

        elif command.split(" ")[0] in actions:
            if command.split(" ")[0] in actions[0]:
                if command.split(" ")[len(command.split(" "))-1] in current_room[len(current_room)-1]:
                    inventory.append(command.split(" ")[len(command.split(" "))-1])
                    current_room[3].remove(command.split(" ")[len(command.split(" "))-1])
                    intro = False
                    time_left -= 1
                else:
                    print("You cannot pick that item up")

        elif command == "inv":
            if len(inventory) > 0:
                print(f"Your inventory:\n{inventory}")
            else:
                print("Your inventory is empty") 

        else:
            print("Please input a valid command")


        if time_left <= 0:
            print(game_over)
            print(score)
            score += time

            for item in inventory:
                if item in items:
                    score += 1

            print(f"SCORE: {score}")

