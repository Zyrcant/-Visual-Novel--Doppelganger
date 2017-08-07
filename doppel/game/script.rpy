# Declare images
init:
    #backgrounds
    image black = Image("Black.png")
    image classroom = Image("classroom.png")
    image hallway = Image("hall.png")
    image office = Image("office.png")
    image library = Image("library.png")
    image locker = Image("locker/openlocker.png")
    
    #Characters
    #Holly
    image holly normal = Image("holly_normal.png")
    image holly normal flip = im.Flip("holly_normal.png", horizontal=True)
    image holly angry = Image("holly_angry.png")
    image holly angry flip = im.Flip("holly_angry.png", horizontal=True)
    image holly sad = Image("holly_sad.png")
    image holly sad flip = im.Flip("holly_sad.png", horizontal=True)
    
    #Jeremy
    image jeremy normal = Image("jeremy_normal.png")
    image jeremy normal flip = im.Flip("jeremy_normal.png", horizontal=True)
    image jeremy hurt = Image("jeremy_hurt.png")
    image jeremy hurt flip = im.Flip("jeremy_hurt.png", horizontal=True)
    
    #Tristan
    image tristan normal = Image("tristan_normal.png")
    image tristan normal flip = im.Flip("tristan_normal.png", horizontal=True)
    image tristan angry = Image("tristan_angry.png")
    image tristan angry flip = im.Flip("tristan_angry.png", horizontal=True)
    
    #Officeperson
    image admin = Image("rachel.png")
    
    #Objects
    image diary = Image("diary.png")
    image arrow = Image("map/arrow.png")
    #phoneObjects
    image phone lock = Image("phoneblack.png")
    image phone messages = Image("phone2.png")
    image phone dadphone = Image("phone/dad_phone.png")
    image phone jeremyphone = Image("phone/jeremy_phone.png")
    image phone rachelphone = Image("phone/rachel_phone.png")
    image phone tiffanyphone = Image("phone/tiffany_phone.png")
    image phone tristanphone = Image("phone/tristan_phone.png")
    #lockerObjects
    image lock note1 = Image("locker/note1.png")
    image lock books = Image("locker/letter.png")
    image report = Image("report.png")
    image newspaper = Image("newspaper.png")
    #Positions
    $ slightleft = Position(xpos=0.2, xanchor='left')
    $ slightright = Position(xpos = 0.7, xanchor = 'center')
    #Variables
    $ letterFound = False
    $ mrBruce = False
    
# Declare characters
define player = Character('You')
define jeremy = Character('Jeremy', color = "#9334C0")
define holly = Character('Holly', color = "#DC7488")
define tristan = Character('Tristan', color = "#CB1212")
define officeperson = Character('Administrator', color = "#487AB2")
define bruce = Character('Mr. Bruce', color = "#ffffff")

#Start of game
label start:
    scene black
    narrator "You wake up and it's pitch black everywhere."
    player "Where am I? The last thing I remember is falling asleep during one of Bruce's biology lectures..."
    narrator "You raise your head and look up."
    scene classroom with fade
    narrator "You're in class, but nobody seems to be there."
    narrator "Even Mr. Bruce has already left."
    player "Oh crap, did I sleep through the whole class?"
    jump sleeping
    
    #if they decide to keep sleeping, they will continue to loop back here.
    label sleepingautism:
            narrator "You wake up."
            scene classroom with fade
            narrator "The classroom is still empty."
    
    #decides whether to stay in that loop or to advance further into the game.
    label sleeping:
        menu:
            player "Should I...."
    
            "Keep sleeping":
                scene black
                narrator "You close your eyes and fall back asleep."
                player "A few more minutes of rest couldn't hurt..."
                jump sleepingautism
            "Get up and leave":
                narrator "You decide to leave the classroom."
                jump scene1
            "skippy":
                jump locker
       
