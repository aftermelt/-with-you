# The script of the game goes in this file.

transform halfsize:
    zoom 0.8

label start:
    jump introduction

label introduction:
    scene bg sleep

    show game_boy_indifferent at halfsize, center
    with easeinleft
    "It's time to wake up."

    scene bg bedroom
    with dissolve
    "The morning sunlight seeps in through the blinds of your studio apartment."
    "The hums of the city outside are louder than usual"
    "You try forcing your eyes close"
    play sound "audio/alarm-sund-radar.mp3"
    "..."
    "You lie still for a moment. Then you grab your phone from the nightstand."

    show phone1 at top
    with easeinbottom

    "The news is as bleak as ever."
    "At least your mother sent you a good morning text."
    "You sigh, and turn off the alarm."
    "After a few more minutes of lying in bed, you finally muster the energy to get up."
    hide phone1
    with easeouttop

    "The stench of yesterday’s night at overtime still lingers from your clothes."
    "You need to get ready for work."

    call screen door1

    jump morning_loop

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define kid = Character("Shíyuè", color="#c8ffc8") 

init python:
    day = 1
    kidPoints = 0
    jobPoints = 0
    mail = []
    def check_mail(day, kidPoints):
        mail_events = []
        # Time-based mail
        if day == 2:
            mail_events.append("Welcome to the team! We are thrilled to have you join our organization and look forward to the fresh perspective you'll bring. Your workspace is ready with all necessary materials and access credentials.!")
        if day == 3:
            mail_events.append("Your child's first quarter report card is now available for review through our online parent portal. Please review the grades and teacher comments, and feel free to contact teachers if you have questions about your child's progress.")
        if day == 7:
            mail_events.append("Recent economic reports show unemployment rates have reached unprecedented levels in our region. Career counseling, job placement assistance, and retraining programs are available through our community resource center for those affected.")
        if day == 30:
            mail_events.append("Parent-teacher conferences are scheduled for next week to discuss your child's progress this semester. Please use our online scheduling system to book your preferred appointment time as soon as possible.")
        # Points-based mail
        if kidPoints <= -5 and day == 5:
            mail_events.append("Your child is struggling significantly in school. Teachers have expressed concern about his participation and grades. Please consider scheduling a meeting to discuss support options.")
        elif kidPoints <= -3 and day == 5:
            mail_events.append("Your child's recent report card shows below average performance. He seems disengaged and has missed several assignments. We recommend checking in with him and his teachers.")
        elif kidPoints <= -1 and day == 5:
            mail_events.append("There are some minor concerns about your child's schoolwork. While not failing, he could benefit from more encouragement and attention at home.")
        elif kidPoints >= 5 and day == 5:
            mail_events.append("Congratulations! Your child is excelling in school, consistently earning top marks and positive feedback. His teachers are impressed with his attitude and effort.")
        elif kidPoints >= 3 and day == 5:
            mail_events.append("Your child is doing well in school, showing improvement and a positive mood. Keep supporting his interests and studies for continued success.")
        elif kidPoints >= 1 and day == 5:
            mail_events.append("Your child is maintaining average performance. He seems content and is keeping up with assignments. Encourage him to keep up the good work.")
        return mail_events

label morning_loop:
    scene bg sleep
    "It's time to wake up."

    "Day [day]"
    "KidPoints: [kidPoints] | JobPoints: [jobPoints]"

    scene bg bedroom
    with dissolve
    play sound "audio/alarm-sund-radar.mp3"
    "..."
    "You lie still for a moment. Then you check the mail."

    show mail at top
    with easeinbottom

    $ mail = check_mail(day, kidPoints)
    if mail:
        "You check your mailbox."
        $ mail_text = "\n".join(mail)
        "[mail_text]"

        hide mail
        with easeouttop

        call screen door1

    label end: 

    scene bg choice
    with dissolve

    "You stand looking at two paths. One leads to the doorway out of your apartment. "
    "The other opens left, to the kitchen where your child sits, swinging his legs on a chair."
    "He looks at you with big, hopeful eyes."

    show game_boy_indifferent at halfsize, left
    with easeinleft
    with hpunch

    kid "Mom said you were busy, but I wanted to see you."
    "You feel a pang of guilt."
    "You can either leave him there, or go see what he wants."
    "But you also have to get to work. Money is tight, and food is running low."

    menu:
        "Take care of kid":
            $ kidPoints += 1
            $ jobPoints -= 1
            $ day += 1
            "You spend time with your kid. He seems happier, but you miss work."
        "Go to job":
            $ jobPoints += 1
            $ kidPoints -= 1
            $ day += 1
            "You go to work. Your kid seems disappointed, but you earn money."

    jump morning_loop



    # These display lines of dialogue.
        # Example: update points based on choices
        # $ kidPoints += 1
        # $ jobPoints -= 1

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
