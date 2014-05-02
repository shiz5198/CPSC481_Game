#Created by Shi Zheng
#Beginner Level Python Programming
#Last update 4-28-14
#Description:
#This is a badic text-based adventure game. The player will be insrutcted
#to create a basic character and explore a house. At the end player will
#enter the boss room. A battle will occur and the ending will be decided
#base on character skills.


import random
import time
import sys


global hp
global strength
global speed
global inventory
global checksofa
global checkfire
global checkportrait
global checkstove
global checkcabinet
global checksink
global checktoilet
global checkbathtub
global monsterhp
global monsterstrength
global monsterspeed
checksink = 0
checktoilet = 0
checkbathtub = 0
checkstove = 0
checkcabinet = 0
checkportrait = 0
checksofa = 0
checkfire = 0
inventory = []
hp = 10
strength = 1
speed = 1


#Game start method.
def start():
    print('''
--------------------------------------------------------------------------------
    WELCOME HERO OF LIGHT! or whoever you are!
    So you finally comes, weeks of emails and messages,
    you finally comes.

    You are in a haunted house. This house has been abandoned for over
    100 years. It is said that the owner of this house was once a
    famous sculptor. One day he started to shut himself inside his bedroom.
    He told everyone not to bother him for he was going to make the most
    beautiful statue in the world. He completely shut himself from the outside
    world. At first no one thought it is unsual. Until a few days later the
    wife started to get worried and went check on him. She open the bedroom
    door. She saw the most beautiful statue of the world. It was so beautiful
    that she stood there and stared at it for a couple of minutes. Then
    she saw her husband, facing the statue. She went closer intend to
    congradulate him for he had indeed made the most beautiful statue
    in the world. She walked closer to him. She became horrified when
    her husband turned and face her. The sculptor's face is pale white. She
    didn't see his pupil in his eyes. His face is emotionless. He started to
    walk toward her, with his knife. And he attacked. He slashed his wife's
    throat. As the wife fell to the ground. She stared at the statue as the
    statue smiles back at her.
    
    After a week, the neighbors called the police as the house had been
    silent for a while, which is unusual. The police come and find the
    house is full of dead bodies. They found the sculptor dead in his
    bedroom with knife still in his hand. They conclude that the sculptor
    killed everyone in the house and then kill himself. The statue is
    nowhere to be found.
    
    The house was owned by a couple other people, but none of the
    owners make it out alive. Every owner ended the same way. Killed
    everyone in the house and suicide with sculptor's knife. This house
    was then abandoned since eveyone wasafraid to live in this house.
    
    There was some advanturers like you who come in this house. But
    none was ever seen after. Now you comes. I don't know why do
    you want to experience the house, but I'm not complaining. I was bored.
    Now I have stuff to do. 
--------------------------------------------------------------------------------
    ''')
    name = input("So what's your name again? \n")
    print("\noh, right. That. Anyways")
    print("are you ready to start this short advanture? " + name)
    prompt_start()

#User input for Start method
def prompt_start():
        

    start = input("\nType Start to begin. Exit to quit.\n")
    if start == 'Start'or start == 'start':
        print('''
----------------------------------------------------------------------
    So let's set up your character shall we?

''')
        character()
    elif start == 'Exit' or start == 'exit':
        print("Ok, the game is going to exit in 2 seconds")
        time.sleep(2)
        print("Bye")
        sys.exit(0);
    else:
        print("You need to follow instructions!")
        prompt_start()

