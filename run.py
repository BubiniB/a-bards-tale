# This is my text adventure 
# game:
# A Bard's Tale
# The code for this game is 
# structured in such a way that 
# each room/scene the player is
# in, is its own function. For 
# the main function to work,
# the game flow is coded in reverse
# order (the first scenes appear last
# in the code, the game end in the 
# beginning).

# Used to clear terminal for Windows
# Mac and Linux.
from os import system, name

# Used for delaying clear terminal
from time import sleep

# Used for creating a typing text effect
import time,sys


def typing_print(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)


# Global variables, which is later used
# in room_two() and in room_three().
torch = False
two_sisters = False


def clear_terminal():
    """
    Clears the terminal for
    devices running on Windows,
    Mac or Linux, after 4 seconds.
    Used in game_over().
    """
    sleep(4)
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def game_over():
    """
    Let's players know the game has
    come to an end and gives choice
    to restart or end game.
    """
    typing_print("""
    And this is how the tale of Esmond
    Covendown ends..

>> GAME OVER <<

    Do you want to play again?
    """)
    while True:
        typing_print("Please choose (yes/no):\n")
        choice_continue = input(">> ").lower()
        try:
            if choice_continue == "yes" or choice_continue == "y":
                typing_print("""
>> RESTARTING GAME
                """)
                clear_terminal()
                main()
                break
            elif choice_continue == "no" or choice_continue == "n":
                typing_print("""
    Thank you for playing! Goodbye!
                """)
                break
            else:
                raise ValueError("This is not a valid option.")
        except ValueError as e:
            typing_print(e)        


def happiness():
    """
    One of the endings in the game,
    unlocked if global variable
    two_sisters is set to True and
    player chose to sing in evil_witch().
    """


def rescue_princess():
    """
    One of the endings in the game,
    unlocked if player chose to fight
    in evil_witch().
    """
    print("""
    The princess seems to have passed
    out. Carefully you pick her up
    and carry her to safety.

    Back in castle Palina, the
    king and the queen have
    prepared a warm welcome for
    you and the princess.

    The celebration lasts several
    days and you are rewarded with
    land and gold. You are a hero!

    Princess Sera however never
    returned to be her former self..
    After the traumatizing fight
    she became but a mere puppet,
    apathic and lost her voice..

    If there only was something you
    could have done for her..
    """)


def mission_failed():
    """
    One of the endings in the game,
    unlocked if player chose to run
    in evil_witch().
    """
    print("""
    
    """)


def evil_witch():
    """
    The last room/scene in the game.
    Players get to make a choice and
    it is validated, and affects the
    outcome of the game. Checks for
    global variable two_sisters and
    presents another choice if set to
    True.
    """
    typing_print("""
    There she is: 
    The evil witch Calandra is waiting for
    you!

    You see the beautiful princess
    Sera far in the distance, waiving
    her arms. She wants to run towards
    you and the witch, but the witch
    just snaps her fingers and starts
    laughing.

    Some sort of transparent wall
    seems to stop the princess in
    her way. You see how she
    desperately tries to smash the
    wall by hitting it with her bare
    hands but to no avail. Her screams
    cannot leave the barrier behind
    her and you don't hear even a
    single sound.

    You turn your attention back to
    the witch, seeing her for the
    first time up close, you are taken
    aback:

    She looks like a darker version
    of princess Sera!!

    What is this sorcery? Is she
    trying to trick you?

    'Bwahahaha! Puny little bard!
    Your journey ends here!
    Princess Sera belongs here'

    The evil witch laughs again.

    You cannot just stand there,
    it is time to act!
    """)
    global two_sisters
    if two_sisters == True:
        typing_print("""
    You don't know why, but you
    cannot shake of the mural and
    tale of the Two Sisters. You
    feel a sudden urge to sing.

    Should you sing? Or would it
    be better to fight? The witch
    does not seem that friendly
    after all.. You could also
    try and run. With more
    preparation and fighting
    experience you could maybe
    stand a better chance.
        """)
    else:
        typing_print("""
    What should you do? Take
    your sword and challenge the
    witch to a fight or run away?
    With more preparation and
    fighting experience you could
    maybe stand a better chance.
        """)
    while True:
        if two_sisters == True:
            typing_print("Please choose (fight/run/sing):\n")
            choice = input(">> ").lower()
        else:
            typing_print("Please choose (fight/run):\n")
            choice = input(">> ").lower()
        try:
            if choice == "fight":
                typing_print("""
    You decide to fight Calandra.
    In a surprise motion you toss
    your torch towrds the witch.

    'Do you really think you can
    beat me with a torch?'

    With a swift motion of her
    hands she waives the torch
    away. 

    What she did not anicipate 
    is your surprise attack,
    which you managed to hide
    while the witch was distracted
    by the torch.

    You stab the witch with your
    sword through her chest and
    her lifeless body falls to the
    ground.

    The barrier vanishes and you 
    are free to go to princess
    Sera.
                """)
                rescue_princess()
                break
            elif choice == "run":
                typing_print("""
                The witch snipes you
                """)
                mission_failed()
                break
            elif choice == "sing" and two_sisters:
                typing_print("""
                Witch starts crying
                calm
                princess comes and hugs
                """)
                happiness()
                break
            else:
                raise ValueError("This is not a valid option.")
        except ValueError as e:
            typing_print(e)