#Scene 2
label scene1:
    narrator "You step out into the hallway."
    scene hallway
    narrator "The hallway seems to be empty as well."
    narrator "You spot Holly and Jeremy out of the corner of your eye."
    show holly normal flip at slightleft with dissolve
    show jeremy normal at slightright with dissolve
    player "Hey Holly! Hey Jeremy!"
    narrator "Neither of them respond."
    player "Are they ignoring me?"
    player "It's not that unusual that Holly would ignore me, but Jeremy too?"
    player "They're even talking to each other. That never happens. Something's got to be going on."
    menu:
        narrator "You decide to..."
        
        "Listen to their conversation":
            narrator "You walk over to them and listen to what they're saying."
            narrator "They seem to have not noticed you at all."
            jump eavesdropping
        "Go home":
            narrator "You decide to leave them and go home instead."
            jump home

#Listen in to the two
label eavesdropping:
    jeremy "Holly, why can't we just talk?"
    holly "You KNOW why, Jeremy. I'm not gonna talk to a nerd like you."
    show jeremy hurt
    jeremy "What the heck Holly? That's really harsh."
    player "Yeah, seriously Holly, that was way overboard."
    holly "Jeremy, just leave me alone."
    narrator "They seem to be totally ignoring you. You decide you need to try to attract their attention."
    menu:
        narrator "You decide to..."
        
        "Scream loudly at the two of them":
            narrator "Screaming seemed to have no effect at all, as they still seem like they haven't even noticed you."
        
        "Talk about the weather":
            narrator "As expected, you're completely ignored and nothing comes of your meaningless attempt at small talk."
            
        "Jump up and down like a child":
            narrator "They ignore you as you try to kick up as much of a fuss as possible. It seems like they still haven't even noticed you."
            
    narrator "While you're still trying to get their attention, Tristan, Holly's boyfriend and the football star, comes in."
    show tristan normal flip with moveinleft
    tristan "Seriously, get lost loser. Quit wasting her time."
    tristan "Let's ditch this loser, Holly, come on."
    hide tristan
    holly "...Bye."
    hide holly
    jeremy "I just wanted to help..."
    hide jeremy
    player "Wow, Holly's as rude as ever. And her boyfriend was even harsher! Man, they're the worst couple in the school."
    player "It seems like no one can see me. Even when I'm right next to them, I'm being completely ignored. I'll worry about it later. For now, I think I should follow one of them."
    menu:
        narrator "You decide to follow..."
        
        "Holly and Tristan":
            player "I should see what those two are doing. Maybe I can get revenge or something on them."
            jump hollyroute
            
        "Jeremy":
            player "Poor Jeremy's really hurt. I should go see if I can comfort him or something."
            narrator "You try to follow after Jeremy, but you can't find him anywhere. It's almost like he disappeared."
            player "Well, if I can't find Jeremy, I might as well go follow Holly and Tristan."
            jump hollyroute
        
    return

#holly
label hollyroute:
    narrator "You stealthily follow Holly and Tristan and see what they're talking about."
    show tristan normal flip at left with moveinleft
    show holly normal at right with moveinright
    tristan "You were wasting your time talking to that guy? I was waiting for you, you know!"
    holly "He stopped me, there was nothing I could do. Like I'd want to talk to HIM."
    tristan "Keep talking to Jeremy, and you'll end up like Sadie."
    player "Wait what? What does he mean? What happened to me?"
    show holly angry
    holly "Tristan, don't joke about that. I expect even you to have some kind of respect for the dead."
    tristan "Who cares, she's gone now and I don't have to deal with her."
    show holly sad
    player "I'm... dead? Everyone's been ignoring me because I'm dead?"
    player "When did I die? How did I die? Why can't I remember anything about this?"
    narrator "Suddenly, you notice Holly begins to glow. You feel drawn to her."
    player "Huh? Holly's glowing? Well, I guess I don't really have anything else to go on."
    narrator "You reach out to Holly, and suddenly everything goes black."
    jump possessholly
    