#character skill point distribution
def character():
    global hp
    global strength
    global speed
    stat_point = 20
    print('''
____________________________________________________________________
       Because i'm feeling generous, I'm going to give
       you 20 skill points for you to spend for free!
       Now kneel and thank me!

       Just so you know, you have 3 attributes:
          -HP
          -Strength
          -Speed

       
       Use you points carefully for you will not be able to
       reset after you assigned them.

       As of now, you have:
       10 HP
       1  Strength
       1  Speed

       WARNING! Enter NUMERICAL NUMBERS ONLY!
       '''
          )
    #While i still have skill points.
    while stat_point > 0:
        #if the skill point is still available 
        if stat_point > 0:
            print('''
######################################################################
    So how many points do you want to put into hp?
    The more hp you have, the more hits you can take before you die.
    hp a.k.a. hitpoints a.k.a. health
    ''')
            print("Your hp is "+str(hp))
            while stat_point > 0:
                hp_point = int(input("\nNote that 1 skill point = 10 hp \n"))
                if hp_point > stat_point:   
                    print('''
Now you are just being greedy! Remember you only have 20 free skill points!
Try Again!''')
                    continue
                else:
                    hp = hp + (hp_point*10)
                    break
            stat_point = stat_point - hp_point    
            print("you now have " +str(hp)+ " health. \n")
            printskill(stat_point)

        #if the skill point is still available
        if stat_point > 0:
            print('''
######################################################################
    Now how many points do you want to put into strength?
    the more strenth you have, the stronger you are. You can
    hit harder!''')
            print("Your strength is " +str(strength))
            while stat_point > 0:
                st_point = int(input("\nNote that 1 skill point = 2 strength. \n"))
                if st_point > stat_point:
                    print('''
Now you are just being greedy! You only have 20 free skill points!!
Try Again!!''')
                    continue
                else:
                    strength = strength + (st_point*2)
                    break
            
            stat_point = stat_point - st_point
            print("you now have " +str(strength)+ " strength\n")
            printskill(stat_point)

        #if the skill point is still available
        if stat_point > 0:
            print('''
#######################################################################
    Now how many points do you want to put into speed?
    the more speed you have, the faster you are. You can
    hit more times!
    ''')
            print("Your speed is "+str(speed))
            while stat_point > 0:
                sp_point = int(input("\nNote that 1 skill point = 1 speed. \n"))
                if sp_point > stat_point:
                    print('''
Now you are really greedy!! I only give you 20 freebies!!
Try Again!!''')
                    continue
                else:
                    speed = speed + sp_point
                    break
            stat_point = stat_point - sp_point
            print("you now have " +str(speed)+ " speed\n")
            printskill(stat_point)
    printstat()
    askagain()

# method to print skill point 
def printskill(stat_point):
    if stat_point > 0:
        print("\nyou still have " +str(stat_point)+" skill points\n")
    else:
        print("\nyou have used up all the skill points!\n")

#method to print character stat
def printstat():
    print("Your stats are below:")
    print("hp:\t\t" +str(hp))
    print("strength:\t" +str(strength))
    print("speed:\t\t" +str(speed)+ "\n")

#method to ask again. For displaying purposes.
#without this method, the display will be too long
#for a single output
def askagain():
    print('''
I'm going to ask you again, Are you sure you want to start
this advanture?''')
    start = input("There will be no way back. \nYes/No\n").lower()
    if start == 'yes' or start == 'y':
        mansion();
    else:
        print("Just as I thought. You are not brave enough. Wuahhahahaha. Bye")
        print("The game will end in 2 seconds")
        time.sleep(2)
        print("Bye")
        sys.exit(0)

#Output mansion
def mansion():
    print("Now your advanture begins!")
    print('''

Open sesame!!

 ______________
|\ ___________ /|
| |  /|,| |   | |
| | |,x,| |   | |
| | |,x,' |   | |
| | |,x   ,   | |
| | |/    |%==| |
| |    /] ,   | |
| |   [/ ()   | |
| |       |   | |
| |       |   | |
| |       |   | |
| |      ,'   | |
| |   ,'      | |
|_|,'_________|_|

''')
    entry()

#entry room. Ask the player for input
def entry():

    print('''
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
You are at the entry of the house. The house looks terrible. It is dark and
all you have is a flash light. You can almost hear someone laughing somewhere
in te house, but you don't know if its just your mind playing with you. Other
thanto freak you out a bit, entry do not serve any purposes. You do not
see anything useful. 

At this point, you can either move (F)orward into the living room,
or (B)ack out and quit like a coward.

You can type 'help' for a full list of commands.
You can type 'stat' anytime to see your stats.
''')
    prompt_entry()

