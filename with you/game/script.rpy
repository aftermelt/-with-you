# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define kid = Character("Shíyuè", color="#c8ffc8") 




## Note: xpos and ypos
## xpos and ypos are the horizontal and vertical position of the image.
## In my example, I'm using a value from 0-1. 
## "xpos 0.5" means the image is at 50% horizontally(start from left). This means it's centered horizontally).
## "ypos 0.28" means the image is at 28% vertically(start from top).

## Note: auto
## This sets the imagebutton's idle image and hovered image.
## auto "zeil_%s.png" is the same as: idle "zeil_idle.png" hover "zeil_hover.png.
## When using auto, the image name format should end with "idle" and "hover".

## Note: action
## The code after hovered is what will happen when the image is clicked.

## Note: hovered
## The code after hovered is what will happen when the image is hovered.

## Note: unhovered
## The code after hovered is what will happen when the image is unhovered.

# The game starts here.

label start:

    scene bg bedroom
    "The morning sunlight seeps in through the blinds of your studio apartment."
    "The hums of the city outside are louder than usual"
    "You try forcing your eyes close"
    play sound "audio/alarm-sund-radar.mp3"
    "..."
    "You lie still for a moment and grab your phone on the nightstand"

    show phone1 at top
    with easeinbottom

    call screen door1

    label end: 
    "You are in \"label end\""

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg choice
    with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show tns1 at left
    with easeinleft
    with hpunch




    # These display lines of dialogue.

    # kid "brooooo no.1 victory royale."

    # "*thinks to self* im finna slime ts kid out word my vrother"

    # kid "ayoooo sus"

    # "yeahhh j hurry up n graduate college li lbro"

    # menu:
    #     "*slime him out*":
    #         jump slimehim
    #     "*feed him mint gum*":
    #         jump book
    
    # label slimehim:

    # kid "nooo i hav ebeen slimed man w speed"

    # jump death

    # label mint:

    # kid "ts gum sooo kevin"

    # "it's poisioned cuh"

    # kid "fuhhhh"

    # jump death

    # label death:

    # "kid has died LOOOOL"

    # This ends the game.

    return
