# #Start of the game
# #NAME: S-class Hunter
# #Classes:
user_playing = True
player_items = []
Darcksmoke_is_alive = True
import random
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
def sword(active):
    if active == True:
        print("\n            /\         ")
        print("           / 和\         ")
        print("           | 的|        ")
        print("           | 和|        ")
        print("           | 平|        ")
        print("           | 破|        ")
        print("           | 冰|        ")
        print("           | 爱|        ")
        print("           | 船|        ")
        print("      \--\ |和和| /--/        ")
        print("           \.../        ")
        print("            |☯|        ")
        print("            |☯|        ")
        print("             ☯          \n")                               

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

list1 = [1, 2, 3, 4, 5, 6]
print(random.choice(list1))

#THIS IS THE FINAL BATTLE WITH THE DRAGON "DARKSMOKE"
class Final_battle:
    global player_items
    # list1 = [0, 1, 2, 3, 4, 5]
    # edge = random.choice(list1)
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
        list1 = [1, 2, 3, 4, 5, 6]
        edge = random.choice(list1)
        print(edge)
        ability_style = input(f"Enter the ability you want to use {self.powers}\n >> ")
        splt = ability_style.split(" ")
        if edge>2:
            if ability_style == "sandals-of-hermes":
                print("\n_`_``_`                        ")
                print("  `--|-`---`                   ")
                print("    ````-|----^^^^^^^^^/        ")
                print("       ---|-^^^^^^^/           ")
                print("         -^^^^^^^^^^^^^\       ")
                print("          \^^^^^^^^^^^^^^^|    ")
                print("           \^^^^^^^^^^^^/      ")
                print("Your speed increased by 10%\n")

            elif ability_style == "absolute-zero":
                print("You stunned your enemy, dealing with 10 damage")
                dragon.health = dragon.health - 10
                print(f"\n{self.name} attacks {dragon.name}!\n{dragon.name} health = {dragon.health}\n")
            elif splt[0] == "use" and splt[1] in player_items:
                if splt[1] == "health_potion":
                    print("you have use your health potion")
                    self.health = self.health + 1000
                    print(self.health)
                    player_items.remove("health_potion")

                elif splt[1] == "unknown_potion" and edge>=4:
                    god_mode(True)
                    self.health = self.health + 1000
                    print("\n\n CONGRATULATIONS YOOHIN HAN!")
                    print("\n\n YOU HAVE REACH THE LEVEL OF A GOD")
                    dragon.health = dragon.health - 1050
                    print("You are in GOD MODE")
                    print("Darksmoke it's suprised that you have reach such level")
                    print("Yoohin Han: For the sake of my brother you are going to die!!")
                    print(f"Your health increased: {self.health}")
                    player_items.remove("unknown_potion")

                elif splt[1] == "unknown_potion" and edge<4:
                    print("OPS! you drink poison from darksmoke!")
                    print("in your attemp to hit him with all your power had left dealt 500 damage but you lost 850 of life")
                    self.health = self.health - 850
                    print("Yoohin Han: I have to finish him quick or else I'm going to be dead!")
                    dragon.health = dragon.health - 500
                    print("Darksmoke laugh of you")
                    print("Darksmoke: You lowly human dare to defeat me?! Darksmoke  HAHAHAAH!")
                    print("Darksmoke: You are dead!")

                elif splt[1] == "sword":
                    sword(True)
                    print("You have sucessfully used sword")
                    dragon.health = dragon.health - 250
                    print(dragon.health)
                    player_items.remove("sword")
            
            elif splt[0] == "use" and splt[1] not in player_items:
                print("You don't have that item")
                self.attack(dragon)

            elif ability_style == "black-blood":
                print("Darksmoke slows you down, you have lost the sandals of hermes")
            elif ability_style == "..":
                print("Darksmoke increased his health by 100")
                dragon.health = dragon.health + 100
            elif ability_style== "ultimate-attack-god-of-hell":
                dragon.health = dragon.health - 1500
                print(f"\n{self.name} attacks {dragon.name}!\n{dragon.name} health = {dragon.health}\n")
            else:
                dragon.health = dragon.health - self.powers[ability_style]
                print(f"\n{self.name} attacks {dragon.name}!\n{dragon.name} health = {dragon.health}\n")
        else:
            print("You missed your ability")


#------------------------------------------------------------------------------------


#INTRODUCTION AND HOW TO MOVE FROM CAVE TO CAVE
intro_1 = "\nCollect items in order to defeat The Dragon \nYou can collect items from defeating monster along the way\n\nYoohin Han: I wish I could have saved my brother\nNo matter what I'm going to avenge him"
intro_2 = "\nYoohin Han: I have 3 options, move to cave3, cave4 or cave 6\nWhich one should I choose?"
intro_3 = "\nYou are in cave 3!\n\nYoohin Han: I wish my I could have been when my brother needed my, but I couldn't (Yoohin starts to cry)\nYoohin Han: I'm searching for something that might have left my brother for me\n"
intro_4 = "\nYou are in cave 4!\n\nYoohin Han: I need items in order to defeat this dragon! There has to be something useful for me here\n"
intro_5 = "\nYou are in cave 5!\n\nYoohin Han: I found it ! There is a key in the rocks!\n"
intro_6 = "\nYou are in cave 6!\n\nYoohin Han: Brother if you are watching me please forgive me! for not beign there for you brother!\n"
intro_7 = "\nYou are in cave 7!\n\nYoohin Ha: I finally found you darksmoke, now there is no going back, I'll fight you to the death\n"
intro_8 = "\nYou are in cave 8!\n\nYoohin Ha: I need potions!\nFound them!"

cave1 = Caves("cave1", intro_1, False, [])
cave2 = Caves("cave2", intro_2, False, [])
cave3 = Caves("cave3", intro_3, False, ["letter"])
cave4 = Caves("cave4", intro_4, False, ["sword"])
cave5 = Caves("cave5", intro_5, False, ["key"])
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
        print("\n\tType 'look' to look everything in that cave\n \tType 'move ____' and the cave you want to move")
        print("\tType 'use' to use a item you have\n\tType 'take' to add an item\n\tType 'cave' to know where can you go")
        print("\tType 'attack' when there is a monster in a cave\n")

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
            print("There is: " + item)

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
        darcksmoke = Final_battle("Darksmoke", 2500, {"flames_of_hell": 480, "emperor": 350, "black-blood": True, "venom": 380, "..": True,"king-of-hell": 500}, {"pot": 0.2, "Flames of hell": 0.5, "cool": 0.2})

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
            print("\t\tDarksmoke will rule the world after escaping The dungeon!")
            print("\t\t\t\t^^\t^^")
            dragon_smoke(True)
            Darcksmoke_is_alive = False
        exit()
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



while user_playing:
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



                 __
                |◑◑|
                |◑◑|
               /◑◑◑◑\
             /◑◑◑◑◑◑◑◑\
           / _◑_◑_◑_◑_◑_\