#player input for entry
def prompt_entry():
    prompt_e = input("\nSo what do you want to do?\n").lower()
    if prompt_e == "f":
        living_room()
    elif prompt_e == "b":
        print("Just as I thought. You are not brave enough. Wuahhahahaha. Bye")
        print("The game will end in 2 seconds")
        time.sleep(2)
        print("Bye")
        sys.exit(0)
    elif prompt_e == "help":
        print('''
type:
f = forward to living room
b = back out to quit
help = list of commands
stat = see your stat

''')
        prompt_entry()
    elif prompt_e == "stat":
        printstat()
        prompt_entry()
    else:
        print("Follow instructions! That is not one of the commands!")
        promt_entry()

#living room. Ask for user input
def living_room():
    print('''
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
You are now at the living room.  You know that
there is no way out now. You can feel the chill. You feel like somebody just
through your body. You start to look around the room. You can't see everything
because it is really dark. You point you light to the ceiling and all you can
see is spider web. You are not sure but you thought you saw some blood
dripping from the ceiling. You start walking to the center of the room.
Every step you walk you hear the floor...

You can go (W)est to the kitchen, (N)orth to go up stairs,
(E)ast to further check out the room, or
(S)outh to get back to the
entrance.

You can type 'help' for a full list of commands.
You can type 'stat' anytime to see your stats.
You can type 'item' to see your inventory.
''')
    prompt_living()

def prompt_living():
    prompt_l = input("\nSo what do you want to do?\n").lower()
    if prompt_l == 'w':
        kitchen()
    elif prompt_l == 'n':
        up_hallway()
    elif prompt_l == 's':
        print('''
You go back to the entry. But the door is locked.
You go back to the loving room''')
        living_room()
    elif prompt_l == 'e':
        check_living()
    elif prompt_l == 'help':
        print('''
type:
w = west to the kitchen
n = north to up stairs
e = check out the room
s = south to the entrance
help = list of commands
stat = see your stat
item = inventory
examine (object) = examine sofa, fire place or portrait
''')
        prompt_living()
    elif prompt_l == 'stat':
        printstat()
        prompt_living()
    elif prompt_l == 'examine sofa':
        if checksofa == 0:
            exam_sofa()
        else:
            print("You already examined the sofa")
        prompt_living()
    elif prompt_l == 'examine fire place':
        if checkfire == 0:
            exam_fire()
        else:
            print("You already examined the fire place")
        prompt_living()
    elif prompt_l == 'examine portrait':
        if checkportrait == 0:
            exam_portrait()
        else:
            print("You already examined the portrait")
        prompt_living()
    elif prompt_l == 'item':
        if len(inventory) == 0:
            print("Your inventory is empty.\n")
        else:
            printinventory()
        prompt_living()
    else:
        print("Follow instructions! That is not one of the commands!")
        prompt_living()

#method to print out character inventory
def printinventory():
    print("YOUR INVENTORY\n")
    for item in inventory:
        print(item)

#method to check living room, ask user input
def check_living():
    print('''
You check out the room. You see a broken sofa,
a broke down dark fire place and
a portrait of the scultpter's family.

You can interact by typing: examine (object)

Object list: sofa
             fire place
             portrait

''')
    prompt_living()

#sofa method. 
def exam_sofa():
    global checksofa
    global hp
    global strength
    global inventory
    print("You look closely at the sofa\n")
    sofa = random.randrange(1,6)
    if sofa == 1:
        print("You find nothing useful, it's just a sofa.\n")
    elif sofa == 2:
        print("You find a dead spider. It's useless.\n")
    elif sofa == 3:
        print("A spider jump up and bit you. You lost 5 hp.\n")
        hp = hp - 5
    elif sofa == 4:
        print("A mutated spider jump up and bit you. You gain 1 strength\n")
        strength = strength + 1
    else:
        print('''
You find a cushion. It gives you some protection.
Hp + 20. Item added to your inventory\n''')
        inventory.append("Sofa Cushion + 20 hp")
        hp = hp + 20
    checksofa = 1

