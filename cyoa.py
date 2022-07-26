# #Start of the game
# #NAME: S-class Hunter
# #Classes:
user_playing = True
player_items = []
Darcksmoke_is_alive = True

# START OF THE FIGURES AND SOME ANIMATION 
def monster_vs(enemy):
    if enemy == True:
        print("        |||||||||   |||||||| |||||||||||| |||||||||||| |          | |||| ||        |              ")
        print("           ||    | |     ||  |          | |          | |          | |||| | |       |              ")
        print("              |   |   |      |          | |          | |          | |||| |  |      |              ")
        print("                |   |        |          | |          | |          | |||| |   |     |              ")
        print("                |   |        |          | |          | |||||||||||| |||| |    |    |              ")
        print("                |   |        |          | |          | |          | |||| |     |   |              ")
        print("                |   |        |          | |          | |          | |||| |      |  |              ")
        print("                |   |        |          | |          | |          | |||| |       | |              ")
        print("                |||||        |||||||||||| |||||||||||| |          | |||| |        ||              ")
        print("\n\n\n                                                                                                  ")
        print("                         \/                /    ///////////                    ")
        print("                          \/              /    |/                              ")
        print("                           \/            /     ||                              ")
        print("                            \/          /      |\                              ")
        print("                             \/        /       //////////\                     ")
        print("                              \/      /                  \|                    ")
        print("                               \/    /                   ||                    ")
        print("                                \/  /                    /|                    ")
        print("                                 \//           ///////////                     ")
        print("\n\n\n                                                                                                  ")
        print("    ||   \       |//////////  ||     //                                        ")
        print("    ||     \     |/        \| ||    //                                         ")
        print("    ||       \   ||        // ||   //                                          ")
        print("    ||        \  ||      //   ||  //                                           ")
        print("    ||         | ||   //      |||((                                            ")
        print("    ||        /  ||   |\      ||  |\                                           ")
        print("    ||       /   ||    |\     ||   |\                                          ")
        print("    ||     /     ||     |\    ||    |\                                         ")
        print("    ||   /       ||      |\   ||     |\                                        ")


        print("    /////////// ||         || |||||||||||| ||     // ||||||||||||              ")
        print("   |/           || \      / | |          | ||    //  |/                        ")
        print("   ||           ||  \    /  | |          | ||   //   |                         ")
        print("   |\           ||   \  /   | |          | ||  //    |\                        ")
        print("    \///////\   ||    \/    | |          | |||((     ||||||||||||              ")
        print("            \|  ||          | |          | ||  |\    |/                        ")
        print("            ||  ||          | |          | ||   |\   |                         ")
        print("            /|  ||          | |          | ||    |\  |\                        ")
        print("   //////////   ||          | |||||||||||| ||     |\ ||||||||||||              \n")
def welcome_user(wlcm):
    if wlcm == True:
        print("\n\n")
        print("       |\                     / |||||||||||| ||           ||||||||||||| |||||||||||| ||         || ||||||||||||    ||")
        print("        |\                   /  |/           ||           |             |          | || \      / | |/              ||")
        print("         |\                 /   |            ||           |             |          | ||  \    /  | |               ||")
        print("          |\               /    |\           ||           |             |          | ||   \  /   | |\              ||")
        print("           |\             /     |||||||||||| ||           |             |          | ||    \/    | ||||||||||||    ||")
        print("            |\     /\    /      |/           ||           |             |          | ||          | |/              ||")
        print("             |\   /  \  /       |            ||           |             |          | ||          | |               ||")
        print("              |\ /    \/        |\           ||           |             |          | ||          | |\              ||")
        print("               |\/    \/        |||||||||||| |||||||||||| ||||||||||||| |||||||||||| ||          | ||||||||||||    ◉\n\n")
def dragon_smoke(smoke):
    if smoke == True:
        print("                                            ^                  ")
        print("                 ^                           ^^)               ")
        print("                ^^>>                     ^>>>>>>^              ")
        print("              <<- >                   ^>^>^^^^^^^^^^^>         ")
        print("             ^^^^ >                  ^^^>^>^^^^^^^^^^          ")
        print("         ^>>>>>>>>>>^^>             ^>>^>^^^^^^^^^             ")
        print("         >>^^^^^>^^^^^^^^^>          >^^>>>^>^^^^^^^^^         ")
        print("     ^^^>^^^^^^^^^^>>^            >^^^^^^^>^^^^^^^^^^          ")
        print("  <<<<^^^^^^^^^^^^^              >>^^^^^^^^>^^^^^^^^^^^^>      ")
        print("    ^^^^>^^^^^^^^>>           >>>>^^^^^^^^>^^^^^^^             ")
        print("        ^^^^^^^>^^^^^^^>       >^^^>>^^^^^^^^^>^^^             ")
        print("            <^^^^^^^^^^^        >^^^^^^^^^^^^^>                ")
        print("             <<^^^^^^^^        >^^^^^^^^^^>>                   ")
        print("             ^^^^^^^^    >>>>^^>>^^>                           ")
        print("              >>>>>>>>>>>>^^^>>>>>                             ")
        print("           ^^^^^^>^>^>^>^>^>>>>>>>>>>                          ")
        print("        ^^^^^  ^>>//////////////////\>>>                       ")
        print("       ^     ^//**>>>>>>////////////...                        ")
        print("      ( ^  ///\        (|) (|)>>>>>>>>>>                        ")
        print("      \  |//> </          >>^>^^^^>>>>>^>^^>>>                 ")
        print("        \ /> </          ^^^        >>>>>>>>^^^^/                ")
        print("                        ^^                \(////               ")
        print("                        ^                   \(//               ")     
        print("                                              \(/               ")
