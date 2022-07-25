#Start of the game
#NAME: S-class Hunter
#Classes:
user_playing = True
player_items = []
Darcksmoke_is_alive = True
class Caves:
    def __init__(self, name, intro, monster, items):
        self.name = name
        self.intro = intro
        self.monster = monster
        self.items = items
        self.paths = []
        self.is_lock = False
        self.unlock = ""
    
    def __repr__(self):
        return f"You can go to {self.name}"

    def enter(self, player_items):
        if self.is_lock == False or self.unlock in player_items:
            print(self.intro)
        else:
            print(f"You need the {self.unlock}")

    def user_items(self):
        print(self.items)

    # def current_room(self):
    #     print(f"You are in {self.name}")

#This is the final battle with the Dragon "Darcksmoke"
class Final_battle:
    def __init__(self, name, health, powers, items):
        self.name = name
        self.health = health
        self.powers = powers
        self.items = items

    def __repr__(self):
        return f"{self.name}"

    def is_alive(self):
        return self.health>0

    def attack(self, dragon):
        ability_style = input(f"Enter the ability you want to use {self.powers}\n >> ")
        if ability_style == "ability3" and self.powers["ability3"] == True:
            print("Your ability has stunned the enemy ")

        elif ability_style == "ability3" and self.powers["ability3"] == False:
            print("You can't stun your enemy")

        elif ability_style == "ability5":
            print("Your next ability is going to be '0%' stronger")
        else:
            dragon.health = dragon.health - self.powers[ability_style]
            print(f"\n{self.name} attacks {dragon.name}!\n{dragon.name} health = {dragon.health}\n")

        # dragon.health = dragon.health - self.powers[ability_style]
        # print(f"\n{self.name} attacks {dragon.name}!\n{dragon.name} health = {dragon.health}\n")

# def nav():
#     Caves.enter(cave1)
#     print("Your going to cave 2")
#     Caves.cave_2("cave2")
#     user_choice = input("What do you want to do?")
#     splitting = user_choice.split(" ")
#     if user_choice == "move":
#         if splitting[1] == "cave 3":
#             Caves.cave_3("cave3")
#         elif splitting[1] == "cave 4":
#             Caves.cave_4("cave4")
#         elif splitting[1] == "cave 6":
#             Caves.cave_6("cave5")

#     elif user_choice == "look":
#         print("Collect the letter")
# nav()


intro_1 = "\nCollect items in order to defeat The Dragon \nYou can collect items from defeating monster along the way\n\nYoohin Han: I wish I could have saved my brother\nNo matter what I'm going to avenge him"
intro_2 = "\nYoohin Han: I have 3 options, move to cave3, cave4 or cave 6\nWhich one should I choose?"
intro_3 = "\nYou are in cave 3!\nYoohin Han: I'm searching for something that might have left my brother for me\n"
intro_4 = "\nYou are in cave 4!\nDefeat the monster\n"
intro_5 = "\nYou are in cave 5!\nYoohin Han:\n"
intro_6 = "\nYou are in cave 6!\nYoohin Han: What can I do?\n"
intro_7 = "\nYou are in cave 7!\nYoohin Ha: I finally found you\n"
intro_8 = "\nYou are in cave 8!\nYoohin Ha: Potion\n"

cave1 = Caves("cave1", intro_1, False, [])
cave2 = Caves("cave2", intro_2, False, [])
cave3 = Caves("cave3", intro_3, False, ["letter"])
cave4 = Caves("cave4", intro_4, False, ["key"])
cave5 = Caves("cave5", intro_5, False, ["sword"])
cave6 = Caves("cave6", intro_6, False, [])
cave7 = Caves("cave7", intro_7, True, [])
cave7.is_lock = True
cave7.unlock = "key"
cave8 = Caves("cave8", intro_8, False, ["health_potion", "unknown_potion"])

cave2.paths = [cave3, cave4, cave6]
cave3.paths = [cave2]
cave4.paths = [cave2, cave5]
cave5.paths = [cave4]
cave6.paths = [cave2, cave7, cave8]
cave8.paths = [cave6]

current_cave = cave2