#fire play method
def exam_fire():
    global checkfire
    global strength
    global inventory
    print("You check out the fire place\n")
    fire = random.randrange(1,10)
    if fire == 1:
        print('''
You find a fire iron. Strength + 15.
Iten added to your inventory\n''')
        inventory.append("Fire Iron + 15 Strength")
        strength = strength + 15
    else:
        print("You find nothing useful\n")
    checkfire = 1

#portrait method
def exam_portrait():
    global checkportrait
    global speed
    global inventory
    print("You check out the portrait\n")
    portrait = random.randrange(1,3)
    if portrait == 1:
        print("You find nothing, but the portrait creeps you out a bit\n")
    else:
        print('''
You find a secret safe behind the portrait.
All it has is a pair of shiny shoes.
You put on the shoes and somehow you feel you can run faster.
Speed + 2\n''')
        inventory.append("Shiny shoes + 2 Speed")
        speed = speed + 2
    checkportrait = 1

#kitchen room
def kitchen():
    print('''
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
You are in the kitchen. This is a old kitchen. It doesn't even has a fridge.
You can go (N)orth to check out the kitchen or
(S)outh to go back to the living room.

You can type 'help' for a full list of commands.
You can type 'stat' anytime to see your stats.
You can type 'item' to see your inventory.
''')
    prompt_kitchen()

#user input for kitchen
def prompt_kitchen():
    prompt_k = input("So what are you going to do?\n").lower()
    if prompt_k == "s":
        living_room()
    elif prompt_k == "n":
        check_kitchen()
        prompt_kitchen()
    elif prompt_k == "help":
        print('''
n = north to check out the room
s = south to the living room
help = list of commands
stat = see your stat
item = inventory
examine (object) = examine stove or cabinet
''')
        prompt_kitchen()
    elif prompt_k == "stat":
        printstat()
        prompt_kitchen()
    elif prompt_k == "examine stove":
        if checkstove == 0:
            exam_stove()
        else:
            print("You already examined the stove\n")
        prompt_kitchen()
    elif prompt_k == "examine cabinet":
        if checkcabinet == 0:
            exam_cabinet()
        else:
            print("You already examined the cabinet\n")
        prompt_kitchen()
    elif prompt_k == "item":
        if not inventory:
            print("your inventory is empty.\n")
        else:
            printinventory()
        prompt_kitchen()
    else:
        print("Follow instructions! That is not one of the commands!\n")
        prompt_kitchen()

#examine kitchen
def check_kitchen():
    print('''
You check out the kitchen. Everything look ruined. You can examine the
stove or the cabinet\n''')
    prompt_kitchen()

#stove method
def exam_stove():
    global checkstove
    global hp
    print("You check out the stove\n")
    stove = random.randrange(1,5)
    if stove == 1:
        print("You see a pot. You look inside the pot and it's empty\n")
    elif stove == 2:
        print('''
You see a pot. You look inside the pot and you see a pot full of red liquid.
It is boiling even though the fire is not on. You back away from the stove.\n''')
    elif stove == 3:
        print('''
you see a pot. You look inside and see a human head.
He smiles at you and you feel a little dizzy. You lose 2 hp.
You back away from the stove\n''')
        hp = hp - 2
    else:
        print('''
You see a pot. You smell something sweet coming from the pot.
You gain 10 hp for some unknown reason.\n''')
        hp = hp + 10
    checkstove = 1