def true_ending():
    """
    Sets global variable two_sisters
    to True.
    """
    global two_sisters
    two_sisters = True


def tale():
    """
    Let's the player make 2 choices,
    validates them and can unlock
    another ending depending on the
    choices.
    """
    typing_print("""
    You enter a dark room. The light
    of your torch helps only modestly
    but shines enough to reveal some
    sort of fire pit close by.

    You could surely light up the
    entire room by lighting a fire
    in the pit.

    What should you do?

    Will you light the fire or
    will you leave?
    """)

    while True:
        typing_print("Please choose (light/leave):\n")
        choice_ending = input(">> ").lower()
        try:
            if choice_ending == "light":
                typing_print("""
    You light up the fire in the middle
    of the room and a mural with beautiful
    carvings is revealed. The carvings are
    of two women hugging each other. 
    
    You find a text written under the image
    of the two women. It seems to be some
    sort of tale!

    Curiously you approach the mural as you
    suddenly hear a faint noise.

    Was that a woman? Could it be the princess?

    Will you read the text or leave?
                """)
                while True:
                    typing_print("Please choose (read/leave):\n")
                    choice_read = input(">> ").lower()
                    try:
                        if choice_read == "read":
                            typing_print("""
    It is the tale of the 2 sisters,
    twins, divided by birth. One grew up
    to become a princess, the other was
    given away as an offer of peace.

    They grow up seperated from each
    other but make up their minds
    to go on an adventure to find 
    their other half, until they are
    finally united again..

    You know of this tale and the
    melody that accompanies it,
    you are a bard after all.
    
    It is however surprising to find
    the tale carved onto a wall in a
    cave at Mount Gylia..

    You decide to study the wall
    a bit more before taking the path
    back to the previous room, as 
    there isn't anything else left
    to explore.

>> RETURN TO PREVIOUS ROOM
    _________________________________
                            """)
                            true_ending()
                            room_four()
                            break
                        elif choice_read == "leave":
                            typing_print("""
    No! You don't really have time
    for this! The princess needs
    you and the faster you get to
    the evil witche's lair the
    better.

    You decide to leave the room 
    and return to the previous
    room in a hurry.

>> RETURN TO PREVIOUS ROOM
    __________________________________
                            """)
                            room_four()
                            break
                        else:
                            raise ValueError("This is not a valid option.")
                    except ValueError as e:
                        typing_print(e)
                break
            elif choice_ending == "leave":
                typing_print("""
    Best you leave everything as is. It
    could be a trap after all and so you
    must excercise caution.

    As fun as exploring can be, you feel
    like you do not have enough time anyway.
    You must find the princess and so you
    decide to go back to the preivous room.

>> RETURN TO PREVIOUS ROOM
    __________________________________
                """)
                room_four()
                break
            else:
                raise ValueError("This is not a valid option.")
        except ValueError as e:
            typing_print(e)


def game_over_trap():
    """
    One of the endings the player
    unlocks.
    """
    typing_print("""
    A trapdoor opens under your feet
    and you cannot react fast enough
    to step down from it.

    Since you are holding the lyre
    tightly in your hands, you cannot
    grab onto the ledge.

    And so you fall into your death..
    """)
    game_over()