def god_mode(activation):
    if activation == True:
        print("\n|----------- |----------| |    \             ")
        print("|            |          | |      \          ")
        print("|----------| |          | |        |       ")
        print("|          | |          | |       /        ")
        print("|__________| |----------| |     /           \n")
        print("| \       /| |----------| |    \     |--------")
        print("|   \   /  | |          | |      \   |        ")
        print("|     |    | |          | |        | |-----  ")
        print("|          | |          | |       /  |       ")
        print("|          | |----------| |     /    |--------\n")

#------------------------------------------------------------------------------------

#THIS IS WHERE I CAN CREATE CAVES AND WHAT IS INSIDE OF IT
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

#------------------------------------------------------------------------------------


#THIS IS THE FINAL BATTLE WITH THE DRAGON "DARKSMOKE"
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
        splt = ability_style.split(" ")
        if ability_style == "ability3" and self.powers["ability3"] == True:
            print("Your ability has stunned the enemy ")
            yoohin1 = ("Yoohin Han", 2200, {"frosty_sigh": 200, "shadowless_day": 250, "sandals-of-hermes": True, "blue-willows": 180, "absolute-zero": True,"ultimate": 400}, {"potion": 0.4, "sword": 0.5, "unknown_potion": 0.2})
            darcksmoke = Final_battle("Darksmoke", 2500, {"flames_of_hell": 280, "emperor-": 250, "black-blood": True, "venom": 180, "..": True,"god-of-hell": 500}, {"pot": 0.2, "Flames of hell": 0.5, "cool": 0.2})
            self.powers.update(yoohin1)

        elif ability_style == "sandals-of-hermes":
            print("_`_``_`                        ")
            print("  `--|-`---`                   ")
            print("    ````-|----^^^^^^^^^/        ")
            print("       ---|-^^^^^^^/           ")
            print("         -^^^^^^^^^^^^^\       ")
            print("          \^^^^^^^^^^^^^^^|    ")
            print("           \^^^^^^^^^^^^/      ")
            print("Your speed increased by 10%")

        elif ability_style == "absolute-zero":
            print("You stunned your enemy, dealing with 10 damage")
            dragon.health = dragon.health - 10

        elif splt[0] == "use":
            if splt[1] == "health_potion":
                print("you have use your health potion")
                self.health = self.health + 1000
            elif splt[1] == "unknown_potion":
                god_mode(True)
                self.health = self.health + 800
                dragon.health = dragon.health - 150
            else:
                print("you missed your ability !!")

        elif ability_style == "black-blood":
            print("Darksmoke slows you down, you have lost the sandals of hermes")
        elif ability_style == "..":
            print("Darksmoke increased his health by 100")
            dragon.health = dragon.health + 100

        else:
            dragon.health = dragon.health - self.powers[ability_style]
            print(f"\n{self.name} attacks {dragon.name}!\n{dragon.name} health = {dragon.health}\n")


#------------------------------------------------------------------------------------


#INTRODUCTION AND HOW TO MOVE FROM CAVE TO CAVE
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


#------------------------------------------------------------------------------------

#THIS IS WHERE THE USER STARTS TO PLAY THE GAME
user_start = input("If your ready to start the game type 'start': \n").lower()
if user_start == "start":
    welcome_user(True)
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
        print("\tType 'use' to use a item you have\n\tType 'take' to add an item\n\t Type 'cave' to know where can you go")

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
        print("\n\n\n")
        monster_vs(True)

        print("Yoohin Han : I'll have to kill you since you killed my little brother, I don't have any choice\n ")
        yoohin = Final_battle("Yoohin Han", 2200, {"frosty_sigh": 200, "shadowless_day": 250, "sandals-of-hermes": True, "blue-willows": 180, "absolute-zero": True,"ultimate": 400}, {"potion": 0.4, "sword": 0.5, "unknown_potion": 0.2})
        darcksmoke = Final_battle("Darksmoke", 2500, {"flames_of_hell": 280, "emperor": 250, "black-blood": True, "venom": 180, "..": True,"god-of-hell": 500}, {"pot": 0.2, "Flames of hell": 0.5, "cool": 0.2})

        while yoohin.is_alive() and darcksmoke.is_alive():
            yoohin.attack(darcksmoke)
            darcksmoke.attack(yoohin)

        if darcksmoke.health < 0:
            print("The Tier-1 Dragon Darksmoke has been defeated\n You won")
            print("You have acquire GOD MODE")
            print("\n\t\tThank you for playing the game!\n")
            dragon_smoke(True)
            Darcksmoke_is_alive = False
        else:
            print("You have been defeated")
            print("\t\t\t\t^\t^")
            print("\t\t\t\t^^\t^^")
            dragon_smoke(True)
            Darcksmoke_is_alive = False
    elif splitting[0] == "attack" and current_cave.monster == False:
        print("There is no monster in this cave")
    elif splitting[0] == "die":
        print("You have die!")
        print("But your angel brother saved you to avenge him.")
    else:
        print("You can't do that")