#cabinet method
def exam_cabinet():
    global checkcabinet
    global inventory
    global strength
    print("you check out the kitchen cabinet\n")
    cabinet = random.randrange(1,4)
    if cabinet == 1:
        print('''
you find a rusty knift. Strength + 10.
Item added to inventory\n''')
        inventory.append("Rusty Knift + 10 Strength")
        strength = strength + 10
    elif cabinet == 2:
        print("You find a human skull. It's useless.\n")
    else:
        print("You find a skeleton of a dead rat. It's useless.\n")
    checkcabinet = 1

#upstair hallway
def up_hallway():
    print('''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
You are in the upstairs hallway. The wall of the hallway is fill with
blood. All you can see is red. It is really cold here. At the end of the
hallway you see the bedroom where the sculptor worked on his masterpieces.
You take a step forward. All the sudden you feel the floor is moving. The
wall is moving. You look closer. They are not actually moving, but there are
a sea of worm looking red creatures crawling.

At this point you can go (N)orth to the master bedroom,
(E)ast to the guest bedroom,
(W)est to the bathroom or
(S)outh back to the living room

You can type 'help' for a full list of commands.
You can type 'stat' anytime to see your stats.
You can type 'item' to see your inventory.
''')
    prompt_up()

#user input for unstair hallway    
def prompt_up():
    prompt_u = input("\nSo what are you going to do?\n").lower()
    if prompt_u == "s":
        living_room()
    elif prompt_u == "n":
        masterbed()
    elif prompt_u == 'w':
        bathroom()
    elif prompt_u == 'e':
        guestbed()
    elif prompt_u == "help":
        print('''
n = north to master bedroom
e = east to the guest bedroom
w = west to the bathroom
s = south to the living room
help = list of commands
stat = see your stat
item = inventory
''')
        prompt_up()
    elif prompt_u == "stat":
        printstat()
        prompt_up()
    elif prompt_u == "item":
        if not inventory:
            print("your inventory is empty.\n")
        else:
            printinventory()
        prompt_up()
    else:
        print("Follow instructions! That is not one of the commands!\n")
        prompt_up()

#bathroom metod
def bathroom():
    print('''
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
You run into the bathroom. It is dim. A candle is lit. This is
unsual as nobody has lived here for years. Then you realized that
it is probably not by a human.

At this point you can either go (N)orth to check out the bathroom
or (S)outh to go back into the hallway.

You can type 'help' for a full list of commands.
You can type 'stat' anytime to see your stats.
You can type 'item' to see your inventory.''')
    prompt_bathroom()

#user input for bathroom
def prompt_bathroom():
    prompt_b = input("\nWhat do you want to do?\n").lower()
    if prompt_b == 'n':
        check_bathroom()
    elif prompt_b == 's':
        up_hallway()
    elif prompt_b == 'stat':
        printstat()
        prompt_bathroom()
    elif prompt_b == 'help':
        print('''
n = north to check out the bathroom
s = south to the hallway
help = list of commands
stat = see your stat
item = inventory
examine (object) = examine sink, bathtub or toilet.
''')
        prompt_bathroom()
    elif prompt_b == 'item':
        if not inventory:
            printinventory()
        else:
            print("your inventory is empty\n")
        prompt_bathroom()
    elif prompt_b == 'examine sink':
        if checksink == 0:
            exam_sink()
        else:
            print("You already examine the sink\n")
        prompt_bathroom()
    elif prompt_b == 'examine bathtub':
        if checkbathtub == 0:
            exam_bathtub()
        else:
            print("You already examine the bathtub\n")
        prompt_bathroom()
    elif prompt_b == 'examine toilet':
        if checktoilet == 0:
            exam_toilet()
        else:
            print("You want to get trolled again? Just move along.\n")
        prompt_bathroom()
    else:
        print("Follow instructions! That is not one of the commands!\n")
        prompt_bathroom()

#examine bathroom
def check_bathroom():
    print('''
The room is dim. But you can still see. There are only three things you can
look at. The sink, toilet and te bathtub.\n''')
    prompt_bathroom()

