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
    print("""
    As you continue on your path
    you notice how everything keeps
    getting darker. But with the torch
    in your hand you are able to light
    up the room.

    *GASP*

    A giant spider is waiting for you in
    the middle of the room.
    You waive your torch at it and scare
    it away.

    There are now 3 paths available to you:
    
    - In front of you
    - to your right,
    - and to your left.

    Which path do you choose?
    """)

    while True:
        print("Please choose (up/left/right):\n")
        choice_path = input(">> ").lower()
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
    print("""
    Darkness engulfs you.

    Eerie noises and sounds are closing
    in on you and suddenly you are 
    getting attacked!

    Unable to parry the attack with your
    sword because of the darkness around
    you, you are mortally wounded
    and die a painful death..
    """)
    game_over()

def darkness():
    """
    Let's the player make a choice
    and validates it.
    """
    print("""
    As you continue on your path you 
    notice how everything keeps getting
    darker. You continue until everything
    in front of you is pitch black.

    You hear sounds, which you have never
    heard before and they send a shiver
    down your spine..

    Should you conquer your fear move on 
    or should you turn back?
    """)

    while True:
        choice_darkness = input("Please choose (up/down): \n").lower()
        try:
            if choice_darkness == "up":
                print("""
    No! You shall not be remembered as a
    coward!

    But maybe instead as a fool..?
    
    Nobody wanders into the darkness
    without seeing something..
                """)
                game_over_darkness()
                break
            elif choice_darkness == "down":
                print("""
    You feel like a coward.. But how are
    you supposed to rescue somebody without
    even seeing where to go?
    
        >> RETURN TO PREVIOUS ROOM
                """)
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
   print("""
   You follow the right path and suddenly
   you notice how everything seems to be getting
   lighter. As you enter the room at the end
   of the path, you notice why:

   There is a torch!

   Will you take the torch?
   """)

   while True:
        print("Please choose (y/n):\n")
        choice_torch = input(">> ").lower()
        try:
            if choice_torch == "y":
                print("""
    You could really use a little
    more light and decide to take
    the torch with you.

        >> TOOK TORCH

    As there is nothing left to
    explore in this room, you decide
    to return to the previous room.

    This time however with a torch!

        >> RETURN TO PREVIOUS ROOM
                """)
                item_torch()
                room_one()
                break
            elif choice_torch == "yes":
                print("""
    You could really use a little
    more light and decide to take
    the torch with you.

        >> TOOK TORCH

    As there is nothing left to
    explore in this room, you decide
    to return to the previous room.

    This time however with a torch!

        >> RETURN TO PREVIOUS ROOM
                """)
                item_torch()
                room_one()
                break
            elif choice_torch == "n":
                print("""
    You are afraid of taking something
    which is not yours and decide to
    to leave the torch where it is.

    As there is nothing left to
    explore in this room, you decide
    to return to the previous room
    without the torch!

        >> RETURN TO PREVIOUS ROOM
                """)
                room_one()
                break
            elif choice_torch == "no":
                print("""
    You are afraid of taking something
    which is not yours and decide to
    to leave the torch where it is.

    As there is nothing left to
    explore in this room, you decide
    to return to the previous room
    without the torch!

        >> RETURN TO PREVIOUS ROOM
                """)
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
    print("""
    You follow the path  until you come to a crossroad.
    The path has now split into two:

    You can continue to the right,
    or simply move onward.

    Which path will you choose?
    """)

    while True:
        print("Please choose (right/up):\n")
        directions_room_one = input(">> ")
        try:
            if directions_room_one.lower() == "right":
                print("""
    You decide to explore the path
    to your right.
                """)
                room_two()
                break
            elif directions_room_one.lower() == "up":
                print("You decide to continue onward.")
                room_three()
                break
            elif directions_room_one.lower() == "left":
                print("""
    Maybe you should try the left!
    *OUCH!*
    You hit your head on the wall.
                """)
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
    print("""
    There are only 2 choices:
    Turn back and admit defeat
    OR
    push forward and become a hero.

    Which direction do you choose?
    Up or down?
    """)
    
    while True:
        print("Please choose (up/down):\n")
        direction_cave = input(">> ")
        try:
            if direction_cave.lower() == "up":
                print("""
    You tighten the grip around
    your sword. There is no
    turning back! You will
    rescue the princess and you
    will be a hero!
                """)
                room_one()
                break
            elif direction_cave.lower() == "down":
                print("""
    Maybe you were not ready
    for this challenge after all.
    Your shaking legs seem at
    least to think so.
                """)
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
    print("""
    Welcome to A Bard's Tale. 
    You are the famous bard Esmond
    Covendown and you are well known 
    around the lands of Palina for your
    beautiful singing voice and colorful 
    expressions when singing of heroic tales

    However..

    The thrill of adventure is calling to you
    when you hear that the beautiful princess
    Blubb has been captured by the evil witch
    Blabb.

    This is your chance to prove to the world
    that you are not but a mere bard..
    You are an adventurer!

    And so your tale begins,
    in front of the ominous cave at Mount Gylia.

    You are greeted by the entrance of the
    giant cave.. An eerie feeling befalls
    you and your heart starts beating faster.
    """)
    adventure_start()

main()