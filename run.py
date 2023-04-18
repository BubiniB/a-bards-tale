# This is my text adventure game:
# A Bard's Tale
# The code for this game is structured in such a way that each
# room/scene the player is in, is its own function. For the main
# function to work, the game flow is coded in reverse order
# (the first scenes appear last in the code, the game end in the beginning).

# Global variable, which is later used
# in room_two() and in room_three().
torch = False

def giant_spider():
    """
    Progresses story and let's players make a
    choice. Validates choices.
    """
    print("As you continue on your path")
    print("you notice how everything keeps")
    print("getting darker. But with the torch") 
    print("in your hand you are able to")
    print("light up the room.\n")
    print("A giant spider is waiting for you in")
    print("the middle of the room.\n")
    print("You waive your torch at it and")
    print("scare it away.\n")
    print("There are now 3 paths available to you:\n")
    print("In front of you,")
    print("to your right,")
    print("and to your left.\n")
    print("Which path do you choose?")

    while True:
        choice_path = input("Please choose (up/left/right): \n").lower()
        try:
            if choice_path == "up":
                goblins()
                break
            elif choice_path == "right":
                dead_end()
                break
            elif choice_path == "left":
                room_four()
                break
            elif choice_path == "down":
                print("You don't want to turn back!")
            else:
                raise ValueError("This is not a valid option.")
        except ValueError as e:
            print(e)
        

def game_over_darkness():
    """
    Runs another ending for players.
    """
    print("Darkness engulfs you.")
    print("Eerie noises and sounds are")
    print("closing in on you and suddenly")
    print("you are getting attacked.\n")
    print("Unable to parry the attack with your")
    print("sword because of the darkness around")
    print("you, you are mortally wounded")
    print("and die a painful death..\n")
    game_over()

def darkness():
    """
    Let's the player make a choice
    and validates it.
    """
    print("As you continue on your path")
    print("you notice how everything keeps")
    print("getting darker. You continue")
    print("until everything in front of")
    print("you is pitch black.\n")
    print("You hear sounds which you")
    print("have never heard before and")
    print("they send a shiver down your spine..\n")
    print("Should you conquer your fear and")
    print("move on or should you turn back?\n")

    while True:
        choice_darkness = input("Please choose (up/down): \n").lower()
        try:
            if choice_darkness == "up":
                print("No! You shall not be")
                print("remembered as a coward!\n")
                print("But maybe instead as a fool?")
                print("Nobody wanders into the darkness")
                print("without seeing something..\n")
                game_over_darkness()
                break
            elif choice_darkness == "down":
                print("You feel like a coward but")
                print("how are you supposed to")
                print("rescue somebody without even")
                print("seeing where to go.")
                print("You return to the previous")
                print("room.\n")
                room_one()
                break
            else:
                raise ValueError("This is not a valid option.")
        except ValueError as e:
            print(e)


def room_three():
    """
    Runs one of 2 functions depending on
    if the global variable torch is set to True
    or False.
    """
    global torch
    if torch == True:
        giant_spider()
    else:
        darkness()

def item_torch():
    """
    Alters the global variable torch and sets it
    to True. Function will be used in room_two().
    """
    global torch
    torch = True

def room_two():
   """
   Runs the item_torch function, which is used
   in room_three(). Let's the player choose whether to
   take the torch or leave it and validates input.
   """ 
   print("You follow the right path and suddenly")
   print("you notice how everything seems to be getting")
   print("lighter. As you enter the room at the end")
   print("of the path, you notice why: \n")
   print("There is a torch!\n")
   print("Will you take the torch?\n")

   while True:
        choice_torch = input("Please choose (y/n): \n").lower()
        try:
            if choice_torch == "y":
                print("You could really use a little")
                print("more light and decide to take")
                print("the torch with you.")
                print("As there is nothing left to")
                print("explore in this room, you decide")
                print("to return to the previous room.")
                print("This time however with a torch!\n")
                item_torch()
                room_one()
                break
            elif choice_torch == "yes":
                print("You could really use a little")
                print("more light and decide to take")
                print("the torch with you.")
                print("As there is nothing left to")
                print("explore in this room, you decide")
                print("to return to the previous room.")
                print("This time however with a torch!\n")
                item_torch()
                room_one()
                break
            elif choice_torch == "n":
                print("You are afraid of taking something")
                print("which is not yours and decide to")
                print("to leave the torch where it is.")
                print("As there is nothing left to")
                print("explore in this room, you decide")
                print("to return to the previous room")
                print("without the torch!\n")
                room_one()
                break
            elif choice_torch == "no":
                print("You are afraid of taking something")
                print("which is not yours and decide to")
                print("to leave the torch where it is.")
                print("As there is nothing left to")
                print("explore in this room, you decide")
                print("to return to the previous room")
                print("without the torch!\n")
                room_one()
                break
            else:
                raise ValueError("This is not a valid option.")
        except ValueError as e:
            print(e)