#This is the start where the user enter if he wants to play
user_start = input("If your ready to start the game type 'start': \n").lower()
if user_start == "start":
    print("\n\t\tWelcome Yoohin Han! \n\tYou have sucessfully enter the Dungeon.")
    print("\tClear the dungeon in order to exit from it")
    print("\tGood luck!\n")
    cave1.enter(player_items)
    print("\nYour moving to cave 2, Type 'Help' to learn how to play")
    cave2.enter(player_items)

def player_question():
        reply = input("What do you want to do ?\n").lower()
        return reply

def nav(input):
    global current_input
    global current_cave
    global player_items
    print("\nchecking question :  " +  input)
    current_input = input

    splitting = current_input.split(" ")

    if current_input == "help":
        print("\tType 'look' to look everything in that cave\n \tType 'move' to move to another cave")
        print("\tType 'use' to use a item you have\n\tType 'take' to add an item\n\tType 'cave' to know where can you go")

    if splitting[0] == "move":
        move =  False
        for cave in current_cave.paths:
            if splitting[1] == cave.name:
                current_cave = cave 
                move = True
                cave.enter(player_items)
        if move == False:
            print("You cannot move to that cave")


    elif splitting[0] == "look":
        for item in current_cave.items:
            print("There is/are: " + item)

    elif splitting[0] == "take":
        taking_item = str(splitting[1])
        c_room = current_cave
        print(taking_item)

        if taking_item in current_cave.items:
            player_items.append(taking_item)
            print("Your current items is/are: "+ str(player_items))
        else:
            print("You can't take anything")

    elif splitting[0] == "use":
        item_use = splitting[1]
        if item_use in player_items:
            print("You can use that item!")

    elif splitting[0] == "cave":
            print(str(current_cave.paths))
                
        
    elif splitting[0] == "attack" and current_cave.monster == True:

        yoohin = Final_battle("Yoohin Han", 1000, {"ability1": 200, "ability2": 150, "ability3": True, "ability4": 180, "ability5": True,"ultimate": 400}, {"potion": 0.4, "sword": 0.5, "unknown_potion": 0.2})
        darcksmoke = Final_battle("Darksmoke", 1500, {"a1": 10, "a2": 150, "a3": True, "a4": 180, "a5": True,"ult": 500}, {"pot": 0.2, "Flames of hell": 0.5, "cool": 0.2})

        while yoohin.is_alive() and darcksmoke.is_alive():
            yoohin.attack(darcksmoke)
            darcksmoke.attack(yoohin)

        if darcksmoke.health < 0:
            print("The Tier-1 Dragon Darksmoke has been defeated\n You won")
            print("You have acquire GOD MODE")
            print("\n\t\tThank you for playing the game!")
            Darcksmoke_is_alive = False
        else:
            print("You have been defeated")
            Darcksmoke_is_alive = False





# game_rules = input("type 'help' to learn more about the game:\n").lower()
# if game_rules == "help":
#     print("\tType 'look' to look everything in that cave\n \tType 'move' to move to another cave")
#     print("\tType 'use' to use a item you have\n\tType 'cave' to know in which cave are you at\n")



while user_playing and Darcksmoke_is_alive == True:
    nav(player_question())



# yoohin = Final_battle("Yoohin Han", 1000, {"ability1": 200, "ability2": 150, "ability3": True, "ability4": 180, "ability5": True,"ultimate": 400}, {"potion": 0.4, "sword": 0.5, "unknown_potion": 0.2})
# darcksmoke = Final_battle("Darksmoke", 1500, {"a1": 10, "a2": 150, "a3": True, "a4": 180, "a5": True,"ult": 500}, {"pot": 0.2, "Flames of hell": 0.5, "cool": 0.2})

# while yoohin.is_alive() and darcksmoke.is_alive():
#     yoohin.attack(darcksmoke)
#     darcksmoke.attack(yoohin)

# if darcksmoke.health < 0:
#     print("The Tier-1 Dragon Darksmoke has been defeated\n You won")
#     print("You have acquire GOD MODE")
# else:
#     print("You have been defeated")







# def use_items(self):
#     if user_inpuit in objects:
#         #wherever the user wants to use
#     else:
#         #he cant use it
# def go(slef, room):
#     if room in self.path:
#         current_room = room
#         room.enter_room(room)

# def  enter_room(self):
#     print(room.description)