#sink method
def exam_sink():
    global checksink
    global speed
    global hp
    global strength
    print("You check out the sink\n")
    sink = random.randrange(1,5)
    if sink == 1:
        print('''
You turn on the sink. Red liquid comes out. That's all.\n''')
    elif sink == 2:
        print('''
You looked at the mirror. You see a reflection of yourself. Slowly the
reflection turns to something else. It turns to your face when you die,
and it is smiling back at you. You quickly step away from the sink\n''')
    elif sink == 3:
        print('''
You open the sink cabinet. You find some adrenaline pills. 
Hp + 10. Strength + 2. Speed + 1.\n''')
        hp = hp + 10
        strength = strength + 2
        speed = speed + 1
    else:
        print('''
You open the sink cabinet. It's empty.\n
''')
    checksink = 1    

#toilet method                  
def exam_toilet():
    global checktoilet
    print('''
BAZINGA! There is nothing really useful here. Just a step to waste your time.
Now move along.\n''')
    checktoilet = 1

#bathtub method
def exam_bathtub():
    global checkbathtub
    global speed
    global hp
    global strength
    print("You check out the bathtub.\n")
    sink = random.randrange(1,5)
    if sink == 1:
        print('''
You look at the bathtub. It's empty.\n''')
    elif sink == 2:
        print('''
You look at the bathtub. It's empty.
The room go dark, then it lit up again. You see a dead body in
a pool of red. Then it disapear again.\n''')
    elif sink == 3:
        print('''
You look at the bathtub. You find a rusty pipe. Strength + 5\n''')
        strength = strength + 5
    else:
        print('''
You look at the bathtub. You see a human skeleton. You back away
from the bathtub\n
''')
    checkbathtub = 1

#Guest bedroom
def guestbed():
    print('''
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
This is a completely ruined room. You should probably get out as soon as
possible. It is fill with darkness.
Not even your flash light helps.\n''')
    guest = input('''
Do you want to check the room anyway?
Yes to check the room
No to back out to the hallway\n
''').lower()
    if guest == 'yes' or guest == 'y':
        badend()
    else:
        up_hallway()

#master bedroom
def masterbed():
    print('''
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
You enter the master bedroom. It is supprising bright. Everything is white.
The floor, the ceiling, the walls. There's not window.
The only thing in the room is a statue of a beautiful woman in the center
of the room. Everything look so peaceful. 

You can step (F)orward to check out the statue, or (B)ack into the hallway.

You can type 'help' for a full list of commands.
You can type 'stat' anytime to see your stats.
''')
    prompt_master()

def prompt_master():
    master = input("\nWhat are you going to do?\n").lower()
    if master == 'f':
        monster()
    elif master == 'b':
        up_hallway()
    elif master == 'stat':
        printstat()
        prompt_master()
    elif master == 'help':
        print('''
f = forward to check the statue
b = back out to the hallway
help = list of commands
stat = see your stat
item = inventory
''')
        prompt_master()
    elif master == 'item':
        if not inventory:
            print("Your inventory is empty.\n")
        else:
            printinventory()
        prompt_master()
    else:
        print("Follow instructions! That is not one of the commands!")
        prompt_master()        

#monster battle
def monster():
    global speed
    global hp
    global monsterhp
    monsterhp = random.randrange(100, 200)
    global monsterstrength
    monsterstrength = random.randrange(10, 20)
    global monsterspeed
    monsterspeed = random.randrange(3, 10)
    print('''
You walk toward the statue. All the sudden the room turn red.
The ceiling start dripping blood. Faces start to appear on the
wall. The statue in the center starts to bleed. It starts to
move toward you. Itstarts to scream at you. A knife appears in
it's hand. It starts to attack you. \n''')
    time.sleep(1)
    if monsterspeed > speed:
        hp = hp - monsterstrength
        print("\nYou are too slow, the statue attack you first!\n")
        print("Your hp decreased by " +str(monsterstrength) + "\n")
        if hp < 0:
            print("Your hp is 0")
        else:
            print("Your hp is " +str(hp)+ "\n")
    else:
        monsterhp = monsterhp - strength
        print("\nYou are faster than the statue. You attack it first!\n")
        print("Statue takes " +str(strength)+ " damage.\n")

    while hp > 0 and monsterhp > 0:
        round()
        if hp <= 0:
            print("You die. Statue laughs and a new face emerge from the wall.")
            print("It is Your face.")
            badend()
        if monsterhp <= 0:
            print('''
You defeat the statue! You win! Everything is back to normal.\n''')
            goodend()