#------------------------------------------------------------------------------------

#CODE THAT MIGHT BE USEFUL OR TO REMEMBER HOW I STARTED

# # game_rules = input("type 'help' to learn more about the game:\n").lower()
# # if game_rules == "help":
# #     print("\tType 'look' to look everything in that cave\n \tType 'move' to move to another cave")
# #     print("\tType 'use' to use a item you have\n\tType 'cave' to know in which cave are you at\n")



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

# print("\n\n\n")

# print("        |||||||||   |||||||| |||||||||||| |||||||||||| |          | |||| ||        |              ")
# print("           ||    | |     ||  |          | |          | |          | |||| | |       |              ")
# print("              |   |   |      |          | |          | |          | |||| |  |      |              ")
# print("                |   |        |          | |          | |          | |||| |   |     |              ")
# print("                |   |        |          | |          | |||||||||||| |||| |    |    |              ")
# print("                |   |        |          | |          | |          | |||| |     |   |              ")
# print("                |   |        |          | |          | |          | |||| |      |  |              ")
# print("                |   |        |          | |          | |          | |||| |       | |              ")
# print("                |||||        |||||||||||| |||||||||||| |          | |||| |        ||              ")
# print("\n\n\n                                                                                                  ")
# print("                         \/                /    ///////////                    ")
# print("                          \/              /    |/                              ")
# print("                           \/            /     ||                              ")
# print("                            \/          /      |\                              ")
# print("                             \/        /       //////////\                     ")
# print("                              \/      /                  \|                    ")
# print("                               \/    /                   ||                    ")
# print("                                \/  /                    /|                    ")
# print("                                 \//           ///////////                     ")
# print("\n\n\n                                                                                                  ")
# print("    ||   \       |//////////  ||     //                                        ")
# print("    ||     \     |/        \| ||    //                                         ")
# print("    ||       \   ||        // ||   //                                          ")
# print("    ||        \  ||      //   ||  //                                           ")
# print("    ||         | ||   //      |||((                                            ")
# print("    ||        /  ||   |\      ||  |\                                           ")
# print("    ||       /   ||    |\     ||   |\                                          ")
# print("    ||     /     ||     |\    ||    |\                                         ")
# print("    ||   /       ||      |\   ||     |\                                        ")


# print("    /////////// ||         || |||||||||||| ||     // ||||||||||||              ")
# print("   |/           || \      / | |          | ||    //  |/                        ")
# print("   ||           ||  \    /  | |          | ||   //   |                         ")
# print("   |\           ||   \  /   | |          | ||  //    |\                        ")
# print("    \///////\   ||    \/    | |          | |||((     ||||||||||||              ")
# print("            \|  ||          | |          | ||  |\    |/                        ")
# print("            ||  ||          | |          | ||   |\   |                         ")
# print("            /|  ||          | |          | ||    |\  |\                        ")
# print("   //////////   ||          | |||||||||||| ||     |\ ||||||||||||              ")


# print("       |\                      / |||||||||||| ||           ||||||||||||| |||||||||||| ||         || |||||||||||| ")
# print("        |\                    /  |/           ||           |             |          | || \      / | |/           ")
# print("         |\                  /   |            ||           |             |          | ||  \    /  | |            ")
# print("          |\                /    |\           ||           |             |          | ||   \  /   | |\           ")
# print("           |\              /     |||||||||||| ||           |             |          | ||    \/    | |||||||||||| ")
# print("            |\     /\     /      |/           ||           |             |          | ||          | |/           ")
# print("             |\   /  \   /       |            ||           |             |          | ||          | |            ")
# print("              |\ /    \ /        |\           ||           |             |          | ||          | |\           ")
# print("               |\/    \/         |||||||||||| |||||||||||| ||||||||||||| |||||||||||| ||          | |||||||||||| ")





# yoohin = Final_battle("Yoohin Han", 1000, {"ability1": 200, "ability2": 150, "ability3": True, "ability4": 180, "ability5": True,"ultimate": 400}, {"potion": 0.4, "sword": 0.5, "unknown_potion": 0.2})
        # darcksmoke = Final_battle("Darksmoke", 1500, {"a1": 10, "a2": 150, "a3": True, "a4": 180, "a5": True,"ult": 500}, {"pot": 0.2, "Flames of hell": 0.5, "cool": 0.2})

#         # dragon.health = dragon.health - self.powers[ability_style]
#         # print(f"\n{self.name} attacks {dragon.name}!\n{dragon.name} health = {dragon.health}\n")