label possessholly:
    hide holly normal
    hide tristan
    show tristan angry flip with fade
    narrator "You suddenly find yourself face to face with Tristan."
    tristan "HELLO? HOLLY? ANYONE IN THERE?"
    player "Huh? What? Me?"
    tristan "No, the other Holly. Of course, I'm talking to you, idiot. Were you listening at all?"
    player "{i}What on earth is happening? I became Holly?{/i}"
    player "{i}Huh, I always knew Tristan was a jerk, but man, he's like this to everyone? Even Holly? Even the \"Perfect Couple\"?{/i}"
    player "Yeah, of course, Tristan. Sorry. I won't talk to him again."
    show tristan normal flip
    tristan "Okay, whatever Holly. Like I told you before, I'm off to go ditch class with the guys. I'll see you later."
    player "See you, Tristan. Take care."
    show tristan angry flip
    tristan "Take care? The hell is wrong with you?"
    show tristan normal flip
    tristan "Whatever. Bye."
    hide tristan normal
    player "Well, that's over with. I guess I'll take this opportunity to find out what I can about myself. What happened to me? Where did I go?"
    player "I'll take this opportunity to go check out Holly's bag."
    
label openbag:
    hide phone
    menu:
        narrator "You open Holly's bag and check her..."
        
        "Diary":
            show diary
            window hide
            pause
            window show
            "You notice that there seems to be a torn page."
            player "I wonder why she ripped this page..."
            hide diary
            jump openbag
       
        "Phone":
            window hide
            show phone lock
            $ renpy.transition(dissolve)
            call screen phone

        "Locker":
            narrator "You decide to leave her bag alone. Maybe you should go check out her locker."
            jump locker
    
    #This will allow you to read Holly's texts.
    label openphone:
        hide phone
        narrator "You unlocked her phone!"
        player "Alright! Time to look through her texts."
        window hide
        show phone messages
        call screen select
        hide phone
        window show
        jump openbag
    #Failed to open phone
    label fail: 
        hide phone
        narrator "You can't open her phone. Maybe try again when you know the passcode."
        jump openbag
#phones
label dadphone:
    show phone dadphone
    pause
    jump plsnomore

label jeremyphone:
    show phone jeremyphone
    pause
    jump plsnomore

label rachelphone:
    show phone rachelphone
    pause
    jump plsnomore

label tiffanyphone:
    show phone tiffanyphone
    pause
    jump plsnomore

label tristanphone:
    show phone tristanphone
    pause
    jump plsnomore

label plsnomore:
    show phone messages
    call screen select
#Go to holly's locker and check its contents
label locker:
    narrator "You walk over to her locker. It's locked."
    player "Huh, how should I get her combo?"
    python:
        hollylocker = renpy.input("Enter the first number of the locker combination: ", allow="0123456789", length=2)
        hollylocker = hollylocker + renpy.input("Enter the second number of the locker combination: ", allow="0123456789", length=2)
        hollylocker = hollylocker + renpy.input("Enter the third number of the locker combination: ", allow="0123456789", length=2)
    #If combination entered properly, opens. Otherwise fails and given options.
    if(hollylocker == "092114" or hollylocker == "92114"):
        call openlocker("True")
    narrator "You fail to open her locker."
    menu:
        narrator "You decide to..."
        
        "Try again!":
            jump locker
        
        "Check her bag again":
            jump openbag
    
#If you open holly's locker, you find a note from jeremy asking to meet
label openlocker(firstTime = False):
    scene hallway
    if(firstTime):
        "You open Holly's locker."
        player "Oh, I found a map. I'll hang on to this for now."
        player "I should check out the locker first."
    show screen mapbutton
    hide window
    scene locker
    call screen locker

