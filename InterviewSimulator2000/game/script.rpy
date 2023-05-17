# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define eil = Character("Eileen")
image BG FutonRoom = ("images/Futon_Room.png")
image entrevistadora = ("images/entrevistadora.png")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene BG FutonRoom with dissolve
    play sound "audio/vntrack01.mp3"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show entrevistadora with dissolve:
        xzoom 0.5 yzoom 0.5

    # These display lines of dialogue.

    eil "You've created a new Ren'Py game."

    eil "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
