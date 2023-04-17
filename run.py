# This is my text adventure game:
# A Bard's Tale
# The code for this game is structured in such a way that each
# room/scene the player is in, is its own function. For the main
# function to work, the game flow is coded in reverse order
# (the first scenes appear last in the code, the game end in the beginning).

def room_one():
    print("bajs")

def game_over_coward():
    print("coward")

def adventure_start():
    """
    The first scene/room in the game. Setting the scene and
    letting the player choose directions through inputs.
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
        direction_cave = input("Choose (up/down): ")
        try:
            if direction_cave.lower() == "up":
                room_one()
                break
            elif direction_cave.lower() == "down":
                game_over_coward()
                break
            elif direction_cave == "right":
                print("You cannot go there right now")
            elif direction_cave == "left":
                print("You cannot go there right now")
            else:
                raise ValueError("This is not a valid option. Please choose 'up' or 'down'")
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