#Meet jeremy after finding the note
label meetingjeremy:
    scene classroom with fade
    show jeremy normal
    jeremy "Oh hey, you actually came. I wasn't expecting you to."
    player "You invited me, why wouldn't I come? What's up?"
    jeremy "Yeah, that's why you haven't met me the past 6 times?"
    player "I've been... busy..."
    jeremy "Sure, whatever."
    jeremy "Holly, I know you've been going through some rough times. I know we grew apart and that it's now an embarrassment to even associate with me, but I'm here for you."
    jeremy "I'm sure what happened to Sadie has affected you a lot too."
    player "Uhh..."
    jeremy "Holly... How's your mom been?"
    player "{i}Holly's MOM? Why is she relevant? How do I respond to this?{/i}"
    player "Oh...she's fine. Why do you ask?"
    narrator "Jeremy gives you a strange look."
    jeremy "Why do I ask? She's been in that condition for YEARS, Holly."
    player "...Uhh."
    show jeremy hurt
    jeremy "You used to care more. I guess you've changed too much."
    jeremy "Look, if you ever need help, I'm here for you. I don't want what happened to Sadie to happen to you."
    player "Jeremy, I'm alright. I'll ring you up if I ever need something, okay?"
    jeremy "Ring you up? That's a new one, Holly. Are you...feeling okay?"
    player "{i} Oh crap.{/i}"
    player "Yeah, just heard it from a...TV show."
    "Jeremy doesn't look like he believes you"
    jeremy "Alright then. Maybe you should talk to Mr.Bruce about it. I know he's been helping you out."
    player "{i} I hated Mr.Bruce. I had no idea Holly was close to him, or even any teacher.{/i}"
    player "Yeah, maybe I will. See you Jeremy."
    hide jeremy
    $mrBruce = True
    player "I still have no idea what happened to me. I need to find some kind of hint."
    call screen map_screen

#meeting mr bruce
label meetingbruce:
    scene classroom with fade
    show bruce normal
    bruce "Hey Holly, shouldn't you be in class?"
    player "Uh..."
    menu:
        "I need your help":
            jump deepconvoswithbruce
    
    
#Go to the office to find information about your death
label office:
    scene office with fade
    show admin
    python:
        officescore = 0
    player "Hello, I'd like to see the file for Sadie Slegab."
    narrator "She gives you a strange look."
    officeperson "What do you need her file for?"
    player "I just wanted to see how she was doing."
    officeperson "You're the last person I'd trust with her file. I'm sure {i}you{/i} cared a whole lot about her."
    player "{i}Well, that's certainly not wrong. Holly always was harsh to me. Maybe it would've been better to possess someone else if I wanted my file. Let's see if I can convince her otherwise anyways.{/i}"
    #Try to convince admin to let you see file. Requires 2/3 correct answers otherwise you get a retry.
    menu:
        player "I want to..."
        
        "Talk with her family":
            python:
                officescore += 1
            officeperson "Hmm. Isn't that kind of you. I could just give you their number though. What do you need the file for?"
        
        "Investigate what happened to her":
            officeperson "Investigate? Investigate what? What exactly are you planning right now, Holly? Tell me."
    
    menu:
        player "Well..."
        
        "She was my friend":
            officeperson "You've got to be joking. We called you in here multiple times to try to stop you from bullying her."
        
        "I never got the chance to apologize. I want to know more about her.":
            python:
                officescore += 1
            officeperson "Well, you would've known had you not bullied her so much. It's good that you show some concern however."
    
    if (officescore < 2):
       officeperson "I'm not letting you see her file."
       player "{i}Well that went horribly. Let's try again, but change my answers this time.{/i}"
       jump office
    officeperson "Alright, I trust you. Here's her file."
    label viewfile:
        hide admin
        show report
        window hide
        pause
        window show
        player "{i}As I thought, I did die. How did it happen? Was it an accident or did someone kill me? I have to find out. I'm going to find out what happened on that date.{/i}"
        window hide
        hide report
        show admin with fade
        window show
        player "I saw what I needed to, thank you."
    player "{i}I should check the school's library and see if I can get a newspaper from that date.{/i}"
    jump wildtristanwantstohavelunch

label wildtristanwantstohavelunch:
    scene hallway
    show tristan angry
    narrator "You're on the way to the library, but you suddenly see Tristan. He seems to be looking for you. He spots you."
    tristan "Holly, what are you doing? You know we're supposed to have lunch together."
    player "{i}Oh shoot, I don't want to have to waste time talking to Tristan right now. Let's see if I can talk him out of having lunch.{/i}"
    menu:
        player "Hey Tristan..."
        
        "I've got to go finish my homework.":
            tristan "Finish your homework? Who cares about that, do it some other time. You know we always have lunch together. Let's go."
            player "But, I need to get it done before next period!"
            tristan "I don't care. This is more important. Come."
            jump forcedlunchwithtristan
            
        "I'm feeling horribly sick right now.":
            show tristan normal
            tristan "You feel sick? You seem fine to me."
            player "Well yeah, of course I'd act fine. I don't want to show everyone you know."
            tristan "Fine. You know where I'll be."
            hide tristan
            jump libraryscene