def treasure():
    """
    Let's players make a choice, validates
    choices and runs one of multiple
    endings, depending on players' choice
    """
    typing_print("""
    There are golden objects everywhere
    scattered across the room. You
    have never seen so much gold in
    your entire life.

    There is however one object
    that catches your attention
    in particular:

    A golden lyre.

    The lyre is placed on a pedestal
    in the middle of the room. It
    looks pure and untouched.

    Maybe you should take it
    with you, as a souvenir to remind
    you of your heroic journey.

    And who knows, it might come in
    handy?

    Will you take the lyre?
    Yes or no?
    """)

    while True:
        typing_print("Please choose (y/n):\n")
        choice_lyre = input(">> ").lower()
        try:
            if choice_lyre == "y" or choice_lyre == "yes":
                typing_print("""
    The lyre is just too beautiful
    to be left behind. You must
    simply have it.

>> TOOK LYRE

    As soon as you take the lyre
    the ground starts shaking.
    This wasn't a good idea after
    all...
                """)
                game_over_trap()
                break
            elif choice_lyre == "n" or choice_lyre == "no":
                typing_print("""
    No! There is no point in being
    greedy! You are here to rescue
    the princess and not on a
    scavenge hunt!

    You resist the urge to take the
    lyre with you and return to the
    previous room.

>> RETURN TO PREVIOUS ROOM
    _________________________________
                    """)
                room_four()
                break
            else:
                raise ValueError("This is not a valid option.")
        except ValueError as e:
            typing_print(e)


def room_four():
    """
    Progresses story and let's players make a
    choice. Validates choices.
    """
    typing_print("""
    You come to a crossroad.

    Will you go to the left, up or
    down?
    """)

    while True:
        typing_print("Please choose (left/up/down):\n")
        choice_path = input(">> ").lower()
        try:
            if choice_path == "up":
                typing_print("""
    You continue on the path in
    front of you.
    _________________________________
                """)
                evil_witch()
                break
            elif choice_path == "left":
                global two_sisters
                if two_sisters == True:
                    typing_print("""
    You return to the mural and study the
    carvings again, trying to imprint
    the image in your memory.

    You then decide to return to the previous
    room.

>> RETURN TO PREVIOUS ROOM.
    ____________________________________
                    """)
                else:
                    typing_print("""
    You choose the left path .
    __________________________________
                    """)
                    tale()
                    break
            elif choice_path == "down":
                typing_print("""
    As you continue on this path you
    see something glittering and shining.
    You seem to have found the treasure
    room!
    _________________________________
                """)
                treasure()
                break
            elif choice_path == "right":
                typing_print("""
    Hey! Don't you remember?

    NO TURNING BACK NOW!
    _________________________________
                """)
            else:
                raise ValueError("This is not a valid option.")
        except ValueError as e:
            typing_print(e)


def game_over_lynched():
    """
    One of the endings in the game
    """
    typing_print("""
    You don't get a chance to
    complete your song, as the
    angry mob of goblins seems
    rather unaffected by the fine
    art of singing.

    They swing their weapons at you
    and strike you to death..
    """)
    game_over()


def game_over_lost_torch():
    """
    One of the endings in the game
    """
    typing_print("""
    You know what hideous monster
    is waiting for you in this
    room.. But this time you don't
    have a torch to scare it away.
    Nor see where you are supposed
    to go.

    But you have a great memory and
    can almost see the room's layout
    in front of you in spite of
    being shrouded in darkness. You
    decide to make a run for it.

    The giant spider is however 
    faster and catches you almost
    immediatly. You feel a sting in 
    your chest and lose consciousness..

    This is how you became spider
    dinner..
    """)
    game_over()


