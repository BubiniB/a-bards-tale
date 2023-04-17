# This is my text adventure game:
# A Bard's Tale
# The code for this game is structured in such a way that each
# room/scene the player is in, is its own function. For the main
# function to work, the game flow is coded in reverse order
# (the first scenes appear last in the code, the game end in the beginning).

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
    print("You are an adventurer!")
    print("And so your tale begins,") 
    print("in front of the ominous cave at Mount Gylia.")

main()