#unimplemented for now, jumps to library scene instead.
label forcedlunchwithtristan:
    scene black
    narrator "Tristan kills you because you're stupid and make bad choices. You die."
    return

label libraryscene:
    show library
    player "Alright, let's see what I can find."
    player "Here it is!"
    show newspaper
    window hide
    pause
    window show
    player "Broken neck with some bruising? Did Tristan kill me? I can't think of anyone else who is strong and hates me enough to want to do that."
    hide newspaper
    player "Wait, I'm in Holly's body. I can talk to Tristan about it. Looks like I'll pay him a little visit."
    jump tristanconvo
    
label tristanconvo:
    scene hallway
    show tristan normal
    player "Hey Tristan, remember what happened to Sadie?"
    tristan "I thought you were the one who said to \"respect the dead\", change your mind?"
    player "I just keep thinking what happened. Why did you do that?"
    show tristan angry
    tristan "What? You're blaming me? I didn't do nothing, you KNOW it was all your own fault."
    player "{i}Holly's fault? But there's no way Holly could have broken my neck.{/i}"
    player "How was it MY fault?"
    tristan "Are you kidding? You should know."
    player "How did Holly kill me? Wait....I think I remember..."
    jump flashback

label flashback:
    scene black
    holly "You're stupid and disgusting who would ever want to hang out with you?"
    holly "There's a reason no one likes you. It's called being a loser."
    narrator "Holly berates you fiercely, while others laugh on. Nobody stops her from her bullying, and she continues even more than usual. Far more."
    narrator "You head home crying that night."
    Character('Dad') "Crying again? Quit being such a wuss and stand up to them already. Dealing with you is such a god damn pain."
    Character('Mom') "Your dad's right, you know. Stand up for yourself and they'll stop. We have enough problems without you."
    player "{i}Nobody cares about me. Nobody at all. Nobody understands my pain. Nobody understands anything at all.{/i}"
    player "{i}They'd all be better off without me. I'm so sick of everything.{/i}"
    narrator "You hang yourself."
    jump ultimatechoice

label ultimatechoice:
    menu:
        "Will you..."
        
        "Forgive Holly":
            player "Holly did some really messed up things. She bullied me far more than she should've. But she has her own problems too."
            player "She messed up my life, but she still has hers to use. She can atone for her mistakes. I'll just help her out in one small way."
            scene hallway
            show tristan angry
            player "Tristan, we're over."
            tristan "What? You can't just end it like this. What's up with you?"
            player "I'm sick of your abuse and harshness. Tristan. We. Are. Done."
            player "I liked you at some point but that's long gone. Leave me alone. If you try anything, I'll make sure you regret it."
            tristan "This is insane! What are you saying, Holly?!"
            player "I've let you do as you please long enough. Goodbye."
            tristan "FINE! Do as you like, go be a loser for the rest of your life."
            narrator "You walk away, ignoring Tristan."
            hide tristan
            player "Well, I've done what she's been wanting to do for a long time. I'll give her life back to her now."
            narrator "You leave Holly's body and move on to the afterlife."
            return
        "Take revenge":
            player "Holly took my life, I deserve to take hers. I'm going to live out the rest of her life for her."
            scene hallway
            show tristan angry
            player "Let's go eat Tristan, I'm just hungry."
            narrator "You live out the rest of your life as Holly."
            scene black with fade
            hide tristan
            return
    return

#jeremyy
label jeremyroute:
    narrator "Unfortunately, this route has not been created yet. You will instead take Holly's route."
    player "Hmm, I can't find Jeremy anywhere. I guess I'll go after Holly and Tristan instead then. Hope I haven't missed anything!"
    jump hollyroute

#You went home
label home:
    narrator "You went home. There's absolutely nothing to do at home and soon you fall asleep. You never awaken."
    return