def goblins():
    """
    Let's players make choices, which
    lead to different outcomes and
    validates these.
    """
    typing_print("""
    You enter the room and notice almost
    immediatly the group of 5 goblins
    in one of the corners of the room.

    Maybe this was not the right path..?

    Before you even get a chance to make
    a choice, the goblins notice you
    and start running towards you. You are
    scared and tighten the grip around
    your sword. They don't seem nice.. But
    maybe a song would cheer them up?

    What should you do?
        - Fight
        - Run
        - Sing
    """)

    while True:
        typing_print("Please choose (fight/run/sing):\n")
        choice_action = input(">> ").lower()
        try:
            if choice_action == "fight":
                typing_print("""
    You aren't a very skilled fighter. In
    order to be able to fight you toss away
    your torch and ready your sword.

>> LOST TORCH

    The goblins charge at you, attacking
    relentlessly. But you don't give up and
    strike at them until one after the
    other falls in battle.

    You are victorious!

    But there is just one little thing
    you remember now..

    Your torch is gone.

    You scan the room for anything
    useful but it only appears to be
    a dead end.

    Exhausted and nervous you return to
    the previous room.

>> RETURN TO PREVIOUS ROOM
    __________________________________
                """)
                game_over_lost_torch()
                break
            elif choice_action == "run":
                typing_print("""
    You aren't a very skilled fighter since
    this is your first adventure.

    It would be crazy to think that
    you would stand a chance against 5
    goblins.

    You run as fast as you can in the
    direction you came from and the
    goblins lose track of you.

>> RETURN TO PREVIOUS ROOM
    __________________________________
                """)
                room_three()
                break
            elif choice_action == "sing":
                typing_print("""
    Right! You could surprise them
    with a song! Maybe this will
    stun them and then you have a
    chance to escape!

>> SINGING

    'Hear the story of Erik the great..'
    ______________________________________
                """)
                game_over_lynched()
                break
            else:
                raise ValueError("This is not a valid option.")
        except ValueError as e:
            typing_print(e)


def dead_end_one():
    """
    Sends the player back to room_three.
    """
    typing_print("""
    As you enter the room, you are
    greeted by a wall.

    Great! A dead end! You have no
    choice but to turn back.

>> RETURN TO PREVIOUS ROOM
    __________________________________
    """)
    room_three()


