# The script of the game goes in this file.

# kitchen ----------------------
default enokiMushroom = 0
default bigMushroom = 0
default beef = 0
default peppers = 0
default lettuce = 0
default tomato = 0
default chickenbreast = 0
# logic ------------------------
default kidPoints = 0
default jobPoints = 0
default day_multiplier = 1
# office -----------------------
default points = 10
default plus = 2
default max_point = 50
default clicked = False

transform halfsize:
    zoom 0.8

label start:
    jump introduction

label introduction:
    scene bg sleep

    "It's time to wake up."
    play music "audio/morning.wav" fadein 0.5 loop

    scene bg bedroom
    with dissolve
    "The morning sunlight seeps in through the blinds of your studio apartment."
    "The hums of the city outside are louder than usual."
    "You try forcing your eyes close."
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

define kid = Character("Shíyuè", color="#2db6c8") 

init python:
    day = 1
    mail = []

    def check_mail(day, kidPoints):
        mail_events = []
        # Time-based mail
        if day == 2:
            mail_events.append("Welcome to the team! We are thrilled to have you join our organization and look forward to the fresh perspective you'll bring. Your workspace is ready with all necessary materials and access credentials.!")
        if day == 3:
            mail_events.append("Your child's first quarter report card is now available for review through our online parent portal. Please review the grades and teacher comments, and feel free to contact teachers if you have questions about your child's progress.")
        if day >= 5 and day <= 7:
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

    def time_acceleration(day):
        if (day >= 5 and day <= 7):
            return 7
        elif day > 30:
            return 30
        return 1

    def drag_placed(drags,drop):
        renpy.play("audio/splash.mp3", channel="sound")
        if not drop:
            return


        store.draggable = drags[0].drag_name
        store.droppable = drop.drag_name
        


        return True

label morning_loop:

    $ day_multiplier = time_acceleration(day)
    $ day *= day_multiplier

    # ENDING HANDLING
    

    stop music fadeout 0.3
    scene bg sleep
    "It's time to wake up."
    play music "audio/morning.wav" fadein 0.5 loop

    "Day [day]"
    "KidPoints: [kidPoints] | JobPoints: [jobPoints]"

    scene bg bedroom
    with dissolve
    play sound "audio/alarm-sund-radar.mp3"
    "..."
    "You lie still for a moment. Then you check the mail."

    show mail at top
    with easeinbottom
    play sound "audio/envelope.mp3"
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

    # daily dialogue
    if day == 1:
        "You stand looking at two paths. One leads to the doorway out of your apartment."
        "The other opens left, to the kitchen where your child sits, swinging his legs on a chair."
        "He looks at you with big, hopeful eyes."
        show game_boy_indifferent at halfsize, center
        with easeinbottom
        kid "You're always so busy, Mom, but I wanted to see you."
    elif kidPoints <= -4 and day > 1:
        "Your kid looks bitter and sobs."
        "He scoots away from you as you enter the room."
        show game_boy_cry at halfsize, center
        with easeinbottom
        kid "..."
    elif kidPoints >= 4 and day > 1:
        "Your kid is bursting with glee."
        "He runs to you as you enter the room."
        show game_boy_happy at halfsize, center
        with easeinbottom
        with hpunch
        kid "HIIIII MOMMY!!! I MISSED YOU SO MUCH!!!"
    elif kidPoints >= 2 and day > 1:
        "Your kid looks happy and energetic."
        "He waves to you as you enter the room."
        show game_boy_smile at halfsize, center
        with easeinbottom
        with hpunch
        kid "Great to see you, Mom!"
    elif kidPoints == 0 and day > 1:
        "Your kid looks bored."
        show game_boy_indifferent at halfsize, center
        with easeinbottom
        kid "Hi..."
    elif kidPoints <= -2 and day > 1:
        "Your kid looks sad and withdrawn."
        "He barely acknowledges you as you enter the room."
        show game_boy_indifferent at halfsize, center
        with easeinbottom
        kid "*sneezes*"
    

    "Time waits for no one."
    "Decide how to spend your day. With your kid, or at work."

    menu:
        "Take care of kid":
            $ kidPoints += 1
            $ jobPoints -= 1
            $ day += 1
            "You spend time with Shíyuè. He seems happier, but you miss work."
            "Don't worry, you still have time. Tomorrow is another day."

            # KITCHEN MINIGAME
            stop music fadeout 0.3
            scene kitchen
            play music "audio/cooking.wav" fadein 0.5 loop
            call hotpotMinigame



        "Go to job":
            $ jobPoints += 1
            $ kidPoints -= 1
            $ day += 1
            "You go to work. Shíyuè seems disappointed, but you earn money."
            "Don't worry, you still have time. Tomorrow is another day."

            # JOB MINIGAME
            stop music fadeout 0.3
            scene Office_Table
            centered "Get Ready!{w=1}{nw}"
            call screen clicker


    jump morning_loop

    return

label hotpotMinigame:
    call screen setDragImages
   
    if draggable == "Beef":
        $ beef += 1
   
    elif draggable == "Enoki Mushroom":
        $ enokiMushroom += 1
   
    elif draggable == "Big Mushroom":
        $ bigMushroom += 1
   
    elif draggable == "Lettuce":
        $ lettuce += 1
   
    elif draggable == "Peppers":
        $ peppers += 1
   
    elif draggable == "Chicken Breast":
        $ chickenbreast += 1
   
    elif draggable == "Tomato":
        $ tomato += 1


    call hotpotCheck


    return