def room_one():
    """
    Let's players choose which directions to go
    and validates input.
    """
    print("You have finally entered the evil witche's")
    print("lair. You follow the path deeper into")
    print("the cave until you come to a crossroad.\n")
    print("The path has now split into two:\n")
    print("You can continue to the right,")
    print("or simply move onward.\n")
    print("Which path will you choose?")

    while True:
        directions_room_one = input("Please choose (right/up): \n")
        try:
            if directions_room_one.lower() == "right":
                print("You decide to explore the path")
                print("to your right.")
                room_two()
                break
            elif directions_room_one.lower() == "up":
                print("You decide to continue onward.")
                room_three()
                break
            elif directions_room_one.lower() == "left":
                print("Maybe you should try the left!")
                print("You hit your head on the wall.")
            elif directions_room_one.lower() == "down":
                print("No! You cannot turn back now!")
            else:
                raise ValueError("This is not a valid option.")
        except ValueError as e:
            print(e)

def game_over_coward():
    """
    Unlocks the 'coward' ending and
    has the reset function, which allows players
    to play another round.
    """
    print("coward")
    game_over()

def adventure_start():
    """
    The first scene/room in the game. Setting the scene and
    letting the player choose directions through inputs.
    Input are validated.
    """
    print("You are greeted by the entrance of the")
    print("giant cave at Mount Gylia. An eerie feeling befalls")
    print("you and your heart starts beating faster.\n")
    print("There are only 2 choices:\n")
    print("Turn back and admit defeat,")
    print("or")
    print("push forward and become a hero.\n")
    print("Which direction do you choose?")
    print("up")
    print("or")
    print("down?\n")
    
    while True:
        direction_cave = input("Please choose (up/down): ")
        try:
            if direction_cave.lower() == "up":
                print("You tighten the grip around")
                print("your sword. There is no")
                print("turning back! You will")
                print("rescue the princess and you")
                print("will be a hero!\n")
                room_one()
                break
            elif direction_cave.lower() == "down":
                print("Maybe you were not ready")
                print("for this challenge after all.")
                print("Your shaking legs seem at")
                print("at least to think so.")
                game_over_coward()
                break
            elif direction_cave.lower() == "right":
                print("You cannot go there right now")
            elif direction_cave.lower() == "left":
                print("You cannot go there right now")
            else:
                raise ValueError("This is not a valid option.")
        except ValueError as e:
            print(e)

def main():
    """
    The main function of this game. Sets the scene and let's
    player immerse themselves in the game world, as well as
    start the game.
    """
    print("Welcome to A Bard's Tale.\n")
    print("You are the famous bard")
    print("Esmond Covendown.\n")
    print("You are well known around the lands") 
    print("of Palina for your beautiful singing voice and")
    print("colorful expressions when singing of heroic tales.\n")
    print("However..\n")
    print("The thrill of adventure is calling to you")
    print("when you hear that the beautiful princess")
    print("Blubb has been captured by the evil witch Samsara.\n")
    print("This is your chance to prove to the world")
    print("that you are not but a mere bard..")
    print("You are an adventurer!\n")
    print("And so your tale begins,") 
    print("in front of the ominous cave at Mount Gylia.\n")
    adventure_start()

main()