#method to account for speed           
def round():
    global hp
    global monsterhp
    monstercounter = monsterspeed/speed
    playercounter = speed/monsterspeed
    if monsterspeed > speed:
        time.sleep(1.5)
        hp = hp - monsterstrength
        print("The statue attack!")
        print("Your hp decreased by " +str(monsterstrength) + "\n")
        if hp < 0:
            print("Your hp is 0")
        else:
            print("Your hp is " +str(hp)+ "\n")
    else:
        time.sleep(1.5)
        monsterhp = monsterhp - strength
        print("You attack the statue!")
        print("Statue takes " +str(strength)+ " damage.\n")
    if hp > 0 and monsterhp > 0:
        while monstercounter > 0:
            time.sleep(1.5)
            if hp > 0:
                hp = hp - monsterstrength
                print("Statue attack you!")
                print("Your hp decreased by " +str(monsterstrength) + "\n")
                if hp < 0:
                    print("Your hp is 0")
                else:
                    print("Your hp is " +str(hp)+ "\n")
            monstercounter = monstercounter - 1
    if hp > 0 and monsterhp > 0:
        while playercounter > 0:
            time.sleep(1.5)
            if monsterhp > 0:
                monsterhp = monsterhp - strength
                print("you attack the statue!")
                print("Statue takes " +str(strength)+ " damage.\n")
            playercounter = playercounter - 1

#if player wins. ask if restart
def goodend():
    print('''
==========================================================================
Everything is back to normal. The house is back to it's ruin states.
No more blood or dead body. You exit the house from the from door. You
look up to the sky. The sun is about to rise. You realize you've been gone
for a couple of hours. You are glad you make it out alive. You walk toward
the sun as it slowly rises.
==========================================================================''')
    print('''

Of couse, unless you want to start all over again. I know this is not
a fun advanture game, but still. I gotta put in a restart option. ''')
    restart = input('''
So do you want to restart and go back to the character skill section?
Yes/No
''').lower()
    if restart == 'yes' or restart == 'y':
        reset()
        character()
    else:
        print("Ok, the game is going to exit in 2 seconds")
        time.sleep(2)
        print("Bye")
        sys.exit(0)

#if player lose, ask if restart
def badend():
    print('''
================================================================================
You die. You become part of the house. Your soul was absorbed by
the evil of the house. You lose you mind. You start to attack anyone
who come in to the house. You are stuck here until a hero, who is better
than you at everything, come to the house and destroy the evil and
you along with it.
================================================================================
''')
    restart = input('''
Not a good game I know, but do you want to restart anyway? It will take you
back to the character skill section.
Yes/No
''').lower()
    if restart == 'yes' or restart == 'y':
        reset()
        character()
    else:
        print("Ok, the game is going to exit in 2 seconds")
        time.sleep(2)
        print("Bye")
        sys.exit(0)

#reset all the stats for game restart
def reset():
    global hp
    global strength
    global speed
    global inventory
    global checksofa
    global checkfire
    global checkportrait
    global checkstove
    global checkcabinet
    global checksink
    global checktoilet
    global checkbathtub
    global monsterhp
    global monsterstrength
    global monsterspeed
    checksink = 0
    checktoilet = 0
    checkbathtub = 0
    checkstove = 0
    checkcabinet = 0
    checkportrait = 0
    checksofa = 0
    checkfire = 0
    inventory = []
    hp = 10
    strength = 1
    speed = 1
    print("Hi. Again. Let's get back to work.")
    
     
start()
input('exit')