def giant_spider():
    """
    Progresses story and let's players make a
    choice. Validates choices.
    """
    typing_print("""
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
        typing_print("Please choose (up/left/right):\n")
        choice_path = input(">> ").lower()
        try:
            if choice_path == "up":
                typing_print("""
    You continue on the path in
    front of you.
    _________________________________
                """)
                goblins()
                break
            elif choice_path == "right":
                typing_print("""
    You choose the path to your right.
    __________________________________
                """)
                dead_end_one()
                break
            elif choice_path == "left":
                typing_print("""
    You choose the path to your left.
    _________________________________
                
    You have made past the giant spider
    and you feel relieved. You take a break
    and collect your thoughts.
    
    This adventure has been more challenging
    than anything you have ever done
    in your entire life. But there is
    no turning back now!

    You take a big breath. Time to
    move on!
                """)
                room_four()
                break
            elif choice_path == "down":
                typing_print("""
    You don't want to turn back!
                """)
            else:
                raise ValueError("This is not a valid option.")
        except ValueError as e:
            typing_print(e)
        

def game_over_darkness():
    """
    Runs another ending for players.
    """
    typing_print("""
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
    typing_print("""
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
        typing_print("Please choose (up/down):\n")
        choice_darkness = input(">> ").lower()
        try:
            if choice_darkness == "up":
                typing_print("""
    No! You shall not be remembered as a
    coward!

    But maybe instead as a fool..?
    
    Nobody wanders into the darkness
    without seeing something..
                """)
                game_over_darkness()
                break
            elif choice_darkness == "down":
                typing_print("""
    You feel like a coward.. But how are
    you supposed to rescue somebody without
    even seeing where to go?
    
>> RETURN TO PREVIOUS ROOM
    _______________________________________
                """)
                room_one()
                break
            else:
                raise ValueError("This is not a valid option.")
        except ValueError as e:
            typing_print(e)


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
   Checks whether player has already torch to avoid
   repitition.
   """ 
    global torch
    if torch == True:
        typing_print("""
    You do not need to enter this room
    again.

    Remember?

    You already have the torch and
    there was nothing left to explore.
    _______________________________________
        """)
        room_one()
    else:
        typing_print("""
   You follow the right path and suddenly
   you notice how everything seems to be getting
   lighter. As you enter the room at the end
   of the path, you notice why:

   There is a torch!

   Will you take the torch?
        """)

        while True:
            typing_print("Please choose (y/n):\n")
            choice_torch = input(">> ").lower()
            try:
                if choice_torch == "y" or choice == "yes":
                    typing_print("""
    You could really use a little
    more light and decide to take
    the torch with you.

>> TOOK TORCH

    As there is nothing left to
    explore in this room, you decide
    to return to the previous room.

    This time however with a torch!

>> RETURN TO PREVIOUS ROOM
    __________________________________
                """)
                    item_torch()
                    room_one()
                    break
                elif choice_torch == "n" or choice == "no":
                    typing_print("""
    You are afraid of taking something
    which is not yours and decide to
    to leave the torch where it is.

    As there is nothing left to
    explore in this room, you decide
    to return to the previous room
    without the torch!

>> RETURN TO PREVIOUS ROOM
    _________________________________
                    """)
                    room_one()
                    break
                else:
                    raise ValueError("This is not a valid option.")
            except ValueError as e:
                typing_print(e)


def room_one():
    """
    Let's players choose which directions to go
    and validates input.
    """
    typing_print("""
    The path has now split into two:
    You can continue to the right,
    or simply move onward.

    Which path will you choose?
    """)

    while True:
        typing_print("Please choose (right/up):\n")
        directions_room_one = input(">> ")
        try:
            if directions_room_one.lower() == "right":
                typing_print("""
    You decide to explore the path
    to your right.
    _______________________________
                """)
                room_two()
                break
            elif directions_room_one.lower() == "up":
                typing_print("""
     You decide to continue onward.
     ______________________________
                """)
                room_three()
                break
            elif directions_room_one.lower() == "left":
                typing_print("""
    Maybe you should try the left!
    *OUCH!*
    You hit your head on the wall.
    _______________________________
                """)
            elif directions_room_one.lower() == "down":
                typing_print("""
    No! You cannot turn back now!
    You are done being a coward!
                """)
            else:
                raise ValueError("This is not a valid option.")
        except ValueError as e:
            typing_print(e)


def game_over_coward():
    """
    Unlocks the 'coward' ending and
    has the reset function, which allows players
    to play another round.
    """
    typing_print("""
    It's no use, you were not ready
    for this challenge..

    You turn around and leave Mount
    Gylia. There would be tales sung
    about your cowardice and that is
    how you left your mark in this
    world..
    """)
    game_over()


def adventure_start():
    """
    The first scene/room in the game. Setting the scene and
    letting the player choose directions through inputs.
    Input are validated.
    """
    typing_print("""
    There are only 2 choices:
    Turn back and admit defeat
    OR
    push forward and become a hero.

    Which direction do you choose?
    Up or down?
    """)
    
    while True:
        typing_print("Please choose (up/down):\n")
        direction_cave = input(">> ")
        try:
            if direction_cave.lower() == "up":
                typing_print("""
    You tighten the grip around
    your sword. There is no
    turning back! You will
    rescue the princess and you
    will be a hero!
    _____________________________________

    You follow the path until you come to a
    crossroad.
                """)
                room_one()
                break
            elif direction_cave.lower() == "down":
                typing_print("""
    Maybe you were not ready
    for this challenge after all.
    Your shaking legs seem at
    least to think so.
    _____________________________________
                """)
                game_over_coward()
                break
            elif direction_cave.lower() == "right":
                typing_print("You cannot go there right now")
            elif direction_cave.lower() == "left":
                typing_print("You cannot go there right now")
            else:
                raise ValueError("This is not a valid option.")
        except ValueError as e:
            typing_print(e)


def main():
    """
    The main function of this game. Sets the scene and let's
    player immerse themselves in the game world, as well as
    start the game.
    """
    typing_print("""
    Welcome to A Bard's Tale.
    _____________________________________

    How to play the game:

    A story will be told to you and leave
    you with challenging choices to be made. 
    A prompt will appear and you will have
    to type your answer, submitting it by
    pressing enter.

    How will your story end?

    While exploring and journeying through
    this world, you will come to different
    rooms and you will have to choose,
    which path to take. Your character is
    always facing the north when entering
    a new room.

    Now, please enjoy a Bard's Tale.
    _____________________________________

    You are the famous bard Esmond
    Covendown and you are well known 
    around the lands of Palina for your
    beautiful singing voice and colorful 
    expressions when singing of heroic tales

    However..

    The thrill of adventure is calling to you
    when you hear that the beautiful princess
    Sera has been captured by the evil witch
    Calandra.

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