label hotpotCheck:
    image finalHotpot = "hotpotfinally.png"
    image failHotpot = "hotpotfail.png"
   
    if (beef == 2 and enokiMushroom == 1 and bigMushroom == 2 and lettuce == 1 and peppers == 1):
        show finalHotpot
        "You made Hot Pot!"
        $ kidPoints += 2
    elif (tomato > 0 or chickenbreast > 0):
        show failHotpot
        "You ruined Hot Pot!"
        $ kidPoints -= 1
    elif (beef > 2 or bigMushroom > 2 or enokiMushroom > 1 or lettuce > 1 or peppers > 1):
        show failHotpot
        "You ruined Hot Pot!"
        $ kidPoints -= 1


    else:
        jump hotpotMinigame



label win:
    $ renpy.pause(2, hard=True)
    centered "Completed! :D"
    return

label lost:
    centered "Failed! :( "
    return

screen setDragImages:
    add "kitchen.png"


    text "Make Hotpot for Shíyuè! Read the recipe on the right and":
        pos (10, 50)
        bold True
        color "#120624"
        outlines [(3, "#FFFFFF", 0, 0)]


    text "drag the correct ingredients into the pot. You only get one chance!":
        pos (10, 90)
        bold True
        color "#120624"
        outlines [(3, "#FFFFFF", 0, 0)]


    text "Hotpot Recipe:":
        pos (1400, 50)
        bold True
        color "#120624"


    text "Enoki Mushroom x1":
        pos (1400, 100)
        color "#120624"




    text "Big Mushroom x2":
        pos (1400, 140)
        color "#120624"


    text "Beef x2":
        pos (1400, 180)
        color "#120624"


    text "Lettuce x1":
        pos (1400, 220)
        color "#120624"
   
    text "Peppers x1":
        pos (1400, 260)
        color "#120624"


    text "Enoki Mushroom = [enokiMushroom]":
        pos (1520, 500)
        color "#120624"
        outlines [(3, "#FFFFFF", 0, 0)]  # white outline, thickness 3




    text "Big Mushroom = [bigMushroom]":
        pos (1520, 550)
        color "#120624"
        outlines [(3, "#FFFFFF", 0, 0)]  # white outline, thickness 3




    text "Beef = [beef]":
        pos (1520, 600)
        color "#120624"
        outlines [(3, "#FFFFFF", 0, 0)]  # white outline, thickness 3




    text "Peppers = [peppers]":
        pos (1520, 650)
        color "#120624"
        outlines [(3, "#FFFFFF", 0, 0)]  # white outline, thickness 3




    text "Lettuce = [lettuce]":
        pos (1520, 700)
        color "#120624"
        outlines [(3, "#FFFFFF", 0, 0)]  # white outline, thickness 3




    text "Chicken Breast = [chickenbreast]":
        pos (1520, 750)
        color "#120624"
        outlines [(3, "#FFFFFF", 0, 0)]  # white outline, thickness 3


    text "Tomato = [tomato]":
        pos (1520, 800)
        color "#120624"
        outlines [(3, "#FFFFFF", 0, 0)]  # white outline, thickness 3
   
    draggroup:
        drag:
            drag_name "pot"
            xpos 670
            ypos 400
            child "pot.png"
            draggable False
            droppable True


        drag:
            drag_name "Enoki Mushroom"
            xpos 50
            ypos 220
            child im.Scale("enokimushrooms.png", 150, 150)
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True


        drag:
            drag_name "Big Mushroom"
            xpos 400
            ypos 220
            child im.Scale("bigmushroom.png", 150, 150)
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True


        drag:
            drag_name "Beef"
            xpos 150
            ypos 300
            child im.Scale("beef.png", 200, 200)
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True


        drag:
            drag_name "Peppers"
            xpos 350
            ypos 350
            child im.Scale("peppers.png", 200, 200)
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True


        drag:
            drag_name "Lettuce"
            xpos 50
            ypos 650
            child im.Scale("lettuce.png", 200, 200)
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True


        drag:
            drag_name "Tomato"
            xpos 20
            ypos 450
            child im.Scale("tomato.png", 200, 200)
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True


        drag:
            drag_name "Chicken Breast"
            xpos 300
            ypos 550
            child im.Scale("chickenbreast.png", 200, 200)
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True

transform flash_anim:
    alpha 1.0
    linear 0.3 alpha 0.0

screen clicker:
    modal True

    add "Office Table.png"

    timer 0.5 repeat True action [
        If(points <= 0, true=Jump("lost"), false=SetVariable("points", points - plus))
    ]

    imagebutton:
        idle "yellow button.png"
        action [
            Play("sound", "click.wav"),
            SetVariable("clicked", False),
            If(points >= max_point, true=Jump("win"), false=SetVariable("points", points + plus))
        ]
        xpos 0.5
        ypos 0.5
        anchor (0.5, 0.5)
        xysize (300, 300)

    text "Score":
        xpos 0.62
        ypos 0.3
        xanchor 1.0
        yanchor 0.5
        size 30
        color "#FFFFFF"
        font "DejaVuSans-Bold.ttf"
        outlines [(1, "#000000", 0, 0)]

    text "[points] / [max_point]":
        xpos 0.65
        ypos 0.35
        xanchor 1.0
        yanchor 0.5
        size 50
        color "#FFD700"
        font "DejaVuSans-Bold.ttf"
        outlines [(2, "#000000", 0, 0)]
        drop_shadow (2, 2)

    vbar:
        value StaticValue(points, max_point)
        xpos 0.05
        ypos 0.5
        xanchor 0.0
        yanchor 0.5
        xsize 40
        ysize 400
